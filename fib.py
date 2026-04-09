#!/usr/bin/env python3
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
def main():
    try:
        n = int(input("введите номер числа Фибоначчи: "))
        if n <= 0:
            print("Пожалуйста, введите положительное число")
            return
        result = fib(n)
        print(f"fib({n}) = {result}")
    except ValueError:
        print("Пожалуйста, введите целое число")
if __name__ == "__main__":
    main()
