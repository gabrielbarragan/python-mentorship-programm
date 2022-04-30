from logging import exception
import matplotlib.pyplot as plt
import random

# Definir la función g
def g(x):
    """ recibe valores de x para generar un valor de y"""
    if x != 0:
        result = (12/2*x)**2
    else:
        result= 0

    return result


# Plotea salida de la función g

def graficar(array_x,array_y):
    """ Esta función toma 2 listas y genera un grafico"""
    fig, ax = plt.subplots()
    ax.plot(array_x, array_y)

    plt.title('Mi grafica')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.grid()

    plt.show()

    return ax
    

# Configurar el gráfico




if __name__ == '__main__':
    """"""
    # Crear un intervalo de valores 'x' de -100 a 100
    x= [ random.randint(-100,100) for number in  range(0,20)]
    x.sort()

    # Obtener los valores 'y' correspondientes de la función
    y = [g(number) for number in x]

    # Graficar 'x' contra g(x)
    graficar(x,y)

    # Plotea un círculo vacío para mostrar el punto indefinido
