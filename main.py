import pandas as pd
import plotly.express as px

reading_csv_file = pd.read_csv('covid.csv')
graph = px.scatter(reading_csv_file, x='date', y='cases', title='COVID-19 CASES AROUND THE WORLD', color='country', size_max=60)
graph.show()

