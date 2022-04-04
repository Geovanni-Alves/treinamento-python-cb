from msilib.schema import ComboBox
from ssl import VERIFY_X509_PARTIAL_CHAIN
from tkinter.ttk import Combobox
import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USD']['bid']
    cotacao_euro = requisicao_dic['EUR']['bid']
    cotacao_btc = requisicao_dic['BTC']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


# pegar_cotacoes()

janela = Tk()
janela.title("Cotação atual das moedas (Dolar, Euro e Bitcoin)")
# janela.geometry("300x200")

texto_orientacao = Label(
    janela, text="Clique no botão para ver as cotações das moedas!")

texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações Dolar/Euro/BTC",
               command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)
texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)
# label_combobox = Label(janela, text="Escolha um estado")
# label_combobox.grid(column=0, row=3)
# combo_box = Combobox(janela, text="Testando o combobox",
#                      values=["GO", "SP", "PA", "BA"])

#combo_box.grid(column=0, row=4, padx=10, pady=10)


def testVal(inStr, acttyp):
    if acttyp == '1':  # insert
        if not inStr.isdigit():
            return False
    return True


#entrada = Entry(janela, validate="key")
#entrada.grid(column=0, row=3, padx=5, pady=5)
#entrada['validatecommand'] = (entrada.register(testVal), '%P', '%d')
# entrada.pack()


#entry = Entry(root, validate="key")


# root.mainloop()


janela.mainloop()
