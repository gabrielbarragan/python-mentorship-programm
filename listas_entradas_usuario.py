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
    num_commands = int(input("Por favor ingresa la cantidad de comandos que vas a usar: \n"))
    intentos=[]
    for value in range(0, num_commands):
        comando = input(">>")
        intentos.append(comando)
    print(intentos)
    return intentos

if __name__=='__main__':
    user_list()
