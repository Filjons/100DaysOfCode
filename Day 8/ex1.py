def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    if not is_prime:
        print("It's not a prime number.")

n = int(input("Gimme a number: "))
prime_checker(number=n)