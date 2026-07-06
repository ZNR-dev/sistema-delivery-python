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
Estado={
    "1":"Pendiente",
    "2":"En preparacion",
    "3":"En camino",
    "4":"Entregado",
    "5":"Cancelado"
}
tarjetas={
    "1":"Mastercad",
    "2":"Visa",
    "3":"mercado pago",
    "4":"Cabal",
    "5":"Naranja",
    "6":"Banco Nacion",
    "7":"Banco del Chaco"

}
b_virtual={
    "1":"Mercado pago",
    "2":"Uola",
    "3":"Persona Pay",
    "4":"Naranja x"
}

################ "Estructuras de Clientes, Stock e ID autoincremental de clientes extraídas de Practica.py"
clientes_datos = {
    "Carlos": {"id_cliente": 1001, "deuda": 0.0, "historial": ["Pizza", "Hamburguesa", "Lomito"], "compras_totales": 3},
    "Ana": {"id_cliente": 1002, "deuda": 1500.0, "historial": ["Ensalada", "Agua"], "compras_totales": 1},
    "Pedro": {"id_cliente": 1003, "deuda": 0.0, "historial": [], "compras_totales": 0}
}
contador_id_cliente = 1004

stock_productos = {
    "Pizza": 5,
    "Hamburguesa": 8,
    "Lomito": 3,
    "Empanada": 12,
    "Gaseosa": 20
}

def obtener_categoria_texto(puntos):
    if puntos > 750: return "ORO"
    if puntos >= 500: return "PLATA"
    return "BRONCE"

def calcular_tiempo_entrega(distancia_repartidor):
    return 5+int(distancia_repartidor*4)

def actualizar_estado(id_pedido,nuevo_estado):
    pedido=pedidos[id_pedido]

    if pedido["estado"]=="Entregado" or pedido["estado"]=="Cancelado":
        print(f"\nError!. El pedido {id_pedido} ya se encuentra '{pedido['estado']}")
        return False
    
    if nuevo_estado in Estado:
        estado=Estado[nuevo_estado]
    
        ################ "Botón de arrepentimiento y recargo por cancelación en viaje integrado desde Practica.py"
        if estado == "Cancelado" and pedido["estado"] == "En camino":
            nombre_c = pedido["cliente"]
            recargo = pedido["total"] * 0.30
            clientes_datos[nombre_c]["deuda"] += recargo
            print(f"[Aviso] Pedido cancelado durante el viaje. Se cargó el 30% (${recargo:.2f}) a la deuda de {nombre_c}.")

        pedido["estado"]=estado

        print(f"estado del pedido #{id_pedido} actualizado a: {estado}")
        return True
    else:
        print("Error! opcion de estado invalida.")

