def liebniz(n):
    den=1
    acc=1

    for i in range(n):
        den= den + 2
        acc= acc - (1/den)
        den= den + 2
        acc= acc + (1/den)
        
    pi= acc*4

    return pi
