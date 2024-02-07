import tkinter as tk
from tkinter.ttk import *
import testes
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib as mpl
from mplcursors import cursor
mpl.use('TkAgg')


def siglas():
    indice = lst_moedas.index(moeda1.get())
    sigla = sigla_moeda[indice]

    indice2 = lst_moedas.index(moeda2.get())
    sigla2 = sigla_moeda[indice2]

    juncao = sigla + "-" + sigla2
    global jsimples
    jsimples = sigla + sigla2

    return juncao

def buscar():
    sigla = siglas()
    if sigla not in combinacao:
        er = tk.Label(root, text='Combinação Invalida')
        er.grid(row=4, column=1)

        vf = tk.Label(root, text='                              ')
        vf.grid(row=3, column=0)

    else:
        cotacao = requests.get(f'https://economia.awesomeapi.com.br/json/last/{sigla}').json()
        er = tk.Label(root, text="                                             ")
        er.grid(row=4, column=1)

        preco  = cotacao[jsimples]['bid']
        valor_moeda = float(preco) * float(valor1.get())

        msg1 = tk.Label(text=f'Valor moeda e igual a {float(preco):.2f}')
        msg1.grid(column=0, row=0)

        vf = tk.Label(root, text=f'{valor_moeda:.2f}')
        vf.grid(row=3, column=0)

def last30():
    #Pegando os precos e a data de cada um dos 30 dias anteriores
    req30 = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{siglas()}/30')
    if req30.status_code == 200:
        lst30 = req30.json()
        lst_dia = []
        lst_preco = []

        for i in lst30:
            a = datetime.fromtimestamp(int(i['timestamp'])).date()
            lst_dia.append(a)
            lst_preco.append(round(float(i['bid']),2))

            lst_dia.reverse()
            lst_preco.reverse()

        plt.plot(lst_dia,lst_preco)
        cursor(hover=True)
        plt.show()


    else:
        pass




lst_moedas = list(testes.moeda_dicionario.keys())
sigla_moeda = list(testes.moeda_dicionario.values())
combinacao = testes.combinacoes_moedas

root = tk.Tk()
root.title("Cotacao")
root.geometry('300x225')


msg1 = tk.Label(text='Valor moeda e igual a ')
msg1.grid(column=0, row=0)

key = tk.StringVar()
moeda1 = Combobox(root, values=lst_moedas, textvariable=key)
moeda1.current(lst_moedas.index("Dólar Americano"))
moeda1.grid(column=1, row=1)

valor1 = tk.Entry()
valor1.insert(0, 0)
valor1.grid(column=0, row=1)


moeda2 = Combobox(root, values=lst_moedas)
moeda2.current(lst_moedas.index("Real Brasileiro"))
moeda2.grid(column=1, row=3)

texto2 = tk.Label(text="Equivalem a: ")
texto2.grid(column=0, row=2)


botao30 = Button(root, text="Ultimos 30 dias", command=last30)
botao30.grid(column=0, row=5)


botao1 = Button(root, text="buscar", command=buscar)
botao1.grid(column=0, row=4)



root.mainloop()





