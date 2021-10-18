def goldbach():
    import math

    MAX = 10000

    primes = []

    def is_even(number: int) -> bool:
        if not isinstance(number, int):
            raise ValueNotNumberInt("Number not integer")
        if number < 3:
            raise ValueNotEven("Integer not greater than 2 ")
        if number % 2 != 0:
            raise ValueNotEven("Value Not Even")
        return True

    def sieveSundaram():
        marked = [False] * (int(MAX / 2) + 100)
        for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
            for j in range((i * (i + 1)) << 1, int(MAX / 2) + 1, 2 * i + 1):
                marked[j] = True
        primes.append(2)
        for i in range(1, int(MAX / 2) + 1):
            if marked[i] == False:
                primes.append(2 * i + 1)

    def findPrimes(n):
        if not is_even(n):
            print("Invalid Input")
            return
        i = 0
        while primes[i] <= n // 2:
            diff = n - primes[i]
            if diff in primes:
                print(primes[i], "+", diff, "=", n)
                return
            i += 1

    while True:
        input_number = input("Please enter an even number greater than 3, Break <q>")
        if input_number == "q":
            break

        try:
            if is_even(int(input_number)):
                sieveSundaram()
                findPrimes(int(input_number))
        except ValueError as exc:
            print(exc)
        finally:
            continue


goldbach()
