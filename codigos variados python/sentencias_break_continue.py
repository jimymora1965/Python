#break, continue, y else

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "es igual a", x, "X", n/x)
            break;
    else:
        print(n, "Es un numero primo")
        
