import pandas as pd
import tensorflow as tf
import random
import numpy as np
import matplotlib.pyplot as plt
import mglearn
import pprint
from sklearn import tree

def readcsv(file_str):

    tests = pd.read_csv(file_str, encoding="unicode_escape")
    testsd = pd.DataFrame(data = tests)
    return(testsd)

income = readcsv("GTEXdata2.csv")
income2 = readcsv("GTEXdata2.csv")
drop_list = []
drop_list_2 = []
#gene_list = ["GALNT10", "LIN7A", "SLC24A3", "PAK1", "PRDX1", "ZNF358", "SPRR1B", "TRIM5", "PRMT5", "DERL2", "DVL2", "MEF2D", "EFEMP1", "THBS1", "GALNT1", "HHIP", "SNAPIN", "PTPRK", "GJA5", "ATP5F1B", "NOTCH1", "RORA", "FZD4", "SCARB1", "ZER1", "DPM3", "USP16", "LGR4", "PPARD", "PDS5B", "RUNX3", "BNIPL", "RPS27L", "SIK1", "B2M", "SP3", "TMED2", "ARID5B", "MARCHF8", "VAPA", "RCHY1", "UBE2E1", "UBE2D1", "ERLIN1", "RNF11", "TRIM33", "GOLT1B", "UFL1", "CTNNBIP1", "TMEM101", "RNF135", "AFG3L2", "NUP214", "DPAGT1", "ANXA6", "ITPR1", "BTN2A1", "DHRS4", "ABI2", "LDB2", "AGTPBP1", "PARK7", "PSMC4", "NLK", "SIRT1", "ACD", "ATXN1", "KIF1B", "CYCS", "POLR3G", "RITA1", "JAG1", "MSH2", "SEPTIN11", "CLN6", "MAP2", "RIMBP2", "NOTCH2NLA", "TTC27", "AMBRA1", "SULT1A1", "MCF2L", "SMIM14", "AGR3", "RGL2", "TCEAL7", "TSR2", "FGD6", "RIOK2", "FAM174A", "SLC66A2", "PGR", "PYHIN1", "GABRA1", "DCP2", "TFB2M", "SEMA4A", "LBHD1", "G6PC3", "MRFAP1", "None", "MPHOSPH8", "LTA4H", "None", "SLC2A8", "None", "None", "FOXI1", "SNAP47", "SUGT1", "JADE1", "POLR3H", "RPL35", "COX7B", "COX7A2", "VGLL3", "YJU2", "None", "LYSMD2", "None", "PLCH2", "FAM13C", "HTR7", "TK2", "TMEM14A", "C19orf53", "AAMDC", "NSA2", "TXNL4B", "LRRC57", "VKORC1", "TTC32", "PRR15", "ABHD4", "SPIB", "ZIC2", "None", "PATJ", "HAUS1", "GUCA2B", "ATP5MC1", "SLC6A12", "CABLES2", "UGT8", "UMOD", "RPL26L1", "CNTRL", "DEPP1", "MTERF3", "AAAS", "None", "CKAP2L", "DUT", "ADGRE2", "RPRD1A", "STK26", "MRPL49", "PTH1R", "ZNF233", "RIOK3", "MARS2", "AKAP12", "RPS19BP1", "TTLL1", "KIAA0930", "SMO", "NDUFA3", "PDK2", "TOM1L2", "RILPL2", "MFSD14A", "GMCL2", "LRRFIP2", "AKR7A2", "ITPR3", "FXYD5", "TULP4", "RANBP9", "CFAP299", "POC5", "PAX6", "PLCB4", "FLII", "RABAC1", "TMEM11", "CYP2J2", "None", "EMC6", "FGG", "MIPEP", "THAP10", "DBF4B", "MYCT1", "MYO19", "MICU1", "RPS23", "RPS24", "DENND4C", "B3GALNT1", "None", "COPG1", "CMTM5", "NCAPH", "PPWD1", "CLDND1", "MRTO4", "CRYBG1", "SHC4", "TADA1", "THEM4", "GNAI1", "KIF4A", "MRPL18", "C1GALT1C1", "PRRC2C", "SRP14", "ELMOD1", "ROS1", "OSM", "UBE3B", "PRR4", "KLF8", "FAM160B2", "CNOT9", "DAPP1", "VPS35", "ZKSCAN7", "IMPA2", "MEF2C", "MEA1", "RPA2", "RPA3", "GSX1", "PPP1R14A", "N4BP2L2", "LIME1", "CARS2", "MCM10", "None", "SACM1L", "FAN1", "C15orf39", "CRIPT", "HOXD10", "SLC15A2", "TRAPPC13", "FMR1", "DPYD", "None", "OIP5", "SLC22A8", "PDCD2", "PSMB4", "PSMB3", "RDX", "REG1A", "ADPRM", "DHX57", "DYM", "FA2H", "DHRS11", "C1orf158", "JUND", "NVL", "CLTRN", "SEC61G", "DDI2", "CLPX", "DMRTB1", "PHTF2", "CLINT1", "BMPR1B", "MTPAP", "LRRC8D", "CDCA8", "ZYG11A", "TKFC", "IL7R", "C7", "TRIM46", "VCPIP1", "GAR1", "TNIP1", "ADAMTS6", "COL5A2", "CSMD3", "CDKL3", "MRPL27", "PCDHB13", "PCDHB9", "PLEKHA6", "NLGN1", "CFAP20", "WDR33", "GADD45GIP1", "KIAA0232", "H3-3A", "LYPD4", "IL1RL1", "SFXN2", "BATF", "MDP1", "IPMK", "MRPS15", "None", "NFIX", "NFIC", "PJVK", "ZMYM2", "SLC10A4", "LRRC45", "SLC25A10", "CSRP2", "HSPA14", "HSPA14", "ZMAT5", "SLC2A9", "IFIT3", "EPB41L1", "SH3GL2", "None", "RAD17", "SLC9A5", "CPD", "TXNDC12", "SEC24C", "TESMIN", "FAM98A", "RNF148", "MRPS35", "CREB3L4", "CYB5B", "RPL23", "EIF4E", "MRPS7", "VIPAS39", "PHLDB3", "None", "ALG6", "KLHL3", "None", "NIM1K", "MOB1A", "CDK12", "UBTF", "PLSCR1", "NCOA1", "NAT14", "ANKRD35", "CXXC4", "BOK", "RAB3GAP2", "AMER3", "CA3", "GIMAP6", "ZFAND6", "CCSER2", "MMD2", "PIAS2", "MAP3K6", "VASH1", "SNRPB2", "CYHR1", "C16orf74", "RPP25L", "PDE6D", "EFCAB7", "ZNF707", "RINT1", "DCUN1D1", "MMD", "CKS1B", "DOK3", "CENPW", "LAPTM4A", "PHACTR2", "EMC7", "PIP4P1", "SEMA4B", "NSUN7", "TEFM", "SLC22A11", "ADPGK", "SF3B5", "EDC3", "ASRGL1", "TRPS1", "ZNF610", "KIF3A", "GAS2L3", "ZNF224", "ZNF215", "ZNF226", "PHACTR3", "CD5", "None", "TMEM267", "KLHDC10", "SFTA2", "SPATA4", "None", "NRG4", "CSNK2A1", "TMA7", "ATRAID", "ARID3B", "CAB39L", "None", "SPRR3", "PDCD7", "TMPO", "PKIA", "POMT1", "CGA", "COX6A1", "LMBR1L", "TENM3", "H2BC9", "RPL9", "RPL11", "SEC62", "HS6ST3", "CDIPT", "WNT4", "None", "KIAA1257", "NLGN4X", "LHFPL4", "LRP3", "PON2", "LRRIQ3", "BBS5", "ARAF", "S1PR2", "SRSF11", "FAM20A", "OTUD6B", "TUBA3D", "ATP6V1B2", "SLC6A18", "TMEM62", "PUS7", "SLC27A5", "CDH11", "LIAS", "GLOD4", "None", "ANKDD1A", "C17orf99", "SEC11C", "HSPA9", "REXO2", "MIIP", "PTGER1", "None", "TMCO1", "S1PR1", "BLCAP", "CCDC59", "SLC30A7", "THNSL1", "TENT5A", "CFAP97", "GATA6", "GATM", "ECSCR", "NEMP1", "DEF6", "SAMD9L", "PHOSPHO1", "ISCA1", "RBP2", "GUF1", "MACIR", "ZNF804A", "HIKESHI", "TTN", "None", "ZFAT", "ARGLU1", "UROS", "DNM1L", "PCDH7", "SELENOH", "NUP42", "CADM3", "None", "None", "NDUFS6", "RPH3AL", "FUCA1", "CARMIL3", "TESC", "ANKRD11", "CLEC2D", "MUC13", "ADSS2", "TYW5", "TIMM8B", "DAZAP1", "GJB2", "CPXM2", "CCDC93", "PCNX1", "RASGRP4", "C1QTNF1", "SRPRA", "HES6", "SLC35E3", "RNASEK", "CLDN11", "FOXL1", "DUSP12", "RMND5B", "ILRUN", "EXO1", "ST8SIA4", "MRC2", "SRGAP3", "G3BP2", "TENT5B", "MFAP1", "TYMS", "PFDN4", "ENTPD1", "ENTPD2", "SRARP", "TEX30", "CPSF7", "EMP2", "POLR2G", "XPA", "INO80D", "DIRAS2", "ATOX1", "KIF27", "ZIC4", "MND1", "None", "HOXA3", "SLCO1A2", "ZC3H10", "CCAR1", "NUP54", "DR1", "GNPDA2", "CES3", "TMEM143", "RPL36AL", "KRTAP9-4", "PIGR", "NTNG2", "THYN1", "TCTA", "SPACA3", "SYNPO", "MEGF8", "ANO5", "ZNF71", "DAW1", "MRPL20", "None", "FCRL2", "PRXL2A", "YPEL4", "RAP1GDS1", "NYX", "ZCCHC10", "BABAM1", "HEBP2", "GDE1", "ARL15", "TACC1", "NAALADL1", "GNPDA1", "CCDC77", "VPS25", "VIL1", "CCL27", "PABPC1L", "BLVRA", "LAS1L", "TRIM66", "STK11IP", "TUBGCP5", "None", "ABHD10", "ZDHHC9", "ADCY1", "ADARB2", "RFX2", "AP4B1", "USP39", "CHRNG", "BCAS1", "MRPS36", "BORCS7", "DEPDC1", "CETN3", "FAU", "WDR78", "ZFYVE16", "None", "EFCAB12", "SCAF11", "GOLGA5", "HS3ST3B1", "PLGRKT", "MRPL36", "ACOD1", "COX7B2", "VPS26A", "METTL22", "DIABLO", "CCDC151", "None", "HOMER2", "EMSY", "TMED9", "C16orf72", "SH3YL1", "GSTK1", "MYDGF", "PRCP", "ZNF311", "COX10", "COX8A", "CPA1", "H4C11", "ANKRD36B", "SH3PXD2A", "MELTF", "NSL1", "RPL27", "RPL27A", "CYP39A1", "ZYG11B", "KRTAP9-8", "BZW2", "SNX24", "MAGEF1", "PIGX", "TIPIN", "GPX2", "AMACR", "ZNF747", "None", "TMC5", "NNMT", "None", "VCPKMT", "FKBP10", "WRAP73", "TMEM248", "NIF3L1", "CPED1", "FAM71E1", "SLC4A2", "MC1R", "SHLD2", "B3GNT5", "GASK1A", "SDCCAG8", "ARL14EP", "SDSL", "CROT", "LINS1", "SMG8", "COG2", "TWF1", "AJUBA", "CISD3", "EPM2AIP1", "ATP6V1G3", "RNF17", "MMP14", "PEG3", "OLA1", "VPS4A", "CDKN2AIP", "UBA52", "DCLK2", "CPNE8", "NAA11", "WIPF1", "VPS33A", "TMEM135", "SLC38A9", "SPATA7", "None", "CTC1", "RPS25", "TUBA8", "ACKR1", "ZNF652", "COBLL1", "GRB7", "CERCAM", "DYNC1LI1", "PLPP6", "PRSS8", "CTU2", "METTL3", "TPX2", "WDR91", "ARL6IP1", "ATP2B3", "TMEM179B", "SLC39A7", "SLC16A11", "DSEL", "ANKRA2", "GPRC5C", "UNC45A", "PPIP5K1", "FAM53B", "ELOB", "DUSP23", "CRELD2", "PDLIM3", "SMG7", "SNU13", "HPS6", "ERG", "STIL", "SLC25A5", "SPG11", "CHD9", "MDFIC", "CKAP4", "TTYH2", "FABP4", "SPDYE1", "SPDYE16", "FIS1", "DESI2", "ADPRHL1", "TFDP1", "NR2F1", "GPN1", "ENOPH1", "CLPS", "SLC25A21", "MAP9", "PLBD1", "HLA-DPA1", "ALKBH3", "ECRG4", "UFD1", "PSMA5", "LDAH", "GTF2H1", "FKRP", "PHF23", "CHMP5", "None", "VAMP7", "ELOF1", "MSX2", "None", "KDM6A", "WDR53", "PRDX4", "OSTC", "CACTIN", "DNAAF2", "LRIG1", "INSM2", "SYCP2", "MRPL2", "FSTL1", "RGS5", "PPFIA2", "RGCC", "SLC16A10", "PLAAT5", "MRAS", "RNLS", "COPS4", "CPT1C", "BCAS4", "PPP6R2", "KIAA0100", "H2AC8", "H2BC5", "OSBPL8", "SLC25A26", "None", "PAPLN", "ST8SIA2", "WFDC5", "ELOVL3", "NEK9", "TBX5", "PPIH", "TAFA4", "WSB1", "SCN2A", "ITPK1", "PRSS21", "GNRH1", "SPCS2", "RBFOX1", "MARVELD3", "ALG14", "MPP6", "NAXE", "HOXB9", "PAQR3", "CHAC2", "ATP5MG", "ARPC3", "None", "CHCHD1", "INTS9", "C8orf37", "RPL39", "TMEM106C", "RFTN2", "MTIF2", "EBPL", "TH", "TDO2", "HARBI1", "None", "CDKL2", "EFNB1", "RASL11B", "None", "CSTF2", "ING5", "GPR132", "NDE1", "COMMD9", "RANGRF", "SPRY3", "MRPL22", "BNC2", "KCTD9", "ELP5", "TMEM50A", "CCNDBP1", "CLEC4E", "TARS1", "SNRPN", "SERBP1", "BOLA3", "DYNLL1", "PDE12", "LYSMD3", "HMHB1", "HAPLN3", "UPB1", "KIAA1109", "PTPN2", "PTPN1", "TAF7L", "SLC26A11", "AREL1", "LMTK2", "GDI1", "HMMR", "SLC22A15", "FLI1", "FBN3", "ACE2","TMPRSS2","CTSL","CSTB","AAR2","AASS","AATF","ABCC1","ACAD9","ACADM","ACSL3","ADAM9","ADAMTS1","AGPS","AKAP8","AKAP8L","AKAP9","ALG11","ALG5","ALG8","ANO6","AP2A2","AP2M1","AP3B1","ARF6","ARL6IP6","ATE1","ATP13A3","ATP1B1","ATP5MG","ATP6AP1","ATP6V1A","BAG5","BCKDK","BCS1L","BRD2","BRD4","BZW2","C1orf50","CCDC86","CDK5RAP2","CENPF","CEP112","CEP135","CEP250","CEP350","CEP43","CEP68","CHMP2A","CHPF","CHPF2","CISD3","CIT","CLCC1","CLIP4","CNTRL","COL6A1","COLGALT1","COMT","COQ8B","CRTC3","CSDE1","CSNK2A2","CSNK2B","CUL2","CWC27","CYB5B","CYB5R3","DCAF7","DCAKD","DCTPP1","DDX10","DDX21","DNAJC11","DNAJC19","DNMT1","DPH5","DPY19L1","ECSIT","EDEM3","EIF4E2","EIF4H","ELOB","ELOC","EMC1","ERC1","ERGIC1","ERLEC1","ERMP1","ERO1B","ERP44","ETFA","EXOSC2","EXOSC3","EXOSC5","EXOSC8","F2RL1","FAM162A","FAM8A1","FAM98A","FAR2","FASTKD5","FBLN5","FBN1","FBN2","FBXL12","FKBP10","FKBP15","FKBP7","FOXRED2","FYCO1","G3BP1","G3BP2","GCC1","GCC2","GDF15","GFER","GGCX","GGH","GHITM","GIGYF2","GLA","GNB1","GNG5","GOLGA2","GOLGA3","GOLGA7","GOLGB1","GORASP1","GPAA1","GPX1","GRIPAP1","GRPEL1","GTF2F2","HDAC2","HEATR3","HECTD1","HMOX1","HOOK1","HS2ST1","HS6ST2","HSBP1","HYOU1","IDE","IL17RA","IMPDH2","INHBE","INTS4","ITGB1","JAKMIP1","LARP1","LARP4B","LARP7","LMAN2","LOX","MAP7D1","MARK1","MARK2","MARK3","MAT2B","MDN1","MEPCE","MFGE8","MIB1","MIPOL1","MOGS","MOV10","MPHOSPH10","MRPS2","MRPS25","MRPS27","MRPS5","MTARC1","MTCH1","MYCBP2","NARS2","NAT14","NDFIP2","NDUFAF1","NDUFAF2","NDUFB9","NEK9","NEU1","NGDN","NGLY1","NIN","NINL","NLRX1","NOL10","NPC2","NPTX1","NSD2","NUP210","NUP214","NUP54","NUP58","NUP62","NUP88","NUP98","NUTF2","OS9","PABPC1","PABPC4","PCNT","PCSK6","PDE4DIP","PDZD11","PIGO","PIGS","PITRM1","PKP2","PLAT","PLD3","PLEKHA5","PLEKHF2","PLOD2","PMPCA","PMPCB","POFUT1","POGLUT2","POGLUT3","POLA1","POLA2","POR","PPIL3","PPT1","PRIM1","PRIM2","PRKACA","PRKAR2A","PRKAR2B","PRRC2B","PSMD8","PTBP2","PTGES2","PUSL1","PVR","QSOX2","RAB10","RAB14","RAB18","RAB1A","RAB2A","RAB5C","RAB7A","RAB8A","RAE1","RALA","RAP1GDS1","RBM28","RBM41","RBX1","RDX","REEP5","REEP6","RETREG3","RHOA","RIPK1","RNF41","RPL36","RRP9","RTN4","SAAL1","SBNO1","SCAP","SCARB1","SCCPDH","SDF2","SELENOS","SEPSECS","SIGMAR1","SIL1","SIRT5","SLC25A21","SLC27A2","SLC30A6","SLC30A7","SLC30A9","SLC44A2","SLC9A3R1","SLU7","SMOC1","SNIP1","SPART","SRP19","SRP54","SRP72","STC2","STOM","STOML2","SUN2","TAPT1","TARS2","TBCA","TBK1","TBKBP1","TCF12","THTPA","TIMM10","TIMM10B","TIMM29","TIMM8B","TIMM9","TLE1","TLE3","TLE5","TM2D3","TMED5","TMEM39B","TMEM97","TOMM70","TOR1A","TOR1AIP1","TRIM59","TRMT1","TUBGCP2","TUBGCP3","TYSND1","UBAP2","UBAP2L","UBXN8","UGGT2","UPF1","USP13","USP54","VPS11","VPS39","WASHC4","WFS1","YIF1A","ZC3H18","ZC3H7A","ZDHHC5","ZNF318","ZNF503","ZYG11B"]
gene_list = ["A1CF", "AACS", "AAGAB", "AAK1", "AAMP", "AARS1", "AARSD1", "AASS", "ABCB1", "ABCB4", "ABCD1", "ABCD3", "ABHD11", "ABHD12", "ABHD14B", "ABR", "ACAA2", "ACACA", "ACAD8", "ACADVL", "ACAT1", "ACAT2", "ACBD6", "ACE2", "ACIN1", "ACLY", "ACOT1", "ACOT13", "ACOT8", "ACOX1", "ACP1", "ACP2", "ACSL1", "ACSL3", "ACSL4", "ACSL5", "ACSS1", "ACTA1", "ACTA2", "ACTB", "ACTBL2", "ACTN1", "ACTR1B", "ACTR2", "ACTR3", "ACTR3B", "ACYP1", "ADA", "ADARB1", "COQ8A", "ADD1", "ADH5", "ADK", "ADRM1", "ADSL", "AFP", "AGA", "AGFG2", "AGPAT5", "AGR2", "AGR3", "AGT", "AHNAK", "AHNAK2", "AIDA", "AIF1L", "AIG1", "AIMP1", "AK2", "AK3", "AK4", "AKAP12", "AKAP13", "AKAP7", "AKAP8", "AKAP9", "AKR1A1", "AKR1B1", "AKR1B15", "AKR1C1", "AKR1C2", "AKR1C3", "AKR7A2", "AKT1", "ALB", "ALDH18A1", "ALDH1A1", "ALDH1A2", "ALDH1B1", "ALDH2", "ALDH3A1", "ALDH3A2", "ALDH3B1", "ALDH4A1", "ALDH5A1", "ALDH9A1", "ALDOA", "ALDOC", "ALG1", "ALG11", "ALG13", "ALG8", "ALPI", "ALPP", "ALS2", "AMDHD2", "AMPD2", "ANAPC1", "ANK3", "ANKFY1", "ANKHD1", "ANKMY2", "ANKRD54", "ANKS1A", "ANLN", "ANO6", "ANP32A", "ANP32B", "ANXA1", "ANXA11", "ANXA13", "ANXA2", "ANXA3", "ANXA6", "AP1B1", "AP1G1", "AP1M1", "AP1S1", "AP2A1", "AP2B1", "AP2M1", "AP4M1", "APEX1", "API5", "APLP2", "APOA1", "NAXE", "APOA2", "APOB", "APOE", "APOL2", "APP", "APPL1", "APTX", "AQR", "ARCN1", "ARF3", "ARF4", "ARF5", "ARFGAP2", "ARFGAP3", "ARFGEF2", "ARFRP1", "ARHGAP1", "ARHGAP12", "ARHGEF1", "ARHGEF16", "ARHGEF6", "ARIH1", "ARL2BP", "ARL6IP1", "ARL6IP6", "ARMC10", "ARPC1A", "ARPC1B", "ARPC3", "ARPC4", "ARPC5", "ARPP19", "ARRB1", "ASCC2", "ASCC3", "ASF1A", "ASGR1", "ASL", "GET3", "ASNS", "ASPH", "ASPSCR1", "ATG16L1", "ATIC", "ATOX1", "ATP1A1", "ATP1B1", "ATP1B3", "ATP2A2", "ATP2A3", "ATP2B1", "ATP2B3", "ATP2B4", "ATP5F1A", "ATP5F1B", "ATP5F1C", "ATP5F1D", "ATP5PB", "ATP5MC1", "ATP5PD", "ATP5PF", "ATP6AP2", "ATP6V0A1", "ATP6V0A2", "ATP6V0A4", "ATP6V0C", "ATP6V1A", "ATP6V1B2", "ATP6V1C1", "ATP6V1D", "ATP6V1E1", "ATP6V1G1", "ATP8A1", "ATP8B1", "ATP9A", "ATP5IF1", "ATRX", "ATXN10", "ATXN2L", "ATXN7L3B", "AURKA", "AURKAIP1", "AURKB", "AVL9", "B3GAT3", "BAG4", "BAG6", "BAIAP2", "BAIAP2L1", "BANF1", "BAX", "BAZ1B", "BCAM", "BCAP29", "BCAP31", "BCAR3", "BCCIP", "BCL2L13", "BCL7C", "BCR", "BDH2", "BID", "BIN1", "BLOC1S2", "BLOC1S3", "BLVRB", "BMS1", "BOLA2", "BPTF", "BRAF", "BRCC3", "BRD3", "BRD4", "BSG", "BST2", "BTAF1", "BTF3", "BUB1B", "BUD31", "BYSL", "BZW1", "BZW2", "C11orf68", "C12orf29", "C12orf43", "ERG28", "GON7", "RTRAF", "METTL26", "VPS35L", "CYBC1", "C1D", "C1GALT1", "C1orf122", "C1QBP", "C20orf27", "LDAH", "MAIP1", "C4BPA", "C4orf33", "C5orf51", "C7orf50", "CA13", "CAB39", "CAB39L", "CAD", "CALD1", "CALR", "CALU", "CAMK1D", "CAMK2D", "CAMK2G", "CAND1", "CANX", "CAP1", "CAPG", "CAPN1", "CAPN2", "CAPN5", "CAPRIN1", "CAPZA1", "CAPZA2", "CARHSP1", "CARM1", "CASC4", "CASKIN2", "CASP3", "CAST", "CAT", "CAV1", "CAV2", "CBFB", "CBR1", "CBR3", "CBR4", "CBX3", "CBX5", "CC2D1A", "KYAT1", "AL441992.3", "KYAT3", "CCDC124", "CCDC134", "CCDC22", "CCDC25", "CCDC43", "CCDC47", "CCDC57", "CCDC58", "CCDC6", "CCDC85C", "CCDC90B", "CCK", "CCNA2", "CCNT1", "CCNY", "CCNYL1", "CCT2", "CCT3", "CCT5", "CCT6A", "CCT8", "CD151", "CD2AP", "CD44", "CD46", "CD47", "CD55", "CD59", "CD74", "CDA", "CDC26", "CDC40", "CDC42BPA", "CDC42EP4", "CDC5L", "CDC73", "CDCP1", "CDH1", "CDH17", "CDHR2", "CDHR5", "CDK1", "CDK2", "CDK4", "CDK5", "CDK7", "CDS1", "CDV3", "CEACAM1", "CEACAM6", "CEBPA", "CENPA", "CENPF", "CENPV", "CES1", "CETN2", "CFDP1", "CFL1", "CFL2", "CHAC2", "CHAF1B", "CHCHD3", "CHCHD4", "CHD1", "CHD1L", "CHD7", "CHD8", "CHERP", "CHKA", "CHMP4A", "CHMP7", "CHURC1", "CIRBP", "CISD3", "CIT", "CKAP4", "CKS1B", "CKS2", "CLASP1", "CLASP2", "CLCN5", "CLCN7", "CLDND1", "CLIC1", "CLINT1", "CLIP1", "CLIP2", "CLN6", "CLPP", "CLPTM1L", "CLPX", "CLTC", "CLTCL1", "CLU", "CMBL", "CMC1", "CMTM4", "CMTM6", "CMTM7", "CNN3", "CNNM2", "CNNM4", "CNOT2", "CNOT3", "CNOT8", "CNP", "CNPY2", "CNPY3", "CERT1", "COL5A1", "COMMD10", "COMMD6", "COMT", "COPB1", "COPB2", "COPE", "COPS7A", "COPS7B", "COQ6", "COQ9", "CORO1B", "CORO1C", "CORO7", "COTL1", "COX11", "COX16", "COX4I1", "COX5A", "COX6B1", "COX6C", "COX7B", "CPD", "CPM", "CPNE1", "CPNE2", "CPNE3", "CPNE7", "CPNE8", "CPS1", "CPSF2", "CPSF7", "CPT1A", "CPT2", "CPVL", "CREB1", "CRIPT", "CRNKL1", "CRTAP", "CRTC3", "CRYAB", "CRYL1", "CS", "CSDE1", "CSNK1G3", "CSRP1", "CSRP2", "CST3", "CSTF2", "CSTF2T", "CTNNA1", "CTNNA2", "CTNNB1", "CTNNBL1", "CTNND1", "CTPS2", "CTSA", "CTSB", "CTSD", "CTSZ", "CTTNBP2NL", "CTU1", "CUL1", "CUL2", "CWC15", "CXADR", "CXCR4", "CYB5B", "CYB5R3", "CYBA", "CYCS", "CYFIP1", "CYP2S1", "CYP2W1", "CYP51A1", "CCN1", "DAB2", "DAD1", "TKFC", "DARS1", "DBI", "DBN1", "DCAF11", "DCAF13", "DCAF6", "DCAF7", "DCAF8", "DCK", "DCP1A", "DCPS", "DCTPP1", "DCXR", "DDAH1", "DDC", "DDI2", "DDOST", "DDR1", "DDR2", "DDRGK1", "DDT", "DDX10", "DDX17", "DDX18", "DDX19A", "DDX19B", "DDX21", "DDX27", "DDX28", "DDX39A", "DDX39B", "DDX3X", "DDX47", "DDX5", "DDX50", "DDX56", "DDX58", "DECR1", "DEF8", "DEGS1", "DENND5B", "DERL1", "DHCR7", "DHFR", "DHODH", "DHRS11", "DHRS7B", "DHTKD1", "DHX15", "DHX30", "DHX38", "DHX8", "DHX9", "DIABLO", "DIP2B", "DIS3", "DLST", "DMAP1", "DMXL1", "DNAH5", "DNAJA1", "DNAJA2", "DNAJB1", "DNAJB11", "DNAJB2", "DNAJB4", "DNAJB6", "DNAJC1", "DNAJC13", "DNAJC17", "DNAJC19", "DNAJC2", "DNAJC21", "DNAJC25", "DNAJC5", "DNAJC8", "DNAJC9", "DNM1", "DNMT1", "DNTTIP1", "DOHH", "DOP1B", "DPM1", "DPP4", "DPP9", "DPY19L1", "DPY30", "DR1", "DSC2", "DSG2", "DSN1", "DST", "DSTN", "DTNBP1", "DUT", "DYNC1H1", "DYNC1LI1", "DYNC1LI2", "DYNLRB1", "DYNLT1", "EBAG9", "EBP", "ECD", "ECE1", "ECH1", "ECHDC1", "ECHDC3", "ECHS1", "ECI1", "ECI2", "EDF1", "EDIL3", "EEF1A1", "EEF1A2", "EEF1B2", "EEF1D", "EEF2", "EFEMP1", "EFTUD2", "EGFR", "EHBP1", "EHBP1L1", "EHD2", "EHMT1", "EHMT2", "EIF1", "EIF1AX", "EIF2B3", "EIF2B4", "EIF2B5", "EIF2S2", "EIF2S3", "EIF3A", "EIF3CL", "EIF3E", "EIF3I", "EIF3L", "EIF4A1", "EIF4A2", "EIF4A3", "EIF4G2", "EIF5A", "ELAVL1", "ELOVL1", "ELOVL5", "ELP2", "ELP4", "EML3", "EML4", "ENO1", "ENO2", "ENO3", "ENOPH1", "ENOSF1", "ENY2", "EPB41L2", "EPB41L4B", "EPB41L5", "EPCAM", "EPHA2", "EPHB3", "EPHX1", "EPHX2", "EPN1", "EPPK1", "EPRS1", "EPS15", "EPS15L1", "EPS8", "EPS8L3", "ERAP1", "ERBIN", "ERCC2", "ERCC5", "ERGIC1", "ERGIC2", "ERH", "ERI3", "ERLEC1", "ERMP1", "ERO1A", "ERP29", "ERP44", "ESD", "ETF1", "ETFB", "ETHE1", "EWSR1", "EXD2", "EXOC5", "EXOC6B", "EXOC8", "EXOG", "EXOSC1", "EXOSC4", "EXOSC6", "EXOSC7", "EZR", "F10", "F11R", "F3", "F5", "FABP1", "FABP5", "FADS1", "FAHD1", "OTULINL", "PHETA1", "FAM114A2", "FAM118B", "FAM120A", "RTL8C", "RETREG3", "PSME3IP1", "MCRIP1", "WASHC2A", "FAM83B", "FAM98A", "FAM98B", "FANCD2", "FANCI", "FARP1", "FARSA", "FARSB", "FAU", "FBLN1", "FBN1", "FBP1", "FBP2", "FBXO2", "FBXO22", "FCF1", "FCGRT", "FDX1", "FEN1", "FERMT1", "FERMT2", "FGD4", "FH", "FHL2", "FHL3", "FHOD1", "FIS1", "FITM2", "FKBP10", "FKBP15", "FKBP2", "FKBP3", "FKBP4", "FKBP5", "FKBP8", "FLII", "FLNA", "FLNB", "FLNC", "FLOT1", "FMNL1", "FN3K", "FNBP4", "FNDC3B", "FOLR1", "FOSL2", "FOXJ3", "FSCN1", "FTSJ1", "FUBP1", "FUCA2", "FUNDC2", "FUS", "FXN", "FXR1", "FXR2", "G6PD", "GABARAP", "GABARAPL1", "GABARAPL2", "GABPA", "GAK", "GALE", "GALK1", "GALK2", "GALM", "GALNS", "GALNT2", "GALNT5", "GALNT7", "GALT", "GANAB", "GAPDH", "GAPVD1", "GAR1", "GARS1", "GART", "GATA6", "GBA3", "NIPSNAP2", "GBE1", "GBF1", "GBP1", "GCAT", "GCHFR", "GCLM", "GCNT3", "GCSH", "GDA", "GDAP1", "GDF15", "GDI1", "GDI2", "GEMIN5", "GET4", "GFM1", "GGCX", "GGH", "GGT1", "GGT1", "GGT7", "GHDC", "GINS1", "GIPC2", "GIT1", "GJA9", "GLA", "GLB1", "GLDC", "GLG1", "GLOD4", "GLRX3", "GLS", "GLUL", "GLYCTK", "GLYR1", "GM2A", "GMDS", "GMFB", "GMNN", "GMPR2", "GMPS", "GNA11", "GNA12", "GNA13", "GNAI1", "GNAI2", "GNAI3", "GNB1", "GNB1L", "GNB2", "GNB4", "GNE", "GNG12", "GNPDA1", "GNPDA2", "GNPNAT1", "GOLGA2", "GOLGA4", "GOLGA5", "GOLM1", "GOLT1B", "GOPC", "GOSR2", "GOT2", "GPA33", "GPAA1", "GPC3", "GPD1", "GPD1L", "GPD2", "GPHN", "GPI", "GPKOW", "ADGRG2", "GPR89B", "GPRC5A", "GRHPR", "GRIPAP1", "GRPEL1", "GRSF1", "GSPT1", "GSPT2", "GSTA1", "GSTA2", "GSTK1", "GSTM1", "GSTM3", "GSTM4", "GSTO1", "GSTP1", "GSTZ1", "GTF2A1", "GTF2B", "GTF2F2", "GTF2H1", "GTF2I", "GTPBP4", "GUK1", "GYG1", "H1-0", "H2AZ2", "H2AX", "MACROH2A1", "H3-3A", "HAAO", "HADHA", "HADHB", "HAGH", "HARS1", "HARS2", "HAT1", "HAUS1", "HAUS5", "HAUS8", "HAVCR1", "HAX1", "HBA1", "HCCS", "HDAC1", "HDAC10", "HDAC2", "HDGF", "HDGFL3", "PUDP", "HDLBP", "HEATR1", "HELLS", "HEXA", "HEXB", "HGD", "HINT1", "HINT3", "HIRIP3", "H1-1", "H1-5", "H1-2", "H1-3", "H1-4", "H2AC6", "H2BC13", "H4C1", "H2AC21", "H2AC20", "H2BC21", "H3C15", "H2BU1", "HK1", "HK2", "HKDC1", "HLA-A", "HLA-B", "HLA-C", "HLA-E", "HLTF", "HM13", "HMBS", "HMG20A", "HMGA1", "HMGA2", "HMGB1", "HMGB2", "HMGCL", "HMGCLL1", "HMGCS1", "HMGCS2", "HMGN1", "HMGN2", "HMGN4", "HMGN5", "HMOX2", "JPT1", "HNF4A", "HNMT", "HNRNPA0", "HNRNPA1", "HNRNPA2B1", "HNRNPA3", "HNRNPAB", "HNRNPC", "HNRNPD", "HNRNPF", "HNRNPH1", "HNRNPH2", "HNRNPH3", "HNRNPK", "HNRNPL", "HNRNPM", "HNRNPR", "HNRNPU", "HNRNPUL1", "HOMER3", "HPCAL1", "HPDL", "HPGD", "HRAS", "RIDA", "HSBP1", "HSCB", "HSD17B11", "HSD17B12", "HSD17B2", "HSDL2", "HSP90AA1", "HSP90AB1", "HSP90B1", "HSPA1B", "HSPA2", "HSPA4", "HSPA4L", "HSPA5", "HSPA8", "HSPA9", "HSPB1", "HSPB11", "HSPD1", "HSPH1", "HTRA1", "HTRA2", "HTT", "HUWE1", "HYI", "HYOU1", "IARS1", "IARS2", "ICAM1", "IDH1", "IDH2", "IDH3A", "IDH3B", "IDH3G", "IDI1", "IDI2", "IFI35", "IFNGR1", "IGBP1", "IGF1R", "IGF2", "IGF2BP1", "IGF2BP2", "IGF2BP3", "IGF2R", "IK", "IKBIP", "IKBKG", "IL18", "ILF3", "ILKAP", "ILVBL", "IMMT", "IMPA2", "IMPAD1", "IMPDH1", "IMPDH2", "INF2", "INPP1", "INPP5K", "INSL4", "INSR", "INTS3", "IPO5", "IPO7", "IPO8", "IPO9", "IQGAP1", "IQGAP2", "IQGAP3", "IRF2BP2", "IRF2BPL", "IRGQ", "ISG15", "ISYNA1", "ITGA1", "ITGA3", "ITGA5", "ITGA6", "ITGAV", "ITGB1", "ITGB6", "ITPA", "ITPKA", "ITPKC", "ITPR1", "ITPR2", "ITPR3", "ITPRIP", "ITSN1", "ITSN2", "IVNS1ABP", "JUNB", "JUND", "JUP", "KALRN", "KARS1", "KCNAB2", "KCTD12", "KCTD3", "KDELR1", "KHK", "PUM3", "WASHC5", "SHTN1", "KIF11", "KIF1B", "KIF20A", "KIF3A", "KLC1", "KLHDC4", "KNTC1", "KPNA1", "KPNA2", "KPNA3", "KPNA4", "KPNA6", "KRAS", "KRT1", "KRT10", "KRT14", "KRT15", "KRT16", "KRT17", "KRT18", "KRT19", "KRT2", "KRT20", "KRT5", "KRT6A", "KRT6B", "KRT7", "KRT8", "KRT80", "KRT9", "KRTCAP2", "KTN1", "KYNU", "L1CAM", "LACTB2", "LAD1", "LAMA3", "LAMA5", "LAMB1", "LAMB3", "LAMC1", "LAMC2", "LAMP1", "LAMP2", "LARP7", "LARS1", "LCLAT1", "LCP1", "LDHA", "LDHD", "LEMD3", "LENG8", "P3H1", "LETM1", "LGALS1", "LGALS14", "LGALS2", "LGALS3", "LGALS3BP", "LGALS4", "LGMN", "LHPP", "LIG1", "LIG4", "LIMA1", "LIMCH1", "LIPA", "LLGL1", "LMBRD1", "LMBRD2", "LMF2", "LMNA", "LMNB1", "LMNB2", "LMO7", "LOX", "LPCAT1", "LPGAT1", "LPIN2", "LPL", "LRP1", "LRP2", "LRP5", "LRPAP1", "LRPPRC", "LRRC1", "LRRC14", "LRRC20", "LRRC40", "LRRCC1", "LRRFIP1", "LRRFIP2", "LRWD1", "LSM3", "LSM7", "LSS", "LTBP1", "LTN1", "LUC7L", "LUC7L2", "LXN", "LY6K", "LYAR", "LYPD3", "LYPLA2", "M6PR", "MACC1", "MACF1", "MAGI1", "MAGOH", "MAK16", "MAN1A1", "MAN1A2", "MAP1B", "MAP2K2", "MAP2K4", "MAP2K6", "MAP4", "MAP4K4", "MAP7", "MAP7D1", "MAPK1", "MAPK14", "MAPKAPK2", "MAPKAPK3", "MAPRE2", "MARCKS", "MARK2", "MARK3", "MAT2A", "MAT2B", "MAVS", "MBD2", "MBD3", "MCAM", "MCEE", "MCFD2", "MCM4", "MCM5", "MCM6", "MCTS1", "MDH1", "MDH2", "ME1", "ME2", "ME3", "MECR", "MED28", "MEN1", "MEP1A", "MEPCE", "MESD", "MET", "METAP2", "EEF1AKNMT", "METTL16", "MFN2", "MFSD10", "MFSD3", "MFSD5", "MGAT2", "MGAT4A", "OGA", "MGLL", "MGMT", "MGST2", "MGST3", "MICALL2", "MIER1", "MIF", "MIF4GD", "MINK1", "MINPP1", "MIPEP", "MKI67", "MRTFB", "MLH1", "AFDN", "MMAB", "MOCOS", "MOCS3", "MOGS", "MORC2", "MORF4L1", "MORF4L2", "MPG", "MPP6", "MPRIP", "MPZL1", "MRC2", "MRI1", "MRPL16", "MRPL20", "MRPL21", "MRPL23", "MRPL24", "MRPL27", "MRPL28", "MRPL40", "MRPL41", "MRPL43", "MRPL44", "MRPL47", "MRPL51", "MRPL55", "MRPS12", "MRPS18A", "MRPS24", "MRPS26", "MRPS30", "MRPS34", "MRPS36", "MRPS5", "MRPS6", "MRRF", "MSH2", "MSN", "MSRB2", "MTA2", "MTA3", "MTCH2", "MTHFD1", "MTHFD1L", "MTIF2", "MTIF3", "MTM1", "MTMR2", "MTPAP", "MTPN", "MTRR", "MTTP", "MTX1", "MTX2", "MUC13", "MUC16", "MUC17", "MVD", "MVK", "MVP", "MYADM", "MYBBP1A", "MYCBP", "MYD88", "MYEF2", "MYH10", "MYH14", "MYH9", "MYL12B", "MYL6", "MYL6B", "MYL9", "MYLK", "MYO1C", "MYO1D", "MYO6", "MYO7B", "MYOF", "NAA10", "NAA15", "NAA16", "NAB1", "NACA", "NACC1", "NAGLU", "NAMPT", "NANS", "NAP1L1", "NAP1L4", "NAPA", "NAPG", "NARS1", "NASP", "NBEAL1", "NBEAL2", "NCAPD2", "NCAPD3", "NCAPG", "NCBP1", "NCBP2", "NCEH1", "NCKAP1", "NCL", "NCLN", "NDUFA10", "NDUFA12", "NDUFA13", "NDUFA4", "NDUFA5", "NDUFA6", "NDUFA7", "NDUFAF2", "NDUFAF3", "NDUFB11", "NDUFB4", "NDUFB5", "NDUFB9", "NDUFS1", "NDUFS6", "NEDD4", "NEDD4L", "NES", "NEU1", "NEXN", "NFATC2", "NFKB2", "NFKBIB", "NFYB", "NHP2", "NIP7", "NIPBL", "NIPSNAP1", "NKAP", "NKIRAS2", "NLE1", "NME1", "NME2", "NMI", "NMRAL1", "NMT1", "NNT", "NOC2L", "NOC4L", "NOL11", "NOL12", "NOL7", "NOLC1", "NOM1", "NONO", "NOP10", "NOP14", "NOP58", "NOSIP", "NOTCH2", "NPC2", "NPEPL1", "NPM1", "NR3C1", "NRAS", "NRBP1", "NRBP2", "NSUN2", "NSUN4", "NT5C2", "NT5DC1", "NUB1", "NUCB1", "NUCB2", "NUCKS1", "NUDCD1", "NUDCD3", "NUDT1", "NUDT19", "NUDT2", "NUDT21", "NUDT4", "NUDT9", "NUF2", "NUP153", "NUP155", "NUP160", "NUP205", "NUP210", "NUP54", "NUP62", "NUP85", "NUP93", "NUP98", "NUSAP1", "NUTF2", "NVL", "NXF1", "OAT", "OCIAD1", "OCLN", "OGDHL", "OGFR", "OGT", "OLA1", "OPA1", "OPLAH", "OPTN", "OR1M1", "OS9", "OSBP", "OSBPL10", "OSBPL9", "OSTC", "OTUB1", "OVCA2", "OXCT1", "P4HA1", "P4HA2", "P4HB", "PABPC1", "PABPC4", "PACSIN3", "PAF1", "PAFAH1B1", "PAG1", "PAICS", "PAIP2", "PAK1", "PAK1IP1", "PAK2", "PALLD", "PANK4", "PAPOLA", "PAPSS1", "PAPSS2", "PARD6B", "PARK7", "PARN", "PARP1", "PAWR", "PBK", "PBLD", "PBXIP1", "PC", "PCBD1", "PCBD2", "PCBP2", "PCCA", "PCCB", "PCID2", "PCIF1", "PCK2", "PCNA", "PCNP", "PCYOX1", "PCYT2", "PDCD4", "PDCD6", "PDCD6IP", "PDCL", "PDE12", "PDE3A", "PDE4D", "PDE4DIP", "PDHA1", "PDHB", "PDHX", "PDIA3", "PDIA4", "PDIA5", "PDIA6", "PDK1", "PDLIM1", "PDLIM5", "PDLIM7", "PDXDC1", "PDZK1", "PEA15", "PEAK1", "PEG10", "PELP1", "PEPD", "PES1", "PEX11B", "PEX19", "PFDN2", "PFDN4", "PFDN5", "PFKFB4", "PFKM", "PFKP", "PFN1", "PGD", "PGK1", "PGLS", "PGM1", "PGM2", "PGM2L1", "PGRMC1", "PGRMC2", "PHB", "PHB2", "PHF3", "PHKG2", "PHPT1", "PHRF1", "PHYHIPL", "PICALM", "PIGF", "PIN4", "PIP4K2A", "PIR", "PITHD1", "PITPNA", "PITPNB", "PITPNM1", "PKLR", "PKP2", "PKP3", "PLA2G12B", "PLA2G2A", "PLA2G4A", "PLAA", "PLBD2", "PLCD3", "PLD1", "PLEC", "PLEKHA3", "PLEKHF2", "PLOD1", "PLOD2", "PLOD3", "PLS3", "PLSCR1", "PMVK", "PNKP", "PNN", "PNP", "PNPLA6", "PNPO", "PNPT1", "PODXL", "POFUT1", "POFUT2", "POLA1", "POLA2", "POLD1", "POLDIP2", "POLR1B", "POLR2A", "POLR2B", "POLR2D", "POLR2F", "POLR2H", "POLR2J", "POM121C", "PON1", "PON2", "POP4", "POR", "POTEI", "PPA1", "PLPP2", "PPAT", "PPFIBP1", "PPHLN1", "PPIA", "PPIB", "PPIC", "PPID", "PPIE", "PPIF", "PPIH", "PPIL2", "PPIL4", "PPM1F", "PPM1G", "PPME1", "PPP1CA", "PPP1CB", "PPP1CC", "PPP1R12C", "PPP1R14A", "PPP1R3G", "PPP1R7", "PPP1R8", "PPP2R1B", "PTPA", "PPP2R5A", "PPP2R5C", "PPP2R5D", "PPP2R5E", "PPP3CB", "PPP3R1", "PPP5C", "PPP6R1", "PPT2", "PRDX1", "PRDX2", "PRDX4", "PREP", "PRIM2", "PRKAA1", "PRKAA2", "PRKACA", "PRKAG1", "PRKAR1B", "PRKAR2A", "CAVIN3", "PRKCSH", "PRKDC", "PRKRIP1", "PRMT1", "PRMT5", "PROM1", "PRPF3", "PRPF31", "PRPF4B", "PRPF6", "PRPS1", "PRPS2", "PRRC1", "PRRC2A", "PRRC2B", "PRRC2C", "PRSS21", "PRSS8", "PSAP", "PSAT1", "PSIP1", "PSMA1", "PSMA3", "PSMA4", "PSMA5", "PSMA6", "PSMB3", "PSMB5", "PSMB6", "PSMB7", "PSMB8", "PSMB9", "PSMC5", "PSMD11", "PSMD13", "PSMD14", "PSMD2", "PSMD4", "PSMD6", "PSMD7", "PSMD8", "PSME1", "PSME2", "PSPH", "PTBP1", "PTGES2", "PTGES3", "PTGFRN", "PTK2", "PTK7", "PTPN12", "PTPN2", "PTPN23", "PTPN6", "PTPRH", "PTPRJ", "CAVIN1", "PTRH2", "PTS", "PUM1", "PUM2", "PUS1", "PUS3", "PUS7", "NECTIN2", "PWWP2A", "PXDN", "PYCR3", "PYGB", "PYGL", "QARS1", "QDPR", "QKI", "QPRT", "QRSL1", "QTRT2", "RAB10", "RAB11A", "RAB11B", "RAB11FIP1", "RAB13", "RAB18", "RAB1B", "RAB21", "RAB22A", "RAB25", "RAB27B", "RAB32", "RAB35", "RAB3GAP1", "RAB3GAP2", "RAB5A", "RAB5B", "RAB5C", "RAB6A", "RAB7A", "RAB8A", "RABEPK", "RABGAP1", "RAC1", "RACGAP1", "RAD21", "RAD23A", "RAF1", "RALA", "RALB", "RALGAPA2", "RALY", "RALYL", "RAN", "RANBP2", "RANGAP1", "RAP1A", "RAP1B", "RAP1GDS1", "RAP2A", "RAP2B", "RAPGEFL1", "RARS1", "RASAL2", "RB1", "RBBP4", "RBBP9", "RBFOX2", "RBKS", "RBM10", "RBM12", "RBM25", "RBM26", "RBM27", "RBM34", "RBM4", "RBM47", "RBM4B", "RBM7", "RBMS1", "RBMS2", "RBMX", "RBMXL1", "RBP4", "RCC1", "RCC2", "RCN1", "RCOR1", "RCOR3", "RDH11", "RDX", "REEP5", "RELL1", "RER1", "RETSAT", "REXO2", "RFC1", "RFC2", "RFC4", "RFK", "RGPD5", "RHBDD2", "RHOA", "RHOB", "RHOC", "RHOF", "RHOT1", "RHOT2", "RILP", "RIN2", "RIOK2", "RNASET2", "RNF121", "RNF128", "RNF170", "RNF20", "RNF213", "RNF220", "RNF40", "RNH1", "RNPEP", "ROCK2", "ROMO1", "RP2", "RPA1", "RPE", "RPF2", "RPIA", "RPL10", "RPL13A", "RPL14", "RPL15", "RPL18", "RPL19", "RPL21", "RPL22", "RPL23", "RPL23A", "RPL27", "RPL27A", "RPL28", "RPL29", "RPL3", "RPL34", "RPL35", "RPL35A", "RPL36", "RPL36A", "RPL36AL", "RPL37A", "RPL4", "RPL6", "RPL7", "RPL7A", "RPLP0", "RPLP2", "RPN1", "RPP30", "RPP40", "RPS10", "RPS12", "RPS16", "RPS18", "RPS19", "RPS19BP1", "RPS27A", "RPS28", "RPS3", "RPS3A", "RPS4X", "RPS6KA1", "RPS6KA3", "RPS6KB1", "RPS7", "RPS8", "RPSA", "RRAS", "RRAS2", "RRM1", "RRM2", "RRM2B", "RRP36", "RRP7A", "RRP8", "RRS1", "RSAD1", "RSF1", "RSL1D1", "RSL24D1", "RSRC2", "RSU1", "RTN4IP1", "RUFY1", "RUVBL2", "S100A10", "S100A11", "S100A13", "S100A4", "S100P", "SAE1", "SAFB", "SAFB2", "SAMD9", "SAMHD1", "SAP30", "SAR1B", "SARS1", "SARS2", "SART3", "SCAF11", "SCAMP1", "SCAPER", "SCARB1", "SCARB2", "SCCPDH", "SCD", "SCO1", "SCO2", "SCP2", "SCRN3", "SCYL1", "SDAD1", "SDC1", "SDC4", "SDCBP", "SDCBP2", "SDF2L1", "SDF4", "SDHA", "SDHAF2", "SDHD", "SEC16A", "SEC22B", "SEC23A", "SEC23B", "SEC24A", "SEC61A1", "SEC61A2", "SEC61B", "SEC63", "SEPTIN10", "SEPTIN11", "SEPTIN6", "SEPTIN8", "SELENOW", "SERBP1", "SERF2", "SERINC1", "SERINC3", "SERPINA1", "SERPINB1", "SERPINB5", "SERPINB6", "SERPINH1", "SET", "SETD3", "SF1", "SF3A2", "SF3B4", "SF3B5", "SFN", "SFXN1", "SFXN4", "SFXN5", "SGPL1", "SGTA", "SH3BGRL2", "SH3BGRL3", "SH3D19", "SH3GL1", "SH3GL2", "SH3KBP1", "SH3PXD2B", "SH3RF1", "SHH", "SHMT1", "SHMT2", "SHROOM2", "SI", "SIGIRR", "SIN3A", "MTREX", "SKP1", "SLAIN2", "SLC12A4", "SLC12A6", "SLC12A7", "SLC12A9", "SLC15A1", "SLC16A1", "SLC16A3", "SLC16A7", "SLC1A3", "SLC20A1", "SLC22A18", "SLC22A5", "SLC23A1", "SLC25A11", "SLC25A13", "SLC25A15", "SLC25A19", "SLC25A24", "SLC25A4", "SLC25A5", "SLC26A2", "SLC26A3", "SLC29A1", "SLC2A5", "SLC2A9", "SLC30A1", "SLC30A8", "SLC38A7", "SLC39A10", "SLC39A14", "SLC39A4", "SLC39A7", "SLC3A2", "SLC41A3", "SLC44A2", "SLC4A7", "SLC6A8", "SLC7A5", "SLC9A3R1", "SLC9A3R2", "SLCO2B1", "SLK", "SMAD2", "SMAD3", "SMAD4", "SMARCA1", "SMARCA2", "SMARCA4", "SMARCA5", "SMARCAD1", "SMARCB1", "SMARCC1", "SMARCC2", "SMARCE1", "SMC1A", "SMC2", "SMC3", "SMC4", "PPP4R3A", "PPP4R3B", "SMG1", "SMN1", "SMN2", "SMOC1", "SNAPIN", "SNCA", "SNCG", "SND1", "SNF8", "SNRNP200", "SNRNP40", "SNRPA", "SNRPA1", "SNRPC", "SNRPD2", "SNRPE", "SNRPF", "SNUPN", "SNX1", "SNX12", "SNX15", "SNX2", "SNX24", "SNX3", "SNX30", "SNX5", "SNX6", "SNX7", "SNX9", "SOD1", "SOD2", "SOD2", "SON", "SORL1", "SOX11", "SP1", "SP100", "SP3", "SP6", "SPAG9", "SPAST", "SPC24", "SPC25", "SPCS2", "SPCS3", "SPEN", "SPART", "SPG7", "SPINT1", "SPINT2", "SPTAN1", "SPTBN1", "SPTBN2", "SPTLC2", "SQLE", "SQOR", "SQSTM1", "SRC", "SRP54", "SRP68", "SRP9", "SRPK2", "SRPRB", "SRR", "SRRM2", "SRRT", "SRSF1", "SRSF10", "SRSF2", "SRSF3", "SRSF4", "SRSF6", "SRSF8", "SRSF9", "SS18L1", "SSB", "SSBP1", "ITPRID2", "SSH3", "SSR2", "SSR4", "SSU72", "ST14", "STAC2", "STAG1", "STAG2", "STAP2", "STARD10", "STAT3", "STAT5B", "STAT6", "STAU1", "STAU2", "STEAP3", "STIM2", "STIP1", "STK10", "STK24", "STK3", "STMN1", "STOM", "STOML2", "STRAP", "STRN", "STRN3", "STRN4", "STT3B", "STUB1", "STX12", "STX18", "STXBP2", "SUB1", "SUCLG1", "SULT1B1", "SULT1E1", "SULT2A1", "SUMF2", "SUOX", "SUPT16H", "SUPT6H", "SUPV3L1", "SURF4", "SVIL", "SYAP1", "SYF2", "SYMPK", "SYNCRIP", "SYNGR2", "SYNPO", "SYPL1", "TAB2", "TACO1", "TAF15", "TAGLN", "TAGLN2", "TALDO1", "TANK", "TAOK3", "TAPT1", "TARS1", "TARS2", "TBC1D17", "TBC1D2", "TBC1D4", "TBCA", "TBCE", "TBCE", "TBL2", "TBL3", "TBPL2", "TBRG4", "TCEA1", "TCEAL4", "ELOB", "TCERG1", "TCIRG1", "TCP1", "TDP2", "TDRD7", "TECR", "TELO2", "TERF2IP", "TEX10", "TF", "TFAM", "TFCP2", "TFIP11", "TFRC", "TGFB1I1", "TGFBI", "TGFBRAP1", "TGOLN2", "THBS1", "THRAP3", "THUMPD1", "THY1", "TIA1", "TIAL1", "TIMM23", "TIMM44", "TIMM50", "TIMM8A", "TIMM8B", "TIPRL", "TJP1", "TJP2", "TK1", "TKT", "TLN1", "TLN2", "TM4SF1", "TM9SF4", "TMBIM1", "TMBIM6", "TMED10", "TMED2", "TMED5", "TMEM11", "TMEM141", "TMEM165", "TMEM167B", "TMEM176B", "TMEM186", "TMEM19", "TMEM30A", "TMEM33", "TLCD4", "TMEM9", "TMEM97", "TMF1", "TMOD2", "TMOD3", "TMPO", "TMSB4X", "TNFAIP2", "TNFAIP8", "TNKS1BP1", "TNPO1", "TNPO2", "TOM1", "TOM1L2", "TOMM20", "TOMM40L", "TOMM5", "TOMM70", "TOP2A", "TOP2B", "TOR1A", "TOR1AIP1", "TOR1AIP2", "TOR1B", "TP53BP1", "TPD52", "TPD52L1", "TPI1", "TPM1", "TPM3", "TPM4", "TPMT", "TPP2", "TPR", "TPT1", "TPX2", "TRA2B", "TRADD", "TRAF2", "TRAP1", "TRAPPC1", "TRAPPC2L", "TRAPPC3", "TRAPPC6A", "TRIM16", "TRIM25", "TRIM65", "TRIO", "TRIP13", "TRIP6", "TRMT11", "TRMT112", "TRPC4", "TSC22D1", "TSC22D2", "TSC22D4", "TSEN34", "TSFM", "TSG101", "TSPAN13", "TSPAN15", "TSPAN31", "TSPAN6", "TSPAN8", "TSPO", "TSPYL1", "TSR2", "TSSC4", "TSTA3", "TSTD1", "TTC19", "TTC27", "TTC37", "TTC38", "TTC39C", "TTC4", "TTLL12", "TTR", "TUBA1A", "TUBA1C", "TUBA4A", "TUBA8", "TUBAL3", "TUBB", "TUBB2A", "TUBB2B", "TUBB3", "TUBB6", "TUBG1", "TUFM", "TUFT1", "TWF1", "TWF2", "TWISTNB", "TXN", "TXN2", "TXNDC5", "TXNL1", "TXNL4A", "TXNRD1", "TYMS", "U2AF1", "U2AF2", "UAP1", "UBA1", "UBA2", "UBA3", "UBA52", "UBA6", "UBAC2", "UBAP2L", "UBE2C", "UBE2D1", "UBE2D2", "UBE2E1", "UBE2E3", "UBE2H", "UBE2I", "UBE2L3", "UBE2N", "UBE2R2", "UBE2T", "UBE2V1", "UBE2Z", "UBL4A", "UBL5", "UBLCP1", "UBN2", "UBQLN1", "UBQLN4", "UBR7", "UBXN1", "UBXN7", "UCHL1", "UEVLD", "UFM1", "UGDH", "UGGT1", "UGGT2", "UGT1A1", "UGT1A6", "UGT2A3", "UHRF1", "UHRF2", "UIMC1", "UQCRB", "UQCRC2", "UQCRFS1", "UQCRH", "UQCRQ", "URB1", "URB2", "URM1", "ATP5MD", "USO1", "USP10", "USP11", "USP16", "USP36", "USP4", "USP5", "USP9X", "UTP11", "UTP15", "UTRN", "UXS1", "UXT", "VAMP2", "VAMP3", "VAMP8", "VAPA", "VAPB", "VARS1", "VASN", "VCL", "VCP", "VCPIP1", "VDAC1", "VDAC2", "VDAC3", "VIL1", "VILL", "VIM", "VPS11", "VPS18", "VPS25", "VPS26A", "VPS26B", "VPS35", "VPS36", "VPS37A", "VPS41", "VPS45", "VRK1", "VSNL1", "VTN", "WAPL", "WARS1", "WARS2", "WASL", "WBP2", "RCC1L", "BUD23", "WDFY1", "WDR1", "WDR26", "WDR3", "WDR37", "WDR4", "WDR46", "WDR55", "WDR70", "WDR82", "WDR92", "NSD2", "WIPI1", "WIPI2", "WLS", "WNK1", "WNK2", "WRNIP1", "WTAP", "XIAP", "XPNPEP1", "XPO4", "XPO7", "XRCC4", "XRCC5", "XRCC6", "ATP23", "XRN2", "YAP1", "YARS1", "YBX1", "YES1", "YIPF1", "YIPF6", "YKT6", "YLPM1", "YTHDC2", "YTHDF1", "YTHDF2", "YTHDF3", "YWHAB", "YWHAE", "YWHAG", "YWHAH", "YWHAQ", "YWHAZ", "YY1", "ZBTB7A", "ZC3H4", "ZC3HAV1", "ZC3HC1", "ZCRB1", "ZDHHC13", "ZDHHC17", "ZDHHC5", "ZFAND2B", "ZFPL1", "ZFYVE16", "ZFYVE19", "ZMPSTE24", "ZNF195", "ZNF207", "ZNF253", "ZNF333", "ZNF592", "ZNF598", "ZNF622", "ZNF830", "ZNHIT2", "ZRANB2", "ZWILCH", "ZYX"]
gene_list_2 = []
x=-1

