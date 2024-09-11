import pandas as pd

# Carregar o arquivo CSV

df = pd.read_csv('C:/Users/User/Downloads/ecommerce_preparados.csv')


# Função para classificar produtos em departamentos mais específicos
def definir_departamento(titulo):
    titulo = titulo.lower()  # Converte o título para minúsculas para facilitar a busca por palavras-chave

    # Moda Feminina
    if any(keyword in titulo for keyword in
           ['blusa', 'camiseta feminina', 'vestido', 'saia', 'calça feminina', 'jeans feminino', 'short feminino',
            'sapato feminino', 'sandália']):
        return 'Moda Feminina'

    # Moda Masculina
    elif any(keyword in titulo for keyword in
             ['camiseta masculina', 'bermuda', 'calça masculina', 'jeans masculino', 'short masculino',
              'sapato masculino', 'tênis']):
        return 'Moda Masculina'

    # Moda Íntima
    elif any(keyword in titulo for keyword in ['cueca', 'calcinha', 'sutiã', 'pijama', 'lingerie']):
        return 'Moda Íntima'

    # Saúde
    elif any(keyword in titulo for keyword in
             ['scrub', 'hospital', 'máscara', 'luva', 'jaleco', 'uniforme', 'cirúrgico', 'médico']):
        return 'Saúde'

    # Acessórios
    elif any(keyword in titulo for keyword in ['relógio', 'óculos', 'bolsa', 'mochila', 'cinto', 'carteira']):
        return 'Acessórios'

    # Kits
    elif 'kit' in titulo:
        return 'Kits de Produtos'

    # Outros
    else:
        return 'Outros'


# Aplicar a função para criar a coluna 'departamento'
df['departamento'] = df['Título'].apply(definir_departamento)

# Exibir as primeiras linhas para verificar a nova coluna
print(df[['Título', 'departamento']].nunique())

# Salvar o DataFrame atualizado
df.to_csv('C:/Users/User/Downloads/ecommerce_preparados.csv', index=False)
