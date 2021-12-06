
import requests
import json
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes= cotacoes.json()
#print (cotacoes)"
cotacao_dolar= float(cotacoes['USDBRL']['bid'])
resultado=0
valor=0

valor= int(input("Digite o valor : "))
resultado= valor * cotacao_dolar
print(resultado)