print(len(gene_list))

newincome2 = pd.DataFrame(income2)

for i in newincome2['ï»¿Des']:
	x+=1
	
	if i in gene_list:
		drop_list_2.append(x)
newincome2 = newincome2.drop(index=newincome2.index[drop_list_2]) 
newincome2.set_index("ï»¿Des", inplace=True)

newincome2 = newincome2.T
newincome2 = newincome2.loc[:,~newincome2.columns.duplicated()]
rand_list = []

for i in range(0,480):
   	rand_list.append(random.choice(newincome2.keys()))

for i in range(0,4950):
    gene_list_2.append(random.choice(newincome2.keys()))

for i in gene_list_2:
    if newincome2[i].max() == 0:
        gene_list_2.remove(i)
    elif newincome2[i].mean() <= 1:
    	gene_list_2.remove(i)

newincome = pd.DataFrame(income)
x = -1
for i in newincome['ï»¿Des']:

    x+=1
    if i in gene_list_2 and i in gene_list:
    	gene_list_2.remove(i)
    if i not in gene_list and i not in gene_list_2:
   
        drop_list.append(x)

print(len(gene_list_2))

newincome = newincome.drop(index=newincome.index[drop_list]) 
newincome.set_index('ï»¿Des', inplace=True)
newincome = newincome.T
newincome = newincome.loc[:,~newincome.columns.duplicated()]

