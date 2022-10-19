def quicksort(array):
    if len(array) <2 :
        return array; #Base case, With zero and 1 element already sorted
    else:
        middle = len(array) / 2

        pivot = array[middle] #Recursive case

        less = [i for i in array[1:] if i < pivot] #Sub-array off all elements less that pivot
        greater = [i for i in array[1:] if i > pivot] #Sub-array off all elements greater that pivot

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    print(quicksort([10, 5, 2, 3]))
