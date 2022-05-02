def listing_fruits(my_list: list):
    """listing_fruits function"""

    new_list = [[i+1, my_list[i]] for i in range(0,len(my_list))]
    flat_new_list = [num for element in new_list for num in element]

    return flat_new_list

if __name__ == '__main__':
    #driver code
    print(listing_fruits(["Banana", "Strawberry", "Lemon"]) == [1, "Banana", 2, "Strawberry", 3, "Lemon"])
