import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/ecommerce_preparados.csv')


def simplificar_genero(genero):
    genero = str(genero).strip().lower()

    if genero in ['masculino', 'meninos', 'menino']:
        return 'Masculino'
    elif genero in ['feminino', 'meninas', 'mulher', 'short menina verao look mulher',
                    'bermuda feminina brilho blogueira']:
        return 'Feminino'
    elif genero in ['sem gênero infantil', 'sem gênero']:
        return 'Unissex'
    elif genero in ['bebês', 'bebê']:
        return 'Bebês'
    elif genero in ['unissex']:
        return 'Unissex'
    else:
        return 'Outros'


# Aplicar a função para criar a nova coluna 'GeneroEcommerc'
df['GeneroEcommerc'] = df['Gênero'].apply(simplificar_genero)

# Exibir as primeiras linhas para verificar o resultado
print(df[['GeneroEcommerc', 'Gênero']].nunique())

# Salvar o DataFrame
df.to_csv('C:/Users/User/Downloads/ecommerce_preparados.csv', index=False)