from extract import extrator_para_excel
from transform import unir_dataframes
from load import  converter_dataframe

lista_de_dataframe = extrator_para_excel("data/input")
print(lista_de_dataframe)

uniao_dataframes = unir_dataframes(lista_de_dataframe)
print(uniao_dataframes)

template = "data/template/template_1.xlsx"
output = "data/output" 

conversao_dados = converter_dataframe(uniao_dataframes,output,"teste",template)

