def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))

    my_list_2 = [1, 3, 5, 7, 4]
    print(sum(my_list_2))
    print(count(my_list_2))
    print(max(my_list_2))
    print(quicksort([10, 5, 2, 3]))
