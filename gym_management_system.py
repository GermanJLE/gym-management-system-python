from datetime import timedelta, datetime
from random import randint


def menuPrincipal():
    print("[1] Registro de socio")
    print("[2] Registrar instructor")
    print("[3] Registrar clase ")
    print("[4] Registrar asistencia en sala maquinas")
    print("[5] Calcular la renovación ")
    print("[6] Ver reportes ")
    print("[7] Menu secundario ")
    print("[8] Menus extras ")
    print("[9] Salir ")
    opcion = ingresoOp("Colocar el numero de su preferencia : ", 1, 9)
    return opcion


def menuSecundario():
    print("[1] Separar casillero")
    print("[2] Calificar instructor")
    print("[3] Lista de calificaciones intructores")
    print("[4] Reporte de maquinas dañadas")
    print("[5] Comprar suplementos")
    print("[6] ES TU CUMPLEAÑOS? CLICAR ACÁ")
    print("[7] Retroceder")
    opcionSecun = ingresoOp("Colocar el numero de su preferencia : ", 1, 7)
    return opcionSecun


def menuExtras():
    print("[1] Tirar dado")
    print("[2] Ver mis ofertas")
    print("[3] Salir")
    opcionExtras = ingresoOp("Colocar el numero de su preferencia : ", 1, 3)
    return opcionExtras


def ingresoOp(boton, inferior, superior):
    while True:
        try:
            numero = int(input(boton))
            if inferior <= numero <= superior:
                return numero
        except ValueError:
            print("Ingrese numeros validos del menu")


def regisDni(largo, mensaje):
    while True:
        verifiDni = input(mensaje)
        if verifiDni.isdigit() and len(verifiDni) == largo:
            return verifiDni
        else:
            print("El dni es invalido")


def validarNom(mensaje):
    while True:
        valiNombre = input(mensaje)
        if valiNombre.strip() != "" and not any(map(str.isdigit, valiNombre)):
            return valiNombre
        else:
            print("porfavor ingresar algo valido sin numeros")


def fechaNaci(mensaje):
    while True:
        try:
            veriNacimiento = input(mensaje)
            if veriNacimiento.isdigit() and len(veriNacimiento) == 8:
                anio = int(veriNacimiento[:4])
                mes = int(veriNacimiento[4:6])
                dia = int(veriNacimiento[6:])
                if 1936 <= anio <= 2026:
                    if 1 <= mes <= 12:
                        if 1 <= dia <= 30:
                            fechita = [anio, mes, dia]
                            return fechita
        except ValueError:
            print("Ingresar cosas validas")


def tipoMembre(mensaje):
    while True:
        try:
            print("[1] Mensual")
            print("[2] Trimestral")
            print("[3] Anual")
            valiMembresi = int(input(mensaje))
            if valiMembresi == 1:
                return "MENSUAL"
            elif valiMembresi == 2:
                return "TRIMESTRAL"
            elif valiMembresi == 3:
                return "ANUAL"
            else:
                print("Ingresar algo valido ")
        except ValueError:
            print("Ingresar cosas validas")


def regisSocio():
    nomSocio = validarNom("Ingresar tu nombre porfavor : ")
    apeSocio = validarNom("Ingersar tu apellido porfavor : ")
    dniSocio = regisDni(8, "Ingersar tu dni : ")
    nacimiento = fechaNaci("Ingresar fecha de nacimiento en AAAAMMDD :")
    membresia = tipoMembre("Elige tu tipo de membresia porfavor :")
    fechaInicio = fechaNaci(
        "Ingresar tu fecha de inicio de membresia (hoy) en AAAAMMDD : "
    )
    print("Socio registrado con exito")
    print("")
    PlantillaSocio = [
        nomSocio,
        apeSocio,
        dniSocio,
        nacimiento,
        membresia,
        fechaInicio
        ]
    return PlantillaSocio


