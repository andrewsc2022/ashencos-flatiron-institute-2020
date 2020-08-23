import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def readcsv(file_str):

    tests = pd.read_csv(file_str, encoding='unicode_escape')
    testsd = pd.DataFrame(data = tests)
    return(testsd)

income = readcsv("GTEXdata2.csv")
drop_list = []
gene_list = ["ACE2", "TMPRSS2", "CTSL", "CSTB"]
x=-1

newincome = pd.DataFrame(income)
#print(income.keys())
"""for i in income['Des']:

    x+=1
    if i not in gene_list:
   
        drop_list.append(x)
"""
#newincome['id2'] = newincome.index
newincome.set_index('ï»¿Des', inplace=True)
newincome = newincome.T
newincome = newincome.loc[:,~newincome.columns.duplicated()]
#print(newincome)
np.seterr(divide='ignore', invalid='ignore')

def r_square(variable, constant):

    x_values = list(newincome[variable])
    y_values = list(newincome[constant])
    
    correlation_matrix = np.corrcoef(x_values, y_values)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
        
    return(r_squared)

print("\U0001f600")
target_gene = ""
print("Type 'STOP' to proceed to graphing.\n")

while target_gene != "STOP":

    try:
        
        target_gene = input("Target gene: ")
        print("========================\n")
        for i in newincome.keys():
            if r_square(i, target_gene) > .8:
                print(str(i) + ": " + str(r_square(i, target_gene)))
        print("========================")
        
    except Exception:
        print("Gene not found\n")
        


while True:

    try:
        x_axis = input("Gene to graph on x-axis: ")
        y_axis = input("Gene to graph on y-axis: ")
        print("\nGenerating graph...\n")
        newincome.plot(x = x_axis, y = y_axis, kind = 'scatter')
        plt.show()
        
    except Exception:
        print("Gene(s) not found\n")
    

#compression_opts = dict(method='zip',
                        #archive_name='GTEXtrans.csv')
#newincome.to_csv('GTEXtrans.zip', index=False,
                 #compression=compression_opts)
