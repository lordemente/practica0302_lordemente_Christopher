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
    

class Pedido:
    # def __init_subclass__(self, código, nombre, precio, lista_productos, lista_cantidades):
    #     super().__init__(código, nombre, precio)
    def __init__(self,lista_productos, lista_cantidades):
        self.__lista_productos = lista_productos
        self.__lista_cantidades = lista_cantidades

    def total_pedido(self):
        total = 0
        for (p,c) in zip(self.__lista_productos, self.__lista_cantidades):
            total = total + p.calcular_total(c)
        return total
    
    def mostrar_producto(self):
        for (p,c) in zip(self.__lista_productos, self.__lista_cantidades):
            print(f"Productos: {p.nombre:15} Cantidad: {c}" )


x1 = Producto(2,"Nike", 5)
x2 = Producto(4,"Adidas", 10)
x3 = Producto(6,"Puma", 20)

# x1.nombre = "piña".capitalize()  # Está reemplazando "Fulanito" por "Cristofo Colombo"

print(x1)

usuario = 5
calcular = x1.calcular_total(usuario)
calcular = x2.calcular_total(usuario)
calcular = x3.calcular_total(usuario)
# # print(f"Precio por unidad: {x1.precio}\tTotal: {x1.precio * calcular}")

# print(f'''
#       Precio unitario:     {x1.precio} €
#       Unidades adquiridas: {usuario} unidades
#       Total              : {calcular} €''')

productos = [x1,x2,x3]
cantidades = [5,10,2]

p = Pedido(productos, cantidades)

print(f"Total pedido: {p.total_pedido()} ")
p.mostrar_producto()