np.seterr(divide='ignore', invalid='ignore')
for i in list(newincome.keys()):
    """for e in list(newincome.index):

        newincome.at[e, i] = sigmoid(newincome.at[e, i])
    """   
    if newincome[i].max() == 0:

        newincome[i] = newincome[i] / 1
        
    else:
        newincome[i] = newincome[i] / newincome[i].max()
        #newincome[i] = (newincome[i] - newincome[i].mean()) / np.std(list(newincome[i]))

for i in list(newincome2.keys()):
    """for e in list(newincome.index):

        newincome.at[e, i] = sigmoid(newincome.at[e, i])
    """   
    if newincome2[i].max() == 0:

        newincome2[i] = newincome2[i] / 1
        
    else:
        newincome2[i] = newincome2[i] / newincome2[i].max()
        #newincome[i] = (newincome[i] - newincome[i].mean()) / np.std(list(newincome[i]))

newincome = newincome.T
newincome2 = newincome2.T
#print(newincome)
target = []
target2 = []

for i in range(len(list(newincome.index))):
	target.append("")

for i in range(len(list(newincome2.index))):
	target2.append("")

newincome["target"] = target

for i in list(newincome.index):

	if i in gene_list:
		newincome.at[i, "target"] = 1
	else:
		newincome.at[i, "target"] = 0

