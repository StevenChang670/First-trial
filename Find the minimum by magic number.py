import numpy as np
    
def func(x,a,b,c):
    f_value = 0.
    f_value = np.sin(a*x) + np.cos(b*x) + c*x
    return float(f_value)

def find_the_minimum(a,b,c):
    interval = list(np.linspace(0,10,31))
    minimum_x = []
    function_value = []
    FRAC = 0.38197
    for j in range(0,30):
        a_1 = interval[j]
        a_2 = interval[j+1]
        fa , fc = func(a_1,a,b,c) , func(a_2,a,b,c)
        a_3 = a_1+(a_2-a_1)*FRAC 
        fb = func(a_3,a,b,c) 
 
        for step in range(150):
            if abs(a_1-a_3)>abs(a_2-a_3): d = a_3+(a_1-a_3)*FRAC
            else: d = a_3+(a_2-a_3)*FRAC 
 
            if abs(a_3-d)<1E-14: break 
            fd = func(d,a,b,c) 
            if fd<fb: 
                a_3, d = d, a_3 
                fb, fd = fd, fb 
 
            if (d-a_3)*(a_1-a_3)>0: a_1, fa = d, fd 
            else: a_2, fc = d, fd

        minimum_x.append(d)
    for value in minimum_x:
        function_value.append(func(value,a,b,c))

    index = function_value.index(min(function_value))
    min_x = minimum_x[index]

    return min_x
        
        
    
