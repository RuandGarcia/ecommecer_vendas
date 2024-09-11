import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/Users/User/Downloads/ecommerce_preparados.csv')
print(df.nunique())

# Gráfico de dispersão
sns.jointplot(x='VendasPorProduto', y='departamento', data=df, kind='scatter')
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.show()

# Mapa de calor
corr = df[['VendasPorProduto', 'Preço']].corr()
plt.subplot(2, 2, 3)  # 2 linhas, 2 colunas e 3 gráficos
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação - Vendas e Preço')
plt.tight_layout()  # Ajustar espaçamento
plt.show()


# Configuração do gráfico de barras
plt.figure(figsize=(10, 6))
df['departamento'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisão por Departamento')
plt.xlabel('Departamentos')
plt.ylabel('Quantidade')
# Ajuste da rotação dos rótulos do eixo x e espaçamento
plt.xticks(rotation=0, ha='right')  # Rotaciona os rótulos em 45 graus e alinha à direita
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.show()


# Gráfico de Pizza
x = df['GeneroEcommerc'].value_counts().index
y = df['GeneroEcommerc'].value_counts().values
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Gêneros')
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.show()



# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade de Preços')
plt.xlabel('Preço')
plt.show()