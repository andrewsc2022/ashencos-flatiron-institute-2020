import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def readcsv(file_str):

    tests = pd.read_csv(file_str, encoding='unicode_escape')
    testsd = pd.DataFrame(data = tests)
    return(testsd)

income = readcsv("networkcsv.csv")

newincome = pd.DataFrame(income)

np.seterr(divide='ignore', invalid='ignore')
newincome.pop("Function")
newincome = newincome.T
print("\U0001f600")
"""line_list = ['/','/','/','/','/','/','/','/','/','/','-','-','-','-','-','-','-','-','-','-','\\','\\','\\','\\','\\','\\','\\','\\','\\','\\','|','|','|','|','|','|','|','|','|','|']
while True:
    for i in line_list:
        print(i)
"""
print(newincome)
indices = list(newincome.keys())
print(indices)
#newincome = newincome.sort_values(0,axis=0)
print(newincome)
print(newincome.shape)
print(len(newincome))

#for i in range(len(newincome)):
new = newincome.loc[newincome[0] >= 2]
print(new)
for i in list(new.index):
    print(i)
#compression_opts = dict(method='zip',
                        #archive_name='GTEXtrans.csv')
#newincome.to_csv('GTEXtrans.zip', index=False,
                 #compression=compression_opts)
