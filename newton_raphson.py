def f(x):
    return x*x - 3*x + 2
def ff(x):
    return 2*x - 3
def newton_raphson(x0):
    for i in range(0,100):
        fx0 = f(x0)
        print(f"Iteration - {i}")
        print(x0)
        
        if fx0 == 0:
            print("Root Found")
            return x0
        else:
            x1 = x0 - f(x0)/ff(x0)
            x0 = x1
    return x0
x0 = 0

print(newton_raphson(x0))

