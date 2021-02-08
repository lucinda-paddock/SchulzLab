import pandas as pd 
import numpy as np 

filePath = "/Users/lucypaddock/Desktop/SchulzLab/Sicegar/20-11-16_deseq2_timecourse_normalized_counts.txt"
timeDict = {"noo_ib_1": "control1", "noo_ib_2": "control2",	"noo_ib_3": "control3",	"ib_3h_1": 180, "ib_3h_2":180, "ib_3h_3": 180, "ib_6h_1": 360,	"ib_6h_2": 360,	"ib_6h_3": 360,	"ib_12h_1":	720, "ib_12h_2": 720,	"ib_12h_3": 720,	"ib_24h_1": 1440,	"ib_24h_2": 1440,	"ib_24h_3": 1440,	"ib_48h_1": 2880,	"ib_48h_2": 2880, 	"ib_48h_3": 2880,	"ib_3d_1": 4320,	"ib_3d_2": 4320,	"ib_3d_3": 4320,	"ib_7d_1": 10080,	"ib_7d_2": 10080,	"ib_7d_3":10080,	"ib_10d_1": 14400,	"ib_10d_2": 14400,	"ib_10d_3": 14400,	"ib_14d_1": 20160,	"ib_14d_2": 20160,	"ib_14d_3": 20160}

def readTable(filePath, outputName):
    '''
    Parameters: 
    filePath - path (as a string) to a .txt produced by deseq2 with columns as time/treatment names 
    (the ones in timeDict) and rows as gene names
    outputName - a string, what the .csv file produced will be named

    Output:
    A .csv file named outputName where each row contains a gene name, treatment, intensity, and time.
    '''
    df = pd.read_table(filePath)
    dataList = []
    # loop through rows (gene names) of df
    for geneName, row in df.iterrows():
        # for each gene, loop through possible treatments
        for treatment, time in timeDict.items():
            intensity = row[treatment]
            dataList.append([geneName, treatment, intensity, time])
    newDf = pd.DataFrame(dataList, columns =['Gene Name', 'Treatment', 'Intensity', 'Time']) 
    newDf.to_csv(outputName)

    



    