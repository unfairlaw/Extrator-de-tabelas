import tabula
import pandas as pd
import os
import logging

def setup_logging(log_file_path):
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create handlers
    file_handler = logging.FileHandler(log_file_path, mode='w')
    console_handler = logging.StreamHandler()

    # Set log level for handlers
    file_handler.setLevel(logging.INFO)
    console_handler.setLevel(logging.INFO)

    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def pdf_to_csv_with_custom_transformation(pdf_path, output_csv_path, log_file_path):
    # Set up logging
    logger = setup_logging(log_file_path)

    logger.info(f"Starting PDF to CSV conversion for: {pdf_path}")

    try:
        # Extract tables from the PDF
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
        
        # Initialize an empty DataFrame to hold all tables
        combined_df = pd.DataFrame()
        
        for table_num, table in enumerate(tables):
            # Check if table has enough columns to process (at least 6 columns)
            if table.shape[1] < 6:
                logger.warning(f"Table {table_num + 1} does not have enough columns to relocate. Skipping table.")
                continue

            # Perform the column relocation
            part1 = table.iloc[:, :3]  # Columns 1, 2, and 3
            part2 = table.iloc[:, 3:6]  # Columns 4, 5, and 6

            # Rename columns for part2 to match part1
            part2.columns = part1.columns

            # Concatenate part2 below part1
            new_table = pd.concat([part1, part2], ignore_index=True)

            # Append the transformed table to the combined DataFrame
            combined_df = pd.concat([combined_df, new_table], ignore_index=True)
            
            # Log the table processing
            logger.info(f"Processed table {table_num + 1} with shape {new_table.shape} after transformation")

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

        # Save the combined DataFrame to a single CSV file
        combined_df.to_csv(output_csv_path, index=False)
        
        logger.info(f"PDF to CSV conversion completed successfully. Combined file saved as: {output_csv_path}")
    except Exception as e:
        logger.error(f"Error during PDF to CSV conversion: {str(e)}")

# Define the path for the input PDF, output CSV file, and log file
input_pdf_path = "sample_with_tables.pdf"
output_csv_path = "output_csv_files/combined_output.csv"
log_file_path = "conversion_log.txt"

# Perform the conversion
pdf_to_csv_with_custom_transformation(input_pdf_path, output_csv_path, log_file_path)

print(f"PDF tables converted to a single CSV file successfully. Output file: {output_csv_path}")
print(f"Log file created: {log_file_path}")
