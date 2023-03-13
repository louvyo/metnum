def f(x):
    return ((x**3 + x + 1) / (x ** 4 + 1))

def regula_falsi(a, b, n):
    if f(a)*f(b) >= 0:
        print("Metode regula falsi tidak berlaku pada interval ini.")
        return None

    c = a
    for i in range(1, n+1):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))

        print("Iterasi ke-", i)
        print("a = {:.6f}, f(a) = {:.6f}".format(a, f(a)))
        print("b = {:.6f}, f(b) = {:.6f}".format(b, f(b)))
        print("x = {:.6f}, f(x) = {:.6f}".format(c, f(c)))

        if f(c) == 0:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c

        if i == n:
            print("Batas iterasi telah dicapai.")

    return c

a = -1
b = 0
n = 3

x = regula_falsi(a, b, n)

print("Nilai solusi akar x = {:.6f}".format(x))
