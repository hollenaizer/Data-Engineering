import pandas as pd
import dask.dataframe as dd
import pandas as pd

# ==================================
# TASK 1.0.1: EXTRACT FLAT FILES
# ==================================

# 1. Extract CSV data
df1 = pd.read_csv("data/example.csv")

# 2. Extract Excel data
df2 = pd.read_excel(
    "data/example.xlsx",
    engine="openpyxl"
)

# 3. Extract JSON data
df3 = pd.read_json("data/example.json")


# ==================================
# DISPLAY EXTRACTED DATA
# ==================================

print("\n========== CSV DATA ==========")
print(df1)

print("\n========== EXCEL DATA ==========")
print(df2)

print("\n========== JSON DATA ==========")
print(df3)
# ==================================
# TASK 1.0.2: DATA LOADING WITH DASK
# ==================================

# Read multiple CSV files
df4 = dd.read_csv("data/dask_data_*.csv")

# Display Dask DataFrame
print("\n========== DASK DATA ==========")
print(df4)

# Display actual records
print("\n========== DASK RECORDS ==========")
print(df4.compute())

# Display number of rows and columns
print("\n========== DASK SHAPE ==========")
print(df4.shape[0].compute(), df4.shape[1])