# O violinplot é útil para visualizar a distribuição 
# de uma variável numérica em diferentes categorias.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#1-Criando Dataframe fictício
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros']
vendas = {
    'Categoria': np.random.choice(categorias, 1000),
    'Vendas': np.random.normal(loc=50, scale=20, size=1000)
}

df = pd.DataFrame(vendas)
print(df)

#2-Criando ViolinPlot com Seaborn
plt.figure(figsize=(8, 6))
sns.violinplot(
    x='Categoria',
    y='Vendas',
    data=df,
    palette='muted'
)
plt.title('Distribuição de Vendas por CAtegoria')
plt.xlabel('Categoria')
plt.ylabel('Vendas')
plt.show()
