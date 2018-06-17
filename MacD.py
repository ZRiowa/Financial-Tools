def MacD(par,coup,r,y):
    
    duration = y - 2018
    i=0
    I=[]
    while i<= duration:
        i+=1
        I.append(i)
    Sum=0
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
    
    
par=input().int()
coup=input().int()
r=input().int()
y=input().int()
print(  MacD(91000,0.20,0.15,2020)     )
        
    