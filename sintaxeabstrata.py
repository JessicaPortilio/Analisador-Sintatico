from abc import abstractmethod
from abc import ABC

# Gramática
# programa : listadecomandos
# listadecomandos : comando
#                | listadecomandos comando
# comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
#         | ID ATRIBUICAO expressao PONTOEVIRGULA
#         | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
#         | WHILE expressao DO listadecomandos ENDWHILE
# expressao : expressao MAIS expressao
#                  | expressao MENOS expressao
#                  | expressao VEZES expressao
#                  | expressao DIVIDE expressao
#                  | ID
#                  | NUMERO


# programa : listadecomandos
#Programa
class Programa():
    def __init__(self, listadecomandos):
        self.listadecomandos = listadecomandos
    @abstractmethod
    def print(self):
        print('[Programa]')
        self.listadecomandos.print()

# listadecomandos → comando
#                 | listadecomandos comando

#Listadecomandos
class Listadecomandos(ABC):
    @abstractmethod
    def print(self):
        pass

class UmComando(Listadecomandos):
    def __init__(self, comando):
        self.comando = comando
    def print(self):
        print('[UmComando]')
        self.comando.print()

class MaisdeUmComando(Listadecomandos):
    def __init__(self, comando, listadecomandos):
        self.comando = comando
        self.listadecomandos = listadecomandos
    def print(self):
        print('[MaisdeUmComando]')
        self.comando.print()
        self.listadecomandos.print()

# comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
#         | ID ATRIBUICAO expressao PONTOEVIRGULA
#         | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
#         | WHILE expressao DO listadecomandos ENDWHILE

#Comando
class Comando(ABC):
    @abstractmethod
    def print(self):
        pass
       

class DeclaracaoVariavel(Comando):
    def __init__(self, ID, expressao):
        self.ID = ID
        self.expressao = expressao
    def print(self):
        print('[DeclaracaoVariavel]')
        print(self.ID)
        self.expressao.print()

class AtribuicaoVariavel(Comando):
    def __init__(self, ID, expressao):
        self.ID = ID
        self.expressao = expressao
    def print(self):
        print('[AtribuicaoVariavel]')
        print(self.ID)
        self.expressao.print()

class expressaoIF(Comando):
    def __init__(self, expressao, listadecomandosIF, listadecomandosElse):
        self.expressao = expressao
        self.listadecomandosIF = listadecomandosIF
        self.listadecomandosElse = listadecomandosElse
    def print(self):
        print('[expressaoIF]')
        self.expressao.print()
        self.listadecomandosIF.print()
        self.listadecomandosElse.print()

class expressaoWhile(Comando):
    def __init__(self, expressao, listadecomandos):
        self.expressao = expressao
        self.listadecomandos = listadecomandos
    def print(self):
        print('[expressaoWhile]')
        self.expressao.print()
        self.listadecomandos.print()

# expressao : expressao MAIS expressao
#                  | expressao MENOS expressao
#                  | expressao VEZES expressao
#                  | expressao DIVIDE expressao
#                  | ID
#                  | NUMERO

#Expressao
class Expressao(ABC):
    @abstractmethod
    def print(self):
        pass

class maisExpressao(Comando):
    def __init__(self, expressao1, expressao2):
        self.expressao1 = expressao1
        self.expressao2 = expressao2
    def print(self):
        print('[maisExpressao]')
        self.expressao1.print()
        self.expressao2.print()

class menosExpressao(Comando):
    def __init__(self, expressao1, expressao2):
        self.expressao1 = expressao1
        self.expressao2 = expressao2
    def print(self):
        print('[menosExpressao]')
        self.expressao1.print()
        self.expressao2.print()
    
class vezesExpressao(Comando):
    def __init__(self, expressao1, expressao2):
        self.expressao1 = expressao1
        self.expressao2 = expressao2
    def print(self):
        print('[vezesExpressao]')
        self.expressao1.print()
        self.expressao2.print()

class divideExpressao(Comando):
    def __init__(self, expressao1, expressao2):
        self.expressao1 = expressao1
        self.expressao2 = expressao2
    def print(self):
        print('[divideExpressao]')
        self.expressao1.print()
        self.expressao2.print()

class idExpressao(Comando):
    def __init__(self, ID):
        self.ID = ID
    def print(self):
        print('[idExpressao]')
        print(self.ID)
        

class numeroExpressao(Comando):
    def __init__(self, NUMERO):
        self.NUMERO = NUMERO
    def print(self):
        print('[idExpressao]')
        print(self.NUMERO)