from sklearn.model_selection import train_test_split

y = np.asarray(newincome.iloc[:, 54].values)
y = y.astype("int32")

X = np.asarray(newincome.iloc[:, 0:54].values)
X = X.astype("float32")

X_new = np.asarray(newincome2.iloc[:, 0:54].values)
X_new = X_new.astype("float32")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05,
 random_state=1)
t = newincome.pop('target')
feature_cols = list(newincome.keys())

"""from sklearn.cluster import KMeans
# generate synthetic two-dimensional data
# build the clustering model
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
print("Cluster memberships:\n{}".format(kmeans.labels_))
print(kmeans.predict(X))
mglearn.discrete_scatter(X[:, 0], X[:, 1], kmeans.labels_, markers='o')
mglearn.discrete_scatter(
	kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], [0, 1],
	markers='^', markeredgewidth=2)
plt.show()"""
"""
from sklearn.ensemble import GradientBoostingClassifier
X_train, X_test, y_train, y_test = train_test_split(
 X, y, random_state=0)
gbrt = GradientBoostingClassifier(learning_rate=1.3, random_state=2, warm_start=True, max_depth=1, subsample=0.8,verbose=1)
gbrt.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(gbrt.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(gbrt.score(X_test, y_test)))
"""

from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(
    n_estimators=100,
    max_depth=90,
    bootstrap=True,
    max_features='auto'
    #max_depth=25,
)

