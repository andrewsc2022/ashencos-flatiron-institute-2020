import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns; sns.set()
import random

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def readcsv(file_str):

    tests = pd.read_csv(file_str, encoding='unicode_escape')
    testsd = pd.DataFrame(data = tests)
    return(testsd)

income = readcsv("GTEXdata2.csv")
income2 = readcsv("GTEXdata2.csv")
drop_list = []
#gene_list = ["ACE2","TMPRSS2","CTSL","CSTB","AAR2","AASS","AATF","ABCC1","ACAD9","ACADM","ACSL3","ADAM9","ADAMTS1","AGPS","AKAP8","AKAP8L","AKAP9","ALG11","ALG5","ALG8","ANO6","AP2A2","AP2M1","AP3B1","ARF6","ARL6IP6","ATE1","ATP13A3","ATP1B1","ATP5MG","ATP6AP1","ATP6V1A","BAG5","BCKDK","BCS1L","BRD2","BRD4","BZW2","C1orf50","CCDC86","CDK5RAP2","CENPF","CEP112","CEP135","CEP250","CEP350","CEP43","CEP68","CHMP2A","CHPF","CHPF2","CISD3","CIT","CLCC1","CLIP4","CNTRL","COL6A1","COLGALT1","COMT","COQ8B","CRTC3","CSDE1","CSNK2A2","CSNK2B","CUL2","CWC27","CYB5B","CYB5R3","DCAF7","DCAKD","DCTPP1","DDX10","DDX21","DNAJC11","DNAJC19","DNMT1","DPH5","DPY19L1","ECSIT","EDEM3","EIF4E2","EIF4H","ELOB","ELOC","EMC1","ERC1","ERGIC1","ERLEC1","ERMP1","ERO1B","ERP44","ETFA","EXOSC2","EXOSC3","EXOSC5","EXOSC8","F2RL1","FAM162A","FAM8A1","FAM98A","FAR2","FASTKD5","FBLN5","FBN1","FBN2","FBXL12","FKBP10","FKBP15","FKBP7","FOXRED2","FYCO1","G3BP1","G3BP2","GCC1","GCC2","GDF15","GFER","GGCX","GGH","GHITM","GIGYF2","GLA","GNB1","GNG5","GOLGA2","GOLGA3","GOLGA7","GOLGB1","GORASP1","GPAA1","GPX1","GRIPAP1","GRPEL1","GTF2F2","HDAC2","HEATR3","HECTD1","HMOX1","HOOK1","HS2ST1","HS6ST2","HSBP1","HYOU1","IDE","IL17RA","IMPDH2","INHBE","INTS4","ITGB1","JAKMIP1","LARP1","LARP4B","LARP7","LMAN2","LOX","MAP7D1","MARK1","MARK2","MARK3","MAT2B","MDN1","MEPCE","MFGE8","MIB1","MIPOL1","MOGS","MOV10","MPHOSPH10","MRPS2","MRPS25","MRPS27","MRPS5","MTARC1","MTCH1","MYCBP2","NARS2","NAT14","NDFIP2","NDUFAF1","NDUFAF2","NDUFB9","NEK9","NEU1","NGDN","NGLY1","NIN","NINL","NLRX1","NOL10","NPC2","NPTX1","NSD2","NUP210","NUP214","NUP54","NUP58","NUP62","NUP88","NUP98","NUTF2","OS9","PABPC1","PABPC4","PCNT","PCSK6","PDE4DIP","PDZD11","PIGO","PIGS","PITRM1","PKP2","PLAT","PLD3","PLEKHA5","PLEKHF2","PLOD2","PMPCA","PMPCB","POFUT1","POGLUT2","POGLUT3","POLA1","POLA2","POR","PPIL3","PPT1","PRIM1","PRIM2","PRKACA","PRKAR2A","PRKAR2B","PRRC2B","PSMD8","PTBP2","PTGES2","PUSL1","PVR","QSOX2","RAB10","RAB14","RAB18","RAB1A","RAB2A","RAB5C","RAB7A","RAB8A","RAE1","RALA","RAP1GDS1","RBM28","RBM41","RBX1","RDX","REEP5","REEP6","RETREG3","RHOA","RIPK1","RNF41","RPL36","RRP9","RTN4","SAAL1","SBNO1","SCAP","SCARB1","SCCPDH","SDF2","SELENOS","SEPSECS","SIGMAR1","SIL1","SIRT5","SLC25A21","SLC27A2","SLC30A6","SLC30A7","SLC30A9","SLC44A2","SLC9A3R1","SLU7","SMOC1","SNIP1","SPART","SRP19","SRP54","SRP72","STC2","STOM","STOML2","SUN2","TAPT1","TARS2","TBCA","TBK1","TBKBP1","TCF12","THTPA","TIMM10","TIMM10B","TIMM29","TIMM8B","TIMM9","TLE1","TLE3","TLE5","TM2D3","TMED5","TMEM39B","TMEM97","TOMM70","TOR1A","TOR1AIP1","TRIM59","TRMT1","TUBGCP2","TUBGCP3","TYSND1","UBAP2","UBAP2L","UBXN8","UGGT2","UPF1","USP13","USP54","VPS11","VPS39","WASHC4","WFS1","YIF1A","ZC3H18","ZC3H7A","ZDHHC5","ZNF318","ZNF503","ZYG11B"]
x=-1
gene_list = []


newincome2 = pd.DataFrame(income2)
newincome2.set_index('ï»¿Des', inplace=True)
newincome2 = newincome2.T
newincome2 = newincome2.loc[:,~newincome2.columns.duplicated()]

for i in range(0,10000):
    gene_list.append(random.choice(newincome2.keys()))

for i in gene_list:
    if newincome2[i].max() == 0:
        gene_list.remove(i)

newincome = pd.DataFrame(income)

for i in newincome['ï»¿Des']:

    x+=1
    if i not in gene_list:
   
        drop_list.append(x)

newincome = newincome.drop(index=newincome.index[drop_list])  
#newincome['id2'] = newincome.index
newincome.set_index('ï»¿Des', inplace=True)
newincome = newincome.T
newincome = newincome.loc[:,~newincome.columns.duplicated()]
#print(newincome)
np.seterr(divide='ignore', invalid='ignore')
for i in list(newincome.keys()):
    for e in list(newincome.index):

        newincome.at[e, i] = sigmoid(newincome.at[e, i])
        """
    if newincome[i].max() == 0:

        newincome[i] = newincome[i] / 1
        
    else:
        newincome[i] = newincome[i] / newincome[i].max()"""
        
ax = sns.heatmap(newincome, vmin=0, vmax=1)
plt.show()


"""
    

compression_opts = dict(method='zip',
                        archive_name='GTEXcontact.csv')
newincome.to_csv('GTEXconstact.zip', index=False,
                 compression=compression_opts)"""
learning_rate = 1