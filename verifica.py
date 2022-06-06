import os
from datetime import datetime

caminho = "/home/adriano/arqui_2/"
lista_arquivos = os.listdir(caminho)

lista_datas = []
for arquivo in lista_arquivos:
    data = os.path.getmtime(f"{caminho}/{arquivo}")
    lista_datas.append((data, arquivo))
    
lista_datas.sort(reverse=True)
ultimo_arquivo = lista_datas[0]
#busca na pasta ultimo aquivo modificado , atraves da data que esta em timestamp.


#print(ultimo_arquivo[0])
ts = datetime.today()
dataseg =ts.timestamp()
#data atual convertita em timestamp


if (round(dataseg, -5)) != (round(ultimo_arquivo[0], -5)):
    print('Não encontrado!')
else:
    print('OK')
#  
print(round(dataseg, -5))
print(round(ultimo_arquivo[0], -5))