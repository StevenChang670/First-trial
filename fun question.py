import numpy as np
## distant 列法: d12,d13,d14,d15, ...d1n,d23,d24,d25,...
## fire 為 h1,h2,h3,...
def optimal(distant, fire):
    n = len(fire)
    U = []
    D = np.zeros([n,n])
    k = 0
    for i in range(n):
        for j in range(i,n):
            if i == j:
                D[i,j] = 0
            else:
                if i == 0:
                    k = 0
                else:
                    k = int((2*n-i-1)*i/2)
                D[i,j] = D[j,i] = distant[k+(j-i)-1]
    
    ex_distant = D.dot(fire)
    ex_distant = list(ex_distant)
    print(D)
    print(ex_distant)
    U.append(ex_distant.index(min(ex_distant)) + 1)

    U.append(list(D[U[0]-1]).index(max(D[U[0]-1])) + 1 )
    
    
        
    return U
