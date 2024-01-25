class Producto():
    def __init__(self,código, nombre, precio):
        self.__código = código
        self.__nombre = nombre
        self.__precio = precio

    '''Metodos Getter y Setter'''
    
    @property
    def código(self):
        return self.__código
    
    @código.setter
    def código(self,valor):
        self.__código = valor
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    
    def calcular_total(self, unidades):
        return self.__precio * unidades
    
    def __str__(self):
        return f"\nCódigo: {self.__código}\tNombre: {self.__nombre}\tPrecio: {self.__precio}"
    

x1 = Producto(10,"Manzana", 2.5)

x1.nombre = "piña".capitalize()  # Está reemplazando "Fulanito" por "Cristofo Colombo"

print(x1)

usuario = 5
calcular = x1.calcular_total(usuario)
# print(f"Precio por unidad: {x1.precio}\tTotal: {x1.precio * calcular}")

print(f'''
      Precio unitario:     {x1.precio} €
      Unidades adquiridas: {usuario} unidades
      Total              : {calcular} €''')
    