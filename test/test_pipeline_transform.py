import pandas as pd
from app.pipeline.transform import unir_dataframes

def test_unir_dataframes():
    # Criando um conjunto de dados de exemplo
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    df3 = None
    data_frames = [df1, df2, df3]
    
    # Unindo os data frames
    result = unir_dataframes(data_frames)
    
    # Verificando se o resultado é o esperado
    expected_result = pd.DataFrame({'A': [1, 2, 5, 6], 'B': [3, 4, 7, 8]})
    assert result.equals(expected_result), f"Resultado incorreto: {result}"
    
    print("Teste passou com sucesso!")

test_unir_dataframes()
    
    
    