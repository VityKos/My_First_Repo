# Here we gonna find a count primal number

def isPrime(num):
    if num <= 1:
        return False
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True


start = int(input('Please input start: '))
end = int(input('Please input end: '))
count = 0
for i in range(start, end+1):
    if isPrime(i):
        count += 1

print('The count of Prime number in range (', start,',', end,') = ', count)