def regisEspecial(mensaje):
    while True:
        try:
            print("[1] Spinning")
            print("[2] Yoga")
            print("[3] Funcional")
            print("[4] Otros")
            especialidad = int(input(mensaje))
            if especialidad == 1:
                return "Spinning"
            elif especialidad == 2:
                return "Yoga"
            elif especialidad == 3:
                return "Funcional"
            elif especialidad == 4:
                otros = validarNom(
                    "Ingresar su especialidad en una palabra porfavor :"
                    )
                return otros
            else:
                print("Ingresar cosas validas")
        except ValueError:
            print("Ingresar cosas validas")


def regisInstructor():
    nomInstructor = validarNom("Ingresar tu nombre porfavor : ")
    dniInstructor = regisDni(8, "Ingresar tu dni : ")
    especialidad = regisEspecial("Selecionar o Ingresar tu especialidad : ")
    print("Instructor registrado con exito")
    print("")
    planillaInstru = [
        nomInstructor,
        dniInstructor,
        especialidad
        ]
    return planillaInstru


def instructoListM():
    instructorlist = []
    instructorr = {
        "In01": {
            "Nombre": "Alvaro",
            "Horario": "0700 - 0900",
            "Capacidad": 20,
            "Especialidad": "Spinning",
        },
        "In02": {
            "Nombre": "Gonzalo",
            "Horario": "1500- 1700",
            "Capacidad": 30,
            "Especialidad": "Yoga",
        },
        "In03": {
            "Nombre": "Antonio",
            "Horario": "1700 - 2000",
            "Capacidad": 25,
            "Especialidad": "Funcional",
        },
    }
    for valores, datos in instructorr.items():
        instructorlist.append((valores, datos))

    return instructorlist


def impriInstru(instructorlist, ingresoHora):
    disponibles = []
    contador = 1
    tit = ("Nro.instructor", "Nombre", "Horario", "Capacidad", "Especialidad")
    print("-" * 85)
    print(f"| {tit[0]:^15}|{tit[1]:^15}|{tit[2]:^15}|" f" {tit[3]:^15}|{tit[4]:^20}|")
    print("-" * 85)

    for clase, valor in instructorlist:
        horario = valor["Horario"]
        inicio = int(horario[:4])
        if inicio > ingresoHora:
            disponibles.append((clase, valor))
            print(
                f"|{contador:^5}{clase:^15}|{valor['Nombre']:^15}|{valor['Horario']}|"
                f"{valor['Capacidad']:^15}|{valor['Especialidad']:^20}|"
            )
            contador += 1

    print("-" * 85)
    if len(disponibles) == 0:
        print("No hay ningun horario ahorita")
        return None
    elegir = ingresoOp("Estos son los horarios disponibles", 1, len(disponibles))
    return disponibles[elegir - 1]


def valiCapacidad(disponibles):
    codigo, valor = disponibles

    if valor["Capacidad"] == 0:
        print("La clase ya esta llena")
        return False

    valor["Capacidad"] = valor["Capacidad"] - 1
    print("Cupo reservado")
    return True


def validarHora(mensaje):
    while True:
        horarios = input(mensaje)
        if horarios.isdigit() and len(horarios) == 4:
            hora = int(horarios[:2])
            minutos = int(horarios[2:])
            if 0 <= hora <= 23 and 0 <= minutos <= 59:
                return int(horarios)

        print("Ingresar hora valida en formato HHMM")


def salaMaquinas(plantillaSocio, asistenciaList, totalmaquinas):
    dNi = regisDni(8, "Ingresar tu DNI : ")
    if dNi == plantillaSocio[2]:
        if totalmaquinas > 0:
            totalmaquinas -= 1
            feCha = fechaNaci("Ingresar la fecha del dia de hoy : ")
            asistencia = [
                plantillaSocio[2],
                plantillaSocio[0],
                plantillaSocio[1],
                feCha,
            ]
            asistenciaList.append(asistencia)
            print("listo")
        else:
            print("Se acabaron las 50 maquinas")
    else:
        print("No eres socio")

    return asistenciaList, totalmaquinas


