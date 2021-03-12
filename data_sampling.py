import random
import plotly.figure_factory as ff
import plotly.express as ps
import csv
import pandas as spb
import statistics

df = spb.read_csv("data_sampling.csv")
data = (df["average"].tolist())


def random_data(datapoint):
    dataset = []
    for i in range(0, datapoint):
        random_number = random.randint(0, (len(data)-1))
        value = data[random_number]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return (mean)
def show_fig(data):
    fig = ff.create_distplot([data],["average"], show_hist=False)
    fig.show()

def showMean():
    mean_list = []
    for i in range(0, 1000):
        a = random_data(100)
        mean_list.append(a)
    show_fig(mean_list)

showMean()