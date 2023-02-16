import pandas as pd

laneData= pd.read_csv("laneChange.csv")
print(laneData)

print(laneData.columns)

print(laneData.Vehicle_type)