def regisClaseAsis(instructorlist,
                   plantillaSocio,
                   asistenciaList,
                   totalmaquinas):
    ingresoClase = validarNom("Ingresar solo tu nombre para tu clase : ")
    if ingresoClase != plantillaSocio[0]:
        print("Ese nombre no pertenece al socio registrado")
        return

    ingresoHora = validarHora("Ingresar la hora formato HHMM formato 24h : ")
    disponibleMos = impriInstru(instructorlist, ingresoHora)
    if disponibleMos is not None:
        puede = valiCapacidad(disponibleMos)
        if not puede:
            return

    maquinaslibres = salaMaquinas(plantillaSocio, asistenciaList, totalmaquinas)
    print("Clase registrada con exito")
    print("")
    planillaAsis = [
        ingresoClase,
        ingresoHora,
        disponibleMos,
        maquinaslibres
    ]
    return planillaAsis


def cstRenovacion(planillaSocio):
    MENSUAL = 100
    TRIMESTRAL = 250
    ANUAL = 1000
    tuInicio = planillaSocio[5]
    anio = tuInicio[0]
    mes = tuInicio[1]
    dia = tuInicio[2]
    realFecha = datetime(anio, mes, dia)
    if planillaSocio[4] == "MENSUAL":
        finalFecha = realFecha + timedelta(days=30)
        costo = MENSUAL
    elif planillaSocio[4] == "TRIMESTRAL":
        finalFecha = realFecha + timedelta(days=90)
        costo = TRIMESTRAL
    elif planillaSocio[4] == "ANUAL":
        finalFecha = realFecha + timedelta(days=365)
        costo = ANUAL

    hoy = datetime.now()
    falta = finalFecha - hoy
    if falta.days <= 5:
        print("TU MEMBRESIA YA VA VENCER")

    print("Tu fecha de vencimiento es: ", finalFecha)
    print("Tu costo de renovación sera de  : ", costo)
    return finalFecha, costo, hoy


def memDescuentos(mensaje, plantillaSocio, hoy, finalFecha):
    descuentos = 0
    respuesta = input(mensaje)
    if respuesta == "SI":
        dNI = regisDni(8, "Ingresar tu dni : ")
        if dNI == plantillaSocio[2]:
            if hoy < finalFecha:
                descuentos = 0.15
        else:
            print("No eres socio")

        return descuentos


def CalPagosReno(
                 plantillaSocio,
                 hoy,
                 finalFecha):
    costosrenova = cstRenovacion(plantillaSocio)
    descuentomem = memDescuentos(
        "Va querer renobar su membresia? SI/NO", plantillaSocio, hoy, finalFecha
    )
    planillaPay = [
        costosrenova,
        descuentomem]
    return planillaPay


def mayorOcupa(ocupaciones):
    if ocupaciones == {}:
        print("No hay datos registrados")
        return

    mayor = 0
    claseTop = ""

    for clase, cantidad in ocupaciones.items():
        if cantidad > mayor:
            mayor = cantidad
            claseTop = clase

    print("La clase con mayor ocupacion es: ", claseTop)
    print("Cantidad de personas: ", mayor)
    return claseTop, mayor


def mayorAsis():
    asistencias = {
        "Lunes": 15,
        "Martes": 22,
        "Miercoles": 30,
        "Jueves": 18,
        "Viernes": 27,
    }

    if not asistencias:
        print("No hay asistencias registradas")
        return

    mayor = 0
    mejorDia = ""

    for dia, cantidad in asistencias.items():
        if cantidad > mayor:
            mayor = cantidad
            mejorDia = dia

    print("El dia con mayor asistencia es:", mejorDia)
    print("Cantidad de asistentes:", mayor)
    return mejorDia, mayor


def mayorInstClass(asistenciaList):
    if asistenciaList == []:
        print("No hay asistencias registradas")
        return

    contaDor = {}

    for datos in asistenciaList:
        dni = datos[0]
        if dni not in contaDor:
            contaDor[dni] = 1
        else:
            contaDor[dni] += 1

    mayor = 0
    dniTop = ""

    for dni, cantidad in contaDor.items():
        if cantidad > mayor:
            mayor = cantidad
            dniTop = dni

    for datos in asistenciaList:
        if datos[0] == dniTop:
            nombre = datos[1]
            apellido = datos[2]

    print("Socio con mayor asistencia mensual:")
    print(nombre, apellido, "-", mayor, "asistencias")


