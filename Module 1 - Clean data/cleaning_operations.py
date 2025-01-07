#--- Import Pandas ---
import pandas as pd
#--- Read in dataset(Uncleaned_employees_final_dataset.csv) ----

df = pd.read_csv("./Uncleaned_employees_final_dataset.csv")
data=df.copy()
data.dropna(inplace=True)

#--- Export the dataset as "employee.csv" ---
data.to_csv("employee",header=False)

#--- Inspect data ---
data.head()
