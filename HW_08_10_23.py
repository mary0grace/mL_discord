import math

f = ["*3", "+1", "exp", "^3", "log"]
x = 2

def grad(f, x):
    arg = x
    answ = 1
    for i in range(len(f)):
        if f[i] == "sin":
            answ = answ*math.cos(arg)
            arg = math.sin(arg)
            continue
        if f[i] == "cos":
            answ = answ*(-math.sin(arg))
            arg = math.cos(arg)
            continue
        if f[i][0] == "^":
            degree = int(f[i][1:])
            answ = answ*degree*arg**(degree-1)
            arg = arg**degree
            continue
        if f[i][0] == "*":
            const = int(f[i][1:])
            answ = answ*const
            arg = const*arg
            continue
        if f[i] == "exp":
            answ = answ*math.exp(arg)
            arg = math.exp(arg)
            continue
        if f[i] == "sqrt":
            answ = answ*1/(2*math.sqrt(arg))
            arg = math.sqrt(arg)
            continue
        if f[i] == "1/x":
            answ = answ*(-1/arg**2)
            arg = 1/arg
            continue
        if f[i] == "log":
            answ = answ*1/(arg*math.log(10))
            arg = math.log(arg, 10)
            continue
        if f[i][0] == "+":
            const = int(f[i][1:])
            arg = arg + const
            continue
    return answ

print(grad(f, x))
print(3*math.exp(3*x+1)*3*(math.exp(3*x+1))**2*1/(math.exp(3*x+1)**3*math.log(10)))
assert grad(f, x) == 3*math.exp(3*x+1)*3*(math.exp(3*x+1))**2*1/(math.exp(3*x+1)**3*math.log(10))