def ingresosMem(ingresos):
    if ingresos == []:
        print("No hay ingresos")
        return

    total = sum(ingresos)
    print("Ingresos totales", total)


def instrucMas(masMesInst):
    if masMesInst == []:
        print("No hay clases registradas")
        return

    Alvaro = 0
    Gonzalo = 0
    Antonio = 0
    for clase in masMesInst:
        instructor = clase[2][1]["Nombre"]
        if instructor == "Alvaro":
            Alvaro += 1
        elif instructor == "Gonzalo":
            Gonzalo += 1
        elif instructor == "Antonio":
            Antonio += 1

    if Alvaro > Gonzalo and Alvaro > Antonio:
        print("Instructor con mas clases dictadas:")
        print("Alvaro -", Alvaro, "clases")
    elif Gonzalo > Alvaro and Gonzalo > Antonio:
        print("Instructor con mas clases dictadas:")
        print("Gonzalo -", Gonzalo, "clases")
    else:
        print("Instructor con mas clases dictadas:")
        print("Antonio -", Antonio, "clases")


def reportesAdd(ingresos, masMesInst):
    ocupacion = mayorOcupa()
    asistenicaMay = mayorAsis()
    InstruTop = mayorInstClass
    memIngresos = ingresosMem(ingresos)
    masClases = instrucMas(masMesInst)

    planillaReport = [
        ocupacion,
        asistenicaMay,
        InstruTop,
        memIngresos,
        masClases
    ]
    return planillaReport


def sepCasillero(mensaje, totcasilleros, planillaSocio):
    libres = 0
    if planillaSocio == []:
        print("No hay socio registrado")
        return

    print(mensaje)
    while True:
        Dni = regisDni(8, "Ingresar dni para separ casillero : ")
        if Dni != planillaSocio[2]:
            print("DNI incorrecto. Intente nuevamente : ")
        else:
            print("DNI correcto")
            break

    print("Casilleros disponibles:")
    for i, casillero  in enumerate(totcasilleros):
        if casillero  == 0:
            print("Casillero", i + 1)
            libres += 1

    if libres == 0:
        print("no hay casilleros")
        return

    numero = ingresoOp("Elegir casillero: ", 1, len(totcasilleros))
    if totcasilleros[numero - 1] == 0:
        totcasilleros[numero - 1] = 1
        print("Casillero", numero, "separado correctamente")
    else:
        print("Ese casillero ya está ocupado")


def caliInstruc(calificaciones):
    nombre = validarNom("Ingresar el nombre del instructor: ")
    nota = ingresoOp("Cual seria su calificación del 1 al 5?", 1, 5)
    calificaciones.append((nombre, nota))
    print("Gracias por realizar la encuesta")


def rptCaliInst(mensaje, calificaciones):
    print(mensaje)
    if len(calificaciones) == 0:
        print("No hay nada en calificaciones todavia")
        return
    print(" Estos son los intructores son su nota:")
    for nombre, nota in calificaciones:
        print(f"{nombre} - {nota}")


def reportmaq(reptmaquinas, planillaSocio):
    if planillaSocio == []:
        print("Registrar a una persona como minimo primero")
        return

    dni = regisDni(8, "Ingresar dni")
    if dni == planillaSocio[2]:
        numeros = ingresoOp("Numero de la maquina no funcionaldel (1,50) : ", 1, 50)
        reptmaquinas.append(numeros)
        print("Tu reporte yasta")
    else:
        print("invalido")


def verRepoMaquina(reptmaquinas):
    print("Ver las maquinas dañadas : ")
    if reptmaquinas == []:
        print("Debe ingresar un dato valido")
        return

    for i, maquina in enumerate(reptmaquinas, 1):
        print(f"{i} esta mala la {maquina}")


