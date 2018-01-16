def maxInList(alist):
    myMax = alist[0]
    for num in alist:
        if myMax < num:
            myMax = num
    return myMax


