import os
from os import listdir
from os.path import isfile, join
import re
import csv
import pandas as pd

mypath = os.path.dirname(__file__)
#print((mypath))


def findslurm():
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #print(mypath)

    for i in onlyfiles:
        x = re.search("^slurm", i)
        if x != None:
            return x.string


def scfcycle():

    cycledictionary = {}

    with open(findslurm()) as file_object:
        contents = file_object.readlines()
    file_name = "output.csv"

    for line in contents:
        if ("DETOT") in line:
            x = re.split("\s+", line)
            a = x[2]
            cycledictionary[a] = {}
            cycledictionary[a]["SCF step"] = int(a)
            cycledictionary[a]["Energy Change / au"] = float(x[6])
    return cycledictionary


def structureoptcycle():

    new_dic = {}
    with open(findslurm()) as file_object:
        contents = file_object.readlines()
        for line in contents:

            if "COORDINATE OPTIMIZATION" in line:
                a = int((re.findall("\d+", line))[0])
                new_dic[a] = {}
                new_dic[a]["Coordinate Optimisation"] = int(a)
            if "PREDICTED ENERGY CHANGE" in line:
                b = (re.split("\s+", line))[4]
                new_dic[a]["Energy Change , au "] = float(b)
            if "MAX GRADIENT" in line:
                c = (re.split("\s+", line))[3]
                new_dic[a]["Max Gradient"] = float(c)
            if "RMS GRADIENT" in line:
                d = (re.split("\s+", line))[3]
                new_dic[a]["RMS Gradient"] = float(d)
            if "MAX DISPLAC." in line:
                e = (re.split("\s+", line))[3]
                new_dic[a]["Max Displacement"] = float(e)
            if "RMS DISPLAC." in line:
                f = (re.split("\s+", line))[3]
                new_dic[a]["RMS Displacement"] = float(f)
            if "TOTAL ENERGY(DFT)(AU)" in line:
                g = (re.split("\s+", line))[4]
                new_dic[a]["Total Energy / au"] = float(g)

    return new_dic


def writecsv(x):

    outputfile = str(x) + ".csv"
    if x == 'scf':
        pd.DataFrame((scfcycle())).T.to_csv(outputfile)
    if x == 'geometry':
        pd.DataFrame((structureoptcycle())).T.to_csv(outputfile)