def comSuplem(mensaje):
    Proteina = 120
    Agua = 3
    Quinua = 10
    Preentreno = 50
    Galleta = 2
    print(mensaje)
    suplementis()
    while True:
        print("[1] Proteina - 120$")
        print("[2] Agua - 3$")
        print("[3] Quinua - 10$")
        print("[4] Pre entreno - 50$")
        print("[5] galleta - 2$")
        op = ingresoOp("Cual el es de su gusto", 1, 5)
        try:
            cantidad = int(input("Cuantos vas a querer comprar : "))
            if op == 1:
                print(f"Eso va costar {Proteina*cantidad}")
                break
            elif op == 2:
                print(f"Eso va costar {Agua*cantidad}")
                break
            elif op == 3:
                print(f"Eso va costar {Quinua*cantidad}")
                break
            elif op == 4:
                print(f"Eso va costar {Preentreno*cantidad}")
                break
            elif op == 5:
                print(f"Eso va costar {Galleta*cantidad}")
                break
        except ValueError:
            print("Ingresar algo valido")


def cumpleSocio(mensaje, planillasocio):
    print(mensaje)
    if planillasocio != []:
        hoy = fechaNaci("Ingresar la fecha en AAAAMMDD (hoy) : ")
        nacimiento = planillasocio[3]
        if nacimiento[1] == hoy[1]:
            if nacimiento[2] == hoy[2]:
                felizcumple()
                torta()
    else:
        print("no hay nada registrado todavia")


def suplementis():
    print("""
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢤⡖⠺⠉⠓⠢⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢞⣿⣿⣭⣟⣯⣾⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⢸⣅⠉⠀⢻⣦⠀⡀⠘⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣟⣿⡿⣿⣿⣿⢟⣿⣿⠟⢿⡀⠀⠀⠀⠀⠀⠀⠀⢟⣿⣾⣿⣿⣿⣇⠀⢡⠘⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣶⣿⣻⡿⠁⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠉⠉⠁⢻⠈⡆⢳⡈⢳⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣽⣿⡏⠀⠐⠾⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠟⢰⡥⠀⢝⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣷⡘⠃⠀⠀⠀⠀⠙⢁⣱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⢣⠞⣀⢇⠈⠱⠚⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢿⣻⣿⣿⣿⡅⠀⠀⠀⢦⣬⡇⠀⠀⠀⠀⠀⠀⠀⢠⠚⡏⠉⠑⢺⡄⠀⠀⠙⣧⡀⠇⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣷⠈⠉⠙⠛⠿⢿⣷⣦⣄⢰⣾⠖⣊⣉⡩⠍⢉⠓⠶⣿⢁⠜⢇⠁⢀⣹⣷⣤⣤⣈⣇⠀⣸⢧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⢛⡇⠉⠀⠀⡀⢀⡀⠀⠀⠉⢙⡏⠁⠀⢹⣇⡀⠙⣏⠢⡌⡉⠉⣒⡷⠚⠉⠉⢻⣿⣿⣿⣵⣾⣷⣾
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠚⠁⢀⣼⠋⣿⡅⠀⠀⠀⠀⠈⠉⠓⣦⡨⠀⡀⠀⠀⢈⣉⡒⠒⣶⡶⠂⠉⠀⠠⣤⣴⣶⣾⣿⣿⠿⠛⠉⠁
⠀⠀⠀⠀⠀⠀⠀⣴⠋⠉⠙⠋⠉⢸⣥⡤⠜⠋⢤⣦⢤⣤⣴⡾⠟⠁⠀⠙⢒⣫⣥⣴⣶⣿⣏⠀⠉⠛⠿⢿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡤⠚⠙⣷⣿⣦⡀⠀⢨⡏⠀⠀⠀⠀⠀⠀⠀⣩⠀⠀⠀⠉⠉⠉⢉⡛⢻⣿⣿⣿⣷⣶⣶⣶⣶⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⠏⢀⠀⠀⣖⠈⠁⠉⠙⢻⣷⣄⣀⣤⣤⡴⠿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡏⢰⡟⠀⠀⣿⡄⠀⠀⠀⣿⠀⠀⠀⠀⠀⢀⣴⠟⠁⢿⣄⣀⡀⠀⣀⣤⣶⣿⣿⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⠀⢸⡁⠀⠀⠸⣿⣄⠀⡀⣿⠀⠀⡠⣶⡷⠋⡀⠀⠀⠚⠛⠛⠛⠛⠛⠛⠃⠈⠑⡿⢸⣯⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠇⠀⠘⣿⣦⣤⣤⣿⡟⠛⠓⢿⣞⠻⠟⣔⠲⡇⣀⡀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⢠⣾⣺⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠀⠀⠀⣿⣿⠉⠛⠿⢦⣄⡠⠘⡆⣀⣤⠀⠀⠀⢐⣮⠗⠃⠋⠛⠛⠛⠛⠛⢻⣿⡿⡍⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠭⠌⣧⢾⣧⣤⣾⣦⠥⢠⣀⣀⢄⣠⣦⣶⣾⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⣀⣴⣿⣿⣿⣿⣦⡂⠀⠀⠀⣾⣙⡇⠀⠀⠀⠀⠀⠀⠁⠀⣡⣿⣿⣿⣿⣯⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡿⢋⣡⣾⣿⣿⣟⣻⠿⣿⠷⣤⣿⣿⣇⠀⠀⠀⠀⠀⠠⣀⣿⣿⣿⠛⠛⠻⠏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡟⣻⣿⣿⣿⣿⣿⣼⡏⠀⠈⠑⢤⣹⡿⣿⣯⠻⢿⣿⣿⣿⣽⠿⢟⣃⣀⣀⡨⣏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣾⠁⠀⠈⢹⣿⣿⠟⠀⠀⠀⠀⠀⠈⠛⢾⣿⡆⣶⣿⣿⠗⠒⢉⣉⣉⣙⣛⢿⣧⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣿⠀⠀⢷⡀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣿⣿⣷⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠿⣄⠀⣸⣿⣄⣻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣉⣉⣉⣉⣉⣿⣏⣉⣉⣉⣉⣉⣉⣙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢷⣌⠧⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⣟⣏⣿⣷⡇⢸⣿⣿⣿⣿⣿⠆⣿⠀⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """)


