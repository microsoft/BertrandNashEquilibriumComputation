
presicion_v=0
max_price_v=0
loop_limit_v=0
convergence_limit_v=0
mix_parameter_v=0

def set_config():
    global presicion_v 
    global mix_parameter_v
    global loop_limit_v
    global convergence_limit_v
    global max_price_v

    file=open("config.txt" , 'r' )
    data=file.read()
    data=data.split()
    data.pop(0)
    presicion_v=float(data.pop(0))
    
    data.pop(0)
    max_price_v=float(data.pop(0))

    data.pop(0)
    loop_limit_v=int(data.pop(0))
    
    data.pop(0)
    convergence_limit_v=float(data.pop(0))

    data.pop(0)
    max_parameter_v=float(data.pop(0))



def max_price():
    return max_price_v

def precision():
    return presicion_v

def loop_limit():
    return loop_limit_v

def convergence_limit():
    return convergence_limit_v

def mix_parameter():
    return mix_parameter_v