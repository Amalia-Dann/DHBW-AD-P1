def numbers(maximum: int):
    for i in range(maximum):
        result = ""
        for j in range(i):
            result += str(i)
        print(result)

numbers(10)
