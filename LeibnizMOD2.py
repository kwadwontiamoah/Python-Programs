def leibniz(terms):
    acc=0
    num=4
    den=1

    for aterm in range(terms):
        nextterm= num/den 

        acc= acc + nextterm * (-1)**aterm

        den= den + 2

    return acc
