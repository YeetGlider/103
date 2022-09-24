import pandas as pd
import plotly.express as px

#reading data from csv files
df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Country", y="Population",size="Percentage",color="InternetUsers")
fig.show()