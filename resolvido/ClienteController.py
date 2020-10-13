from ClienteView import ClienteView
from Cliente import Cliente
import PySimpleGUI as sg 

class ClienteController:
    def __init__(self):
        self.__telaCliente = ClienteView(self)
        self.__clientes = {}
        sg.theme('Reddit')

    def inicia(self):
        self.__telaCliente.tela_consulta()
        
        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__telaCliente.le_eventos()
            self.__telaCliente.prepara_area_texto(1)

            if event == sg.WIN_CLOSED:
                rodando = False
            else:
                try:
                    if event == 'Cadastrar':
                        codigo = int(values['codigo'])
                        nome = values['nome']
                        resultado = self.adiciona_cliente(codigo, nome)
                    elif event == 'Consultar':
                        codigo = self.get_codigo(values)
                        resultado = self.busca_codigo(codigo)
                    elif event == 'Remover':
                        codigo = self.get_codigo(values)
                        resultado = self.remove_cliente(codigo)
                    elif event == 'Listar':
                        self.__telaCliente.prepara_area_texto(len(self.__clientes))
                        resultado = self.clientes_to_string()
                except ValueError:
                    resultado = 'Código deve ser um número inteiro!'
                except KeyError:
                    resultado = 'Valor não cadastrado!'
                except NameError:
                    resultado = 'Digite ao menos um campo!'

            if resultado != '':
                dados = str(resultado)
                self.__telaCliente.mostra_resultado(dados)
                self.__telaCliente.limpa_dados()

        self.__telaCliente.fim()

    # se o cadastro não existir, levanta key error
    def busca_codigo(self, codigo):
        return self.__clientes[codigo]
    
    def busca_nome(self, nome):
        for key, val in self.__clientes.items():
            if val.nome == nome:
                return key 

        raise KeyError

    # retona código, buscando pelo nome se necessários
    # se o cadastro não existir, levanta NameError
    def get_codigo(self, values):
        if values['codigo'] != '':
            codigo = int(values['codigo'])
        elif values['nome'] != '':
            codigo = self.busca_nome(values['nome'])
        return codigo

    # cria novo OBJ cliente e adiciona ao dict
    def adiciona_cliente(self, codigo, nome):
        if nome == '':
            return 'Campo nome vazio!'
        elif codigo not in self.__clientes:
            self.__clientes[codigo] = Cliente(codigo, nome)
            return 'Cliente adicionado com sucesso'
        else:
            return 'Código já cadastrado!'

    # remove cliente do dict
    def remove_cliente(self, codigo):
        if codigo in self.__clientes:
            del self.__clientes[codigo]
            return 'Cliente removido com sucesso'
        else:
            return 'Código não cadastrado!'

    def clientes_to_string(self):
        return '\n'.join([str(c) for c in self.__clientes.values()])