clf.fit(X_train,y_train)

y_pred=clf.predict_proba(X_test)
def prob_list(threshold, proba):
    prob_labels = []
    for i in range(len(proba)):
        if proba[i][0] >= threshold:
            prob_labels.append(1-proba[i][0])
        else:
            prob_labels.append(proba[i][1])
    return(prob_labels)
prob_list = prob_list(0.5, y_pred)
#print(prob_list)
#print(y_pred)

def to_binary(threshold, proba):
    test_labels = []
    for i in range(len(proba)):
        if proba[i][0] >= threshold:
            test_labels.append(0)
        else:
            test_labels.append(1)
    return(test_labels)

y_pred = to_binary(0.5, y_pred)
plt.plot(prob_list, y_test, 'o', color='DarkBlue');
plt.show()

y_new = list(pd.DataFrame(data = clf.predict_proba(X_new))[1])

newincome2["target"] = y_new

all_list = []

for i in list(newincome2.index):
	if newincome2.at[i, "target"] >= 0.83:
		all_list.append(i)
		print(i)

#for e in all_list:
	#print(e)
hubber_list = ["CSTB", "PALLD", "ABL1", "ABR", "JAG1", "TES", "TRPC4AP", "ENO2", "ENG", "ENO1", "TRIM28", "SGSH", "LTBR", "LTBP3", "LTBP2", "ITPKC", "CYBB", "CFP", "DAXX", "CFD", "PILRA", "ANXA5", "ANXA6", "ANXA1", "ANXA2", "XAB2", "CREB3L1", "USF2", "TMED9", "ACADVL", "LGALS9", "NAGK", "CDV3", "SMG9", "MICALL1", "TNFRSF1B", "TNFRSF1A", "BAX", "PRCC", "PRAF2", "RNF24", "LRRFIP1", "YWHAE", "PDLIM5", "RBCK1", "TGOLN2", "MCOLN1", "MICAL2", "PPM1F", "ZNF592", "FCER1G", "TNC", "MGAT1", "MFGE8", "R3HDM4", "TMEM259", "GANAB", "PTPN23", "CAPN2", "PI4KB", "TIMP3", "TIMP1", "TIMP2", "GIT1", "FAM3A", "TMBIM1", "BASP1", "SSH3", "EPHA2", "CTDSP1", "GRK6", "NKIRAS2", "DDA1", "BRD9", "NME4", "NNMT", "NMT1", "SORBS3", "SNX11", "CRISPLD2", "ARID1A", "KLC2", "ELOVL1", "ZFAND3", "CHD8", "TINF2", "WIPF2", "ACTB", "SLC3A2", "SLC4A2", "SMTN", "MAZ", "UPP1", "NR1H2", "USP4", "MIER2", "CPSF1", "RBM15B", "CDK9", "TRIOBP", "STX10", "ANTXR2", "DUSP7", "DUSP6", "DUSP1", "DUSP5", "DUSP3", "GTPBP2", "POLD4", "KLHL36", "BCR", "CCN2", "SLC38A7", "MYO1F", "ACTG2", "ACTG1", "ACTC1", "RNF216", "TOLLIP", "CREB3", "NXF1", "CAP1", "CCND2", "CCND3", "DNM2", "MTMR14", "PLXND1", "BRAT1", "SLC35A4", "MMP14", "MMP19", "HLX", "USP22", "MAN2B2", "LRRC59", "SNAPC2", "NAGA", "NAB2", "PECAM1", "ADM", "ACTN1", "WNK1", "CSRNP1", "BCL7C", "DEF8", "GSN", "GSK3A", "PARVB", "CABIN1", "SRRM2", "USP36", "C11orf24", "SUPT6H", "SURF4", "IGF2BP2", "STK10", "TRAF2", "WAS", "WARS1", "NOL6", "FLNB", "MGAT4B", "B4GALT7", "PNKP", "NPC2", "COLGALT1", "MVP", "MED12", "ITGB2", "ITGAL", "ITGAX", "SLC35B2", "SERINC2", "ARL8A", "MAP3K11", "MRPL12", "TUBA1B", "RRBP1", "RRAS", "CAMK2G", "CALR", "CALU", "SERPINA1", "CDC42EP1", "GPAA1", "G6PD", "FYN", "DLGAP4", "BCAR1", "EHBP1L1", "ATN1", "GRB10", "GRB2", "RAPGEF1", "SELENOM", "SELENOW", "ABCD1", "JOSD2", "STING1", "GNA15", "GNA11", "SLC27A1", "HDLBP", "HDGF", "TRMT61A", "PLEKHM2", "LCP1", "P4HB", "MYO1B", "FAM219A", "TSPAN4", "MAPK3", "MAPK7", "C16orf58", "FAM50A", "ARHGEF1", "FKBP8", "PEA15", "MFSD12", "TMEM158", "ARAP1", "ACAP3", "HEG1", "SDC3", "SLC25A44", "ICAM1", "MAP3K3", "ANAPC15", "RHOQ", "RAB1B", "TCF3", "CCDC22", "CDC42EP2", "IFI30", "RBM42", "GOLGA3", "GOLGA2", "ATG9A", "NUP62", "KPNA6", "POM121", "SENP3", "CASKIN2", "ERF", "LYPLA2", "SIRT6", "ANPEP", "DBN1", "PER1", "CLIC1", "ARF1", "ARF3", "CKAP4", "FERMT2", "PORCN", "SPATA20", "FHL3", "FHL2", "FHL1", "MOSPD3", "TSPAN14", "PCBP4", "ARSA", "LSR", "KLF13", "DYNC1H1", "PPP2R1A", "ATP6AP1", "ATP6V0B", "SLC1A5", "SLC2A3", "UBTD1", "TYROBP", "RHOF", "KLF7", "SLC27A3", "HBEGF", "DNAJB2", "CAMTA2", "KRT17", "SETD5", "MAP1S", "LUZP1", "TMC6", "FKBP9", "PTBP1", "LAPTM5", "TP53INP2", "CLPTM1", "CLN3", "TPP1", "MEX3D", "ZNF787", "SEZ6L2", "NUPR1", "LPCAT1", "MRTFA", "INF2", "GARS1", "LRRC32", "MAP3K14", "CLSTN1", "MMP9", "HLA-DQB1", "HLA-DPB1", "HLA-DPA1", "DNAJB5", "TMEM184B", "BCL9L", "RENBP", "RELB", "RELA", "UPF1", "SLC12A9", "TIAF1", "SF3B4", "CDK2AP2", "GTF2F1", "PPDPF", "FKRP", "MBOAT7", "IGSF8", "PLTP", "PLXNA1", "NUMA1", "EXT1", "VAMP2", "KCTD12", "HK1", "SCAMP2", "SPRED2", "AKT1S1", "PKD1", "PKM", "TFPT", "VASP", "VARS1", "RNPEPL1", "SIPA1", "SCAF1", "CACTIN", "LRFN4", "PRR14", "YIPF2", "SLC2A4RG", "NSMF", "C5AR1", "NEDD9", "NCF4", "ZMIZ1", "TUBB4B", "TUBB3", "TSTA3", "PHLDA2", "MRPL2", "SLC25A22", "COL4A2", "COL4A1", "DBNL", "IER5", "UBAP1", "BAG3", "ATF5", "HCFC1R1", "KIF21B", "AKIP1", "TLE5", "AP2A1", "AP2A2", "AP1B1", "TNKS1BP1", "MAP2K2", "MAP2K3", "ALDOA", "CUX1", "PSME3", "ALG3", "RNF41", "IKBKG", "IFITM1", "TMEM127", "TNFRSF12A", "GRAMD1A", "CLU", "CIZ1", "TP53", "FOSL1", "ZCCHC24", "ETHE1", "VOPP1", "PYGL", "PYGB", "FILIP1L", "MAN1B1", "BSG", "MICAL1", "CRTC3", "HGS", "SYNGR2", "TOR4A", "ASCC2", "ITGA5", "ITGA3", "SZRD1", "UBL7", "MEN1", "S100P", "S100A9", "S100A10", "S100A11", "PFN1", "PFKP", "PFKL", "SLC25A37", "CD63", "CD44", "CD68", "YWHAH", "DDX41", "PXDC1", "TLCD3A", "IDH3G", "ELF4", "TM4SF1", "FAM214B", "SLC38A10", "PREB", "ITPK1", "STARD3", "KDELR1", "THEMIS2", "FES", "NCLN", "RIC8A", "PIEZO1", "SLC43A3", "CHMP6", "ZFHX3", "LIMK1", "PTPA", "PPP2R5B", "PPP2R5D", "SLC7A1", "SLC9A1", "COPS7B", "GAS2L1", "ARPC4", "ARPC1B", "CBX6", "MRGBP", "PIM1", "TGM2", "THBS1", "SLC7A5", "SLC9A3R2", "CTNNA1", "C7orf26", "NABP2", "TPST2", "CHST11", "MPZL1", "CD9", "ESYT1", "CD14", "NAA10", "F8A1", "RALGDS", "RANGAP1", "GSTP1", "CDC42EP4", "ZNF581", "HSF1", "TAPBP", "MAP4", "CFL1", "EPHB2", "BRD2", "UCP2", "SH2B3", "SLC35A2", "HDAC5", "OGFR", "ABHD2", "SOCS1", "VIM", "ARID5A", "CORO1B", "TRABD", "PLEKHO2", "CXXC1", "ZFP36L2", "PGLS", "UBE2S", "C1R", "SERPING1", "PTPN6", "PPM1M", "PRR13", "SLC25A28", "AGPAT2", "ADAM15", "PTP4A3", "CORO1A", "WDR45", "SHISA5", "CDC25B", "CDC34", "GDI1", "GEM", "NR4A1", "HMOX1", "BRMS1", "TECPR1", "TBC1D2", "MYO1E", "MYO1C", "PDGFA", "ADD1", "SLX4"]
# fibro hubber_list = ["TGFA", "TP63", "SOX17", "EDA", "ADORA2B", "LDB1", "KLF4", "PTHLH", "DSP", "SPRR1A", "CSGALNACT1", "HBA2", "LATS1", "INHBA", "CARM1", "TGFB1", "GLG1", "GALNT1", "NR3C1", "MAMLD1", "SRF", "VCL", "LAMC1", "ACTN1", "ARAP1", "CTNNA1", "PNPLA6", "FLT1", "BTG1", "EPHA2", "CD59", "STMN1", "ARRB1", "RBPMS", "APLP2", "WNT2", "TPD52L1", "MAD2L2", "DUSP22", "DUSP6", "CCNB1", "MAP3K5", "MAP2K3", "HIPK3", "NENF", "AGRN", "FSTL3", "CADM1", "BRCA1", "VDAC1", "TBL1X", "IL6ST", "NAPA", "HES1", "ANAPC5", "SUZ12", "SQSTM1", "NFKBIA", "HSP90B1", "SMURF2", "BIRC2", "MAN2A1", "SIGIRR", "ADH5", "EXT2", "SESTD1", "ID3", "TGIF1", "LRP1", "PLOD3", "KAT2A", "HLX", "BLM", "ATXN1", "PFN2", "MAML1", "HBA1", "JAG1", "STOM", "PRNP", "VASP", "ZC3HAV1", "AGPS", "ARHGDIA", "ENTPD7", "RAB3B", "CIB1", "APPBP2", "CALCR", "TUBB2A", "CD3G", "MMS19", "CSH2", "SAMD4A", "MYO15A", "IFNGR1", "FOXF1", "ANP32A", "GLUD2", "GLUD1", "TNFAIP2", "MTA1", "COX7A1", "SF3A2", "SERPINB1", "EPHB4", "EPRS1", "CEBPA", "UGT2B15", "UBE2C", "DEPP1", "EIF3A", "BCL3", "KRT5", "KRT4", "CAVIN1", "MNDA", "GRIK5", "IVL", "NELFA", "CLIP2", "FLII", "XPO1", "PISD", "FGFR4", "IFT74", "TRIO", "GDF15", "MYCL", "SLC22A17", "SLC4A7", "UTP14C", "IFIT5", "ATP1B3", "TPP2", "PDLIM1", "WFDC2", "COPA", "MAFF", "B9D1", "DAPP1", "IMPA2", "PKP3", "PTPRF", "ST3GAL1", "HNRNPA2B1", "VWA5A", "NAMPT", "SLC16A2", "PSMD4", "TSC22D2", "EFCAB14", "SMAD9", "SMAD6", "SOX2", "RDX", "IL32", "CTPS1", "ETF1", "BZW1", "COL6A3", "COL5A2", "GEMIN2", "ENPP4", "MLXIP", "MICU2", "ACSL3", "TBCA", "PACS2", "ERG28", "AP4M1", "TAX1BP1", "EGLN3", "CAV1", "CAV2", "SLC29A1", "TSPAN2", "TSFM", "HIGD2A", "ZBTB7A", "LIG1", "MSN", "TRIM52", "TOMM7", "DHX32", "MGP", "EIF4B", "PPOX", "RBMS2", "MARCHF3", "OGDH", "UBTF", "LSM2", "STAB1", "QSOX1", "HMGCR", "GEMIN4", "PDE3B", "PTMA", "CKS1B", "KCNMB1", "BMP2K", "TMEM47", "STAM", "RAB5C", "DDX28", "NFE2L1", "PHF2", "ZNF215", "CD5L", "MAIP1", "RIPOR1", "LEF1", "NMB", "GLUL", "DGCR6L", "PRKAA1", "TLR2", "TRIP13", "TUBGCP3", "RIBC2", "TBC1D9", "PLXNC1", "DAPK1", "CCNI", "CHST2", "GYPC", "GYS1", "ADIPOR2", "ADGRA2", "SLC1A2", "MCM5", "MCM6", "CDH11", "TRGC1", "PTGER4", "PTGER1", "SLC35G2", "CARMIL1", "CSAD", "MAD2L1BP", "DENND3", "SPAM1", "SLC22A4", "HHEX", "PCCB", "PLAGL1", "PLA2G5", "PLAUR", "NR5A2", "GRK2", "EMC10", "ALK", "CHRNA5", "GZMB", "LAMA4", "TPD52L2", "SNX2", "TXK", "TYMS", "SALL2", "MBOAT2", "GPNMB", "PCP4", "WIPI2", "FRY", "ZNF263", "XK", "CD93", "FADS3", "HOXA9", "SLC20A2", "EPB41L4B", "HNRNPDL", "SLC26A3", "IGSF3", "RPL35A", "PSMC1", "CELSR2", "CTBS", "OVOL2", "NXN", "GSTM1", "TMEM243", "HEBP2", "ORC6", "OAZ2", "ETV5", "PMS1", "LAD1", "NDUFB4", "METTL7A", "TCP11L1", "PRODH", "CARD10", "KCNH2", "ATP11A", "NEBL", "SPHK1", "MYO18A", "GAA", "CCNT2", "CD1A", "CSTF3", "TES", "LTBP2", "DARS1", "PARP8", "LGALS8", "PDLIM5", "SNX27", "SLC6A16", "SCP2", "SCAPER", "ZSWIM6", "ALDH7A1", "SMTN", "SLC5A3", "TNFSF9", "CDK6", "STX16", "DUSP1", "TNPO1", "USP40", "RTEL1", "OGFOD1", "LRRC41", "CCNA2", "DYNC1I2", "DNMT1", "HMGB1", "SASH1", "SIGLEC1", "KLHDC3", "WNK1", "NUDC", "PARVB", "SRRM2", "ANKRD10", "AURKA", "NR4A3", "VWF", "CNTNAP2", "MLF1", "PWP1", "FYN", "BCAR1", "CDC42SE1", "IGFLR1", "FOXN3", "DOCK4", "TPX2", "HDC", "FAM219A", "HSD17B8", "TMEM158", "KIAA0040", "CNKSR1", "CFI", "PDLIM3", "ZBED4", "XCL1", "FERMT2", "STARD7", "VTI1A", "TRMT12", "DYNC2LI1", "SLC2A1", "PLA2G4C", "CDH15", "HSPA1B", "TFDP1", "SCRN1", "TOMM20", "ZMAT2", "GARS1", "GALT", "RRP8", "PSMA2", "MAGI1", "RAMP2", "GTF2E2", "PMAIP1", "KARS1", "SMARCA1", "KCTD12", "PKM", "FAM167A", "VARS1", "RPS12", "COL4A1", "TNFRSF14", "PPFIBP2", "ALDOA", "DBP", "LAMA2", "FOSL1", "CRTC3", "SYNGR3", "CYP51A1", "ITGA5", "ITGA3", "CENPU", "TBXAS1", "BBS9", "IFI16", "IDI1", "DIO1", "MTSS1", "SLC43A3", "GCOM1", "LIMK2", "FAM171A1", "ITIH5", "EFNA5", "KLF11", "ABCF1", "F8A1", "DYNLL1", "EFHD1", "PLEKHO2", "TTLL12", "PASK", "RGL1", "BRI3", "C1S", "C1R", "CDC25A", "TBC1D2", "ANKRD23", "ADD2"]
#hubber_list = ["RHOG", "ARHGDIA", "LGALS9", "LGALS3", "LGALS1", "LATS1", "INHBA", "ELF1", "RAB27A", "ARHGEF2", "GRN", "MYO9B", "THBS1", "CD55", "CD74", "MGST2", "RELA", "WFS1", "FLNA", "TRIP6", "GIPC1", "SRF", "BAG6", "IL17RA", "TFE3", "PCYT1A", "LAMC1", "SERPINH1", "COL6A1", "MYH9", "DGKZ", "DECR1", "EHD1", "CD81", "CSPG4", "SHC1", "SORBS3", "DUSP3", "MAP3K11", "GRB2", "NUP62", "LRP1", "HSPB1", "PRNP", "NFKBIA", "NR1H2", "NPC2", "SLC27A1", "HIF1A", "YWHAH", "QKI", "SF1", "KLF10", "CAP1", "PNPLA6", "ACTN4", "USF2", "BTG1", "RNH1", "PLXND1", "MAPK7", "TNFRSF1A", "HLX", "UBE2G2", "EGR1", "ENO1", "RHOC", "LTBR", "TANK", "GCLM", "DNM2", "ACTN1", "RFNG", "EXOC7", "PAFAH1B3", "ZMIZ2", "LST1", "DHPS", "HOMER3", "ATF3", "SHMT2", "ANXA7", "SYDE1", "TNFAIP2", "MTA1", "ATP6V0D1", "MAP7D1", "INPP1", "MAPKAPK3", "SEMA3B", "VAT1", "CAVIN1", "AKAP12", "HLA-E", "RFLNB", "GRINA", "YRDC", "NAA60", "SUPT5H", "PLEC", "CLIP2", "IFI44", "SOCS2", "ITGB5", "NEU1", "TRIO", "SERPINB8", "PHLDA1", "FXR2", "PIP5K1C", "NUP88", "NUCB1", "LASP1", "SREBF2", "SLC16A3", "PDLIM1", "YKT6", "ILK", "CD33", "TNFRSF8", "N4BP2L2", "INTS1", "SARS1", "NAMPT", "DCTD", "DCTN1", "FGR", "CIDEB", "SCO2", "RAB31", "RBPMS", "PPP1R15A", "PLD3", "TAGLN2", "PTPN18", "IGFBP4", "DDAH2", "FBXL6", "EHD2", "RAB32", "CTSD", "APOBEC3C", "CXCL8", "SH3TC1", "COL6A3", "MLXIP", "PYCARD", "TM9SF4", "HSD17B10", "PACS2", "AIMP2", "TAX1BP1", "GPSM1", "NETO2", "TP53I11", "STX11", "CD151", "ADGRE5", "GPI", "CSRP1", "IFI35", "SLC29A1", "SH3BGRL", "ZBTB7A", "LIF", "EMD", "RAC2", "RAD23A", "PGAP6", "EIF4EBP1", "OGDH", "STRN4", "QSOX1", "CALCOCO1", "PDLIM7", "TAGLN", "SH3BGRL3", "CAPNS1", "CAPN1", "CAPG", "EED", "CSNK1D", "CRLF3", "NMB", "GLUL", "HCLS1", "VCAM1", "ID3", "TLR2", "EIF5", "GPC1", "TMEM109", "DAPK3", "ATP6V1F", "ATP6V0C", "UBA1", "KDELR2", "GLIPR1", "SMOX", "GALNT2", "SP100", "NCF2", "RTF2", "PLAT", "PLAUR", "FTH1", "AGPAT1", "LRP10", "MYL9", "DMWD", "SMG5", "ENC1", "LAMA4", "TPD52L2", "SNX2", "MX1", "GNG12", "EMP1", "LMNA", "ACTR1B", "GADD45A", "TOMM34", "CD93", "GNB2", "SH3BP5", "FADS3", "ARHGEF5", "DRG2", "IGSF3", "TGFBI", "TGFB1I1", "UBR4", "TRAM2", "CYC1", "BMP1", "EML3", "FAM89B", "CBX4", "CETN3", "ST14", "HYOU1", "NEBL", "SPHK1", "GAA", "TES", "CFP", "ANXA5", "LGALS8", "ZNF592", "FCER1G", "MGAT1", "THUMPD2", "BASP1", "EGR3", "NNMT", "ACTB", "SMTN", "MAZ", "DUSP7", "BLOC1S1", "MMP11", "MMP14", "BCL7C", "RPL13A", "CABIN1", "SRRM2", "SUPT6H", "NOL6", "CCT4", "MVP", "ITGB2", "CALU", "DLGAP4", "ATN1", "IFRD1", "C16orf58", "IL15RA", "OLFML2B", "RBM42", "POM121", "YES1", "FERMT2", "PPP2R1A", "ATP6AP1", "SLC1A5", "RBM47", "FAM193A", "LILRB4", "TCIM", "MAP1S", "PSME2", "LAPTM5", "CLN3", "TPP1", "SCRN1", "NUPR1", "GARS1", "LRRC32", "RELB", "SF3B4", "PPDPF", "PLTP", "PKM", "VASP", "SEPTIN2", "COL4A2", "IER5", "AP2A2", "AP1B1", "TNKS1BP1", "ALDH3B1", "TNFRSF12A", "CIZ1", "FILIP1L", "ITGA5", "ITGA7", "ITGA3", "S100A9", "S100A10", "PFN1", "CD63", "CD68", "PXDC1", "M6PR", "TM4SF1", "FAM214B", "PTPA", "PPP2R5B", "BST2", "RPL41", "PI4KA", "THBS2", "TDG", "GPER1", "CTNNA1", "TPST2", "MPZL1", "CD9", "CD14", "BRD2", "SH2B3", "OGFR", "CORO1B", "PGLS", "C1R", "NR4A1"]
both_list = []

