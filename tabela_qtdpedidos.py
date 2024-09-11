import pandas as pd


# Função para converter strings como '+10mil' ou '20k' em números inteiros
def convert_to_int(value):
    if isinstance(value, str):
        # Remover sinais de mais e espaços
        value = value.replace('+', '').replace(' ', '')
        # Converter 'mil' e 'k' para multiplicadores
        if 'mil' in value:
            number = float(value.replace('mil', '').replace(',', '.'))
            return int(number * 1000)
        elif 'k' in value:
            number = float(value.replace('k', '').replace(',', '.'))
            return int(number * 1000)
        elif value.isdigit():
            return int(value)
        else:
              # Retornar 0 ou outro valor padrão para valores não reconhecidos
            return 0
    return 0

# Carregar o arquivo CSV (ajuste o nome do arquivo e o caminho conforme necessário)
df = pd.read_csv('C:/Users/User/Downloads/ecommerce_preparados.csv')

# Aplicar a função de conversão à coluna 'Qtd_Vendidos'
df['VendasPorProduto'] = df['Qtd_Vendidos'].apply(convert_to_int)

# Verificar o DataFrame resultante
print(df)

# (Opcional) Salvar o DataFrame ajustado de volta para um arquivo CSV
df.to_csv('C:/Users/User/Downloads/ecommerce_preparados.csv', index=False)
