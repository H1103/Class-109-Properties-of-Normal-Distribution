import plotly.figure_factory as ff 
import statistics
import csv
import pandas as pd 
import random 

dice_result = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)

mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
print("Mean:",mean,"\nStandard Deviation:" ,std_deviation,"\nMedian:",median,"\nMode:",mode)
fig.show()