def gamificacion(id_pedido,estado_num):
    pedido=pedidos[id_pedido]

    id_rep=pedido.get("id_repartidor")

    if isinstance(id_rep,dict):
        id_rep=None

    if not id_rep or id_rep not in repartidores:

        repartidor_data=pedido.get("repartidor")
        
        if isinstance(repartidor_data,dict): 
            nombre_buscar=repartidor_data.get("Nombre","").strip().lower()
        else:
            nombre_buscar=str(repartidor_data).strip().lower()
       
        for k, v in repartidores.items():
            if v.get("Nombre","").strip().lower()==nombre_buscar:
                id_rep=k
                break

    if id_rep in repartidores:
        rep=repartidores[id_rep]
    else:
        primer_id=None
        for k in repartidores:
            primer_id=k
            break

        rep=repartidores[primer_id]

   
    nombre_rep=rep.get("Nombre","Repartidor")

    cancelados_actuales = rep.get("Pedidos_cancelados", 0)
    exitosos_actuales = rep.get("Pedidos_exitosos", 0)
    puntos_actuales = rep.get("Puntos", 0)
    ganancias_actuales = rep.get("Ganancias_viajes", 0.0)
    propinas_actuales = rep.get("Propinas", 0.0)

    if estado_num=="5":
        rep["Pedidos_cancelados"]=cancelados_actuales+1
        
        print("¡Se le descontara del sueldo para pagar por el producto cancelado al Repartido!")
        
        precio_a_descontar=pedido.get('precio_prod',0.0)
        rep["Ganancias_viajes"]-= precio_a_descontar
        print("\n")
        print("-"*80)
        print(f"En el transcurso de la semana se le devolvera el pago total de ${pedido.get('precio_prod',0.0):.2f}")
        print("-"*80)
        if rep["Pedidos_cancelados"]==10:
            rep["Puntos"]=puntos_actuales-30
            print(f"\n¡Penalizacion alcanzada!{nombre_rep} acumulo 10 pedidos cancelados")
    
    elif estado_num=="4":
        rep["Pedidos_exitosos"]=exitosos_actuales+1
        puntos_actuales+=10
        print(f"\n¡Pedido entregado con Exito por {nombre_rep}!(+10 puntos)")

        if "Bici (Eco)" in rep.get("Vehiculo",""):
            puntos_actuales+=5
            print("¡Viaje Ecologico Sustentable!(+5 puntos extra Eco-Green)")
        
        rep["Puntos"]=puntos_actuales

        rep["Ganancia_viajes"]= ganancias_actuales+500.0

        print("¿Desea dejarle propina?\n1.Sí\nNo")

        if input().strip()=="1":
            try:
                monto=float(input("¿Cuántos:$"))
                rep["Propinas"]=propinas_actuales+monto
                print(f"¡Propina de ${monto:.2f} agregada!")

            except ValueError:
                print("Monto inválido")
        
        print("¿Desea dejar una reseña?\n1.Sí\n2.No")
        if input().strip()=="1":
            rep["Resena"]=input("Comentario:").strip()

        if exitosos_actuales %10==0:
            print(f"\n¡Premio Alcanzado! Bono al Buen Servicio para {nombre_rep}.")

def ver_pedidos():
    if not pedidos:
        print("\n[Info] No hay pedidos registrados.")
        return
        
    print("\n  Reporte de operaciones:")
    for id_p, p in pedidos.items():
        print("\n")
        print("-"*70)
        print(f"Tique Fctura B                                          N°:{id_p}")
        print(f"                                                        Fecha:{datetime.now().strftime('%d/%m/%y')}")
        print(f"                                                        Hora:{datetime.now().strftime('%H:%M')}")
        print("-"*70)
        print("CONSUMIDOR FINAL")
        ################ "Visualización de ID Cliente agregada en el reporte desde Practica.py"
        print(f"ID Cliente: {p.get('id_cliente','No asignado')} | Cliente:{p.get('cliente','No especificado')}")
        print(f"Zona:{p.get('zona','No especificado')}")
        print("-"*70)
        print(f"Total:${p.get('precio_prod',0.0):.2f}")
        print(f"{p.get('productos_texto','')}")
        print("-"*70)
        print("DETALLES DE ENTREGA/PAGO")
        print(f"Tarjeta:{p.get('tarjeta','No especificado')} ")
        print(f"Cantidad de cuotas:{p.get('cant_cuo',0)}")
        if p.get("regalo")!="Ninguno":
            print(f"Premio mundial:{p['regalo']}")
        if p.get("tip_transf")!="":
             print(f"{p.get('tip_transf','No esppecificado')}                                             Total:{p.get('total',0.0)}")
        else:
            print(f"{p.get('tipo_tarj','No esppecificado')}                                               Total:{p.get('total',0.0)}")
        id_rep=pedidos[id_p].get('id_repartidor')
        print(f"Repartidor:{repartidores[id_rep].get('Nombre')}")
        print(f"Estado: {p.get('estado')}")

