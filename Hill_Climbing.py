import random
def f(x):return -(x-3)**2+10
x=random.randint(-10,10)
for _ in range(50):
    nx=x+random.choice([-1,1])
    if f(nx)>f(x):x=nx
print(x,f(x))
