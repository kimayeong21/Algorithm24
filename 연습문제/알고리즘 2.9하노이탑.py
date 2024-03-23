def hanoi_tower(n, fr, tmp, to):
    if(n==1):
        print("원판 1: %s --> %s"%(fr,to))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" %(n,fr,to))
        hanoi_tower(n-1, tmp, fr, to)
print('n=1')
hanoi_tower(1,1,2,3)
print('n=2')
hanoi_tower(2,1,3,2)
print('n=3')
hanoi_tower(3,1,3,2)

