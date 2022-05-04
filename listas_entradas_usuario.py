import re, fileinput, sys 
from io import StringIO
def menu():
    """
    no arguments.
    Description: Show a menú for any function
    """

    message = """
    ---------------------------------------Bienvenido al menú--------------------------------------------
    -----------------------------------------------------------------------------------------------------
    -- El siguiente menú representa una serie de funciones que pueden ser usadas para modificar listas --
    -----------------------------------------------------------------------------------------------------
    -- 1) Ingresa la cantidad de comandos que deseas usar.                                             --
    -----------------------------------------------------------------------------------------------------
    -- Estas son las diferentes opciones:                                                              --
    -- Comando                        -> Uso                                                           --
    -- insert <<posición>> <<valor>>  -> Agrega un valor a la lista en la posición dada                --    
    -- append <<valor>>               -> Agrega un valor a la lista en la última posición              --
    -- remove <<valor>>               -> Elimina de la lista el valor indicado                         --
    -- pop                            -> Elimina el valor de la última posición de la  lista           --
    -- sort                           -> Ordena la lista de menor a mayor valor                        --
    -- reverse                        -> Invierte el orden de la lista                                 --
    -----------------------------------------------------------------------------------------------------
    -----------------------------------------------------------------------------------------------------

        """
    return message


def user_list():
    """number-> int: Toma un número ingresado por el usuario y espera la cantidad de entradas y comandos representada por este número."""
    options = {
        "insert": 1,
        "remove": 2,
        "append": 3,
        "pop": 6,
        "sort": 5,
        "reverse": 7,
    }
    print(menu())
    num_commands=""
    while type(num_commands) is not int:
        num_commands = input("por favor ingresa la cantidad de comandos que vas a usar: \n")
        try: 
            num_commands = int(num_commands)
        except TypeError:
            print("el valor debe ser un número")
        except ValueError:
            print("el valor debe ser un número")

    intentos=[]
    parametros=[]
    result = []
    for value in range(0, num_commands):
        comando = input(">>")
        parametros= [int(n) for n in re.findall(r'-?\d+\.?\d*', comando)]
        
        if comando.find('append') > -1:
            result.append(parametros[0])
        elif comando.find('insert') > -1:
            result.insert(parametros[0], parametros[1])
        elif comando.find('remove') > -1:
            result.remove(parametros[0])
        elif comando.find('remove') > -1:
            result.pop()
        elif comando.find('sort') > -1:
            result.sort()
        elif comando.find('reverse') > -1:
            result.reverse()
        elif comando.find('pop') > -1:
            result.pop()
        else: 
            raise Exception(f'el comando {comando} no es válido')

        parametros = []
    print(result)
    return result

if __name__=='__main__':

    print(user_list() == [15, 7, 8, 9, 3])
    print(user_list() == [3, 7, 15, 20, 90, 100])
    print(user_list() == [47, 7, 9, 15, 20, 90])

