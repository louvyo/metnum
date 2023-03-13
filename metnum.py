def f(x):
    # Masukkan fungsi yang ingin dicari faktor x-nya
    return ((x**3 + x + 1) / (x ** 4 + 1))

def regula_falsi(a, b, eps):
    # a dan b adalah batas awal interval
    # eps adalah toleransi kesalahan
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))
    while abs(f(c)) > eps:
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
    return c

# Contoh penggunaan fungsi regula_falsi untuk mencari akar dari f(x)
a = -1
b = 0
eps = 0.001
x = regula_falsi(a, b, eps)
print("Faktor x yang dicari adalah", x)
