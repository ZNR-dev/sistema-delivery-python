
from datetime import datetime
import random

pedidos = {}  
contador_id_pedido = 1
historial_clientes = {}  
fecha_actual = datetime.today() 

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
    "5":0.20,
    "6":0.166,
    "7":0.15,
    "8":0.13,
    "9":0.12,
    "10":0.105,
    "11":0.910,
    "12":0.840
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
promos_dia={
    "Jueves":"pomo",
    "Sabado":"pomo",
    "Domingo":"pomo"
}
vehiculos={
    "1":"Moto",
    "2":"Bici (Eco)",
    "3":"Auto",
    "4":"Ninguno"
}




def obtener_categoria_texto(puntos):
    if puntos > 150: return "ORO"
    if puntos >= 100: return "PLATA"
    return "BRONCE"

def calcular_tiempo_entrega(distancia_repartidor):
    return 5+int(distancia_repartidor*4)

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


def cuenta():
    print("\n¿Queres ser parte de este grupo de Deliverys?\n1. Ya soy parte\n2. Quiero unirme\n3. volver al menu anterior")

    c_op=input("seleccione una opcion (1-3):").strip()

    if c_op=="1":
        print("ingrese su Id de usuario:")
        try:
            id_repartidor=int(input().strip())
        except ValueError:

            print("Error!. el Id ingresado debe ser un numero entero")

            return   

        if id_repartidor in repartidores:
            print("----------Tu Informacion----------")
            datos=repartidores[id_repartidor]
            print(f"ID de repartidor:{id_repartidor}")
            print(f"Nombre:{datos['Nombre']}")
            print(f"Edad:{datos['Edad']}años")
            print(f"Categoria:{datos['Categoria']}")
            print(f"puntos ganados:{datos['Puntos']}pts")
            print(f"Vehiculo:{datos['Vehiculo']}")
            print(f"Pedidos Exitosos:{datos['Pedidos_exitosos']}")
            print(f"Pedidos cancelados:{datos['Pedidos_cancelados']}")
            print(f"Ganancias_viajes:{datos['Ganancias_viajes']}")
            print(f"Propinas:{datos['Propinas']}")
            print(f"Ultima Reseña:{datos['Resena']}")

        else:
            print("Error!.El Id ingresado no se encuentra en el sistema")

    elif c_op=="2":
        print("\n---------- ¡Crea tu Cuenta Ya! ----------")
        try:
            id_nuevo=int(input("Defina su numero de usuarios:").strip())
            if id_nuevo in repartidores:
                print("Error: Ese Id ya esta en uso por otro repartidor")
                return
        except ValueError:
            print("Error:El ID ya esta en uso por otro repartidor.")
            return         
        try:
            # Pedimos la edad como entero
            Edad = int(input("Ingrese la Edad (mientras sea mayor a 18 años): ").strip())
        except ValueError:
            print("Error: Debe ingresar un número válido para la edad.")
            return

        if Edad<18:
            print("Usted es un menor de edad.No admitimos el trabajo para menores de 18 años")
        else:
            print("Ingrese nombre:")
            nom_r=input().strip().capitalize()

            print("Ingrese vehiculo con el que trabajara ")
            print("1.Moto\n2.Bici(Eco)\n3.Auto\nNinguno")
            vehi=input("seleccione una opcion(1-4):").strip()

            repartidores[id_nuevo]={
                "Nombre":nom_r,
                "Edad": Edad,
                "Categoria":"BRONCE",
                "Puntos":0,
                "Vehiculo":f"{vehiculos[vehi]}",
                "Pedidos_exitosos":0,
                "Pedidos_cancelador":0,
                "Ganancias_viajes":0,
                "Propinas":0,
                "Resena":""
            }        

            print(f"\n¡Cuenta creada con exito para {nom_r}! Bienvenido a Delivery")
    elif c_op=="3":
        print("Volviendo al menu anterior.")
    else:
        print("Error!.Su eleccion no esta dentro de la opciones permitidas") 

def promos_horarios():
    config_promos={
        "Almuerzo":"+300 por viaje y +5 puntos extra",
        "Cena Peak":"+$500 por viaje y multiplicador de puntos x2",
        "Trasnocheros":"$700 por viaje (Bono nocturno por seguridad)"
    }

    hora_actual=datetime.now().hour
    minutos_actuales=datetime.now().minute

    print("*"*50)
    print("               PROMOS Y BONOS HORARIOS                    ")
    print("*"*50)

    print(f"Hora actual: {hora_actual:02d}:{minutos_actuales:02d}")
    print("-"*50)
    print("Cronograma de Incentivos Diarios:")
    print(f"-11:00 a 14:00[Almuerzo]: {config_promos['Almuerzo']}")
    print(f"-19:00 a 23:00[Cena Peak]: {config_promos['Cena Peak']}")
    print(f"-00:00 a 04:00[Trasnocheros]: {config_promos['Trasnocheros']}")

    if 11<=hora_actual<14:
        print("Estas en horario e promo![Turno Almuerzo]")
        print(f"Beneficio activo en tus viajes: {config_promos['Almuerzo']}")
    elif 20<=hora_actual<23:
        print("Zona Peak Activo![Turno Cena]")
        print(f"Beneficio activo en tus viajes:{config_promos['Cena Peak']}")
    elif 0<=hora_actual<4:
        print("¡Bono nocturno Activo![Trasnocheros]")
        print(f"Beneficio activo en tus viajes:{config_promos['Trasnocheros']}")
    else:
        print("actualmente no hay ninguna promo horaria activa.")
        print("proximo turno de bonos: Revisa en cronograma de Arriba")
    
    print("-"*50)