def lista_repartidores():
    print("\n=== Repartidores Disponibles (Con distancia en tiempo Real) ===")

    distancias = {}
    
    for id_rep, stats in repartidores.items():
        nombre_rep = stats["Nombre"]
        distancias[nombre_rep] = round(random.uniform(0.5, 7.5), 1)
    
    repartidor_mas_cercano = None
    distancia_minima = 99.0
    for k in distancias:
        if distancias[k] < distancia_minima:
            distancia_minima = distancias[k]
            repartidor_mas_cercano = k

    for id_repartidor, stats in repartidores.items():
        nombre_rep = stats["Nombre"]
        puntos_rep = stats.get("Puntos", 0) 
        exitosos_rep=stats.get('pedidos_exitosos',0)
        cancelados_rep=stats.get('pedidos_cancelados',0)

        cat = obtener_categoria_texto(puntos_rep)
        
        dist = distancias[nombre_rep] 
        transporte = stats.get("Vehiculo","No especificado")
        info_bici = "[Eco-Friendly]" if "Bici" in transporte else ""
        recomendado = "¡RECOMENDADO POR CERCANÍA!" if nombre_rep == repartidor_mas_cercano else ""
        
        print(f"{id_repartidor}. {nombre_rep}({cat}), {transporte}{info_bici}->A {dist} km {recomendado}")
        print(f"   puntos:{puntos_rep}, Historial:{exitosos_rep} éxitos/{cancelados_rep} fallas")
        print("-" * 75)
        
    return distancias

def cuenta_repartidor():
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
            Edad = int(input("Ingrese la Edad (mientras sea mayor a 18 años): ").strip())
        except ValueError:
            print("Error: Debe ingresar un número válido para la edad.")
            return

        if Edad<18:
            print("Usted es un menor de edad.No admitimos el trabajo para menores de 18 años")
        else:
            print("Ingrese nombre:")
            nom_r=input().strip()

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
                "Pedidos_cancelados":0,
                "Ganancias_viajes":0,
                "Propinas":0,
                "Resena":""
            }        

            print(f"\n¡Cuenta creada con exito para {nom_r}! Bienvenido a Delivery")
            print("----------Tu Informacion----------")
            print(f"ID de repartidor:{id_nuevo}")
            print(f"Nombre:{nom_r}")
            print(f"Edad:{Edad}años")
            print(f"Categoria:{repartidores[id_nuevo].get('Categoria','BRONCE')}")
            print(f"puntos ganados:{repartidores[id_nuevo].get('Puntos',0.0)}pts")
            print(f"Vehiculo:{vehiculos[vehi]}")
            print(f"Pedidos Exitosos:{repartidores[id_nuevo].get('Pedidos_exitosos',0.0)}")
            print(f"Pedidos cancelados:{repartidores[id_nuevo].get('Pedidos_cancelados',0.0)}")
            print(f"Ganancias_viajes:{repartidores[id_nuevo].get('Ganancias_viajes')}")
            print(f"Propinas:{repartidores[id_nuevo].get('Propinas')}")
            print(f"Ultima Reseña:{repartidores[id_nuevo].get('Resena')}")
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
    print("           PROMOS Y BONOS HORARIOS ")
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

def Estadisticas_Rankings():
    print("="*52)
    print("ESTADÍSTICAS GENERALES DEL SISTEMA")
    total_facturado = 0.0
    for p in pedidos.values():
        total_facturado += p.get("total",0.0)
    print(f"Cantidad de pedidos totales del local: {len(pedidos)}")
    print(f"Total Facturado en Ventas (con envíos): ${total_facturado:.2f}")
    print("="*52)
    print("\n   RANKING GENERAL DE REPARTIDORES:")
    print("-"*52)
    for id_repartidor, stats in repartidores.items():
        nombre_rep= stats["Nombre"]
        puntos_rep=stats.get("puntos",stats.get("Puntos",0))
        edad_rep=stats.get("edad",stats.get("Edad","No especificado"))
        transporte_rep=stats.get("vehiculos",stats.get("Vehiculo","No especificado"))
        resena_rep=stats.get("resena",stats.get("Resena","Sin resena"))
        ganancias=stats.get("ganancias_viajes",stats.get("Ganancias_viajes",0.0))
        propinas= stats.get("propinas",stats.get("Propinas",0.0))
        total_neto = ganancias+propinas
        cat = obtener_categoria_texto(puntos_rep)
        print(f"Nombre:{nombre_rep} \nEdad:{edad_rep} \nCategoria: {cat} \nPuntos: {puntos_rep} pts")
        print(f"Vehiculo:{transporte_rep} \nReseña destacada: {resena_rep}")
        print(f"Ganancias Netas (Viajes + Propinas): ${total_neto:.2f}")
        print("-"*52)

