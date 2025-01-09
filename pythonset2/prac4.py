import pandas as pd
import statistics as st
df = pd.read_csv(r"D:\vscode\pythonset2\studentDetail.csv") 
average = st.mean(df["Student_Marks"])
print(round(average,3))
print(df)