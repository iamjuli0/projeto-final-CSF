import pandas as pd

# Função novamente para processar os dados com SSIDs fixos
def processar_com_ssids_fixos(caminho_csv, ssids_fixos):
    df = pd.read_csv(caminho_csv, sep=',', engine='python', on_bad_lines='skip')
    registros = []

    for _, row in df.iterrows():
        ponto = row['Ponto']
        leitura = {'rp': ponto}

        # Inicializa todos os SSIDs fixos com 0
        for ssid in ssids_fixos:
            leitura[ssid] = -100

        for i in range(1, 11):
            ssid = row.get(f'SSID{i}')
            rssi = row.get(f'RSSI{i}')
            if pd.notna(ssid) and ssid in ssids_fixos and pd.notna(rssi):
                leitura[ssid] = float(rssi)

        registros.append(leitura)

    df_processado = pd.DataFrame(registros)

    # Remove o prefixo "RP" ou "TP" e mantém só o número
    df_processado['rp'] = df_processado['rp'].str.replace('RP', '', regex=False)
    df_processado['rp'] = df_processado['rp'].str.replace('TP', '', regex=False)

    df_processado['rp'] = df_processado['rp'].astype(int)

    return df_processado

# Lista dos 10 SSIDs mais frequentes
ssids_fixos = [
    'CETELI_WIFI', 'CETELI_TREINAMENTOS', 'CETELI_P&D', 'VISITANTE_CETELI',
    'eduroam', 'wifi-zone-ufam-1', 'dlink-9A00', 'TPV', 'BRITO_AP', 'S80'
]

# Processar e salvar
df_treino = processar_com_ssids_fixos(r'C:\Users\julio\OneDrive\Área de Trabalho\Nova Pasta\datasets\dadosRP_corrigido.csv', ssids_fixos)
caminho_saida = r'C:\Users\julio\OneDrive\Área de Trabalho\Nova Pasta\datasets\dadosRP_final.csv'
df_treino.to_csv(caminho_saida, index=False)