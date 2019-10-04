def c():
    p1 = 2
    p2 = 3
    

def p():
    c()
    global p1
    global p2
    print(p1, p2)
