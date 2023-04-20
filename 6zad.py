number = int(input("Введите число: "))

if number < 2:
    print("Число должно быть больше 1")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Простое")
    else:
        print("Составное")
