def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        count = 0
        for i in range(1, result + 1):
            if result % i == 0:
                count += 1
        if count == 2:
            print("Простое")
        else:
            print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(f, s, t):
    sum = f + s + t
    return sum


result = sum_three(2, 3, 6)
print(result)
