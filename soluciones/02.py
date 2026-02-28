import pandas as pd
import codecs 

datos= pd.read_csv('data/personas.csv')

texto_original = "MARIA"

#filtrar (ROT13)
texto_cifrado =codecs.encode(texto_original,'rot 13')
print(f"cifrado:(texto_cifrado)")

#MARIA = ZNEVN

condicion = datos ['nombre_cifrado']== 'Znevn'
datos_nuevos= datos [condicion]
print("El numero de repeticiones de Maria es:", datos _nuevos.shape[0])