from datetime import date

# Variables globales para almacenar la información del sistema
pedidos = {}  # Estructura: {id_pedido: {datos_dict}}
contador_id_pedido = 1
historial_clientes = {}  # Estructura: {"NombreCliente": cantidad_compras} 
fecha_actual = date.today()

def ver_pedidos():
    # Validación por si el diccionario de pedidos está vacío
    if not pedidos:
        print("\n[Info] No hay pedidos registrados.")
        return
        
    print("\n  Reporte de operaciones:")
    # Recorremos el diccionario de pedidos usando su clave (id) y valor (datos)
    for id_p, p in pedidos.items():
        print(f"ID: {id_p} | Cliente: {p['cliente']} | Fecha: {p['fecha']}")
        print(f"Productos: {p['productos_texto']}")
        print(f"Total: ${p['total']:.2f}")
        print("-" * 30)

def menu_sistema():
    # Se declara global para poder modificar el contador de IDs desde esta función
    global contador_id_pedido  
    
    print("\n--- Menu del Delivery ---")
    print("1. Registrar nuevo pedido")
    print("2. Ver todos los pedidos")
    print("3. Cambiar estado de un pedido")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4): ").strip()

    if opcion == "1":
        print("\nRegistrando pedido....")

        fecha_dia = fecha_actual.strftime("%d/%m/%y")
        print("\nFecha:", fecha_dia)
        print("- - - - - - - - - - - - - - - - - - - - - -")
        cliente = input("Nombre del cliente: ").strip().capitalize()
        print("- - - - - - - - - - - - - - - - - - - - - -")
        
        # AGREGADO: Lista para almacenar los productos y variable para acumular el costo total
        productos_pedidos = []
        total_pedido = 0.0
        
        while True:
            nombre_prod = input("\nNombre del producto: ").strip()
            try:
                precio_prod = float(input(f"Precio de '{nombre_prod}': $"))
                # Guardamos el producto actual en la lista y sumamos su valor al total
                productos_pedidos.append({"nombre": nombre_prod, "precio": precio_prod})
                total_pedido += precio_prod
            except ValueError:
                print("Error: Precio invalido. Producto no Agregado.")
                continue
                
            print("\n¿Desea seguir agregando productos a su lista?")
            print("1. Sí, deseo seguir agregando")
            print("2. No, Finalizar carga de productos")
            
            bucle_prod = input("Seleccione una opcion (1 o 2): ").strip()
            if bucle_prod != "1":
                break
        
        # AGREGADO: Guardado efectivo del pedido e incremento del historial
        if productos_pedidos:
            # Convertimos la lista de productos en una sola cadena de texto separada por comas
            nombres_prod_texto = ", ".join([prod["nombre"] for prod in productos_pedidos])
            
            # Guardamos toda la información recolectada dentro del diccionario global 'pedidos'
            pedidos[contador_id_pedido] = {
                "cliente": cliente,
                "productos_texto": nombres_prod_texto,
                "total": total_pedido,
                "fecha": fecha_dia,
                "repartidor": "No asignado"
            }
            
            # Registramos la compra en el historial del cliente
            if cliente in historial_clientes:
                historial_clientes[cliente] += 1
            else:
                historial_clientes[cliente] = 1
                
            print(f"\n[Éxito] Pedido #{contador_id_pedido} guardado correctamente.")
            print(f"Total a pagar: ${total_pedido:.2f}")
            print(f"Historial: El cliente {cliente} lleva {historial_clientes[cliente]} compra(s) registrada(s).")
            
            # Incrementamos el ID para que el siguiente pedido tenga un número único
            contador_id_pedido += 1
        else:
            print("\n[Cancelado] No se ingresaron productos. Pedido no registrado.")
            
    elif opcion == "2":
        ver_pedidos()
    elif opcion == "3":
        print("Proximamente la parte para cambiar el estado del programa.")
    elif opcion == "4":
        print("Volviendo al menu de inicio.")
    else:
        print("[Error] Opcion invalida. Intente de nuevo.")

def ejecutar_inicio():
    while True:
        print("\n-----Bienvenido a sistema delivery-----")
        print("1. Ver menu")
        print("2. Cerrar sesion")
        op = input("Seleccione una opcion (1 o 2): ").strip()
        if op == "1":
            menu_sistema()
        elif op == "2":
            print("Finalizando ejecucion del programa.")
            break
        else:
            print("[Error] Opcion invalida. Intente de nuevo.")

if __name__ == "__main__":     
    ejecutar_inicio()
