print("=== Калькулятор на Python ===")
print("Доступные операции: +, -, *, /")
print("Введите 'exit' чтобы выйти")

result = float(input("Введите первое число: "))

while True:
    operator = input("Введите операцию (+, -, *, /): ")
    if operator.lower() == "exit":
        print("Выход из программы...")
        break

    number = float(input("Введите число: "))

    if operator == "+":
        result = result + number
    elif operator == "-":
        result = result - number
    elif operator == "*":
        result = result * number
    elif operator == "/":
        result = result / number
    else:
        print("Ошибка: неизвестная операция!")
        continue

    print("Текущий результат:", result)

