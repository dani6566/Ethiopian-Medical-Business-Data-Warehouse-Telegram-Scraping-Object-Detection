# Ethiopian Medical Businesses Data Warehouse

This project focuses on building a **Data Warehouse** for storing and managing data related to Ethiopian medical businesses, primarily sourced from **Telegram channels**. It involves data scraping, cleaning, transformation, and object detection (using YOLO), with a backend developed using **FastAPI**, **SQLAlchemy**, and **Pydantic** for API exposure and data management.

## Features

- **Data Scraping**: Collect business-related data from Telegram channels.
- **Object Detection**: YOLO is used to detect and extract relevant images (e.g., business logos).
- **Data Cleaning & Transformation**: Prepares raw data for analysis and storage.
- **Data Storage**: Uses PostgreSQL as the primary data warehouse.
- **API Access**: RESTful APIs built with FastAPI for easy data retrieval.

## Tech Stack

- **Programming Language**: Python
- **Database**: PostgreSQL
- **Backend**: FastAPI
- **ORM**: SQLAlchemy
- **Data Transformation**: DBT (Data Build Tool)
- **Object Detection**: YOLO

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/dani6566/Medical-Business-Data-Warehouse-Telegram-Scraping-Object-Detection.git
cd ethiopian-Medical-Business-Data-Warehouse-Telegram-Scraping-Object-Detection
```
## Future Improvements
-**Add advanced data analytics capabilities.**<br>
-**Enhance object detection to classify more medical business entities.**<br>
-**Broaden data sources beyond Telegram channels.**<br>
## License
This project is licensed under the MIT License.
