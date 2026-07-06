from datetime import datetime

pedidos = {}  
contador_id_pedido = 1
fecha_actual = datetime.today() 

clientes_datos = {
    "Carlos": {"id_cliente": 1001, "deuda": 0.0, "historial": ["Pizza", "Hamburguesa", "Lomito"], "compras_totales": 3},
    "Ana": {"id_cliente": 1002, "deuda": 1500.0, "historial": ["Ensalada", "Agua"], "compras_totales": 1},
    "Pedro": {"id_cliente": 1003, "deuda": 0.0, "historial": [], "compras_totales": 0}
}
contador_id_cliente = 1004

repartidores = {
    101: {"Nombre": "Juan", "Categoria": "ORO", "Vehiculo": "Moto", "Pedidos_exitosos": 12, "Pedidos_cancelados": 1, "Activo": True},
    105: {"Nombre": "Ana", "Categoria": "PLATA", "Vehiculo": "Bici(Eco)", "Pedidos_exitosos": 5, "Pedidos_cancelados": 0, "Activo": False}
}

#inventario de stock
stock_productos = {
    "Pizza": 5,
    "Hamburguesa": 8,
    "Lomito": 3,
    "Empanada": 12,
    "Gaseosa": 20
}

zonas_opciones = {
    "1": "Resistencia",
    "2": "Barranqueras",
    "3": "Fontana",
    "4": "Puerto Vilelas"
}

cuotas = {"1": 0.0, "2": 0.50, "3": 0.33, "4": 0.25, "5": 0.20}
forma_pago = {"1": 0, "2": 0, "3": 0}
tabla_zonas = {"Resistencia": 1000.0, "Barranqueras": 2000.0, "Fontana": 3500.0, "Puerto Vilelas": 4000.0}

def ver_pedidos():
    if not pedidos:
        print("\n[Info] No hay pedidos registrados.")
        return
        
    print("\n  Reporte de operaciones:")
    for id_p, p in pedidos.items():
        print(f"ID Pedido: {id_p} | ID Cliente: {p['id_cliente']} | Cliente: {p['cliente']} | Estado: {p['estado']}")
        print(f"Productos: {p['productos_texto']} | Repartidor: {p['repartidor']}")
        print(f"Total: ${p['total']:.2f}")
        print("-" * 30)

def actualizar_estado(id_pedido, nuevo_estado):
    pedido = pedidos[id_pedido]
    if pedido["estado"] == "Entregado" or pedido["estado"] == "Cancelado":
        print(f"\n Error: El pedido #{id_pedido} ya se encuentra '{pedido['estado']}' y NO puede ser modificado.")
        return False

    if nuevo_estado in ["1", "2", "3", "4", "5"]:
        if nuevo_estado == "1": estado_texto = "Pendiente"
        elif nuevo_estado == "2": estado_texto = "En preparacion"
        elif nuevo_estado == "3": estado_texto = "En camino"
        elif nuevo_estado == "4": estado_texto = "Entregado"
        else: estado_texto = "Cancelado"

        #Boton de arrepentimiento (idea de mercado pago)
        if estado_texto == "Cancelado" and pedido["estado"] == "En camino":
            nombre_c = pedido["cliente"]
            recargo = pedido["total"] * 0.30
            clientes_datos[nombre_c]["deuda"] += recargo
            print(f"[Aviso] Pedido cancelado durante el viaje. Se cargó el 30% (${recargo:.2f}) a la deuda de {nombre_c}.")

        pedido["estado"] = estado_texto
        print(f"Estado del pedido #{id_pedido} actualizado a: {estado_texto}")
        return True
    else:
        print(f"Error: Opción de estado no válida.")
        return False

