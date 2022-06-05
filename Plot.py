import pandas as pd
import matplotlib.pyplot as plt
import ReadFile

def __init__(self):
    pass

def make_single_plot(index, function):
    fig = plt.figure()
    df = pd.DataFrame(function).T
    x = df.iloc[:, 0]
    y = df.iloc[:, index]
    plt.plot(x, y, marker='o')
    plt.xlabel(str(df.columns[0]))
    plt.ylabel(str(df.columns[index]))
    plt.xticks(range(1, len(df)))

    return fig


def make_all_plots(SCF=True, **kwargs):
    temp = []
    for key, value in kwargs.items():
        print(key,value)
    if "structureoptcycle" in kwargs.keys():
        for i in kwargs["structureoptcycle"]:
            print(str(i))
            temp.append(make_single_plot(i, ReadFile.structureoptcycle()))
            plt.savefig(str(i))
    if SCF == True:
        (make_single_plot(1, ReadFile.scfcycle()))
        plt.savefig("scf")
    plt.show()

