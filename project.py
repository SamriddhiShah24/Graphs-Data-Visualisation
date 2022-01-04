import pandas as pd
import plotly.express as px

df= pd.read_csv("hwdata.csv")
fig=px.scatter(df, x="date", y="cases", color="country", size="cases", size_max=30, title="Covid Cases Trend")
fig.show()