import plotly.express as py
import pandas as pd
import plotly.figure_factory as ff
import csv

height=[]
df=pd.read_csv("data.csv")
ratings=df["Avg Rating"].tolist()
fig=ff.create_distplot([ratings],["Average Phone Ratings"],show_hist=False)
fig.show()