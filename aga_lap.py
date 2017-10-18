def lap(p,x):
    
    cd = x[0]
    rd = x[1]
    sg = x[2]
    
    Sp = math.sqrt(p)
    
    k0 = sp.special.kn(0,Sp) 
    k1 = sp.special.kn(1,Sp)
    
    s = sp.special.kn(0,rd*Sp)/(p*(((1+p*cd*sg)*Sp*k1)+(cd*p*k0)))
    
    return s
    
    
