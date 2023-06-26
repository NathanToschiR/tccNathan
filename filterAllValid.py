import pandas as pd

print("Executing")

# Leitura da planilha original
# df_original = pd.read_excel("testeDP.xlsx")
df_original = pd.read_excel('notas_alunos_graduacao_ufjf_2019_2022.xlsx')

# Exclude rows based on column values
excluded_values = ['TE', 'RE', 'APR', 'REP', 'NC', 'ITR']
filtered_df = df_original[~df_original['NOTA'].isin(excluded_values)]
filtered_df['NOME'] = filtered_df['NOME'].str.replace('/', '_')

# Save the filtered data to a new Excel file
filtered_df.to_excel('notas_All_Filtradas.xlsx', index=False)

print("Done!")