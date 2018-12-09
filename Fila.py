
class No:
    def __init__(self,conteudo):
        self.conteudo = conteudo
        self.proximo = None
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0
        self.__iterando = None

    def is_empty(self):
        return self.__tamanho == 0

    def __iter__(self):
        return self

    def __len__(self):
        return self.__tamanho

    def __repr__(self):
        return self.__str__()

    def __get__index(self,ind):
        if ind >= self.__tamanho:
            return None
        else:
            perc = self.__tamanho
            for i in range(self.__tamanho-1):
                if i == ind:
                    return perc.conteudo
                else:
                    perc = perc.proximo

    def __getitem__(self, ind):
        perc = self.__get__index(ind)
        if perc:
            return perc.conteudo
        else:
            raise IndexError("xxxx")

    def __next__(self):
        if self.__tamanho is None:
            self.__iterando = self.primeiro
        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando

    def __setitem__(self, ind, conteudo):
        perc = self.__get__index(ind)
        if perc:
            perc.conteudo = conteudo
        else:
            raise IndexError(" xxx")

    def __str__(self):
        perc = self.primeiro
        conteudo = '['
        for i in range(self.__tamanho):
            conteudo += str(perc.conteudo) + ', '
            perc = perc.proximo
        conteudo = conteudo.strip(', ')
        return conteudo

    def aumen(self,conteudo):
        novo = No(conteudo)
        if self.is_empty():
            self.primeiro = novo
            self.ultimo = novo

        else:
            self.ultimo.proximo = novo
            self.ultimo = novo
        self.__tamanho += 1

    def dimin(self):
        if self.is_empty():
            return False
        else:
            aux = self.primeiro
            self.primeiro = aux.proximo
            self.__tamanho -= 1

    Fila = FilaC(0)
    Fila.aumen(1)
    Fila.aumen(2)
    Fila.aumen(3)
    Fila.dimin()

