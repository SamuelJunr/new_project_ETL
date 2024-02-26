import pandas as pd
import os # biblioteca para manipulação de arquivos e pastas 
import glob  #biblioteca para listar arquivos

from typing import List

"""
     função para ler arquivos de uma pasta data/input e retornar uma lista de dataframes
     
     args: input_path (str): caminho da pasta que contém os dados a serem lidos.
     
     return: lista de dataframes
"""
 
##path = "data/input"   # Caminho padrão para buscar os arquivos
  
def extrator_para_excel(path: str) -> List[pd.DataFrame]: 
     files = glob.glob(os.path.join(path, "*.xlsx")) # busca todos os arquivos .xlsx na pasta informada
          
     data_frame_lista = []
     for file in files:
          data_frame_lista.append(pd.read_excel(file))
               
     return data_frame_lista
"""
if __name__ == "__main__":
     data_frame_list = extrator_para_excel(path)
     print(data_frame_list)                 
"""