import pandas as pd

# Caminho do arquivo CSV
caminho_csv = r'C:\Users\julio\OneDrive\Área de Trabalho\Nova Pasta\datasets\dadosTP_corrigido.csv'

# Carrega o CSV
df_raw = pd.read_csv(caminho_csv, sep=',', engine='python', on_bad_lines='skip')

# 1. Coletar todos os SSIDs encontrados
ssids_encontrados = []

for _, row in df_raw.iterrows():
    for i in range(1, 11):
        ssid = row.get(f'SSID{i}')
        if pd.notna(ssid) and ssid.strip() != '':
            ssids_encontrados.append(ssid.strip().upper())

# 2. Contagem de SSIDs
ssid_counts = pd.Series(ssids_encontrados).value_counts().reset_index()
ssid_counts.columns = ['SSID', 'Ocorrencias']
print("\n--- SSIDs Detectados e Suas Ocorrências ---")
print(ssid_counts)

# 3. Estatísticas sobre SSIDs por linha
df_qtd_por_linha = df_raw.apply(
    lambda row: sum(pd.notna(row.get(f'SSID{i}')) and row.get(f'SSID{i}').strip() != '' for i in range(1, 11)),
    axis=1
)

print("\n--- Estatísticas por Linha ---")
print("Total de SSIDs únicos:", ssid_counts.shape[0])
print("Média de SSIDs por linha:", df_qtd_por_linha.mean())
print("Máximo de SSIDs em uma linha:", df_qtd_por_linha.max())
print("Mínimo de SSIDs em uma linha:", df_qtd_por_linha.min())

# 4. Função robusta para verificar linhas onde um SSID está ausente
def encontrar_linhas_sem_ssid(df, ssid_procurado):
    ssid_procurado = ssid_procurado.strip().upper()
    linhas_ausentes = []

    for index, row in df.iterrows():
        ssids_na_linha = [
            str(row.get(f'SSID{i}', '')).strip().upper()
            for i in range(1, 11)
            if pd.notna(row.get(f'SSID{i}')) and str(row.get(f'SSID{i}')).strip() != ''
        ]
        if ssid_procurado not in ssids_na_linha:
            linhas_ausentes.append(index)

    print(f'\n🔍 {ssid_procurado} está ausente em {len(linhas_ausentes)} linhas.')
    return linhas_ausentes

# 5. Exemplo
linhas_sem_eduroam = encontrar_linhas_sem_ssid(df_raw, 'dlink-9A00')
