class Animal:
    def __init__(self, tipo):
        self.tipo=tipo

    def piernas(self):
        pass
    def volador(self):
        pass
    def raza(self):
        print(f"La raza es {self.tipo}")

class Perro(Animal):
    def piernas(self):
        return 4
    def volador(self):
        return False

class Ave(Animal):
    def piernas(self):
        return 2
    def volador(self):
        return True
    
perro=Perro('chihuahua')
perro.raza()

ave=Ave('avestruz')
print(ave.raza())