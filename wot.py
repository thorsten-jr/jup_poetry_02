import numpy as np
import pandas as pd
import plotly.express as px

file = 'BEG_03_ff_22_v10.xlsx'
sheet = 'Performance'
days = 275 # März bis November 2022
require_cols1 = [0, 3, 4, 20] # für 39, 78 und 107. Alle mit 15° Neigung und ca. 180° Ausrichtung
df1 = pd.read_excel(file, nrows = days, usecols = require_cols1, sheet_name = sheet, na_values = 0, converters= {'Datum': pd.to_datetime} )

fig1 = px.line(df1, title = sheet, x="Datum", y=df1.columns, hover_data={"Datum": "|%B %d, %Y"})
#fig1 = px.scatter(df4, title = sheet, x="Datum", y=df4.columns, hover_data={"Datum": "|%B %d, %Y"})
fig1.update_xaxes(
dtick="M1",
tickformat="%b\n%Y",
ticklabelmode="period")

fig1.show()
