import pandas as pd

print("Executing")

# Lista com os 3 primeiros caracteres desejados
primeiros_caracteres = ['DCC', 'EST', 'FIS', 'MAT', 'QUI']

# Leitura da planilha original
# df_original = pd.read_excel("testeDP.xlsx")
df_original = pd.read_excel('notas_All_Filtradas.xlsx')

# Filtragem das linhas com base na coluna "DISCIPLINAS"
df_filtrado = df_original[df_original['DISCIPLINA'].str[:3].isin(primeiros_caracteres)]

# Criação de uma nova planilha com as linhas filtradas
df_filtrado.to_excel("result_filtrados_soExatas.xlsx", index=False)

print("Done!")