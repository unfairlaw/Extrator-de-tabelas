import tabula
import pandas as pd
import os

def pdf_to_csv(pdf_path, output_dir):
    # Extract tables from the PDF
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for table_num, table in enumerate(tables):
        # Define the output CSV file path
        csv_file_path = os.path.join(output_dir, f"table_{table_num + 1}.csv")
        
        # Save the table to a CSV file
        table.to_csv(csv_file_path, index=False)

    print(f"PDF tables converted to CSV files successfully. Output directory: {output_dir}")

# Define the path for the input PDF and the output directory
input_pdf_path = "C:\\Documents\\seuarquivoaqui"
output_csv_directory = "C:\\Documents"

# Perform the conversion
pdf_to_csv(input_pdf_path, output_csv_directory)
