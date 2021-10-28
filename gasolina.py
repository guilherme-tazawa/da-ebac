import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço médio da gasolina em julho', xlabel='Dias', ylabel='Preço médio')
  grafico.figure.savefig(fname="gasolina.png", bbox_inches="tight");