class Calculator:
    def add(self, val1, val2):
        return val1 + val2

    def Valid_age(self,value):
        if 0 < value < 100:
            return True
        else:
            return False

    def Maxim(self,maxi1,maxi2,maxi3):
        return max(maxi1,maxi2,maxi3)

    def isVocal(self,caracter1):
        respu = ' '
        if caracter1.isalpha() :
            if caracter1 == 'a' or caracter1 == 'e' or caracter1 == 'i' or caracter1 == 'o' or caracter1 == 'u' or caracter1 == 'A' or caracter1 == 'E' or caracter1 == 'I' or caracter1 == 'O' or caracter1 == 'U':
                respu = 'Vocal'
            else:
                respu = 'Consonante'
        elif caracter1.isnumeric() :
            respu = 'Numero'
        else:
            respu = 'no identificado'
        return respu

    def invertir_cadena(self,cadena):
        return cadena[::-1]

    def Palindromo(self,cadena):
        if cadena == cadena[::-1]:
            return True
        else:
            return False

    def Ope(self,lista):
        L = len(lista)
        Suma = 0
        for i in lista:
            Suma=i+Suma
        Prom=Suma/L
        return [max(lista),min(lista),Prom]

    def Pais(self,paises):
        lena = 0
        j = 0
        for i in paises:
            if len(i) > lena:
                j = i
        return j

    def binario(self,Ndecimal):
        bin = ''
        val = []
        if '.' in Ndecimal:
            bin = 'no valido'
        else:
            if 0 < int(Ndecimal):
                decimal = int(Ndecimal)
                while decimal !=0:
                    val.append(decimal % 2)
                    decimal //= 2
                val = val[::-1]
                for i in val:
                    bin += str(i)
            else:
                bin = 'no valido'
        return bin

    def long(self,cad):
        return len(cad)