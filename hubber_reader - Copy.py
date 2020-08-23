import pandas as pd
import random
import time
import requests
import re
from urllib.request import urlopen
from time import sleep
from lxml import html
import os
import sys

print("\U0001f600")
#print("(225) 828-0563")
def clean_txt(file_path):
	a_file = open(file_path, "r")
	line_list = []

	for i in a_file:
		line_list.append(i)

	del line_list[0:11]
	new_file = open(file_path, "w+")

	for line in line_list:
		new_file.write(line)
	new_file.close()

#data = pd.read_csv(file_str, sep="\t", error_bad_lines=False)
#print(data)

def readcsv(file_str):

    tests = pd.read_csv(file_str, encoding='unicode_escape')
    testsd = pd.DataFrame(data = tests)
    return(testsd)
#print(newincome)

def rand_bojk():
	
	top_500 = ""
	bojk = ["CSTB", "PALLD", "ABL1", "ABR", "JAG1", "TES", "TRPC4AP", "ENO2", "ENG", "ENO1", "TRIM28", "SGSH", "LTBR", "LTBP3", "LTBP2", "ITPKC", "CYBB", "CFP", "DAXX", "CFD", "PILRA", "ANXA5", "ANXA6", "ANXA1", "ANXA2", "XAB2", "CREB3L1", "USF2", "TMED9", "ACADVL", "LGALS9", "NAGK", "CDV3", "SMG9", "MICALL1", "TNFRSF1B", "TNFRSF1A", "BAX", "PRCC", "PRAF2", "RNF24", "LRRFIP1", "YWHAE", "PDLIM5", "RBCK1", "TGOLN2", "MCOLN1", "MICAL2", "PPM1F", "ZNF592", "FCER1G", "TNC", "MGAT1", "MFGE8", "R3HDM4", "TMEM259", "GANAB", "PTPN23", "CAPN2", "PI4KB", "TIMP3", "TIMP1", "TIMP2", "GIT1", "FAM3A", "TMBIM1", "BASP1", "SSH3", "EPHA2", "CTDSP1", "GRK6", "NKIRAS2", "DDA1", "BRD9", "NME4", "NNMT", "NMT1", "SORBS3", "SNX11", "CRISPLD2", "ARID1A", "KLC2", "ELOVL1", "ZFAND3", "CHD8", "TINF2", "WIPF2", "ACTB", "SLC3A2", "SLC4A2", "SMTN", "MAZ", "UPP1", "NR1H2", "USP4", "MIER2", "CPSF1", "RBM15B", "CDK9", "TRIOBP", "STX10", "ANTXR2", "DUSP7", "DUSP6", "DUSP1", "DUSP5", "DUSP3", "GTPBP2", "POLD4", "KLHL36", "BCR", "CCN2", "SLC38A7", "MYO1F", "ACTG2", "ACTG1", "ACTC1", "RNF216", "TOLLIP", "CREB3", "NXF1", "CAP1", "CCND2", "CCND3", "DNM2", "MTMR14", "PLXND1", "BRAT1", "SLC35A4", "MMP14", "MMP19", "HLX", "USP22", "MAN2B2", "LRRC59", "SNAPC2", "NAGA", "NAB2", "PECAM1", "ADM", "ACTN1", "WNK1", "CSRNP1", "BCL7C", "DEF8", "GSN", "GSK3A", "PARVB", "CABIN1", "SRRM2", "USP36", "C11orf24", "SUPT6H", "SURF4", "IGF2BP2", "STK10", "TRAF2", "WAS", "WARS1", "NOL6", "FLNB", "MGAT4B", "B4GALT7", "PNKP", "NPC2", "COLGALT1", "MVP", "MED12", "ITGB2", "ITGAL", "ITGAX", "SLC35B2", "SERINC2", "ARL8A", "MAP3K11", "MRPL12", "TUBA1B", "RRBP1", "RRAS", "CAMK2G", "CALR", "CALU", "SERPINA1", "CDC42EP1", "GPAA1", "G6PD", "FYN", "DLGAP4", "BCAR1", "EHBP1L1", "ATN1", "GRB10", "GRB2", "RAPGEF1", "SELENOM", "SELENOW", "ABCD1", "JOSD2", "STING1", "GNA15", "GNA11", "SLC27A1", "HDLBP", "HDGF", "TRMT61A", "PLEKHM2", "LCP1", "P4HB", "MYO1B", "FAM219A", "TSPAN4", "MAPK3", "MAPK7", "C16orf58", "FAM50A", "ARHGEF1", "FKBP8", "PEA15", "MFSD12", "TMEM158", "ARAP1", "ACAP3", "HEG1", "SDC3", "SLC25A44", "ICAM1", "MAP3K3", "ANAPC15", "RHOQ", "RAB1B", "TCF3", "CCDC22", "CDC42EP2", "IFI30", "RBM42", "GOLGA3", "GOLGA2", "ATG9A", "NUP62", "KPNA6", "POM121", "SENP3", "CASKIN2", "ERF", "LYPLA2", "SIRT6", "ANPEP", "DBN1", "PER1", "CLIC1", "ARF1", "ARF3", "CKAP4", "FERMT2", "PORCN", "SPATA20", "FHL3", "FHL2", "FHL1", "MOSPD3", "TSPAN14", "PCBP4", "ARSA", "LSR", "KLF13", "DYNC1H1", "PPP2R1A", "ATP6AP1", "ATP6V0B", "SLC1A5", "SLC2A3", "UBTD1", "TYROBP", "RHOF", "KLF7", "SLC27A3", "HBEGF", "DNAJB2", "CAMTA2", "KRT17", "SETD5", "MAP1S", "LUZP1", "TMC6", "FKBP9", "PTBP1", "LAPTM5", "TP53INP2", "CLPTM1", "CLN3", "TPP1", "MEX3D", "ZNF787", "SEZ6L2", "NUPR1", "LPCAT1", "MRTFA", "INF2", "GARS1", "LRRC32", "MAP3K14", "CLSTN1", "MMP9", "HLA-DQB1", "HLA-DPB1", "HLA-DPA1", "DNAJB5", "TMEM184B", "BCL9L", "RENBP", "RELB", "RELA", "UPF1", "SLC12A9", "TIAF1", "SF3B4", "CDK2AP2", "GTF2F1", "PPDPF", "FKRP", "MBOAT7", "IGSF8", "PLTP", "PLXNA1", "NUMA1", "EXT1", "VAMP2", "KCTD12", "HK1", "SCAMP2", "SPRED2", "AKT1S1", "PKD1", "PKM", "TFPT", "VASP", "VARS1", "RNPEPL1", "SIPA1", "SCAF1", "CACTIN", "LRFN4", "PRR14", "YIPF2", "SLC2A4RG", "NSMF", "C5AR1", "NEDD9", "NCF4", "ZMIZ1", "TUBB4B", "TUBB3", "TSTA3", "PHLDA2", "MRPL2", "SLC25A22", "COL4A2", "COL4A1", "DBNL", "IER5", "UBAP1", "BAG3", "ATF5", "HCFC1R1", "KIF21B", "AKIP1", "TLE5", "AP2A1", "AP2A2", "AP1B1", "TNKS1BP1", "MAP2K2", "MAP2K3", "ALDOA", "CUX1", "PSME3", "ALG3", "RNF41", "IKBKG", "IFITM1", "TMEM127", "TNFRSF12A", "GRAMD1A", "CLU", "CIZ1", "TP53", "FOSL1", "ZCCHC24", "ETHE1", "VOPP1", "PYGL", "PYGB", "FILIP1L", "MAN1B1", "BSG", "MICAL1", "CRTC3", "HGS", "SYNGR2", "TOR4A", "ASCC2", "ITGA5", "ITGA3", "SZRD1", "UBL7", "MEN1", "S100P", "S100A9", "S100A10", "S100A11", "PFN1", "PFKP", "PFKL", "SLC25A37", "CD63", "CD44", "CD68", "YWHAH", "DDX41", "PXDC1", "TLCD3A", "IDH3G", "ELF4", "TM4SF1", "FAM214B", "SLC38A10", "PREB", "ITPK1", "STARD3", "KDELR1", "THEMIS2", "FES", "NCLN", "RIC8A", "PIEZO1", "SLC43A3", "CHMP6", "ZFHX3", "LIMK1", "PTPA", "PPP2R5B", "PPP2R5D", "SLC7A1", "SLC9A1", "COPS7B", "GAS2L1", "ARPC4", "ARPC1B", "CBX6", "MRGBP", "PIM1", "TGM2", "THBS1", "SLC7A5", "SLC9A3R2", "CTNNA1", "C7orf26", "NABP2", "TPST2", "CHST11", "MPZL1", "CD9", "ESYT1", "CD14", "NAA10", "F8A1", "RALGDS", "RANGAP1", "GSTP1", "CDC42EP4", "ZNF581", "HSF1", "TAPBP", "MAP4", "CFL1", "EPHB2", "BRD2", "UCP2", "SH2B3", "SLC35A2", "HDAC5", "OGFR", "ABHD2", "SOCS1", "VIM", "ARID5A", "CORO1B", "TRABD", "PLEKHO2", "CXXC1", "ZFP36L2", "PGLS", "UBE2S", "C1R", "SERPING1", "PTPN6", "PPM1M", "PRR13", "SLC25A28", "AGPAT2", "ADAM15", "PTP4A3", "CORO1A", "WDR45", "SHISA5", "CDC25B", "CDC34", "GDI1", "GEM", "NR4A1", "HMOX1", "BRMS1", "TECPR1", "TBC1D2", "MYO1E", "MYO1C", "PDGFA", "ADD1", "SLX4"]
	for i in range(500):
		random_bojk = random.choice(bojk)
		top_500 = top_500 + random_bojk + "\n"
		bojk.remove(random_bojk)
	return(top_500)

