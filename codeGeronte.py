"""
Programa que permite agregar y buscar un encargado
Autor: Leonardo Rios
Colaboradores:
Version: 1.0
"""
import json
import os
import sys

#Funciones:
def modificarDatos(encargado):
    """
    Funcion que modifica los datos del encargado
    Parametros:
    encargado: encargado a modificar
    Retorno:
    Ninguno
    Autor: Leonardo Rios
    Colaboradores:
    """
    limpiarPantalla()
    print("Seleccionó Modificar Datos")
    print("="*70)
    while True:
        openOpcion = input("Quiere modificar paciente o encargado? P/E o '0' para salir:  ").upper()
        if openOpcion == "0":
            limpiarPantalla()
            break
        if openOpcion == "P":
            print("Seleccionó modificar Paciente")
            print("="*70)
            buscaEncar = input("Ingrese el DNI del encargado a modificar:  ")
            for encargado in encargados:
                if encargado["dniEncar"] == buscaEncar:
                    print(f'Modificará el paciente a cargo de ')
                    nombrePaciente = input("Ingrese el nombre del paciente: ")
                    apellidoPaciente = input("Ingrese el apellido del paciente: ")
                    dniPaciente = input("Ingrese el DNI del paciente: ")
                    anosPaciente = input("Ingrese los años del paciente: ")
                    paciente = {
                        "nombrePac": nombrePaciente,
                        "apellidoPac": apellidoPaciente,
                        "dniPac": dniPaciente,
                        "anosPac": anosPaciente
                    }
                    encargado.update(paciente)
                    guardarEncargados(encargados)
                    print("Paciente modificado")
                    break
        elif openOpcion == "E":
            print("Seleccionó modificar Encargado")
            print("="*70)
            buscaEncar = input("Ingrese el DNI del encargado a modificar:  ")
            for i in range (len(encargados)):
                if encargado[i]["dniEncar"] == buscaEncar:
                    nombreEncargado = input("Ingrese el nombre del encargado: ")
                    apellidoEncargado = input("Ingrese el apellido del encargado: ")
                    dniEncargado = input("Ingrese el DNI del encargado: ")
                    telefonoEncargado = input("Ingrese el teléfono del encargado: ")
                    emailEncargado = input("Ingrese el email del encargado: ")
                    encargado = {
                        "dniEncar": dniEncargado,
                        "nombreEncar": nombreEncargado,
                        "apellidoEncar": apellidoEncargado,
                        "telefonoEncar": telefonoEncargado,
                        "emailEncar": emailEncargado
                    }
                    encargados[i].update(encargado)
                    guardarEncargados(encargados)
                    print("Encargado modificado")
                    break
            else:
                print("Encargado no encontrado")
                print("Vuelva intentarlo")
                input("Presione Enter para continuar")

def borrarEncargados(encargado):
    """
    Funcion que borra un encargado
    Parametros:
    encargado: encargado a borrar
    Retorno:
    Ninguno
    Autor: Leonardo Rios
    Colaboradores:
    """
    respon = input("Desea borrar por selección o por lista? S/L:  ").upper()
    if respon == "S":
        buscaEncargado = input("Ingrese el DNI del encargado a borrar:  ")
        for encargado in encargados:
            if encargado["dniEncar"] == buscaEncargado:
                encargados.remove(encargado)
                guardarEncargados(encargados)
                print("Encargado borrado")
                break
        else:
            print("Encargado no encontrado")
            print("Vuelva intentarlo")
            input("Presione Enter para continuar")
    elif respon == "L":
        listarEncargados(encargados)
        numBorrar = input("Ingrese el numero del encargado a borrar:  ")
        encargados.pop(int(numBorrar)-1)
        guardarEncargados(encargados)
        print("Encargado borrado")
        input("Presione Enter para continuar")
    else:
        print("Opcion no valida")
        print("Ingrese una opcion valida")
        input("Presione Enter para continuar")

def listarEncargados(encargados):
    """
    Funcion que lista los encargados
    Parametros:
    encargados: lista de encargados
    Retorno:
    Ninguno
    Autor: Leonardo Rios
    Colaboradores:
    """
    limpiarPantalla()
    print("Encargados:")
    print("="*70)
    conteo = 0
    for encargado in encargados:
        conteo += 1
        print(f"{conteo}.")
        print(f"Nombre del encargado: {encargado['nombreEncar']} {encargado['apellidoEncar']}")
        print(f"DNI del encargado: {encargado['dniEncar']}")
        print(f"Telefono del encargado: {encargado['telefonoEncar']}")
        print(f"Email del encargado: {encargado['emailEncar']}")
        print("="*70)
        respo2 = input("Desea también ver los datos del paciente? S/N:  ").upper()
        print()
        if respo2 == "S":
            print("Paciente:")
            print("="*70)
            print(f"Nombre del paciente: {encargado['nombrePac']} {encargado['apellidoPac']}")
            print(f"DNI del paciente: {encargado['dniPac']}")
            print(f"Años del paciente: {encargado['anosPac']}")
            print("="*70)
        elif respo2 == "N":
            continue
        else:
            print("Opcion no valida")
            print("Ingrese una opcion valida")
            continue

    input("Presione Enter para continuar")
    limpiarPantalla()

def limpiarPantalla():
    """
    Funcion que limpia la consola en pantalla
    Sirve para Linux y windows
    """
    if "linux" in sys.platform:
        os.system("clear")
    else:
        os.system("cls")

