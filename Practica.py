from datetime import datetime
import random

pedidos = {}  
contador_id_pedido = 1
fecha_actual = datetime.today() 

#ID cliente para identificar a cada cliente, ID unico
#Deuda para saber si tiene pagos atrasados
#Historial de compras para recomendar posibles productos
clientes_datos = {
    "Carlos": {"id_cliente": 1001, "deuda": 0.0, "historial": ["Pizza", "Hamburguesa", "Lomito"], "compras_totales": 3},
    "Ana": {"id_cliente": 1002, "deuda": 1500.0, "historial": ["Ensalada", "Agua"], "compras_totales": 1},
    "Pedro": {"id_cliente": 1003, "deuda": 0.0, "historial": [], "compras_totales": 0}
}
contador_id_cliente = 1004

dias_semana={
    0:"Lunes",
    1:"Martes",
    2:"Miercoles",
    3:"Jueves",
    4:"Viernes",
    5:"Sabado",
    6:"Domingo"
}
repartidores={
    101:{"Nombre":"Juan","Edad":25,"Categoria":"ORO","Puntos":22500,"Vehiculo":"Moto","Pedidos_exitosos": 12, "Pedidos_cancelados": 1,"Ganancias_viajes": 6000.0, "Propinas": 450.0, "Resena": "Muy rápido"},
    105:{"Nombre":"Ana","Edad":30,"Categoria":"PLATA","Puntos":110,"Vehiculo":"Bici(Eco)","Pedidos_exitosos": 5, "Pedidos_cancelados":0 ,"Ganancias_viajes": 600.0, "Propinas": 40.0, "Resena": "rápido"}
}

zonas_opciones = {
    "1": "Resistencia",
    "2": "Barranqueras",
    "3": "Fontana",
    "4": "Puerto Vilelas"
}

