# dbexcel module
import pandas as pd

kgdata = pd.ExcelFile('kgdata.xlsx')
barnehage = pd.read_excel(kgdata, 'barnehage', index_col=0)
forelder = pd.read_excel(kgdata, 'foresatt', index_col=0)
barn = pd.read_excel(kgdata, 'barn', index_col=0)
soknad = pd.read_excel(kgdata, 'soknad', index_col=0)




# Importering av data
df_Uvasket = pd.read_excel("./barnehage/ssb-barnehager-2015-2023-alder-1-2-aar.xlsm", sheet_name="KOSandel120000", 
						header=3, 
						names=["kom", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"], 
						na_values=[".", ".."])
yr = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]

#Vasking av data
for coln in ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]:
	mask_over_100 = (df_Uvasket[coln] > 100)
	df_Uvasket.loc[mask_over_100, coln] = float("nan")
df_Uvasket.loc[724:779, 'kom'] = "NaN"
df_Uvasket["kom"] = df_Uvasket['kom'].str.split(" ").str[:2].str.join(" ")

df = df_Uvasket.drop(df_Uvasket.index[724:]) # Ferdigvasket data
df["kom"] = df["kom"].str.split(" ").apply(lambda x: x[1] if len(x) > 1 else (x[0] if len(x) == 1 else ""))
df4 = df.dropna().groupby("kom")[yr].sum().reset_index()

"""
Referanser
[] https://www.geeksforgeeks.org/list-methods-python/
"""