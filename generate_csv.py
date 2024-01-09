import pandas as pd
path = 'D:/Proyectos/Local/RPA-Rosaqui/test.xls'
path_csv = 'D:/Proyectos/Local/RPA-Rosaqui/test.csv'
df = pd.read_excel(path)
df.drop(df.index[0:6], inplace=True)
#df.drop(df.columns[1], axis='columns')
df=df.drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'], axis=1)
df.rename(
    columns={"Unnamed: 9": "Estado", "Unnamed: 10": "Numero movil", "Unnamed: 11": "Nombre del producto", "Unnamed: 12": "Saldo de productos"},
    inplace=True,
)
df['Nombre del producto'].replace('Recaudación','Recaudacion', inplace=True)
#df.fillna(method='ffill', inplace=True)
df = df.dropna(subset=["Nombre del producto"])
df.ffill(inplace=True)
df.to_csv(path_csv)