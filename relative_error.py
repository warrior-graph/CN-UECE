from absolute_error import *

# Calcula o erro relativo
def relative_error(x, x_aprox):    
   
    # e_absoluto recebe o valor do erro absoluto
    absolute_e = absolute_error(x,x_aprox)  
    # e_relativo receber o valor do erro relativo 
    relative_e = absolute_e / abs(x_aprox)
    return relative_e
