from datetime import date

pedidos = {}  
contador_id_pedido = 1
historial_clientes = {}  
fecha_actual = date.today() 

zonas_opciones = {
    "1": "Resistencia",
    "2": "Barranqueras",
    "3": "Fontana",
    "4": "Puerto Vilelas"
}

cuotas={
    "1":0.0,
    "2":0.050,
    "3":0.076,
    "4":0.10,
    "5":0.124,
    "6":0.155,
    "7":0.1821,
    "8":0.207,
    "9":0.226,
    "10":0.258,
    "11":0.280,
    "12":0.300
}

forma_pago={
    "1":0,
    "2":0,
    "3":0
}

tabla_zonas = {
    "Resistencia": 1000.0,
    "Barranqueras": 2000.0,
    "Fontana":3500.0,
    "Puerto Vilelas":4000.0
}

def ver_pedidos():
    if not pedidos:
        print("\n[Info] No hay pedidos registrados.")
        return
        
    print("\n  Reporte de operaciones:")
    for id_p, p in pedidos.items():
        print(f"ID: {id_p} | Cliente: {p['cliente']} | Fecha: {p['fecha']} | Zona: {p['zona']}")
        print(f"Productos: {p['productos_texto']}")
        if p["regalo"] != "Ninguno":
            print(f"Premio Mundial: {p['regalo']}")
        print(f"Total: ${p['total']:.2f}")
        print("-" * 30)

def menu_sistema():
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
            nombre_prod = input("Nombre del producto (o '0' para terminar'): ").strip()
            if nombre_prod.lower() == '0':
                break
            try:
                precio_prod = float(input(f"Precio de '{nombre_prod}': $"))
                subtotal+=precio_prod
                if productos_texto == "":
                    productos_texto=nombre_prod
                else:
                    productos_texto+=","+nombre_prod

            except ValueError:
                print("Error: Precio invalido. Producto no Agregado.")
        
        if subtotal==0.0:
            print("operacion cancelada:no se agregaron productos.")
            return

        print("\nZonas\n1.Resistencia\n2.Barranqueras\n3.Fontana\n4.Puerto Vilelas")
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

        # Se agrego fechas de promo y evento especial
        descuento_promo = 0.0
        print("\n¿Que dia de la semana es hoy?")
        print("1. Lunes\n2. Martes\n3. Miercoles\n4. Jueves\n5. Viernes\n6. Sabado\n7. Domingo")
        dia_opc = input("Seleccione una opcion (1-7): ").strip()
        if dia_opc == "4":
            descuento_promo = total_final * 0.15
            total_final -= descuento_promo
        elif dia_opc == "6" or dia_opc == "7":
            print("dia 6, mañana 7, six seven")
            descuento_promo = total_final * 0.067
            total_final -= descuento_promo

        # Referencia al mundial, tim payne mi idolo
        premio_mundial = "Ninguno"
        if total_final > 15000:
            premio_mundial = "Llavero de Tim Payne"
        elif total_final > 10000:
            premio_mundial = "Llavero de Messi"
     
        print(f"\nN°:{contador_id_pedido}")
        print("-------------------------------------------------")  
        print(f"Cliente:{cliente}")
        print(f"productos:{productos_texto}")
        print(f"subtotal:${subtotal:.2f}")
        print(f"Costo del Envío({zona_elegida}):${costo_envio:.2f}")
        if descuento_promo > 0:
            print(f"Descuento aplicado: -${descuento_promo:.2f}")
        # Muestra que premio se llevo basicamente
        if premio_mundial != "Ninguno":
            print(f"Se consiguio el llavero de {premio_mundial.replace('Llavero de ', '')}")
        print(f"\nTOTAL A PAGAR:${total_final:.2f}")
        print("----------------------------------------------------")
        print("\nDesea seguir con el pago?\n1.Sí\n2.No")

        if input("seleccione (1-2):").strip()=="1":
            if es_frecuente:
                historial_clientes[cliente]=0
            
            print("\n¿Como desea pagar?\n1.tarjeta de credito\n2.tarjeta de debito\n3.efectivo")
            f_pago=input("seleccione una opcion (1-3):").strip()

            if f_pago in forma_pago:
                forma_pago[f_pago]+=1
                if f_pago!="3":
                    print("\n¿En cuantas cuotas desea pagar?")
                    cuo=input("ingrese la cantidad de cuotas (1-12):").strip()
                    if cuo in cuotas:
                        total_final=total_final+(total_final)*cuotas[cuo]
                        
                        premio_mundial = "Ninguno"
                        if total_final > 15000:
                            premio_mundial = "Llavero de Tim Payne"
                        elif total_final > 10000:
                            premio_mundial = "Llavero de Messi"

                        print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")
                        if premio_mundial != "Ninguno":
                            print(f"¡Te llevas un {premio_mundial} de regalo!")
                        print(f"Total a pagar ${total_final:.2f} en {cuo} cuotas")
                        
                        fecha_dia = fecha_actual.strftime("%d/%m/%y")
                        pedidos[contador_id_pedido] = {
                            "cliente": cliente,
                            "zona": zona_elegida,
                            "productos_texto": productos_texto,
                            "total": total_final,
                            "fecha": fecha_dia,
                            "regalo": premio_mundial,
                            "repartidor": "No asignado"
                        }
                        contador_id_pedido+=1
                    else:
                        print("Error!,la cantidad de cuotas se excedio el tope(1-12)")
                else:
                    print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")
                    if premio_mundial != "Ninguno":
                        print(f"¡Te llevas un {premio_mundial} de regalo!")
                    print(f"Total a pagar ${total_final:.2f}")
                    
                    fecha_dia = fecha_actual.strftime("%d/%m/%y")
                    pedidos[contador_id_pedido] = {
                        "cliente": cliente,
                        "zona": zona_elegida,
                        "productos_texto": productos_texto,
                        "total": total_final,
                        "fecha": fecha_dia,
                        "regalo": premio_mundial,
                        "repartidor": "No asignado"
                    }
                    contador_id_pedido+=1

            else:
                print("Error!, su eleccion no esta dentro de las opciones")

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
            print("[Error] Opcion invalida. intente de nuevo.")

if __name__ == "__main__":     
    ejecutar_inicio()