def gsea_analysis(file):
	income = pd.read_csv(file, sep="\t", error_bad_lines=False)
	newincome = pd.DataFrame(income)
	bojk_processes = []

	for i in range(len(list(newincome.index))):
		if newincome.iloc[i]["upload_1 (fold Enrichment)"] >= 2 and newincome.iloc[i]["upload_1 (over/under)"] == "+":

			bojk_processes.append(newincome.iloc[i]["GO biological process complete"])

	income2 = readcsv("Hubber_Files/actual.csv")
	newincome2 = pd.DataFrame(income2)
	pred_processes = []

	for i in range(len(list(newincome2.index))):
		if newincome2.iloc[i]["upload_1 (over/under)"] == "+" and newincome2.iloc[i]["upload_1 (fold Enrichment)"] >= 2:

			pred_processes.append(newincome2.iloc[i]["GO biological process complete"])

	income3 = readcsv("Hubber_Files/hubber_enrichment.csv")
	newincome3 = pd.DataFrame(income3)
	hubb_processes = []

	for i in range(len(list(newincome3.index))):
		if newincome3.iloc[i]["upload_1 (fold Enrichment)"] >= 2 and newincome3.iloc[i]["upload_1 (over/under)"] == "+":

			hubb_processes.append(newincome3.iloc[i]["GO biological process complete"])

	print(len(bojk_processes))
	print(len(pred_processes))
	print(len(hubb_processes))
	bojk_pred = []
	bojk_hubb = []

	for i in bojk_processes:
		if i in pred_processes:
			bojk_pred.append(i)

		if i in hubb_processes:
			bojk_hubb.append(i)
	return bojk_processes, pred_processes, hubb_processes, bojk_pred, bojk_hubb

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
import win32com.client
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')  # Last I checked this was necessary.

