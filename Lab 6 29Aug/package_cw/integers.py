def max1(x,y,z):
    if x>y:
        M=x
        sm=y
    else:
        M=y
        sm=x
    if z>M:
        sm=M
        M=z
    elif z>sm:
        s=sm
        sm=z
    print('Maximum=',M)

def min1(x,y,z):
    if x>y:
        M=x
        sm=y
    else:
        M=y
        sm=x
        
    if z>M:
        sm=M
        M=z
    elif z>sm:
        s=sm
        sm=z
    print('Minimum=',s)
    
def sum1(z,y,x):
    s=x+y+z
    print(s)
def average1(x,y,z):
    a=(x+y+z)/3
    print(a)
