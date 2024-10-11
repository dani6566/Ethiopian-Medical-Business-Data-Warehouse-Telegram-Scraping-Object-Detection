import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='data_cleaning.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class DataHouse:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        try:
            logging.info('Data cleaning started.')

            # Removing Duplicates
            self.df.drop_duplicates(inplace=True)
            logging.info('Duplicates removed.')
        
            # Handling Missing Values
            
            column_names = self.df.columns

            # Loop through each column to check for NaN values
            for column in column_names:
                print(f"Checking for NaN values in the '{column}' column:")
                nan_count = self.df[column].isnull().sum()  # Count NaN values in the column
                print(f"Number of NaN values in '{column}' column: {nan_count}")

                # If you want to drop rows with NaN values in the current column
                self.df.dropna(subset=[column], inplace=True)
                print(f"Rows with NaN values in '{column}' column dropped.")

            logging.info("NaN value check and cleaning completed.")
            print(f"Dataset shape after dropping NaN values in '{column_names}' column: {self.df.shape}")
            logging.info('Missing values handled.')

            # Standardizing Formats (e.g., Date format)
            self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
            logging.info('Date format standardized.')

            # # Data Validation (e.g., ensuring non-negative values in a column)
        
            numeric_columns = self.df.select_dtypes(include="number").columns

            # Loop through each numeric column and check for negative values
            for column in numeric_columns:
                if (self.df[column] < 0).any():
                    logging.warning(f'Negative values found in {column}.')
                    # Fix negative values by converting to their absolute value
                    self.df[column] = self.df[column].apply(lambda x: abs(x))

            logging.info("Data validation for numeric columns completed.")


            logging.info('Data cleaning completed.')

            # Storing cleaned data
            self.df.to_csv('cleaned_data.csv', index=False)
            logging.info('Cleaned data saved to CSV.')

        except Exception as e:
            logging.error(f'Error during data cleaning: {e}')


