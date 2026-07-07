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
    105:{"Nombre":"Ana","Edad":30,"Categoria":"PLATA","Puntos":550,"Vehiculo":"Bici(Eco)","Pedidos_exitosos": 5, "Pedidos_cancelados":0 ,"Ganancias_viajes": 600.0, "Propinas": 45.0, "Resena": "Rápido"},
    105:{"Nombre":"Maria","Edad":45,"Categoria":"BRONCE","Puntos":100,"Vehiculo":"Bici(Eco)","Pedidos_exitosos": 4, "Pedidos_cancelados":1 ,"Ganancias_viajes": 456.0, "Propinas": 40.0, "Resena": "Amable"},
    
}
clientes={
    2500:{"Nombre":"Maria","Edad":"27","Documento":"27899234","Cant_compras":0,"Puntos_cl":0,"Rango":"PLATA"},
    4044:{"Nombre":"Juan","Edad":"34","Documento":"36489560","Cant_compras":0,"Puntos_cl":0,"Rango":"BRONCE"},
    3504:{"Nombre":"Malena","Edad":"25","Documento":"41473800","Cant_compras":0,"Puntos_cl":0,"Rango":"BRONCE"},
    2004:{"Nombre":"Juan","Edad":"30","Documento":"37003509","Cant_compras":0,"Puntos_cl":0,"Rango":"PLATA"},
    5566:{"Nombre":"Juan","Edad":"22","Documento":"42748509","Cant_compras":0,"Puntos_cl":0,"Rango":"ORO"},
    1010:{"Nombre":"Juan","Edad":"60","Documento":"23747305","Cant_compras":0,"Puntos_cl":0,"Rango":"ORO"},
    2020:{"Nombre":"Juan","Edad":"51","Documento":"25543788","Cant_compras":0,"Puntos_cl":0,"Rango":"PLATA"},
    
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


def obtener_categoria_texto(puntos):
    if puntos > 750: return "ORO"
    if puntos >= 500: return "PLATA"
    return "BRONCE"

def obtener_rango(puntos_cli):
    if puntos_cli>=500: return "ORO"
    elif puntos_cli>=200:return "PLATA"
    return"BRONCE"

def calcular_tiempo_entrega(distancia_repartidor):
    return 5+int(distancia_repartidor*4)

def actualizar_estado(id_pedido,nuevo_estado):
    pedido=pedidos[id_pedido]

    if pedido["estado"]=="Entregado" or pedido["estado"]=="Cancelado":
        print(f"\nError!. El pedido {id_pedido} ya se encuentra '{pedido['estado']}")
        return False
    
    if nuevo_estado in Estado:
        estado=Estado[nuevo_estado]
    
        pedido["estado"]=estado

        print(f"estado del pedido #{id_pedido} actualizado a: {estado}")
        return True
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("         Error! opcion de estado invalida.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def gamificacion(id_pedido,estado_num):
    pedido=pedidos[id_pedido]

    id_cliente=pedido.get("id_cli")
    cliente_encontrado=id_cliente in clientes if id_cliente else False

    if cliente_encontrado:
        cli=clientes[id_cliente]
        compras_cliente=cli.get("Cant_compras",0)
        puntos_cliente=cli.get("Puntos_cl",0)
        nombre_cli=cli.get("Nombre","Clientes")

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
        print("-"*50)
        print(f"En el transcurso de la semana se le devolvera el pago total de ${pedido.get('precio_prod',0.0):.2f}")
        print("-"*50)
        if rep["Pedidos_cancelados"]==10:
            rep["Puntos"]=puntos_actuales-30
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"¡Penalizacion alcanzada!{nombre_rep} acumulo 10 pedidos cancelados")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if cliente_encontrado:
            if puntos_cliente>=15:
                cli["Puntos_cl"]=puntos_cliente-15
            else:
                cli["Puntos_cl"]=0
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"¡Disculpe pero por su cancelacion a Delivery, se le descontara 15 puntos de buen cliente!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    elif estado_num=="4":
        rep["Pedidos_exitosos"]=exitosos_actuales+1
        puntos_actuales+=10
        print(f"\n¡Pedido entregado con Exito por {nombre_rep}!(+10 puntos)")

        if "Bici (Eco)" in rep.get("Vehiculo",""):
            puntos_actuales+=5
            print("¡Viaje Ecologico Sustentable!(+5 puntos extra Eco-Green)")
        
        rep["Puntos"]=puntos_actuales

        rep["Ganancias_viajes"]= ganancias_actuales+500.0

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

        if cliente_encontrado:
            cli["Cant_compras"]=compras_cliente+1

            total_factura=pedido.get('precio_prod',0.0)
            puntos_ganados_cli=int(total_factura/100)

            cli["Puntos_cli"]=puntos_cliente+puntos_ganados_cli
            print(f"\n¡Felicitaciones haz ganado mas puntos que suman a tu reputacion de buen Cliente!")
            print("")

        cli["Rango"]=obtener_rango(cli["Puntos_cl"])
        
def ver_pedidos():
    print("Ingrese su id de cliente para ver su historial")
    try:
        cl_buscar=int(input().strip())
    except ValueError:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("             Error:El Id debe ser un numero entero.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return
    
    if cl_buscar in clientes:  
        datos_cliente=clientes[cl_buscar]


        print("\n  Reporte de operaciones:")
        print("---------------------Informacion de Cliente----------------------")
        print(f"Id de cliente:{cl_buscar}")
        print(f"Nombre de cliente:{datos_cliente['Nombre']}")
        print(f"N° doc:{datos_cliente['Documento']}")
        print(f"Puntos de reputacion:{datos_cliente['Puntos_cl']}pts")
        print(f"Rango:{datos_cliente['Rango']}")

        tiene_pedidos=False


        for id_p, p in pedidos.items():
            if p.get('cliente')==datos_cliente['Nombre']:
                tiene_pedidos=True

                print("\n")
                print("-"*70)
                print(f"Tique Fctura B                                          N°:{id_p}")
                print(f"                                                        Fecha:{datetime.now().strftime('%d/%m/%y')}")
                print(f"                                                        Hora:{datetime.now().strftime('%H:%M')}")
                print("-"*70)
                print("CONSUMIDOR FINAL")
                print(f"Cliente:{p.get('cliente','No especificado')}")
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
                    print(f"{p.get('tip_transf','No esppecificado')}                                    Total:{p.get('total',0.0)}")
                else:
                    print(f"{p.get('tipo_tarj','No esppecificado')}                                      Total:{p.get('total',0.0)}")
                id_rep=pedidos[id_p].get('id_repartidor')
                print(f"Repartidor:{repartidores[id_rep].get('Nombre')}")
                print(f"Estado: {p.get('estado')}")

        if not tiene_pedidos:
            print("\n Registraste cuenta en el sistema, pero aun no realizaste ninguna compra/pedido")   
    else:
        print("\n¡¡¡No se encontro el cliente en el sistema de Delivery!!!")
        return
    
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
    print("\n¿Queres ser parte de este grupo de Deliverys?")
    print("             1. Ya soy parte")
    print("             2. Quiero unirme")
    print("             3. volver al menu anterior")

    c_op=input("\nseleccione una opcion (1-3):").strip()

    if c_op=="1":
        print("ingrese su Id de usuario:")
        try:
            id_repartidor=int(input().strip())
        except ValueError:

            print("Error!. el Id ingresado debe ser un numero entero")

            return   

        if id_repartidor in repartidores:
            datos=repartidores[id_repartidor]
            print("\n")
            print(f"              ¡HOLA {datos['Nombre']}!")
            print("--------------Tu Informacion-------------")
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
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Error!.El Id ingresado no se encuentra en el sistema")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    elif c_op=="2":

        print("\n---------- ¡Crea tu Cuenta Ya! ----------")
        try:
            id_nuevo=int(input("Defina su numero de usuarios(de hasta 3 digitos):").strip())
            if id_nuevo>1000:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("¡¡¡Error. El id definido esta rfeservado para clientes")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                return

            if id_nuevo in repartidores:
                print("Error: Ese Id ya esta en uso por otro repartidor")
                return
        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("         Error:El Id no debe contener letras.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return         
        try:
            Edad = int(input("Ingrese la Edad (mientras sea mayor a 18 años): ").strip())
        except ValueError:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Error: Debe ingresar un número válido para la edad.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return

        if Edad<18:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("¡Usted es un menor de edad, Nuestra politica NO ADMITE el trabajo para menores de 18 años!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("Ingrese nombre:")
            nom_r=input().strip()

            print("\nIngrese vehiculo con el que trabajara ")
            print("             1.Moto")
            print("             2.Bici(Eco)")
            print("             3.Auto")
            print("             4.Ninguno")
            vehi=input("\nseleccione una opcion(1-4):").strip()

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

            print(f"\n¡Cuenta creada con exito para {nom_r}!")
            print("\n")
            print("_______________¡Bienvenido a Delivery!_____________")
            print("         ----------Tu Informacion----------")
            print(f"ID de repartidor:{id_nuevo}")
            print(f"Nombre:{nom_r}")
            print(f"Edad:{Edad}años")
            print(f"Categoria:{repartidores[id_nuevo].get("Categoria","BRONCE")}")
            print(f"puntos ganados:{repartidores[id_nuevo].get("Puntos",0.0)}pts")
            print(f"Vehiculo:{vehiculos[vehi]}")
            print(f"Pedidos Exitosos:{repartidores[id_nuevo].get("Pedidos_exitosos",0.0)}")
            print(f"Pedidos cancelados:{repartidores[id_nuevo].get("Pedidos_cancelados",0.0)}")
            print(f"Ganancias_viajes:{repartidores[id_nuevo].get("Ganancias_viajes")}")
            print(f"Propinas:{repartidores[id_nuevo].get("Propinas")}")
            print(f"Ultima Reseña:{repartidores[id_nuevo].get("Resena")}")


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

def Estadisticas_Rankings():
    print("\n")
    print("="*52)
    print("             ESTADÍSTICAS GENERALES DEL SISTEMA          ")

    total_facturado = 0.0
    for p in pedidos.values():
        total_facturado += p.get("total",0.0)

    print(f"Cantidad de pedidos totales del local: {len(pedidos)}")
    print(f"Total Facturado en Ventas (con envíos): ${total_facturado:.2f}")
    print("="*52)
    
    print("\n               RANKING GENERAL DE REPARTIDORES             ")
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
        print(f"Vehiculo:{transporte_rep}  \nÚltima Reseña: \"{resena_rep}\"")
        print("-" * 52)


def menu_repartidor()  :
    while True:
        print("\n")
        print("-"*50)
        print("---------------- Menu de Delivery ----------------")
        print("                  1.Cuenta Personal")
        print("                  2.Promos de Horarios")
        print("                  3.Estadisticas y Rankings")
        print("                  4. Salir")
        print("-"*50)
        op2=input("\nseleccione una opcion (1-4):").strip()

        if  op2=="1":
            cuenta_repartidor()
        elif op2=="2":
            promos_horarios()
        elif op2=="3":
            Estadisticas_Rankings()
        elif op2=="4":
            print("Volviendo a el menu anterior....")
            break
        else:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Error!. Eleccion Fuera de Rango")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    


def registrar_pedido():
    global contador_id_pedido
    print("\n¿Eres cliente de Delivery?")
    print("     1.Soy Cliente")
    print("     2.No soy cliente")
    print("     3.Volver al menu anterior")
    cl_o=input("\nseleccione una opcion(1-3):").strip()
    if cl_o=="1":
        try:
            print("\nIngrese id de cliente")
            id_cl=int(input().strip())
        except ValueError:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Error: el Id debe ser un entero")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return

    elif cl_o=="2":
        print("\n----------------Vamos a crear tu cuenta--------------")
        try:
            id_cln=int(input("Defina su numero de usuarios:").strip())
            if id_cln in clientes or id_cln<1000:
                print("¡¡¡Error: Ese Id ya esta en uso por otro cliente o es id de repartidor!!!!")
                return
                
        except ValueError:
            print("\n!!!!!!!!!!!!!!!!!!!!")
            print("Numero de id invalido")
            print("!!!!!!!!!!!!!!!!!!!!!")
            return         
        try:
            # Pedimos la edad como entero
            Ed_cl = int(input("Ingrese la Edad (mientras sea mayor a 18 años): ").strip())
        except ValueError:
            print("\n¡Error: Debe ingresar un número válido para la edad.!")
            return
        
        if Ed_cl<18:
            print("\n¡Usted es menor de edad por lo tanto no podemos dejarle ser cliente¡")
            return
        cliente = input("Ingrese su nombre del cliente: ").strip().capitalize()

        if cliente.replace(" ", "").isalpha() and cliente != "":
            doc=int(input("Ingrese numero de documenmto del cliente: "))

            if doc>3125407:
                
                clientes[id_cln]={
                    "Nombre":cliente,
                    "Edad":Ed_cl,
                    "Documento":doc,
                    "Cant_compras":0,
                    "Puntos_cl":0,
                    "Rango": "BRONCE"
                }
                print(f"\n¡Cuenta creada con exito! Tu id de cliente es:{id_cln}")
            else:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Error!!. Numero de documento no valido")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
        else:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("\nError!! El nombre no puede contener números ni caracteres especiales.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
        print("\nVolviendo al menu Delivery...")
        return

       
    else:
        print("\nVolviendo al menu Delivery..")
        return
        
    
    if id_cl in clientes:    
        subtotal=0.0
        productos_texto=""
        descontados_dic = {}
        cliente=clientes[id_cl]["Nombre"]

        print(f"                \nBienvenido de vuelta {cliente}")
        print("            ¿Que deseas encargar hoy al Equipo Delivery?")
            
        while True:
            nombre_prod = input("               Nombre del producto (o '0' para terminar'): ").strip()
            if nombre_prod.lower() == '0':
                break
            try:
                precio_prod = float(input(f"                Precio de '{nombre_prod}': $"))
                subtotal+=precio_prod
                if productos_texto == "":
                    productos_texto=nombre_prod
                else:
                    productos_texto+=","+nombre_prod
                

            except ValueError:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Error!!Precio invalido. Producto no Agregado.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
        print("\nRegistrando pedido....")
            
        if subtotal==0.0:
            print("\n OPERACION CANCELADA:no se agregaron productos.")

        print("\n¿Cuál es tu Zona?")
        print("         1.Resistencia")
        print("         2.Barranqueras")
        print("         3.Fontana")
        print("         4.Puerto Vilelas")
        z_op=input("\nseleccione zona(1-4):").strip()

        if z_op in zonas_opciones:
            zona_elegida=zonas_opciones[z_op]
        else:
            zona_elegida="Resistencia"
        
        
            
        if cliente not in historial_clientes:
            historial_clientes[cliente]=0
        historial_clientes[cliente]+=1

        es_frecuente=(historial_clientes[cliente]==3)
        costo_envio=0.0 if es_frecuente else tabla_zonas[zona_elegida]

        print("\n           ¿Desea un pedido Eco-Green?")
        print("                   1.Sí, Me encantaria")
        print("                   2.No Por el momento")
        es_eco=(input("\nselecciones(1-2):").strip()=="1")

        descuento_eco=0.10 if es_eco else 0.0

        total_final=subtotal+costo_envio-(subtotal*descuento_eco)

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
                        descuento_promo=0.15
                        total_final= total_final-(subtotal*descuento_promo)
                        print("\nDescuento aplicado con exito!!")

                elif nombre_dia=="Sabado" or nombre_dia=="Domingo":
                    print("\n--------DESCUENTO DE LOCOS!-----------")
                    print("Sabados y domingo con descuento de hasta 50% por su compra")
                    print("\n¿Desea aplicar el descuento?\n1.Sí\n2.No")
                    des=input().strip()
                    if des=="1":
                        descuento_promo=0.5
                        total_final =total_final-(subtotal*descuento_promo)
                        print("\nDescuento aplicado con exito!!")

        premio_mundial = "Ninguno"
        if total_final > 15000:
            premio_mundial = "Llavero de Tim Payne"
        elif total_final > 10000:
            premio_mundial = "Llavero de Messi"
            
        print("\n                                               ")
        print("                RESUMEN DE COMPRA              ")
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
                id_repartidor_elegido=rep_op
                nombre_rep=repartidores[rep_op]["Nombre"]
                distancia_final=distancia_sistema[nombre_rep]
            else:
                id_repartidor_elegido=repartidores[101]
                nombre_rep=repartidores[101]["Nombre"]
                distancia_final=distancia_sistema[nombre_rep]

                
            print("\n               ¿Como desea pagar?")
            print("                 1.tarjeta de credito")
            print("                 2.tarjeta de debito")
            print("                 3.Transferencia/efectivo")
            f_pago=input("seleccione una opcion (1-3):").strip()

            if f_pago in forma_pago:
                forma_pago[f_pago]+=1
                if f_pago!="3":
                    print("\nIngrese nombre de su tarjeta")
                    print("         1.master card")
                    print("         2.visa")
                    print("         3.mercado pago")
                    print("         4.cabal")
                    print("         5.naranja")
                    print("         6.bna")
                    print("         7.bch")
                    marca_tarj=input().strip()

                    if marca_tarj in tarjetas:
                        print("\n           ¿En cuantas cuotas desea pagar?")
                        cuo=input("    ingrese la cantidad de cuotas (1-12):").strip()
                        if cuo in cuotas:
                            total_final=total_final-(total_final)*cuotas[cuo]
        
                            premio_mundial = "Ninguno"
                            if total_final > 15000:
                                premio_mundial = "Llavero de Tim Payne"
                            elif total_final > 10000:
                                premio_mundial = "Llavero de Messi"

                            print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")
                            if premio_mundial != "Ninguno":
                                print(f"¡Te llevas un {premio_mundial} de regalo!")
                            print(f"Total a pagar ${total_final:.2f} en {cuo} cuotas")
                            tiempo_est=calcular_tiempo_entrega(distancia_final)
                            print(f"tiempo estimado en llegar su pedido {tiempo_est}minutos")
                                
                            if f_pago=="1":
                                form_p="Credito"
                            else:
                                form_p="Debito"
                                
                            fecha_dia = fecha_actual.strftime("%d/%m/%y")
                            pedidos[contador_id_pedido] = {
                                "fecha_compra":fecha_dia,
                                "cliente": cliente,
                                "id_cli":clientes[id_cl],
                                "productos_texto": productos_texto,
                                "precio_prod":subtotal,
                                "tip_transf":"",
                                "tarjeta":tarjetas[marca_tarj],
                                "tipo_tarj":form_p,
                                "cant_cuo":cuo,
                                "id_repartidor":id_repartidor_elegido,
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
                            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("Error!,la cantidad de cuotas se excedio el tope(1-12)")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    else:
                        print("¡¡¡Error!.La tarjeta ingresada no esta asociada al sistema de modo de pago!!!")
                        
                else:
                    print("         usted desea pagar en:")
                    print("            1.Transferencia")
                    print("            2.Efectivo")
                    tipo_p=int(input())

                    premio_mundial = "Ninguno"
                    if total_final > 15000:
                        premio_mundial = "Llavero de Tim Payne"
                    elif total_final > 10000:
                        premio_mundial = "Llavero de Messi"

                    if tipo_p==1:
                        print("         ¿Que billetera virtual desea usar?")
                        print("             1.Meracdo Pago")
                        print("             2.Uala")
                        print("             3.Personal Pay")
                        print("             4.Naranja X")
                        billetera=input().strip()
                
                        if billetera in b_virtual:
                            
                            print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")

                            if premio_mundial != "Ninguno":
                                print(f"¡Te llevas un {premio_mundial} de regalo!")

                            print(f"Total a pagar ${total_final:.2f}")
                            tiempo_est=calcular_tiempo_entrega(distancia_final) 
                            print(f"tiempo estimado en llegar su pedido {tiempo_est}minutos")

                            fecha_dia = fecha_actual.strftime("%d/%m/%y")
                            pedidos[contador_id_pedido] = {
                                "fecha_compra":fecha_dia,
                                "cliente": cliente,
                                "id_cli":clientes[id_cl],
                                "productos_texto": productos_texto,
                                "precio_prod":subtotal,
                                "tip_transf":b_virtual[billetera],
                                "tarjeta":"",
                                "tipo_tarj":"",
                                "cant_cuo":"",
                                "id_repartidor":id_repartidor_elegido,
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
                            print("     ¡¡¡Error!.billetera virtual no aceptada!!!")
                    else:
                        print(f"\n¡PEDIDO #{contador_id_pedido} REGISTRADO!")
                        if premio_mundial != "Ninguno":
                            print(f"        ¡Te llevas un {premio_mundial} de regalo!")

                        print(f"            Total a pagar ${total_final:.2f}")
                        tiempo_est=calcular_tiempo_entrega(distancia_final) 
                        print(f"            tiempo estimado en llegar su pedido {tiempo_est}minutos")
                            
                        fecha_dia = fecha_actual.strftime("%d/%m/%y")
                        pedidos[contador_id_pedido] = {
                            "fecha_compra":fecha_dia,
                            "cliente": cliente,
                            "id_cli":clientes[id_cl],
                            "productos_texto": productos_texto,
                            "precio_prod":subtotal,
                            "tip_transf":"efectivo",
                            "tarjeta":"",
                            "tipo_tarj":"",
                            "cant_cuo":"",
                            "id_repartidor":id_repartidor_elegido,
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
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("     ¡¡¡Error, su eleccion no esta dentro de las opciones!!!")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("             Compra No realizada!!")
        
          
    else:
        print("        ¡¡¡Error!. El cliente no es parte de Delivery!!!")
        return

def cambio_estado():
    if not pedidos:
        print("     ¡No hay pedidos para modificar!")
        return
    try:
        id_buscar=int(input("Numero de compra:"))

        if id_buscar in pedidos:
            print("\n")
            print("-"*70)
            print(f"Tique Fctura B                                           N°:{id_buscar}")
            print(f"                                                         Fecha:{datetime.now().strftime("%d/%m/%y")}")
            print(f"                                                         Hora:{datetime.now().strftime("%H:%M")}")
            print("-"*70)
            print("CONSUMIDOR FINAL")
            print("Domi:")
            print("Barr:")
            print("-"*70)
            print(f"Total:${pedidos[id_buscar].get('precio_prod',0.0):.2f}")
            print("RECIBI/MOS")
            print(f"Tarjeta:{pedidos[id_buscar].get('tarjeta','No especificado')} ")
            print(f"Cantidad de cuotas:{pedidos[id_buscar].get('cant_cuo',0)}")
            if pedidos[id_buscar].get("regalo")!="Ninguno":
                print(f"Premio mundial:{pedidos[id_buscar].get('regalo','Ninguno')}")

            if pedidos[id_buscar].get("tip_transf")!="":
                print(f"{pedidos[id_buscar].get('tip_transf','No esppecificado')}                                               Total:{pedidos[id_buscar].get('total',0.0)}")
            else:
                print(f"{pedidos[id_buscar].get('tipo_tarj','No esppecificado')}                                                Total:{pedidos[id_buscar].get('total',0.0)}")
            id_rep=pedidos[id_buscar].get('id_repartidor')
            print(f"Repartidor:{repartidores[id_rep].get('Nombre')}")
            print(f"Estado: {pedidos[id_buscar].get('estado')}")

            print("REGIMEN DE TRANSFERENCIA FISCAL AL CONSUMIDOR")

            print("\nEstados:\n1.Pendiente\n2.En preparacion\n3.En camino\n4.Entregado \n5.Cancelado")
            nuevo_est=input("seleccione nuevo estado (1-5):").strip()

            if actualizar_estado(id_buscar,nuevo_est):
                    
                gamificacion(id_buscar,nuevo_est)

        else:

            print("         ¡¡¡No existe esa compra!!!")
                
    except ValueError:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Error!!!Numero de compra Invalido")   
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def menu_cliente():
    while True:
        global contador_id_pedido 
        global pedidos 
        
        print("\n---------------- Menu de Delivery -----------------")
        print("             1. Registrar nuevo pedido")
        print("             2. Historial de pedidos")
        print("             3. Cambiar estado de un pedido")
        print("             4. Salir")
        print("-"*50)

        opcion = input("\nSeleccione una opcion (1-4): ").strip()

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

def ejecutar_inicio():
    while True:
        print("\n")
        print("-"*50)
        print("♦♦♦♦♦♦♦♦♦♦Bienvenido a Sistema Delivery♦♦♦♦♦♦♦♦♦♦")
        print("             1. Menu de cliente")
        print("             2. Menu de Repartidor")
        print("             3. Cerrar sesion")
        print("-"*50)
        op = input("\nSeleccione una opcion (1 o 2): ").strip()
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
