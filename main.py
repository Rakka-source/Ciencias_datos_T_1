import pandas as pd

def nombre_integrantes():
    print(f"Jeyson_Fernandez_Fabres_Felipe_Gutierrez_Benitez \n {'-' * 40}" )

# Cargar los datos desde CSV con codificación 'latin-1' o 'utf-8'
data = pd.read_csv('./DEMRE_Jeyson_Fernandez_Fabres_Felipe_Gutierrez_Benitez.csv', encoding='latin-1',delimiter=';')

#1
# nombre_integrantes()
# print(data.shape)

#2
# nombre_integrantes()
# data.drop_duplicates(inplace=True)
# print(data.info())

#3
data=data.drop(["numero_secretaria_admision", "nombre_secretaria_admision"],axis=1)
#nombre_integrantes()
#print(data.info())

#4
data= data.dropna(subset=["ptje_nem"])
# nombre_integrantes()
# print(data.info())

#5
columnas_a_omitir = ['ptje_cien', 'ptje_hycs']
columnas_a_verificar = [col for col in data.columns if col not in columnas_a_omitir]
data.dropna(inplace=True, subset=columnas_a_verificar)
# nombre_integrantes()
# print(data.info())


#6
data=data.applymap(lambda x: x.lower() if isinstance(x, str) else x)

#7 
for col in data.columns:
    if data[col].nunique() == 1:
        print(f'Columna: {col} || valor registrado  = " {data.iloc[0][col]} "')
        data.drop(col, axis=1, inplace=True)
nombre_integrantes()
print(data.info())


#8
data= data.sort_values(by='orden_preferencia').drop_duplicates(subset='numero_documento_postulante', keep='first')
nombre_integrantes()
print(data.info())

# --
print(data.describe())
nombre_integrantes()

#9
data.to_csv('./Data_Export/DEMRE_Jeyson_Fernandez_Fabres_Felipe_Gutierrez_Benitez.csv', index=False, encoding='latin-1', sep=';')

