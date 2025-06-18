import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#1-Criando dados fictícios de preços de ações
# para diferentes empresas ao longo de trimestres
empresas = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D']
trimestres = ['T1', 'T2', 'T3', 'T4']

dados = np.random.rand(4, 4) * 100
# Valores aleatórios entre 0 a 100 para simular os preços das ações

#2-Criando um Dataframe com os dados
df = pd.DataFrame(
    dados,
    columns=trimestres,
    index=empresas
)

print(df)

#3-Criando o heatmap usando Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Preço de Ações por Trimestre')
plt.xlabel('Trimestre')
plt.ylabel('Empresa')
plt.show()