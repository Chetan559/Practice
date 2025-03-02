import os
import pandas as pd

# Set the folder path containing the PDFs and the Excel file path
folder_path = "C:/Users/Chetan/Downloads/3rdfebpdf"
excel_path = "C:/Users/Chetan/Downloads/Certificate Copy of Workshop on Effective Sales and Marketing Strategies for Entrepreneurs_Startups (Responses).xlsx"

# Load the Excel file
df = pd.read_excel(excel_path)

# Column containing the new names
name_col = "Name"  # Ensure this matches exactly with your Excel file

# Get a list of PDF files in the folder
pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".pdf")])

# Check if the number of PDFs matches the number of names in the Excel file
if len(pdf_files) != len(df):
    print("Warning: Number of PDFs and number of names in the Excel file do not match!")

# Rename the PDF files based on the order in the Excel file
for pdf_file, new_name in zip(pdf_files, df[name_col]):
    old_path = os.path.join(folder_path, pdf_file)
    new_path = os.path.join(folder_path, f"{new_name}.pdf")

    # Rename the file if the new name does not already exist
    if os.path.exists(new_path):
        print(f"Skipping: {new_name}.pdf already exists.")
    else:
        os.rename(old_path, new_path)
        print(f"Renamed: {pdf_file} -> {new_name}.pdf")

print("Renaming process completed.")
-