for i in hubber_list:

	if i in all_list:
		both_list.append(i)

print("Hubber: ", len(hubber_list))
print("Predictions: ", len(all_list))
print("Intersection: ", len(both_list))
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

feature_imp = pd.Series(clf.feature_importances_,index=feature_cols).sort_values(ascending=False)

import seaborn as sns

# Creating a bar plot
sns.barplot(x=feature_imp, 
            y=feature_imp.index,
            color='DarkBlue')
# Add labels to your graph

plt.xlabel('Feature Importance (Mean Decrease Impurity)')
plt.ylabel('Tissues')
plt.title("Feature Importance")
plt.legend()
plt.show()

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.model_selection import RandomizedSearchCV
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 10, stop = 200, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}


"""rc_random = RandomizedSearchCV(estimator = clf, param_distributions = random_grid, n_iter = 50, cv = 3, verbose=2, random_state=42, n_jobs = -1)
# Fit the random search model
rc_random.fit(X_train, y_train)

print(rc_random.best_params_)"""
 
from sklearn.tree import export_graphviz

# Export as dot file

"""export_graphviz(clf.estimators_[15], out_file='tree_1.dot', 
                feature_names = feature_cols,
                class_names = ["non-disease", "disease"],
                rounded = True, proportion = False, 
                precision = 2, filled = True)

# Convert to png using system command (requires Graphviz)
from subprocess import call
call(['dot', '-Tpng', 'tree_1.dot', '-o', 'tree_1.png', '-Gdpi=600'])
"""
"""fn=feature_cols
cn=["Non-disease", "HCoV-2-Linked"]
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(clf.estimators_[2],
               feature_names = fn, 
               class_names=cn,
               filled = True);
fig.savefig('clf_individualtree.png')
"""
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot
# generate 2 class dataset