def lista_repartidores():
    print("\n===Repatidores Disponibles (Con distancia en tiempo Real)")

      # Simulamos distancias en variables individuales o diccionario temporal
    distancias = {
        "Carlos": round(random.uniform(0.5, 7.5), 1),
        "Ana": round(random.uniform(0.5, 7.5), 1),
        "Pedro": round(random.uniform(0.5, 7.5), 1),
        "Sofía": round(random.uniform(0.5, 7.5), 1),
        "Juan": round(random.uniform(0.5, 7.5), 1)
    }
    
    # Algoritmo manual para encontrar el menor sin usar funciones de listas
    repartidor_mas_cercano = "Carlos"
    distancia_minima = distancias["Carlos"]
    
    for k in distancias:
        if distancias[k] < distancia_minima:
            distancia_minima = distancias[k]
            repartidor_mas_cercano = k

    # Imprimimos recorriendo nuestro mapeo numérico fijo
    for id_repartidor, stats in repartidores.items():
        nombre_rep=stats["Nombre"]
        cat=obtener_categoria_texto(stats["Puntos"])

        dist=distancias[nombre_rep]

        transporte=stats["Vehiculo"]
        info_bici="[Eco-Friendly]" if "Bici" in transporte else""

        recomendado="¡Recomendado por cercania!" if nombre_rep==repartidor_mas_cercano else ""

        print(f"{id_repartidor}.{nombre_rep}({cat}), {transporte}{info_bici}->A{dist} km{recomendado}")
        print(f"puntos:{stats['Puntos']}, Historial:{stats['Pedidos_exitosos']} exitos/{stats['Pedidos_cancelados']}fallas")   
        print("-"*75)
    return distancias



def Estadisticas_Rankings():
    print("="*52)
    print("ESTADÍSTICAS GENERALES DEL SISTEMA")
    total_facturado = 0.0
    for p in pedidos.values():
        total_facturado += p["total"]
    print(f"Cantidad de pedidos totales del local: {len(pedidos)}")
    print(f"Total Facturado en Ventas (con envíos): ${total_facturado:.2f}")
    print("="*52)
    
    print("\n RANKING GENERAL DE REPARTIDORES:")
    print("-"*52)
    # Como no podemos usar listas ni ordenamientos complejos como .sort() o sorted(),
    # listamos los repartidores directamente desde nuestro diccionario ordenado visualmente.
    for id_repartidor, stats in repartidores.items():
        nombre_rep= stats["Nombre"]

        cat = obtener_categoria_texto(stats["Puntos"])

        total_neto = stats["Ganancias_viajes"] + stats["Propinas"]
        
        print(f"Nombre:{nombre_rep} \nEdad:{stats['Edad']} \nCategoria: {cat} \nPuntos: {stats['Puntos']} pts")
        print(f"Vehiculo:{stats['Vehiculo']}  \nÚltima Reseña: \"{stats['Resena']}\"")
        print("-" * 52)

def menu_repartidor()  :
    print("\n--- Menu del Delivery ---")
    print("1.Cuenta del repartidor")
    print("2.Promos de Horarios")
    print("3.Estadisticas y Rankings")
    print("4. Salir")
    op2=input("seleccione una opcion (1-4):").strip()

    if  op2=="1":
        cuenta()
    elif op2=="2":
        promos_horarios()
    elif op2=="3":
        Estadisticas_Rankings()
    elif op2=="4":
        print("Volviendo a el menu anterior")
    else:
        print("Error!. Eleccion Fuera de Rango")