def registrar_pedido():
    global contador_id_pedido
    global contador_id_cliente
    global pedidos

    print("\nRegistrando pedido....")
    cliente = input("\nNombre del cliente: ").strip().capitalize()

    ################ "Gestión e identificación de deudas, historial y asignación de ID único traída de Practica.py"
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

    ################ "Muestra del stock controlado según el inventario disponible de Practica.py"
    print("\nMenú de Stock Disponible:")
    for prod, cant in stock_productos.items():
        print(f"- {prod}: {cant} unidades disponibles")

    while True:
        nombre_prod = input("\nNombre del producto (o '0' para terminar'): ").strip().capitalize()
        if nombre_prod == '0':
            break

        ################ "Validación y detención por falta de stock según el inventario de Practica.py"
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
            
            ################ "Descuento del producto del inventario de stock de Practica.py"
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

    print("\nCalculando distancias de repartidores...")
    mapa_distancias = lista_repartidores()

    repartidor_asignado_nombre = "No asignado"
    repartidor_asignado_id = None
    distancia_minima = 99.0

    ################ "Asignación exclusiva de repartidores Activos integrada desde Practica.py"
    for id_rep, datos_rep in repartidores.items():
        if datos_rep.get("Activo", True):
            nombre_rep = datos_rep["Nombre"]
            dist_rep = mapa_distancias.get(nombre_rep, 5.0)
            if dist_rep < distancia_minima:
                distancia_minima = dist_rep
                repartidor_asignado_nombre = nombre_rep
                repartidor_asignado_id = id_rep

    if repartidor_asignado_id is None:
        print("\n[Aviso Operativo] No hay repartidores con turno activo en este momento. El pedido quedará en espera.")
        for primer_k in repartidores:
            repartidor_asignado_id = primer_k
            repartidor_asignado_nombre = repartidores[primer_k]["Nombre"]
            break

    tiempo_est = calcular_tiempo_entrega(distancia_minima)

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
    
    print(f"\nTOTAL A PAGAR:${total_final:.2f} | Tiempo de espera estimado: {tiempo_est} min")
    print("----------------------------------------------------")
    print("\nDesea seguir con el pago?\n1.Sí\n2.No")

    if input("seleccione (1-2):").strip() == "1":
        if es_frecuente:
            clientes_datos[cliente]["compras_totales"] = 0
        
        print("\n¿Como desea pagar?\n1.tarjeta de credito\n2.tarjeta de debito\n3.efectivo\n4.Billetera Virtual\n5.Transferencia Bancaria")
        f_pago = input("seleccione una opcion (1-5):").strip()

        t_usada = ""
        c_cuo = 0
        tipo_t = ""
        t_trans = ""

        if f_pago == "1":
            print("Seleccione tarjeta:")
            for k,v in tarjetas.items(): print(f"{k}.{v}")
            t_usada = tarjetas.get(input().strip(), "No especificada")
            
            cuo = input("ingrese la cantidad de cuotas (1-12):").strip()
            if cuo in cuotas:
                c_cuo = int(cuo)
                total_final = total_final + (total_final) * cuotas[cuo]
                if total_final > 15000: premio_mundial = "Llavero de Tim Payne"
                elif total_final > 10000: premio_mundial = "Llavero de Messi"
            tipo_t = "tarjeta de credito"

        elif f_pago == "2":
            print("Seleccione tarjeta de Debito:")
            for k,v in tarjetas.items(): print(f"{k}.{v}")
            t_usada = tarjetas.get(input().strip(), "No especificada")
            tipo_t = "tarjeta de debito"

        elif f_pago == "3":
            tipo_t = "efectivo"

        elif f_pago == "4":
            print("Seleccione Billetera Virtual:")
            for k,v in b_virtual.items(): print(f"{k}.{v}")
            t_usada = b_virtual.get(input().strip(), "No especificada")
            tipo_t = "Billetera Virtual"

        elif f_pago == "5":
            print("Seleccione a que banco transferir:")
            print("1.Banco nacion\n2.Banco del Chaco")
            op_b = input().strip()
            t_trans = "Banco Nacion" if op_b == "1" else "Banco del Chaco"
            tipo_t = "Transferencia Bancaria"

        if f_pago in ["1","2","3","4","5"]:
            print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")
            if premio_mundial != "Ninguno":
                print(f"¡Te llevas un {premio_mundial} de regalo!")
            
            fecha_dia = fecha_actual.strftime("%d/%m/%y")
            pedidos[contador_id_pedido] = {
                "id_cliente": id_actual,
                "cliente": cliente,
                "zona": zona_elegida,
                "productos_texto": productos_texto,
                "precio_prod": subtotal,
                "total": total_final,
                "fecha": fecha_dia,
                "regalo": premio_mundial,
                "estado": "Pendiente",
                "id_repartidor": repartidor_asignado_id,
                "repartidor": repartidor_asignado_nombre,
                "tarjeta": t_usada,
                "cant_cuo": c_cuo,
                "tipo_tarj": tipo_t,
                "tip_transf": t_trans
            }
            for p_item in lista_productos_aux:
                clientes_datos[cliente]["historial"].append(p_item)
            contador_id_pedido += 1
        else:
            print("Error!, su eleccion no esta dentro de las opciones")
    else:
        clientes_datos[cliente]["compras_totales"] -= 1
        ################ "Devolución automática al inventario de stock si la operación se cancela de Practica.py"
        for p_item in lista_productos_aux:
            if p_item in stock_productos:
                stock_productos[p_item] += 1

