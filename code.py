import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv('StudentsPerformance.csv')
data = df['reading score'].tolist()

mean=sum(data)/len(data)
std_deviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)

first_std_deviation_start,first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-std_deviation, mean+std_deviation
third_std_deviation_start,third_std_deviation_end = mean-std_deviation, mean+std_deviation

fig = ff.create_distplot([data],['reading scores'],showhist=False)
