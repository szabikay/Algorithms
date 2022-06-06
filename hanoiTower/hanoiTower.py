def move(f,t):
    print("Move disc from  {} to {}!".format(f,t))

def hanoi(n,f,h,t):
    #number of discs, from, helper, target
    if n > 0:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(3,"A","B","C")