def menu():
    """
    Funcion que muestra el menu
    Parametros:
    Ninguno
    Retorno:
    Ninguno
    Autor: Leonardo Rios
    Colaboradores:
    """
    print("MENU")
    print("="*70)
    print("1. Agregar Paciente")
    print("2. Buscar Paciente")
    print("3. Listar Encargados")
    print("4. Borrar Encargado")
    print("5. Modificar Datos")
    print("0. Salir")
    print("="*70)
    return

def buscarEncargado(encargado):
    """
    Funcion que busca un encargado
    Parametros:
    encargados: lista de encargados
    Retorno:
    Ninguno
    Autor: Leonardo Rios
    Colaboradores:
    """
    limpiarPantalla()
    print("Seleccionó Buscar Encargado")
    print("="*70)
    while True:
        dniEncargado = input("Ingrese el DNI del encargado o '0' para salir:  ")
        if dniEncargado == "0":
            limpiarPantalla()
            break
        dniEncar = dniEncargado
        for encargado in encargados:
            if encargado["dniEncar"] == dniEncar:
                print(f"Nombre del encargado: {encargado['nombreEncar']} {encargado['apellidoEncar']}")
                print(f"DNI del encargado: {encargado['dniEncar']}")
                print(f"Telefono del encargado: {encargado['telefonoEncar']}")
                print(f"Email del encargado: {encargado['emailEncar']}")
                cargarPaciente = input("Quiere ver los datos del un paciente? S/N:  ").upper()
                if cargarPaciente == "S":
                    print()
                    print("Paciente:")
                    print("="*70)
                    print(f"Nombre del paciente: {encargado['nombrePac']} {encargado['apellidoPac']}")
                    print(f"DNI del paciente: {encargado['dniPac']}")
                    print(f"Años del paciente: {encargado['anosPac']}")
                    break
                elif cargarPaciente == "N":
                    break
                else:
                    print("Opcion no valida")
                    print("Ingrese una opcion valida")
                continue
        else:
            print("Encargado no encontrado")
            print("Vuelva intentarlo")
            input("Presione Enter para continuar")
    return

def guardarEncargados(encargados):
    """
    Funcion que guarda los encargados en un archivo json
    Parametros:
    encargados: lista de encargados
    Retorno:
    Ninguno
    Autor: Leonardo Rios
    Colaboradores:
    """
    with open("encargados.json", "w") as f:
        json.dump(encargados, f, indent=4)

def cargarEncargados():
    """
    Funcion que carga los encargados desde un archivo json
    Parametros:
    Ninguno
    Retorno:
    encargados: lista de encargados
    Autor: Leonardo Rios
    Colaboradores:
    """
    try:
        with open("encargados.json", "r") as f:
            encargados = json.load(f)
    except FileNotFoundError:
        encargados = []
    return encargados

def agregarEncargados():
    """
    Funcion que agrega un encargado
    Parametros:
    Ninguno
    Retorno:
    encargados: lista de encargados
    Autor: Leonardo Rios
    Colaboradores:
    """
    limpiarPantalla()
    print("Seleccionó Agregar Encargado")
    print("="*70)
    while True:
        nombreEncargado = input("Ingrese el nombre del encargado o '0' para salir: ")
        if nombreEncargado == "0":
            limpiarPantalla()
            break
        apellidoEncargado = input("Ingrese el apellido del encargado: ")
        dniEncargado = input("Ingrese el DNI del encargado: ")
        telefonoEncargado = input("Ingrese el teléfono del encargado: ")
        emailEncargado = input("Ingrese el email del encargado: ")
        encargado = {
            "dniEncar": dniEncargado,
            "nombreEncar": nombreEncargado,
            "apellidoEncar": apellidoEncargado,
            "telefonoEncar": telefonoEncargado,
            "emailEncar": emailEncargado
        }
        encargados.append(encargado)
        guardarEncargados(encargados)
        while True:
            respo1 = input("Quiere agregar a un paciente? S/N:  ").upper()
            if respo1 == "S":
                    nombrePaciente = input("Ingrese el nombre del paciente: ")
                    apellidoPaciente = input("Ingrese el apellido del paciente: ")
                    dniPaciente = input("Ingrese el DNI del paciente: ")
                    anosPaciente = input("Ingrese los años del paciente: ")
                    paciente = {
                        "nombrePac": nombrePaciente,
                        "apellidoPac": apellidoPaciente,
                        "dniPac": dniPaciente,
                        "anosPac": anosPaciente
                    }
                    encargado.update(paciente)
                    guardarEncargados(encargados)
            elif respo1 == "N":
                break
            else:
                print("Opcion no valida")
                print("Ingrese una opcion valida")
                continue
    return encargados

#Menu Principal
limpiarPantalla()
encargados = cargarEncargados()
while True:
    menu()
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        agregarEncargados()
    elif opcion == "2":
        buscarEncargado(encargados)
    elif opcion == "3":
        listarEncargados(encargados)
    elif opcion == "4":
        borrarEncargados(encargados)
    elif opcion == "5":
        modificarDatos(encargados)
    elif opcion == "0":
        limpiarPantalla()
        break
    else:
        print("Opcion no valida")
        print("Ingrese una opcion valida")
        continue
print("Hasta Luego")
    

