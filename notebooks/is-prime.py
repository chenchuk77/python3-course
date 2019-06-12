# program to check if number is a prime number
# prime numbers = [1,2,3,5,7,11.....]
#
while True:
    number_str = input ('please enter a number, or just <ENTER> to quit: \n')
    if not number_str:
        exit(0)
    number = int(number_str)
    devisors = []

    for i in range(2, number):
        if number % i == 0:
            devisors += [i]
    if devisors:
        print('{} is not prime.\n(devides by {}).'.format(number, devisors))
        # break
    else:
        print('{} is a prime number.'.format(number))