def menu_cliente():
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

        print("\n¿Desea un pedido Eco-Green?\n1. Sí\n2. No")
        es_eco=(input("selecciones(1-2):").strip()=="1")

        descuento_eco=50.0 if es_eco else 0.0

        total_final=subtotal+costo_envio-descuento_eco

        # Se agrego fechas de promo y evento especial
        descuento_promo = 0.0
        numero_dia=datetime.now().weekday()

        nombre_dia=dias_semana[numero_dia]

        if nombre_dia in promos_dia:
            print("\n---------¡¡¡HOY ES DIA DE PROMOS!!!--------")
            print("\ndesea saber sobre la promo del dia dew hoy?\n1.Sí\n2.No")
            p_op=input().strip()
            if p_op=="1":
                if nombre_dia=="Jueves":
                    print("\n-------DESCUENTOS QUE ALEGRAN TU JUEVES!!------")
                    print("Jueves de promocion, con descuentos del 15%")
                    print("\n¿Desea aplicar el descuento?\n1.Sí\n2.No")
                    des=input().strip()
                    if des=="1":
                        descuento_promo=0.15*100
                        total_final= total_final-(total_final*0,15)
                        print("\nDescuento aplicado con exito!!")

                elif nombre_dia=="Sabado" or nombre_dia=="Domingo":
                    print("\n--------DESCUENTO DE LOCOS!-----------")
                    print("Sabados y domingo con descuento de hasta 50% por su compra")
                    print("\n¿Desea aplicar el descuento?\n1.Sí\n2.No")
                    des=input().strip()
                    if des=="1":
                        descuento_promo=0.5*100
                        total_final =total_final-(total_final * 0.5)
                        print("\nDescuento aplicado con exito!!")

        # Referencia al mundial, tim payne mi idolo
        premio_mundial = "Ninguno"
        if total_final > 15000:
            premio_mundial = "Llavero de Tim Payne"
        elif total_final > 10000:
            premio_mundial = "Llavero de Messi"

        print("\n                RESUMEN DE COMPRA              ")
        print(f"N°:{contador_id_pedido}")
        print("-"*50)  
        print(f"Cliente:{cliente}")
        print(f"productos:{productos_texto}")
        print(f"subtotal:${subtotal:.2f}")
        if es_eco:
            print(f"Descuento Incentivo Verde:{descuento_eco:.2f}%")

        print(f"Costo del Envío({zona_elegida}):${costo_envio:.2f}")
        if descuento_promo > 0:
            print(f"Descuento aplicado: {descuento_promo:.2f}%")
        # Muestra que premio se llevo basicamente
        if premio_mundial != "Ninguno":
            print(f"Se consiguio el llavero de {premio_mundial.replace('Llavero de ', '')}")
        
        print(f"\nTOTAL A PAGAR:${total_final:.2f}")
        print("-"*50)
        print("\nDesea seguir con el pago?\n1.Sí\n2.No")

        if input("seleccione (1-2):").strip()=="1":
            if es_frecuente:
                historial_clientes[cliente]=0

            distancia_sistema=lista_repartidores()

            ent_usu=input("Numero de id del repartidor que desee:").strip()

            if ent_usu.isdigit():
                rep_op=int(ent_usu)
            else:
                rep_op=101

            if rep_op in repartidores:
                repartidor_elegido=repartidores[rep_op]
                distancia_final=distancia_sistema[repartidor_elegido["Nombre"]]
            else:
                repartidor_elegido=repartidores[101]
                distancia_final=distancia_sistema[101]
            
            tiempo_est=calcular_tiempo_entrega(distancia_final)

            
            print("\n¿Como desea pagar?\n1.tarjeta de credito\n2.tarjeta de debito\n3.efectivo")
            f_pago=input("seleccione una opcion (1-3):").strip()

            if f_pago in forma_pago:
                forma_pago[f_pago]+=1
                if f_pago!="3":
                    print("\n¿En cuantas cuotas desea pagar?")
                    cuo=input("ingrese la cantidad de cuotas (1-12):").strip()
                    if cuo in cuotas:
                        total_final=total_final-(total_final)*cuotas[cuo] #cuotas arreglado
                        
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
                            "fecha_compra":fecha_dia,
                            "cliente": cliente,
                            "productos_texto": productos_texto,
                            "repartidor":repartidor_elegido,
                            "zona": zona_elegida,
                            "costo_envio":costo_envio,
                            "distancia_repartidor":distancia_final,
                            "regalo": premio_mundial,
                            "es_ecogreen":es_eco,
                            "estado":"Pendiente",
                            "total": total_final,
                            "tiempo_estimado":tiempo_est
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
                        "fecha_compra":fecha_dia,
                        "cliente": cliente,
                        "productos_texto": productos_texto,
                        "repartidor":repartidor_elegido,
                        "zona": zona_elegida,
                        "costo_envio":costo_envio,
                        "distancia_repartidor":distancia_final,
                        "regalo": premio_mundial,
                        "es_ecogreen":es_eco,
                        "estado":"Pendiente",
                        "total": total_final,
                        "tiempo_estimado":tiempo_est
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
        print("1. Ver menu como cliente")
        print("2.Ver menu como Repartidor")
        print("3. Cerrar sesion")
        op = input("Seleccione una opcion (1 o 2): ").strip()
        if op == "1":
            menu_cliente()
        elif op=="2":
            menu_repartidor()     
        elif op == "3":
            print("Finalizando ejecucion del programa.")
            break
        else:
            print("[Error] Opcion invalida. intente de nuevo.")

if __name__ == "__main__":     
    ejecutar_inicio()
