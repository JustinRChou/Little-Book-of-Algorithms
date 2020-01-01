def find_lowest(numbers_list_in):
    lowest = numbers_list_in[0]
    for count in range(len(numbers_list_in)):
        if numbers_list_in[count] < lowest:
            lowest = numbers_list_in[count]
    return lowest
numbers_list = [9,8,7,5,6,2,1,12,14,0,13]
lowest_num = find_lowest(numbers_list)
print("The lowest number in the list is ", lowest_num)