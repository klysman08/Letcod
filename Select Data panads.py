import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]

# test: pd.DataFrame({'student_id': [101, 102, 103], 'name': ['John', 'Paul', 'Ringo'], 'age': [22, 21, 23]})
teste = selectData(pd.DataFrame({'student_id': [101, 102, 103], 'name': ['John', 'Paul', 'Ringo'], 'age': [22, 21, 23]}))
print(teste)