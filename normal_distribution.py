import pandas
import plotly.figure_factory as figFactory

dataframe = pandas.read_csv("data.csv")

figure = figFactory.create_distplot([dataframe["Avg Rating"].tolist()], [
                                    "Mobile Brand"])
figure.show()
