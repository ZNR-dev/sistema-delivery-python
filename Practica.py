'''
sistema-delivery-python
Sistema de gestión de delivery desarrollado en Python que permite registrar y administrar pedidos, calcular importes automáticamente, gestionar estados de entrega y facilitar el control de operaciones del servicio. El proyecto está diseñado siguiendo una estructura modular y buenas prácticas de programación.

Descripción

Este sistema permite gestionar pedidos de un servicio de delivery, incluyendo registro de pedidos, cálculo de importes y control de estados.
Funcionalidades

    Crear pedidos
    Ver pedidos
    Calcular el total
    Cambiar estado del pedido
'''

#Usaremos una clase para crear cada pedido, ya que es por asi decir una "libreria" que contiene informacion sobre los distintos pedidos.
class Pedido:
    # Un contador que va a incrementar para distintos pedidos, asi cada uno tiene una ID individual y unica
    contador_id = 1
    # usamos def para definir una funcion, __init__ basicamente crea un objeto vacio donde guardaremos la informacion del pedido.
    def __init__(self, cliente, productos_con_precio):
        #self, cliente, productos con precio : son las caractersticas del objeto, self se usa para llamarse a si mismo
        self.id = Pedido.contador_id
        Pedido.contador_id += 1
        #Aca asignamos un id al pedido, y luego incrementamos el contador para el siguiente pedido
        self.cliente = cliente
        # Se espera una lista de diccionarios: [{"nombre": str, "precio": float}]
        self.productos = productos_con_precio 
        self.estado = "Pendiente" #Se coloca pendiente por defecto
        self.total = self.calcular_total() #Llamamos a otra funcion que calcula un precio

    def calcular_total(self):
        total_acumulado = 0.0
        for prod in self.productos:
            # Uso de .get() si el diccionario viene incompleto
            total_acumulado += prod.get("precio", 0.0)
        return total_acumulado #Aca devuelve el total acumulado, la funcion devuelve este valor

    def actualizar_estado(self, nuevo_estado):
        estados_validos = ["Pendiente", "En Camino", "Entregado"]
        #Podemos cambiar esto igual, agregando o quitando estados del pedido
        if nuevo_estado in estados_validos: #Aca controlamos que el estado que colocamos este dentro de estados validos
            self.estado = nuevo_estado
            print(f"Estado del pedido #{self.id} actualizado a: {nuevo_estado}")
        else:
            print(f"Error: '{nuevo_estado}' no es un estado de entrega valido.")
            #Esto devuelve error porque colocamos algo que no era un estado o un estado que no existe

class SistemaDelivery:
    def __init__(self):
        # Almacenamiento indexado por ID
        self.pedidos = {}

    def crear_pedido(self, cliente, productos_con_precio):
        nuevo_pedido = Pedido(cliente, productos_con_precio)
        self.pedidos[nuevo_pedido.id] = nuevo_pedido
        print(f"Pedido #{nuevo_pedido.id} registrado para {cliente}. Total: ${nuevo_pedido.total:.2f}")
        return nuevo_pedido

    def ver_pedidos(self):
        if not self.pedidos:
            print("[Info] No hay pedidos registrados en el sistema.")
            return

        print("\n   Reporte de Operaciones:")
        for pedido in self.pedidos.values():
            nombres_productos = [prod.get("nombre", "Desconocido") for prod in pedido.productos]
            print(f"ID: {pedido.id} | Cliente: {pedido.cliente}")
            print(f"Productos: {', '.join(nombres_productos)}")
            print(f"Total: ${pedido.total:.2f} | Estado: {pedido.estado}")
            print("-" * 30)


def ejecutar_menu():
    sistema = SistemaDelivery()

    while True:
        print("\n Menu del Delivery")
        print("1. Registrar nuevo pedido")
        print("2. Ver todos los pedidos")
        print("3. Cambiar estado de un pedido")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion (1-4): ").strip()

        if opcion == "1":
            print("\n Registrando pedido")
            cliente = input("Nombre del cliente: ").strip()
            
            productos_pedido = []
            while True:
                nombre_prod = input("Nombre del producto (o 'fin' para terminar): ").strip()
                if nombre_prod.lower() == 'fin':
                    break
                
                try:
                    precio_prod = float(input(f"Precio de '{nombre_prod}': $"))
                    productos_pedido.append({"nombre": nombre_prod, "precio": precio_prod})
                except ValueError:
                    print("Error: El precio debe ser un valor numerico decimal. Reintente el producto.")
            
            if productos_pedido:
                sistema.crear_pedido(cliente, productos_pedido)
            else:
                print("Operacion cancelada: No se ingresaron productos al pedido.")

        elif opcion == "2":
            sistema.ver_pedidos()

        elif opcion == "3":
            if not sistema.pedidos:
                print("[Info] No existen pedidos en el sistema para modificar.")
                continue
                
            print("\n Actualizando estado")
            try:
                id_buscar = int(input("Ingrese el ID del pedido: "))
                if id_buscar in sistema.pedidos:
                    print("Estados validos: Pendiente, En Preparación, En Camino, Entregado")
                    nuevo_estado = input("Ingrese el nuevo estado: ").strip()
                    sistema.pedidos[id_buscar].actualizar_estado(nuevo_estado)
                else:
                    print(f"Error: El pedido con ID {id_buscar} no existe.")
            except ValueError:
                print("Error: El ID del pedido debe ser un numero entero.")

        elif opcion == "4":
            print("Finalizando ejecucion del programa.")
            break
        else:
            print("Error: Opcion fuera de rango. Ingrese un numero del 1 al 4.")


if __name__ == "__main__":
    ejecutar_menu()