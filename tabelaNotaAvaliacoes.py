import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('C:/Users/User/Downloads/ecommerce_preparados.csv')

# Criar a nova coluna 'NotaAvaliacoes' arredondando as notas para o inteiro mais próximo
df['NotaAvaliacoes'] = df['Nota'].round()

# Exibir as primeiras linhas para verificar o resultado
print(df[['Nota', 'NotaAvaliacoes']].head())

# Salvar o DataFrame com a nova coluna em um novo arquivo CSV, se necessário
df.to_csv('C:/Users/User/Downloads/ecommerce_preparados.csv', index=False)
