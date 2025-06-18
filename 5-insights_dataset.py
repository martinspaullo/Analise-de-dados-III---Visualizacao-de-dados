import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("dados/Pedidos.csv")

# Lista de cores (uma para cada barra)
cores = ['red', 'blue', 'orange']

#Gráfico 1 - Quantidade de Unidades vendidas por região
plt.figure(figsize=(8, 6))
df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color=cores)
plt.title('Quantidade de Unidades Vendidas por Região')
plt.xlabel('Região')
plt.ylabel('TOtal de Unidades Vendidas')
plt.xticks(rotation=45)
plt.show()

#Gráfico 2 - DIstribuição das vendas por item (Pizza)
plt.figure(figsize=(8, 6))
df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das Vendas por Item')
plt.axis('equal')
plt.show()

#Gráfico 3- Relação entre preço unitário e quantidade de unidades
plt.figure(figsize=(8, 6))
plt.scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)
plt.title('Relação entre Preço Unitário e Quantidade de Unidades')
plt.xlabel('Preço Unitário')
plt.ylabel('Quantidade de Unidades')
plt.grid(True)
plt.show()


# #Gráfico 4 - Quantidade de Unidades Vendidas ao Longo do Tempo
# Convertendo a coluna DataPedido para o formato de data
df['DataPedido'] = pd.to_datetime(df['DataPedido'])

plt.figure(figsize=(10, 6))
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='green')
plt.title('Quantidade de Unidades Vendidas ao Longo do Tempo')
plt.xlabel('Data do Pedido')
plt.ylabel('Total de Unidades Vendidas')
plt.grid(True)
plt.show()

#Gráfico 5 - Quantidade de Unidades Vendidas por Estado em cada região
pivot = df.pivot_table(
    index='Estado',
    columns='Regiao',
    values='Unidades',
    aggfunc='sum',
    fill_value=0
)
plt.figure(figsize=(10, 6))
pivot.plot(kind='bar',stacked=True)
plt.title('Quantidade de Unidades Vendidas por Estado em cada Região')
plt.xlabel('Estado')
plt.ylabel('Total de Unidades Vendidas')
plt.legend(title='Regiao', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()
