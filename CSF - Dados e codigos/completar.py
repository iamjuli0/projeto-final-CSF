import pandas as pd

# Caminho do arquivo original
caminho = r'C:\Users\julio\OneDrive\Área de Trabalho\Nova Pasta\datasets\dadosTP.csv'
saida = r'C:\Users\julio\OneDrive\Área de Trabalho\Nova Pasta\datasets\dadosTP_corrigido.csv'

# Etapa 1: Remove vírgula final de cada linha diretamente na memória
with open(caminho, 'r', encoding='utf-8') as f:
    linhas = [linha.rstrip().rstrip(',') + '\n' for linha in f]

# Etapa 2: Salva temporariamente para que o pandas possa ler
from io import StringIO
conteudo_corrigido = StringIO(''.join(linhas))

# Etapa 3: Carrega e preenche os campos vazios
df = pd.read_csv(conteudo_corrigido)

for col in df.columns:
    if 'SSID' in col:
        df[col] = df[col].fillna('SEM_AP')
        df[col] = df[col].replace(r'^\s*$', 'SEM_AP', regex=True)
    elif 'RSSI' in col:
        df[col] = df[col].fillna(0)
        df[col] = df[col].replace(r'^\s*$', 0, regex=True)

# Etapa 4: Salva o arquivo corrigido
df.to_csv(saida, index=False)

print(f'Arquivo salvo como: {saida}')
