import PySimpleGUI as sg 
import Cliente

# View do padrão MVC
class ClienteView():
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__container = []
        self.__largura_resposta = 40 #aux. var
        self.__window = sg.Window('Consulta de clientes', self.__container ,font=('Helvetica', 14))

    def tela_consulta(self):
        linha0 = [sg.Text('Digite o código ou o nome do cliente e clique na ação desejada:')]
        linha1 = [sg.Text('Código:'), sg.InputText('', key='codigo')]
        linha2 = [sg.Text('Nome:'), sg.InputText('', key='nome')]
        linha3 = [sg.Button('Cadastrar'), sg.Button('Consultar'), sg.Button('Remover'), sg.Button('Listar')]
        linha4 = [sg.Text('', size=(self.__largura_resposta, 1), key='resultado')]
        
        self.__container = [linha0, linha1, linha2, linha3, linha4]
        self.__window = sg.Window('Consulta de clientes', self.__container ,font=('Helvetica', 14))


    def prepara_area_texto(self, nlinhas):
        self.__window.Element('resultado').set_size((self.__largura_resposta, nlinhas))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)

    def limpa_dados(self):
        self.__window.Element('nome').Update('')
        self.__window.Element('codigo').Update('')

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()