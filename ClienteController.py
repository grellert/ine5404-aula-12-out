from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {}

    def inicia(self):
        container = self.__telaCliente.tela_consulta()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Cadastrar':
                #FIX ME - implementar lógica de cadastro
                pass
            elif event == 'Consultar':
                #FIX ME - implementar lógica de consulta
                pass
            
            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)

        self.__telaCliente.fim()


    def buscaCodigo(self, codigo):
        try:
            return self.__clientes[codigo]
        except KeyError:
            raise KeyError

    # cria novo OBJ cliente e adiciona ao dict
    def adicionaCliente(self, codigo, nome):
        self.__clientes[codigo] = Cliente(codigo, nome)
    
    def buscaNome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return key 

        raise LookupError
