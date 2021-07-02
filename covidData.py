import pandas
import plotly.express as px

data = pandas.read_csv("coviddata.csv")
graph = px.scatter(data, x = "date", y = "cases", title = "Covid Data", size = "cases")
graph.show()