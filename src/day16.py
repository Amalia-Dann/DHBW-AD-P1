def sqrfunc_1(size):
    for i in range(5):
        skk.fd(size)
        skk.left(90)
        size = size + 7
        skk.color("white")

def sqrfunc_2(size):
    for i in range(5):
        skk.fd(size)
        skk.right(120)
        size = size + 5
        skk.color("blue")

def sqrfunc_3(size):
    for i in range(5):
        skk.fd(size)
        skk.right(240)
        size = size + 9
        skk.color("indigo")

for j in range(6, 146,20):
    sqrfunc_1(j)
    sqrfunc_2(j)
    sqrfunc_3(j)
