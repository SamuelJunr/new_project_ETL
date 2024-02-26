import pandas as pd
from typing  import List, Union


"""
    modulo de transformação de uma lista de data frames em um unico dataframe. 
"""  

def unir_dataframes(data_frames:List[Union[pd.DataFrame, None]]) -> Union[pd.DataFrame,None]:
    if not data_frames:
       raise ValueError("A lista de dataframes está vazia.")
   
    try:
       # Filtrando os data frames validos
       dfs_validos = [df for df in data_frames if df is not None] 
    
       if not dfs_validos:
           raise ValueError("Não há data frames válidos na lista")
      
       #Unir data frames válidos em um só
       result = pd.concat(dfs_validos,ignore_index=True)    # noqa: E999
    
       return result
    
    except ValueError as ve:
        print(ve)
        return None
    
    except Exception as e:
        print(f"Erro ao unir os data frames: {e}")
        return None
    
    
    