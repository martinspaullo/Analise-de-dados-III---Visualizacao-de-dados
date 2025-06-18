import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("dados/Pedidos.csv")

#1-Criando uma única figura com quatro subplots
fig, ax = plt.subplots(2, 2, figsize=(15, 15))

#Gráfico 1 - Quantidade de Unidades vendidas por região
df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color='skyblue', ax=ax[0, 0])
ax[0, 0].set_title('Quantidade de Unidades Vendidas por Região')
ax[0, 0].set_xlabel('Região')
ax[0, 0].set_ylabel('TOtal de Unidades Vendidas')
ax[0, 0].tick_params(axis='x', rotation=45)

#Gráfico 2 - DIstribuição das vendas por item (Pizza)
df['Item'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax[0, 1])
ax[0, 1].set_title('Distribuição das Vendas por Item')
ax[0, 1].axis('equal')

#Gráfico 3- Relação entre preço unitário e quantidade de unidades
ax[1, 0].scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)
ax[1, 0].set_title('Relação entre Preço Unitário e Quantidade de Unidades')
ax[1, 0].set_xlabel('Preço Unitário')
ax[1, 0].set_ylabel('Quantidade de Unidades')
ax[1, 0].grid(True)

#Gráfico 4 - Quantidade de Unidades Vendidas ao Longo do Tempo
# Convertendo a coluna DataPedido para o formato de data
df['DataPedido'] = pd.to_datetime(df['DataPedido'])

df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='green', ax=ax[1, 1])
ax[1, 1].set_title('Quantidade de Unidades Vendidas ao Longo do Tempo')
ax[1, 1].set_xlabel('Data do Pedido')
ax[1, 1].set_ylabel('Total de Unidades Vendidas')
ax[1, 1].grid(True)

plt.tight_layout()

plt.show()