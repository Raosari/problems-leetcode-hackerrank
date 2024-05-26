# crea una funcion que dado un array, te devuelva el primer elemento que se repite
# ejemplo [1,2,4,1,3] en este caso la funcion retorna 1
array = [2,5,2,5,2]
def FirstDuplicated(arr):
    dicc = {}
    for element in arr:
        if element in dicc:
            return element
        else:
            dicc[element] = element
    return None
print(FirstDuplicated(array))








