def multiples_of_three_and_five(value):
    s = 0
    for i in range(value):
        if i % 5 == 0 or i % 3 == 0:
            s += i
    print(s)

multiples_of_three_and_five(1000)
