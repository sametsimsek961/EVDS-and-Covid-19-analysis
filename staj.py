import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from evds import evdsAPI
import csv

#### for taking EVDS data into Python

evds = evdsAPI('Lb4qWxFtXa')
data = evds.get_data(['TP.KKHARTUT.KT1','TP.KKHARTUT.KT16'], startdate="10-03-2020", enddate="06-08-2020")
data_pandas = pd.DataFrame(data)

with open('full_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = -1
    data_case = []
    data_death = []
    for row in csv_reader:
            if row[1]  == 'Turkey':
                if row[6] != '':
                    line_count += 1
                    if (line_count % 7) == 0:
                        data_case.append(row[6])
                        data_death.append(row[7])
                        data_pandas2 = pd.DataFrame({"Weekly Cases": data_case})
                        data_pandas3 = pd.DataFrame({"Weekly Deaths": data_death})
data_pandas = data_pandas.join(data_pandas2)
data_pandas = data_pandas.join(data_pandas3)
display(data_pandas)