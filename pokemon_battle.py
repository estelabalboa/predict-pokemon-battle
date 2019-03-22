import numpy as np
import pandas as pd
from time import time
from IPython.display import display
import matplotlib.pyplot as plt


class PokemonBattle:

    def __init__(self):
        pokemon_data = pd.read_csv("Dataset_Pokemon_AI6/pokemons_data.csv")
        combats = pd.read_csv("Dataset_Pokemon_AI6/combats.csv")
        test_data = pd.read_csv("Dataset_Pokemon_AI6/tests.csv")

        # Mostrar número de filas y columnas del dataframe
        print("Filas: " + str(pokemon_data.shape[0]) + " Columnas: " + str(pokemon_data.shape[1]))

        # Mostrar las primeras 10 filas
        display(pokemon_data.head(10))

        # Descripción analítica básica del dataframe
        print(np.round(pokemon_data.describe()))

        # Visualizando la distribución de cada variable
        import matplotlib.pyplot as plt
        pokemon_data.hist(bins=50, figsize=(10, 8))
        plt.show()





if __name__ == '__main__':
    battle_result = PokemonBattle()

