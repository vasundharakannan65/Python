def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result
print(concatenate_list_data([1, 11, 1111, 11111]))