def menu_cliente():
    global contador_id_pedido 
    global pedidos 
    global contador_id_cliente
    
    print("\n--- Menu del Delivery ---")
    print("1. Registrar nuevo pedido")
    print("2. Ver todos los pedidos")
    print("3. Cambiar estado de un pedido")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4): ").strip()

    if opcion == "1":
        print("\nRegistrando pedido....")
        cliente = input("\nNombre del cliente: ").strip().capitalize()
        
        if cliente in clientes_datos:
            id_actual = clientes_datos[cliente]["id_cliente"]
            deuda_actual = clientes_datos[cliente]["deuda"]
            if deuda_actual > 0.0:
                print(f"\n[Aviso] El cliente posee una deuda pendiente de: ${deuda_actual:.2f}")
                pagar_deuda = input("¿Desea abonar la deuda ahora mismo? (1.Si / 2.No): ").strip()
                if pagar_deuda == "1":
                    clientes_datos[cliente]["deuda"] = 0.0
                    print("¡Deuda saldada con éxito!")
                else:
                    print("Operación cancelada. No se pueden procesar pedidos con deudas activas.")
                    return
            
            historial_actual = clientes_datos[cliente]["historial"]
            if len(historial_actual) > 0:
                print(f"\n[Recomendación] Basado en tus gustos anteriores: ¡Te sugerimos una deliciosa {historial_actual[0]} hoy!")
        else:
            clientes_datos[cliente] = {"id_cliente": contador_id_cliente, "deuda": 0.0, "historial": [], "compras_totales": 0}
            id_actual = contador_id_cliente
            contador_id_cliente += 1
            print(f"¡Bienvenido! Se te ha asignado el ID único: #{id_actual}")

        subtotal = 0.0
        productos_texto = ""
        lista_productos_aux = []
        
        print("\nMenú de Stock Disponible:")
        for prod, cant in stock_productos.items():
            print(f"- {prod}: {cant} unidades disponibles")

        while True:
            nombre_prod = input("\nNombre del producto (o '0' para terminar'): ").strip().capitalize()
            if nombre_prod == '0':
                break
                
            if nombre_prod in stock_productos:
                if stock_productos[nombre_prod] <= 0:
                    print(f"[Sin Stock] Lo sentimos, no quedan unidades de {nombre_prod}. Elige otro producto.")
                    continue
            else:
                print("[Aviso] Este producto no está en la lista de stock controlado, se añadirá de igual forma.")

            try:
                precio_prod = float(input(f"Precio de '{nombre_prod}': $"))
                subtotal += precio_prod
                lista_productos_aux.append(nombre_prod)
                
                if nombre_prod in stock_productos:
                    stock_productos[nombre_prod] -= 1

                if productos_texto == "":
                    productos_texto = nombre_prod
                else:
                    productos_texto += "," + nombre_prod
            except ValueError:
                print("Error: Precio invalido.")
        
        if subtotal == 0.0:
            print("Operación cancelada: No se agregaron productos.")
            return

        print("\nZonas\n1.Resistencia\n2.Barranqueras\n3.Fontana\n4.Puerto Vilelas")
        z_op = input("seleccione zona(1-4):").strip()
        zona_elegida = zonas_opciones[z_op] if z_op in zonas_opciones else "Resistencia"
        
        clientes_datos[cliente]["compras_totales"] += 1
        es_frecuente = (clientes_datos[cliente]["compras_totales"] == 3)
        costo_envio = 0.0 if es_frecuente else tabla_zonas[zona_elegida]
        total_final = subtotal + costo_envio

        repartidor_asignado = "No asignado"
        for id_rep, datos_rep in repartidores.items():
            if datos_rep["Activo"]:
                repartidor_asignado = datos_rep["Nombre"]
                break
        
        if repartidor_asignado == "No asignado":
            print("\n[Aviso Operativo] No hay repartidores con turno activo en este momento. El pedido quedará en espera.")

        print(f"\nTOTAL A PAGAR: ${total_final:.2f} | Repartidor de Turno: {repartidor_asignado}")
        print("\nDesea seguir con el pago?\n1.Sí\n2.No")

        if input("seleccione (1-2):").strip() == "1":
            if es_frecuente:
                clientes_datos[cliente]["compras_totales"] = 0
            
            print("\n¿Como desea pagar?\n1.tarjeta de credito\n2.tarjeta de debito\n3.efectivo")
            f_pago = input("seleccione una opcion (1-3):").strip()

            if f_pago in forma_pago:
                forma_pago[f_pago] += 1
                if f_pago != "3":
                    cuo = input("ingrese la cantidad de cuotas (1-5):").strip()
                    if cuo in cuotas:
                        total_final = total_final + (total_final) * cuotas[cuo]
                
                print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")
                fecha_dia = fecha_actual.strftime("%d/%m/%y")
                pedidos[contador_id_pedido] = {
                    "id_cliente": id_actual,
                    "cliente": cliente,
                    "zona": zona_elegida,
                    "productos_texto": productos_texto,
                    "total": total_final,
                    "fecha": fecha_dia,
                    "estado": "Pendiente",
                    "repartidor": repartidor_asignado
                }
                for p_item in lista_productos_aux:
                    clientes_datos[cliente]["historial"].append(p_item)
                contador_id_pedido += 1
            else:
                print("Error!, su eleccion no esta dentro de las opciones")
        else:
            clientes_datos[cliente]["compras_totales"] -= 1
            for p_item in lista_productos_aux:
                if p_item in stock_productos:
                    stock_productos[p_item] += 1

    elif opcion == "2":
        ver_pedidos()
    elif opcion == "3":
        if not pedidos:
            print("no hay pedidos para modificar")
            return
        try:
            id_buscar = int(input("Numero de compra:"))
            if id_buscar in pedidos:
                print("\nEstados:\n1.Pendiente\n2.En preparacion\n3.En camino\n4.Entregado \n5.Cancelado")
                nuevo_est = input("seleccione nuevo estado (1-5):").strip()
                actualizar_estado(id_buscar, nuevo_est)
            else:
                print("No existe esa compra")
        except ValueError:
            print("Numero de compra Invalido")
    elif opcion == "4":
        print("Volviendo al menu de inicio.")

#Horarios de repartidores (capaz no sea necesario, esperar confirmación Zahira)
def menu_repartidor():
    print("\n--- Panel de Control de Repartidores ---")
    for id_rep, r in repartidores.items():
        estado_turno = "ACTIVO" if r["Activo"] else "PASIVO"
        print(f"ID: {id_rep} | Nombre: {r['Nombre']} | Estado: {estado_turno}")
    
    try:
        cambiar = int(input("\nIngrese el ID del repartidor para cambiar su disponibilidad (o 0 para salir): "))
        if cambiar in repartidores:
            repartidores[cambiar]["Activo"] = not repartidores[cambiar]["Activo"]
            print(f"El estado de {repartidores[cambiar]['Nombre']} fue modificado con éxito.")
    except ValueError:
        print("Entrada inválida.")

def ejecutar_inicio():
    while True:
        print("\n-----Bienvenido a Sistema Delivery-----")
        print("1. Ver menu como cliente")
        print("2. Ver menu como Repartidor")
        print("3. Cerrar sesion")
        op = input("Seleccione una opcion (1-3): ").strip()
        if op == "1":
            menu_cliente()
        elif op == "2":
            menu_repartidor()     
        elif op == "3":
            print("Finalizando ejecucion del programa.")
            break

if __name__ == "__main__":
    ejecutar_inicio()
