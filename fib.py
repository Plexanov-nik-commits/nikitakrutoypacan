#!/usr/bin/env python3

def fib(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])
    return result

def main():
    try:
        n = int(input("Введите количество чисел Фибоначчи: "))
        if n <= 0:
            print("Пожалуйста, введите положительное число")
            return
        numbers = fib(n)
        for num in numbers:
            print(num)
    except ValueError:
        print("Пожалуйста, введите целое число")
if __name__ == "__main__":
    main()
