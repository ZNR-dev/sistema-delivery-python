pedidos= {} #Estructura :{id_pedido:{datos_dict}}
contador_id_pedido=1
historial_clientes= {} #Estructura:{ "NombreCliente":cantidad_compras } 
from datetime import date
fecha_actual = date.today()

def ver_pedidos():
    if not pedidos:
        print("\n[Info] No hay pedidos registrados")
        return
    print("\n  reporte de operaciones:")
    for id_p , p in pedidos.items():
        print(f"ID: {id_p} | Cliente: {p['cliente']} ")
        print(f"Repartido:{p['repartidor']} | Productos: {p['productos_texto']}")
        print("-" * 30)

def menu_sistema():
    print("\n--- Menu del Delivery ---")
    print("1. Registrar nuevo pedido")
    print("2. ver todos los pedidos")
    print("3. Cambiar estado de un pedido")
    print("4. Salir")

    opcion = input("seleccione una opcion (1-4):").strip()

    if opcion == "1":
        print("\nRegistrando pedido....")

        fecha_dia = fecha_actual.strftime("%d/%m/%y")
        print("\nFecha:", fecha_dia)
        print("- - - - - - - - - - - - - - - - - - - - - -")
        cliente = input("Nombre del cliente: ").strip()
        print("- - - - - - - - - - - - - - - - - - - - - -")
        productos_pedidos = []
        while True:
            nombre_prod = input("\nNombre del producto: ").strip()
            try:
                precio_prod = float(input(f"Precio de '{nombre_prod}':$"))
                productos_pedidos.append({"nombre":nombre_prod,"precio":precio_prod})
            except ValueError:
                print("Error:Precio invalido. Producto no Agregado")
                continue
            print("\n¿Desea seguir agregando productos a su lista")
            print("1. Sí, deseo seguir agregando")
            print("2.No, Finalizar carga de productos")
            
            bucle_prod = input("Seleccione una opcion (1 o 2): ").strip()
            if bucle_prod != "1":
                break
                
            
            
    elif opcion == "2":
        ver_pedidos()
    elif opcion == "3":
        print("proximamente la parte para cambiar el estado del programa")
    elif opcion == "4":
        print("Volviendo al menu de inicion")

    else:
        print("[Error] opcion invalida. Intente de nuevo.")



def ejecutar_inicio():
    global contar_id_pedido
    while True:
        print("\n-----Bienvenido a sistema delivery-----")
        print("1.Ver menu")
        print("2.cerrar sesion")
        op = input("seleccione una opcion (1 o 2): ").strip()
        if op == "1":
            menu_sistema()
        elif op == "2":
            print("finalizando ejecucion del programa")
            break
        else:
            print("[Error] opcion invalida. intente de nuevo.")


if __name__ == "__main__":     
        ejecutar_inicio()