def cambio_estado():
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

def menu_cliente():
    while True:
        print("\n--- Menu del Delivery ---")
        print("1. Registrar nuevo pedido")
        print("2. Historial de pedidos")
        print("3. Cambiar estado de un pedido")
        print("4. Salir")

        opcion = input("Seleccione una opcion (1-4): ").strip()

        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            cambio_estado()
        elif opcion == "4":
            print("Volviendo al menu de inicio.")
            break
        else:
            print("[Error] Opcion invalida. Intente de nuevo.")

################ "Menú y panel de control de disponibilidad real para Repartidores traído de Practica.py"
def menu_repartidor():
    while True:
        print("\n--- Panel de Control de Repartidores ---")
        print("1. Ver Repartidores en Turno y cambiar disponibilidad")
        print("2. Ver promos y bonos horarios")
        print("3. Ver Estadisticas y Rankings del local")
        print("4. Administrar cuenta/Crear cuenta repartidor")
        print("5. Volviendo al menu de inicio")
        
        op_rep = input("Seleccione una opción: ").strip()
        if op_rep == "1":
            for id_rep, r in repartidores.items():
                estado_turno = "ACTIVO" if r.get("Activo", True) else "PASIVO"
                print(f"ID: {id_rep} | Nombre: {r['Nombre']} | Estado: {estado_turno}")
            try:
                cambiar = int(input("\nIngrese el ID del repartidor para cambiar su disponibilidad (o 0 para salir): "))
                if cambiar in repartidores:
                    repartidores[cambiar]["Activo"] = not repartidores[cambiar].get("Activo", True)
                    print(f"El estado de {repartidores[cambiar]['Nombre']} fue modificado con éxito.")
            except ValueError:
                print("Entrada inválida.")
        elif op_rep == "2":
            promos_horarios()
        elif op_rep == "3":
            Estadisticas_Rankings()
        elif op_rep == "4":
            cuenta_repartidor()
        elif op_rep == "5":
            break
        else:
            print("Opción inválida.")

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