cuotas={
    "1":0.0,
    "2":0.50,
    "3":0.33,
    "4":0.25,
    "5":0.20
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
        print(f"ID Pedido: {id_p} | ID Cliente: {p['id_cliente']} | Cliente: {p['cliente']} | Fecha: {p['fecha']} | Zona: {p['zona']}")
        print(f"Productos: {p['productos_texto']}")
        if p["regalo"] != "Ninguno":
            print(f"Premio Mundial: {p['regalo']}")
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

        pedido["estado"] = estado_texto
        print(f"Estado del pedido #{id_pedido} actualizado a: {estado_texto}")
        return True
    else:
        print(f"Error: Opción de estado no válida.")
        return False

def gamificacion(id_pedido, estado_num):
    pedido = pedidos[id_pedido]
    pass

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
        
        # Validaciones, acumulación y lógica para el sistema de Clientes integrado
        if cliente in clientes_datos:
            # #ID cliente para identificar a cada cliente, ID unico
            id_actual = clientes_datos[cliente]["id_cliente"]
            
            # #Deuda para saber si tiene pagos atrasados
            deuda_actual = clientes_datos[cliente]["deuda"]
            if deuda_actual > 0.0:
                print(f"\n[Aviso] El cliente posee una deuda pendiente de: ${deuda_actual:.2f}")
                print("Debe regularizar su cuenta para continuar.")
                pagar_deuda = input("¿Desea abonar la deuda ahora mismo? (1.Si / 2.No): ").strip()
                if pagar_deuda == "1":
                    clientes_datos[cliente]["deuda"] = 0.0
                    print("¡Deuda saldada con éxito!")
                else:
                    print("Operación cancelada. No se pueden procesar pedidos con deudas activas.")
                    return
            
            # #Historial de compras para recomendar posibles productos
            historial_actual = clientes_datos[cliente]["historial"]
            if len(historial_actual) > 0:
                print(f"\n[Recomendación] Basado en tus gustos anteriores ({', '.join(historial_actual)}):")
                print(f"¡Te sugerimos volver a pedir una deliciosa {historial_actual[0]} hoy!")
        else:
            # Registro de un nuevo cliente en la estructura
            clientes_datos[cliente] = {
                "id_cliente": contador_id_cliente,
                "deuda": 0.0,
                "historial": [],
                "compras_totales": 0
            }
            id_actual = contador_id_cliente
            contador_id_cliente += 1
            print(f"¡Bienvenido! Se te ha asignado el ID de cliente único: #{id_actual}")

        subtotal = 0.0
        productos_texto = ""
        lista_productos_aux = []
        
        while True:
            nombre_prod = input("Nombre del producto (o '0' para terminar'): ").strip()
            if nombre_prod.lower() == '0':
                break
            try:
                precio_prod = float(input(f"Precio de '{nombre_prod}': $"))
                subtotal += precio_prod
                lista_productos_aux.append(nombre_prod)
                if productos_texto == "":
                    productos_texto = nombre_prod
                else:
                    productos_texto += "," + nombre_prod

            except ValueError:
                print("Error: Precio invalido. Producto no Agregado.")
        
        if subtotal == 0.0:
            print("operacion cancelada:no se agregaron productos.")
            return

        print("\nZonas\n1.Resistencia\n2.Barranqueras\n3.Fontana\n4.Puerto Vilelas")
        z_op = input("seleccione zona(1-4):").strip()

        if z_op in zonas_opciones:
            zona_elegida = zonas_opciones[z_op]
        else:
            zona_elegida = "Resistencia"
        
        clientes_datos[cliente]["compras_totales"] += 1
        es_frecuente = (clientes_datos[cliente]["compras_totales"] == 3)
        costo_envio = 0.0 if es_frecuente else tabla_zonas[zona_elegida]

        total_final = subtotal + costo_envio

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

        premio_mundial = "Ninguno"
        if total_final > 15000:
            premio_mundial = "Llavero de Tim Payne"
        elif total_final > 10000:
            premio_mundial = "Llavero de Messi"
     
        print(f"\nN°:{contador_id_pedido}")
        print("-------------------------------------------------")  
        print(f"ID Cliente: #{id_actual} | Cliente:{cliente}")
        print(f"productos:{productos_texto}")
        print(f"subtotal:${subtotal:.2f}")
        print(f"Costo del Envío({zona_elegida}):${costo_envio:.2f}")
        if descuento_promo > 0:
            print(f"Descuento aplicado: -${descuento_promo:.2f}")
        if premio_mundial != "Ninguno":
            print(f"Se consiguio el llavero de {premio_mundial.replace('Llavero de ', '')}")
        print(f"\nTOTAL A PAGAR:${total_final:.2f}")
        print("----------------------------------------------------")
        print("\nDesea seguir con el pago?\n1.Sí\n2.No")

        if input("seleccione (1-2):").strip() == "1":
            if es_frecuente:
                clientes_datos[cliente]["compras_totales"] = 0
            
            print("\n¿Como desea pagar?\n1.tarjeta de credito\n2.tarjeta de debito\n3.efectivo")
            f_pago = input("seleccione una opcion (1-3):").strip()

            if f_pago in forma_pago:
                forma_pago[f_pago] += 1
                if f_pago != "3":
                    print("\n¿En cuantas cuotas desea pagar?")
                    cuo = input("ingrese la cantidad de cuotas (1-5):").strip()
                    if cuo in cuotas:
                        total_final = total_final + (total_final) * cuotas[cuo]
                        
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
                            "id_cliente": id_actual,
                            "cliente": cliente,
                            "zona": zona_elegida,
                            "productos_texto": productos_texto,
                            "total": total_final,
                            "fecha": fecha_dia,
                            "regalo": premio_mundial,
                            "estado": "Pendiente",
                            "repartidor": "No asignado"
                        }
                        for p_item in lista_productos_aux:
                            clientes_datos[cliente]["historial"].append(p_item)
                        contador_id_pedido += 1
                    else:
                        print("Error!,la cantidad de cuotas se excedio el tope(1-5)")
                else:
                    print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")
                    if premio_mundial != "Ninguno":
                        print(f"¡Te llevas un {premio_mundial} de regalo!")
                    print(f"Total a pagar ${total_final:.2f}")
                    
                    fecha_dia = fecha_actual.strftime("%d/%m/%y")
                    pedidos[contador_id_pedido] = {
                        "id_cliente": id_actual,
                        "cliente": cliente,
                        "zona": zona_elegida,
                        "productos_texto": productos_texto,
                        "total": total_final,
                        "fecha": fecha_dia,
                        "regalo": premio_mundial,
                        "estado": "Pendiente",
                        "repartidor": "No asignado"
                    }
                    for p_item in lista_productos_aux:
                        clientes_datos[cliente]["historial"].append(p_item)
                    contador_id_pedido += 1

            else:
                print("Error!, su eleccion no esta dentro de las opciones")

        else:
            clientes_datos[cliente]["compras_totales"] -= 1

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
                if actualizar_estado(id_buscar, nuevo_est):
                    gamificacion(id_buscar, nuevo_est)
            else:
                print("No existe esa compra")
        except ValueError:
            print("Numero de compra Invalido")
    elif opcion == "4":
        print("Volviendo al menu de inicio.")
    else:
        print("[Error] Opcion invalida. Intente de nuevo.")

def menu_repartidor():
    pass

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
        else:
            print("[Error] Opcion invalida. intente de nuevo.")

if __name__ == "__main__":
    ejecutar_inicio()
