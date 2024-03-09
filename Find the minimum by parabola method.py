import numpy as np
    
def func(x,a,b,c):
    f_value = 0.
    f_value = np.sin(a*x) + np.cos(b*x) + c*x
    return float(f_value)

def find_the_minimum(a,b,c):
    interval = list(np.linspace(0,10,6))#在0到10分81個點#
    minimum_x = []
    function_value = []
    for j in range(0,5):
        a_1 = interval[j]
        a_2 = interval[j+1]
        for step in range(200):#開始在第j和j+1中間找最小值#
            a_3 = (a_2+a_1)/2
            f1 = func(a_1,a,b,c)
            f2 = func(a_2,a,b,c)
            f3 = func(a_3,a,b,c)
            min_x = ((a_3**2-a_1**2)*f2 + (a_2**2-a_3**2)*f1 + (a_1**2-a_2**2)*f3)/(2*((a_1-a_2)*f3+(a_2-a_3)*f1+(a_3-a_1)*f2))
            #min_x為(a_1,f1)等三個點所估計的parabola的極值所發生的點x#
            if  min_x<a_1 or min_x>a_2 : break#如果min_x落到a_1 , a_2外則極值可能發生在非此區間，故不繼續計算。注意此時a_1<a_3<a_2#
            if abs(min_x - a_1) < abs(min_x - a_2):#把距離min_x最遠的a_1,a_2點改其值為a_3(名稱仍然為a_1或a_2)#
                a_2 = a_3
            else :
                a_1 = a_3
            if abs(a_1 - a_2) < 1E-14 : break
        
        the_minimum = 0.
        if func(a_1,a,b,c)>func(a_2,a,b,c):#雖然a_1 a_2很接近，但我還想比較f(a_1),f(a_2)誰比較小#
            the_minimum = a_2
        else :
            the_minimum = a_1
        minimum_x.append(the_minimum)#比較小的加進來minimum_x#
    
    for value in minimum_x:
        function_value.append(func(value,a,b,c))#把全部的f(minimum_x)比大小#
        
    the_index = function_value.index(min(function_value))#最小的f(minimum_x)在function_value的index 與 其對應的minimum_x在minimum_x的index 一致#
    
    the_number_i_desire = minimum_x[the_index]#取出那個index的值#
    
    return the_number_i_desire
        
    
