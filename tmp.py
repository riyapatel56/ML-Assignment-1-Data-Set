import pandas as pd

# Specify the path to your .data file
data_file_path = 'adult.data'

# Define column names
column_names = [
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"
]

# Read the .data file into a DataFrame
df = pd.read_csv(data_file_path, header=None, names=column_names, sep=',\s*', engine='python')

# Specify the path where you want to save the CSV file
csv_file_path = 'adult.csv'

# Save the DataFrame as a CSV file
df.to_csv(csv_file_path, index=False)