def felizcumple():
    print("""
          ღ♪*•.¸¸.•*¨¨*•.¸.•*¨¨*•.¸¸.•*•♪ღ♪
ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░♪ღ
•♪ღ♪*•.¸¸.•*¨¨*••*¨¨*•.¸¸.•*•♪ღ♪
          """)


def torta():
    print("""
          ──()──()──()── ()──()───
            ──▄──▄──▄──▄──▄───
            ──▓──▓──▓──▓──▓───
            ─░░░░░░░░░░░░░░░░─
            ██████████████████
          ║░✧ Ŧ乇ĿΙZ ĊUMPĿ乇✧ ░║
            ██████████████████
          """)


def regisSecund(
    totcasilleros,
    planillaSocio,
    calificaciones,
    reptmaquinas,
):
    casilleros = sepCasillero(
        "Bienvenido para seprar casillero", totcasilleros, planillaSocio
    )
    calificarIns = caliInstruc(calificaciones)
    reporteIns = rptCaliInst("Este es el reporte de los instructores : ",
                             calificaciones)
    maquinasmal = reportmaq(reptmaquinas,
                            planillaSocio)
    suplementos = comSuplem("Bienvenido para la compra de suplementos")
    cumpleaSocio = cumpleSocio("Ingresa tu DNI :", planillaSocio, felizcumple, torta)

    planillamenS = [
        casilleros,
        calificarIns,
        reporteIns,
        maquinasmal,
        suplementos,
        cumpleaSocio,
    ]
    return planillamenS


def dado1():
    print("""
    ┏━━━━━━━━━━━━━━━┓
    ┃               ┃
    ┃               ┃
    ┃       ●       ┃
    ┃               ┃
    ┃               ┃
    ┗━━━━━━━━━━━━━━━┛
    """)


def dado2():
    print("""
    ┏━━━━━━━━━━━━━━━┓
    ┃ ●             ┃
    ┃               ┃
    ┃               ┃
    ┃               ┃
    ┃             ● ┃
    ┗━━━━━━━━━━━━━━━┛      
    """)


def dado3():
    print("""
    ┏━━━━━━━━━━━━━━━┓
    ┃ ●             ┃
    ┃               ┃
    ┃       ●       ┃
    ┃               ┃
    ┃             ● ┃
    ┗━━━━━━━━━━━━━━━┛      
    """)


