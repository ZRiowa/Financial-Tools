def MacD(par,coup,r,y):
    
    duration = y - 2018
    i=0
    I=[]
    while i<= duration:
        i+=1
        I.append(i)
    Sum=0
    Pv=0
    if coup == 0:
        return y
    elif coup > 0 :
        for i in I:
            Factor = (par*coup)/((1+r)**i)
            Factorize = i *Factor 
            Pv+=Factor
            Sum += Factorize
        Macd = Sum/Pv
        return Macd
    else:
        print("parameters set wrong!")
    

print(  MacD(91000,0.05,0.10,2020)     )
        
    