prefs = {'download.default_directory' : 'C:\\Users\\incre\\Documents\\python stuff\\Hubber_Files'}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome("C:\\Users\\incre\\Documents\\python stuff\\chromedriver.exe", options=options)

def get_enrichment(gene_set):
	
	driver.get('http://www.geneontology.org') 
	unform = driver.find_element_by_xpath('//*[@id="landing_gene_input"]')
	unform.send_keys(gene_set)
	
	login_button = driver.find_element_by_xpath(
	'/html/body/div/div/div[1]/div[2]/div/div/div[2]/form/div[2]/span/button[2]')

	login_button.click()
	actions = ActionChains(driver)   
	driver.switch_to.window(driver.window_handles[-1])
	download = driver.find_element_by_xpath('/html/body/a[1]')
	download.click()

bojk_processes, pred_processes, hubb_processes, bojk_pred, bojk_hubb = []

for i in range(100):
	get_enrichment(rand_bojk())
	bojk_processes, pred_processes, hubb_processes, bojk_pred, bojk_hubb = gsea_analysis('Hubber_Files/analysis.txt')
	bojk_processes_list.append(len(bojk_processes))
	pred_processes_list.append(len(pred_processes))
	hubb_processes_list.append(len(hubb_processes))
	bojk_pred_list.append(len(bojk_pred))
	bojk_hubb_list.append(len(bojk_hubb))
driver.quit()

print("Bojkova-Hubber: ", len(bojk_hubb))
print("Bojkova-Predictions: ", len(bojk_pred))

import numpy as np
import matplotlib.pyplot as plt
 
# Fake dataset
width = 0.35
height = [len(bojk_processes), len(pred_processes), len(hubb_processes)]
bars = ('Bojkova', 'Random Forest', 'Hubber')
y_pos = np.arange(len(bars))
height2 = [len(bojk_processes), len(bojk_pred), len(bojk_hubb)]
 
# Create bars and choose color
p1 = plt.bar(y_pos, height, width, color = "DarkBlue", zorder=1)
p2 = plt.bar(y_pos, height2, width, color = "#1ed0d0", zorder=2)
# Add title and axis names
plt.title('GSEA Comparison Across Gene Sets')
plt.xlabel('Gene Sets')
plt.ylabel('Enriched Biological Processes')
plt.legend((p1[0], p2[0]), ('Total', 'Overlap with Bojkova Set'))
 
# Limits for the Y axis

 
# Create names
plt.xticks(y_pos, bars)
 
# Show graphic
plt.show()