def dado4():
    print("""
    ┏━━━━━━━━━━━━━━━┓
    ┃ ●           ● ┃
    ┃               ┃
    ┃               ┃
    ┃               ┃
    ┃ ●           ● ┃
    ┗━━━━━━━━━━━━━━━┛      
    """)


def dado5():
    print("""
    ┏━━━━━━━━━━━━━━━┓
    ┃ ●           ● ┃
    ┃               ┃
    ┃       ●       ┃
    ┃               ┃
    ┃ ●           ● ┃
    ┗━━━━━━━━━━━━━━━┛     
    """)


def dado6():
    print("""
    ┏━━━━━━━━━━━━━━━┓
    ┃ ●           ● ┃
    ┃ ●           ● ┃
    ┃               ┃
    ┃ ●           ● ┃
    ┃ ●           ● ┃
    ┗━━━━━━━━━━━━━━━┛     
    """)


def trebol():
    print("""
        ⣀⠤⠄⠀⠠⠐⠒⠈⠑⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠊⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⡇⠀⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⣰⡔⠉⠀⠀⠀⠈⠑⡄⠀⠀
⠀⠀⠀⣀⣀⣀⠈⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀
⢀⠞⠁⠀⠀⠀⠈⠑⠬⡓⢄⠀⠀⠀⠘⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠷⣄⠀⣄⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀
⠘⡆⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡷⠳⢖⡂⠀⠀⠀⠀⠐⠂⠉⠀⠀⠀⢣⠀
⠀⡇⠀⠀⠀⠉⠁⠀⠀⠉⠉⠀⡰⠁⠀⠠⠈⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠆
⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⢡⠀⠀⠙⢦⢄⠀⠀⠀⠀⣀⠜⠀
⠀⠀⠓⢄⡀⠀⠀⠀⡠⢰⢿⠁⠀⠀⠀⠀⠀⡆⠀⠀⠀⠳⡈⠉⠀⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠉⡩⠋⡔⢡⠃⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠎⠀⠌⠀⡇⠀⠀⠀⠀⠀⠀⢀⠁⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠃⢀⠌⠀⠀⠹⡄⠀⠀⠀⠀⠀⡌⣀⣀⡀⠤⠊⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠧⢄⡘⠀⠀⠀⠀⠈⠑⠂⠐⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           
          """)


def minijuego(planillasocio):
    if planillasocio == []:
        print(" no pueden jugar")
        return

    Dni = regisDni(8, "Ingresar dni")
    if Dni != planillasocio[2]:
        print("No puedes jugar a este mini juego si no eres socio")
        return

    oferta = 0
    premioswin = []
    print("Bienvenido a este minijuego de ofertas")
    print("Vamos a probar tu suerte")
    trebol()
    print("[1] Lanzar dado")
    print("[2] salir")
    while True:
        numero = ingresoOp("Ingresar un numero : ", 1, 2)
        if numero == 1:
            aleatorio = randint(1, 6)
            if aleatorio == 1:
                dado1()
                oferta = 10
                print(f"Tienes una oferta del {oferta}%")
                premioswin.append(oferta)
                break
            elif aleatorio == 2:
                dado2()
                oferta = 20
                print(f"Tienes una oferta del {oferta}%")
                premioswin.append(oferta)
                break
            elif aleatorio == 3:
                dado3()
                oferta = 30
                print(f"Tienes una oferta del {oferta}%")
                premioswin.append(oferta)
                break
            elif aleatorio == 4:
                dado4()
                oferta = 40
                print(f"Tienes una oferta del {oferta}%")
                premioswin.append(oferta)
                break
            elif aleatorio == 5:
                dado5()
                oferta = 50
                print(f"Tienes una oferta del {oferta}%")
                premioswin.append(oferta)
                break
            elif aleatorio == 6:
                dado6()
                oferta = 60
                print(f"Tienes una oferta del {oferta}%")
                premioswin.append(oferta)
                break
        elif numero == 2:
            break
    return premioswin


