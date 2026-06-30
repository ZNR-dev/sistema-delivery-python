from datetime import date

# Variables globales para almacenar la información del sistema
pedidos = {}  # Estructura: {id_pedido: {datos_dict}}
contador_id_pedido = 1
historial_clientes = {}  # Estructura: {"NombreCliente": cantidad_compras} 
fecha_actual = date.today() #para mostrar la fecha del dia
#diccionario para las zonas que estan permitidas
zonas_opciones = {
    "1": "Resistencia",
    "2": "Barranqueras",
    "3": "Fontana",
    "4": "Puerto Vilelas"
}
#diccionario de los precios segun la zona
tabla_zonas = {
    "Resistencia": 1000.0,
    "Barranqueras": 2000.0,
    "Fontana":3500.0,
    "Puerto Vilelas":4000.0
}

def ver_pedidos():
    # Validación por si el diccionario de pedidos está vacío
    if not pedidos:
        print("\n[Info] No hay pedidos registrados.")
        return
        
    print("\n  Reporte de operaciones:")
    # Recorremos el diccionario de pedidos usando su clave (id) y valor (datos)
    for id_p, p in pedidos.items():
        fecha_dia = fecha_actual.strftime("%d/%m/%y")
        print("\nFecha:", fecha_dia) 
        print(f"ID: {id_p} | Cliente: {p['cliente']} | Fecha: {p['fecha']} | Zona: {p['zona']}")
        print(f"Productos: {p['productos_texto']}")
        print(f"Total: ${p['total']:.2f}")
        print("-" * 30)

def menu_sistema():
    # Se declara global para poder modificar el contador de IDs desde esta función
    global contador_id_pedido 
    global pedidos 
    
    print("\n--- Menu del Delivery ---")
    print("1. Registrar nuevo pedido")
    print("2. Ver todos los pedidos")
    print("3. Cambiar estado de un pedido")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4): ").strip()

    if opcion == "1":
        print("\nRegistrando pedido....")

      
        cliente = input("\nNombre del cliente: ").strip().capitalize()
        
        subtotal=0.0
        productos_texto=""
        
        while True:
            nombre_prod = input("\nNombre del producto (o '0' para terminar'): ").strip()
            if nombre_prod.lower() == '0':
                break
            try:
                precio_prod = float(input(f"Precio de '{nombre_prod}': $"))
                subtotal+=precio_prod
                # Guardamos el producto actual en la lista y sumamos su valor al total
                if productos_texto == "":
                    productos_texto=nombre_prod
                else:
                    productos_texto+=","+nombre_prod

            except ValueError:
                print("Error: Precio invalido. Producto no Agregado.")
        
        if subtotal==0.0:
            print("operacion cancelada:no se agregaron productos.")
            return

        print("\nZonas\n1.Resistencia\n2.Barranqueras\n3.Fontana\n4.Puerto Vilelas"),
        z_op=input("seleccione zona(1-4):").strip()

        if z_op in zonas_opciones:
            zona_elegida=zonas_opciones[z_op]
        else:
            zona_elegida="Resistencia"
        
        if cliente not in historial_clientes:
            historial_clientes[cliente]=0
        historial_clientes[cliente]+=1

        es_frecuente=(historial_clientes[cliente]==3)
        costo_envio=0.0 if es_frecuente else tabla_zonas[zona_elegida]

        total_final=subtotal+costo_envio
        fecha_dia=fecha_actual.strftime("%d/%m/%y")
        print(f"\nTICKET                                     N°:{contador_id_pedido}")
        print("Fecha                                  ",fecha_dia) 
        print("             Sistema Delivery                    ")
        print("-------------------------------------------------")  
        print(f"Cliente:{cliente}")
        print(f"productos:{productos_texto}")
        print(f"subtotal:${subtotal:.2f}")
        print(f"Costo del Envío({zona_elegida}):${costo_envio:.2f})")
        print(f"\nTOTAL A PAGAR:${total_final:.2f}")
        print("----------------------------------------------------")
        print("\nDesea seguir con el pago?\n1.Sí\n2.No")

        if input("seleccione (1-2):").strip()=="1":
            if es_frecuente:
                historial_clientes[cliente]=0

            print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")
            contador_id_pedido+=1
        else:
            historial_clientes[cliente]-=1
              
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
        print("\n-----Bienvenido a Sistema Delivery-----")
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
