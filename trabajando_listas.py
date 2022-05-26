"""function to return the first n elements of the list"""
from os import remove
from re import A


def first_n(array: list, pos: int):
    """function to drop the first n elements of the list and return the rest"""
    
    array = array[:pos]

    return array


def drop_n(array: list, pos:int):
    """function to add 'element' to the end of the list"""
    
    array = array[pos:]

    return array


def end_lis_add(array:list, num: int):
    """function to add 'element' to the beginning of the list"""
    array= array + [num]
    # array.append(num)
    return array





def begin_lis_add(array:list, num: int):
    """function to add 'element' at position 'index' to the list"""
    
    array= [num] + array
    # array.insert(0,num)
    
    return array



def index_lis_add(array: list, pos: int, num: int):
    """function to add any two elements to the list at the index"""

    array_left = array[0:pos]
    array_right = array[pos:]
    array= array_left+[num]+array_right
    # array.insert(pos,num)
    
    return array



def index_lis_multiple_add(array: list, pos: int, num: int, num_2:int):
    """function to delete the element from the end of the list and return the deleted element"""

    array_left = array[0:pos]
    array_right = array[pos:]
    array= array_left+[num, num_2]+array_right
    # array.insert(pos,num)
    # array.insert(pos+1,num_2)
    
    return array



def end_list_delete(array:list):
    """function to delete the element at the beginning of the list"""
    pos= len(array)-1 
    array = array[pos] # para borrar todo menos el último elemento de la lista
    #para borrar solo el último elemento de la lista
    # array.pop()
    
    return array



def start_lis_delete(array:list):
    
    array = array[1:] # para borrar el primer elemento de la lista
    
    return array

def delete_at_lis(array: list, pos: int):
    """function to delete the element at the position 'index'"""
    array_left = array[0:pos]
    array_right = array[pos+1:]
    array= array_left+array_right

    # array.pop(pos)

    return array



def remove_val_lis(array: list, num: int):
    """function to delete the element of the list where element = val"""
        
    array = [element for element in array if element != num ]

    return array
    





if __name__ == '__main__':
    
    print(first_n([1, 4, 3, 6, 5], 3) == [1, 4, 3])

    print(drop_n([1, 4, 3, 6, 5], 3) == [6, 5])

    print(end_lis_add([1, 4, 3, 6, 5], 20) == [1, 4, 3, 6, 5, 20])

    print(begin_lis_add([1, 4, 3, 6, 5], 34) == [34, 1, 4, 3, 6, 5])

    print(index_lis_add([1, 4, 3, 6, 5], 2, 100) == [1, 4, 100, 3, 6, 5])

    print(index_lis_multiple_add([1, 4, 3, 6, 5], 3, 34, 23) == [1, 4, 3, 34, 23, 6, 5])

    print(end_list_delete([1, 4, 3, 6, 5]) == 5)

    print(start_lis_delete([1, 4, 3, 6, 5]) == [4, 3, 6, 5])

    print(delete_at_lis([1, 4, 3, 6, 5], 2) == [1, 4, 6, 5])

    print(remove_val_lis([1, 4, 3, 6, 5], 6) == [1, 4, 3, 5])
