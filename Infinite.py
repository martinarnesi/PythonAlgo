def countdown(i):
    print(i)
    if i == -700:
        return
    else:
        countdown(i - 1)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

if __name__ == '__main__':
    i = 3
    print(countdown(i))
    print(fact(5))