# generate a no skill prediction (majority class)
ns_probs = [0 for _ in range(len(y_test))]
# fit a model
lr_probs = clf.predict_proba(X_test)
# keep probabilities for the positive outcome only
lr_probs = lr_probs[:, 1]
# calculate scores
ns_auc = roc_auc_score(y_test, ns_probs)
lr_auc = roc_auc_score(y_test, lr_probs)
# summarize scores
print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('Logistic: ROC AUC=%.3f' % (lr_auc))
# calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)
# plot the roc curve for the model
pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
pyplot.plot(lr_fpr, lr_tpr, marker='.', label='Random Forest', color='DarkBlue')
# axis labels
pyplot.xlabel('False Positive Rate')
pyplot.ylabel('True Positive Rate')
# show the legend
pyplot.legend()
# show the plot
pyplot.show()
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc

precision, recall, thresholds = precision_recall_curve(y_test, lr_probs)
f1 = f1_score(y_test, y_pred)
#auc = auc(recall, precision)

# generate 2 class dataset
lr_probs = clf.predict_proba(X_test)
# keep probabilities for the positive outcome only
lr_probs = lr_probs[:, 1]
# predict class values
yhat = clf.predict(X_test)
lr_precision, lr_recall, _ = precision_recall_curve(y_test, lr_probs)
lr_f1 = f1_score(y_test, y_pred) 
lr_auc  = auc(lr_recall, lr_precision)
# summarize scores
print('Forest: f1=%.3f auc=%.3f' % (lr_f1, lr_auc))
# plot the precision-recall curves
no_skill = len(y_test[y_test==1]) / len(y_test)
pyplot.plot([0, 1], [no_skill, no_skill], linestyle='--', label='No Skill')
pyplot.plot(lr_recall, lr_precision, marker='.', label='Random Forest')
# axis labels
pyplot.xlabel('Recall')
pyplot.ylabel('Precision')
# show the legend
pyplot.legend()
# show the plot
pyplot.show()
x=0
for i in all_list:
	if i in gene_list:
		x+=1
print("Overlap: ", x)