def verofertas(premioswin, planillasocio):
    if planillasocio == []:
        print("No hay socios registrados")
        return

    Dni = regisDni(8, "Ingresar dni")
    if Dni != planillasocio[2]:
        print("No puedes ver los premios si no eres socio")
        return

    if premioswin == []:
        print("no hay premios disponibles")

    for i, premios in enumerate(premioswin, 1):
        print(f"Premio numero {i} y es {premios}% en tu proxima membresia")


def regiExtras(planillasocio,
               premioswin):
    minigame = minijuego(planillasocio)
    ofertasdispo = verofertas(premioswin, planillasocio)
    planillaExtra = [
        minigame,
        ofertasdispo
    ]
    return planillaExtra


def mostrarSocios(socios):
    if socios == []:
        print("No hay socios registrados")
        return

    print("Socios registrados:")
    for i, socio in enumerate(socios, 1):
        print(i, socio[0], socio[1], "- DNI:", socio[2])


def main():
    socios = []
    ingresos = []
    asistenciaList = []
    masMesInst = []
    ocupaciones = {"Spinning": 0, "Yoga": 0, "Funcional": 0}
    totalmaquinas = 50
    totcasilleros = [0] * 50
    calificaciones = []
    reptmaquinas = []
    planillasocio = []
    premioswin = []
    instructorList = instructoListM()

    while True:
        opcion = menuPrincipal()
        if opcion == 1:
            planillasocio = regisSocio()
            socios.append(planillasocio)
            if planillasocio[4] == "MENSUAL":
                ingresos.append(100)
            elif planillasocio[4] == "TRIMESTRAL":
                ingresos.append(250)
            elif planillasocio[4] == "ANUAL":
                ingresos.append(1000)
        elif opcion == 2:
            planillaInstruc = regisInstructor()
            print(planillaInstruc)
        elif opcion == 3:
            if not planillasocio:
                print("Primero registra un socio")

            else:
                planillaAsis = regisClaseAsis(
                    instructorList,
                    planillasocio,
                    asistenciaList,
                    totalmaquinas
                )
                if planillaAsis is not None:
                    clase = planillaAsis[2][1]["Especialidad"]
                    ocupaciones[clase] = ocupaciones[clase] + 1
                    masMesInst.append(planillaAsis)
        elif opcion == 4:
            if not planillasocio:
                print("Registra un socio primero")
            else:
                asistenciaList, totalmaquinas = salaMaquinas(
                    planillasocio,
                    asistenciaList,
                    totalmaquinas
                )
        elif opcion == 5:
            if not planillasocio:
                print("Registra un socio")
            else:
                finalFecha, costo, hoy = cstRenovacion(planillasocio)
                print("Cuesta", costo)
        elif opcion == 6:
            mayorOcupa(ocupaciones)
            ingresosMem(ingresos)
            mayorInstClass(asistenciaList)
            instrucMas(masMesInst)
        elif opcion == 7:
            while True:
                opcionsec = menuSecundario()
                if opcionsec == 1:
                    sepCasillero(
                        "Bienvenido esto es para separar casillero",
                        totcasilleros,
                        planillasocio,
                    )
                elif opcionsec == 2:
                    caliInstruc(calificaciones)
                elif opcionsec == 3:
                    rptCaliInst("Reporte de instructores", calificaciones)
                elif opcionsec == 4:
                    reportmaq(reptmaquinas, planillasocio)
                elif opcionsec == 5:
                    comSuplem("Bienvenido")
                elif opcionsec == 6:
                    cumpleSocio("Verificando cumpleaños", planillasocio)
                elif opcionsec == 7:
                    break

        elif opcion == 8:
            while True:
                opcionExt = menuExtras()
                if opcionExt == 1:
                    if premioswin:
                        print("Ya tiraste el dado una vez")
                    else:
                        premioswin = minijuego(planillasocio)
                elif opcionExt == 2:
                    verofertas(premioswin, planillasocio)
                elif opcionExt == 3:
                    break

        elif opcion == 9:
            mostrarSocios(socios)
            print("Finalizando el programa , gracias")
            print("Adios")
            break


main()
