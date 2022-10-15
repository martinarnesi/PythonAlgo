def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 1

    while low <= high:
        print("Step:" + str(count))
        count += 1
        mid = round((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def create_array(number):
    return list(range(1,number))


if __name__ == '__main__':
    #Divide and Conquer O(Log n)
    my_list = create_array(9999)
    print('Found at position:' + str(binary_search(my_list, 3454)))
