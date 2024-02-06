import tkinter as tk
from tkinter.ttk import *
import testes
import requests
def siglas():
    indice = lst_moedas.index(moeda1.get())
    sigla = sigla_moeda[indice]

    indice2 = lst_moedas.index(moeda2.get())
    sigla2 = sigla_moeda[indice2]

    juncao = sigla + "-" + sigla2

    return juncao

def buscar():
    sigla = siglas()
    if sigla not in combinacao:
        print("Combinacao invalida")
    else:
        cotacao = requests.get(f'https://economia.awesomeapi.com.br/json/last/{sigla}').json()
        print(cotacao)




lst_moedas = list(testes.moeda_dicionario.keys())
sigla_moeda = list(testes.moeda_dicionario.values())
combinacao = testes.combinacoes_moedas

root = tk.Tk()
root.title("Cotacao")
root.geometry('250x250')



msg1 = tk.Label(text='Valor moeda e igual a ')
msg1.grid(column=0, row=0)

key = tk.StringVar()
moeda1 = Combobox(root, values=lst_moedas, textvariable=key)
moeda1.current(lst_moedas.index("Dólar Americano"))
moeda1.grid(column=1, row=1)

valor1 = tk.Entry()
valor1.grid(column=0, row=1)


moeda2 = Combobox(root, values=lst_moedas)
moeda2.current(lst_moedas.index("Real Brasileiro"))
moeda2.grid(column=1, row=3)

texto2 = tk.Label(text="Equivalem a: ")
texto2.grid(column=0, row=2)

#valor2 vai ser o resultado entre a moeda1  e a moeda2
valor2 = tk.Entry()
valor2.grid(column=0, row=3)

#moeda1.set(moeda1.bind("<<ComboboxSelected>>"))

botao1 = Button(root, text="buscar", command=buscar)
botao1.grid(column=0, row=4)



root.mainloop()





