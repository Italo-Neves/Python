import pandas as pd
uri ="https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.1/movies.csv"
filmes = pd.read_csv(uri)
#print(filmes)
filmes.columns = ["filmes_ID","titulo","genero"]
print(filmes.head())
urin = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
notas = pd.read_csv(urin)
print(notas.head())