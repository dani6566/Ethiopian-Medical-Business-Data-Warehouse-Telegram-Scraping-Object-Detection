import torch 
import cv2
import pandas as pd
from sqlalchemy import create_engine
import logging
import os
from load_data import create_db_engine_from_env

# Set up logging
logging.basicConfig(filename='object_detection.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Load YOLOv5 model (pre-trained on COCO dataset)
model = torch.hub.load('../yolov5', 'yolov5s', source='local')

# Directories for images and output
image_dir = '../data/photos'  # Folder containing original images
output_dir = '../data/object_detection'  # Folder for saving detected images
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))]

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Database connection setup
engine = create_db_engine_from_env()

# List to store detection data
detection_data = []

# Function to perform object detection on a single image and store the results
def detect_objects(image_path):
    try:
        # Read the image using OpenCV
        img = cv2.imread(image_path)

        # Perform object detection
        results = model(img)

        # Process detection results
        detections = results.pandas().xyxy[0]  # Bounding boxes in pandas DataFrame format

        # Add each detection to the list with bounding box, confidence, and class label
        for _, detection in detections.iterrows():
            detection_data.append({
                'Image Path': image_path,
                'Bounding Box': f"({detection['xmin']}, {detection['ymin']}, {detection['xmax']}, {detection['ymax']})",
                'Confidence': detection['confidence'],
                'Class Label': detection['name']
            })

        logging.info(f"Object detection completed for {image_path}")

    except Exception as e:
        logging.error(f"Error during object detection for {image_path}: {e}")

# Function to visualize object detection results and save images
def save_detected_images():
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)

        # Read the image
        img = cv2.imread(image_path)

        # Perform detection
        results = model(img)

        # Render the results (bounding boxes and labels)
        results.render()

        # Save the result in the output folder
        output_image_path = os.path.join(output_dir, f"detected_{image_file}")
        cv2.imwrite(output_image_path, img)

# Main process: Detect objects and save to database
def main_object_detection():
    # Loop through all images and run object detection
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        detect_objects(image_path)

    # Convert detection data to a pandas DataFrame and save it to the database
    df = pd.DataFrame(detection_data)
    df.to_sql('yolo_detections', engine, if_exists='replace', index=False)

    # Optionally, save to a CSV file
    df.to_csv('yolo_detections.csv', index=False)

    # Save images with bounding boxes
    save_detected_images()

# Function to perform object detection on 20 sampled images
def visual_object_detection(df_image):
    # Load the CSV with image data
    # df_image = pd.read_csv("../data/cleaned_data.csv")

    # Sample 20 rows randomly
    sampled_images = df_image.sample(n=20, random_state=42)  # Set random_state for reproducibility

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load YOLO model (assuming you're using a PyTorch implementation)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    # Process each sampled image and save the detection results
    for _, row in sampled_images.iterrows():
        print(row.columns)
        image_file = row['Media Path']  # Adjust column name if needed to match your CSV

        image_path = os.path.join(image_dir, image_file)
        
        if os.path.exists(image_path):
            # Read the image
            img = cv2.imread(image_path)
            
            # Perform detection
            results = model(img)
            
            # Render the results (bounding boxes and labels)
            results.render()

            # Save the result in the output folder
            output_image_path = os.path.join(output_dir, f"detected_{image_file}")
            cv2.imwrite(output_image_path, img)
        else:
            print(f"Image {image_file} not found at {image_path}")

    print("Object detection completed on 20 sampled images and results saved.")



# Entry point
if __name__ == "__main__":
    main_object_detection()
