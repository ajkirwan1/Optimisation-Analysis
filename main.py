# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Plot
import ReadFile
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


ReadFile.writecsv("scf")

f = Plot.make_all_plots(structureoptcycle=(1, 2, 3), scfcycle=1)
