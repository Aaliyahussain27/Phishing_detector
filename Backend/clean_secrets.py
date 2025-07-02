import re
import pandas as pd

input_file = 'data/merged_urls.csv' 
output_file = 'cleaned_' + input_file

aws_access_key_id_pattern = r'AKIA[0-9A-Z]{16}'  # 20 chars starting with AKIA
aws_secret_key_pattern = r'(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])'  # 40-char base64 style

def clean_cell(cell):
    if isinstance(cell, str):
        cell = re.sub(aws_access_key_id_pattern, '***REMOVED***', cell)
        cell = re.sub(aws_secret_key_pattern, '***REMOVED***', cell)
    return cell

df = pd.read_csv(input_file, encoding='utf-8', engine='python')

df_cleaned = df.copy()
for col in df_cleaned.select_dtypes(include=['object']):
    df_cleaned[col] = df_cleaned[col].apply(clean_cell)

df_cleaned.to_csv("data/cleaned_file.csv", index=False)

print("✅ Cleaned file saved as: data/cleaned_file.csv")
