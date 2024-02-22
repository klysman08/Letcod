
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)

# test: pd.DataFrame({'name': ['John', 'Paul', 'Ringo'], 'age': [22, 21, 23]})
teste = getDataframeSize(pd.DataFrame({'name': ['John', 'Paul', 'Ringo'], 'age': [22, 21, 23]}))
print(teste)