
import pandas as pd
import glob
import os

# Specify the path to the CSV files (e.g., all CSVs in a folder)
csv_files = glob.glob(os.path.join("source/", "*.csv"))
print(csv_files)


# Create an empty list to hold dataframes
dfs = []

# Iterate over the list of CSV files
for file in csv_files:
    df = pd.read_csv(file, usecols=[0])

    row_count = len(df)

    # Print the row count for the current CSV file
    print(f"{file}, {row_count}")

    dfs.append(df)


# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Remove duplicates
combined_df = combined_df.drop_duplicates()

# Save the combined dataframe to a new CSV file
combined_df.to_csv("combined_output.csv", index=False)

print("CSV files have been combined and duplicates removed.")
