from erro_absoluto import *

# Calcula o erro relativo
def erro_relativo(x, x_aprox):    
   
    # e_absoluto recebe o valor do erro absoluto
    e_absoluto = erro_absoluto(x,x_aprox)  
    # e_relativo receber o valor do erro relativo 
    e_relativo = e_absoluto / x_aprox
    return e_relativo
