# def suma(a=10,b=15):
#     print("Estas sumando")
#     c=a+b
#     print(str(c))
# suma()

#Es lo mismo pero de diferente manera
# def suma(a:int,b:int):
#     print("Estas sumando")
#     c=a+b
#     print(str(c))

# suma(10,15)



# def nombres(name):
#     print(name)

# nombres('Reyli')

# def operaciones(a:int,b:int,op:str):
#     if op == '+':
#         print(a+b)
#     elif op == '-':
#         print(a-b)
#     elif op=='*':
#         print(a*b)
#     else:
#         print(a/b)

# operaciones(10,20,'-')


#---------diccionario--------
# persona={
#     "name":"reyli",
#     "edad":22,
#     "nacionalidad":"Mexicana"
# }
# print(persona["edad"])


#--------clases---------
class persona:
    nombre='Reyli'
    apellido='Cisneros'
    edad=22

    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def getDescription(self):
        print(self.nombre)

    def getEdad(self):
        if self.edad == 22:
            return print("Mayor de edad")

persona=persona()
persona.getDescription()
persona.getEdad()