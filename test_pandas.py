#! C:\Users\shirw\OneDrive\Documents\Tech2_NHH_part2\testN\Scripts\python.exe

import numpy as np
import pandas as pd

#data  = np.arange(5,10)
#print(data)
#test = pd.Series(data)
#print(test)

#example DataFrames

data1 = np.arange(15).reshape((-1,3))
print(data1)

var_names = ["A", "B", "C"]
test2 = pd.DataFrame(data1, columns=var_names)
print(test2)

#DataFrame from non-homogenous data as follows:

names  = ["Suc", "uew", "maa"]
bdates = pd.to_datetime(["2011-02-03","1985-01-02", "1997-05-12"])
Income = np.array([70000, 900000, np.nan])

# create Dataframes from dictionary

test3 = pd.DataFrame({
    "Name":names,
    "Birthdates": bdates,
    "Income":Income
    
})

print(test3)