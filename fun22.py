def draw_1d(n,c):
    for loop in range(3):
        print(c*n)



def draw_2d(n,m,char):
    for loop in range(n):
        print(m*char)


def draw_3d(n,m,border,fill):
    print(border*m)
    for loop in range(n-2):
        print(border+fill*(m-2)+border)
    print(border*m)
         
        
