class pila:
    def __init__(self,n):
        self.pila_inversa=([])
        self.pila=[]
        self.n=n

#se apilan los elementos en una pila mientras x!=""
    def apilar(self):
        while self.n != "1":
            self.pila+=[self.n]
            print("otro caracter")
            self.n=input()
        print("La pila tiene valores de: ", *self.pila)

#se desapila los caracteres y se almacena en una nueva pila mediante un for de manera inversa
    def desapilar(self):
        for self.n in self.pila[::-1]:
            self.pila_inversa+=[self.n]
        return self.pila_inversa