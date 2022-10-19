def countdown(i):
    print(str(i))
    if i <= 0:
        return
    else:
        countdown(i-1)


def recursive_sum(list):
    if list == []:
        return 0
    return list[0] + recursive_sum(list[1:]) #1: Starting from 5


if __name__ == '__main__':
    print(countdown(99))
    print(recursive_sum([5,4,3,2,1]))

    list = [5,4,3,2]
    print(list[:2])



