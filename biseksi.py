def f(x):
    return ((x**3 + x + 1) / (x ** 4 + 1))

def bisection(a, b, eps, N=9):
    if f(a)*f(b) >= 0:
        print("Metode biseksi gagal: fungsi memiliki tanda sama pada a dan b")
        return None
    i = 1
    while i <= N:
        c = (a+b)/2
        if abs(f(c)) < eps:
            print(f"Solusi ditemukan pada iterasi ke-{i}: x = {c}")
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
        print(f"Iterasi ke-{i}: x = {c}")
        i += 1
    print("Metode biseksi gagal: batas iterasi maksimum tercapai")
    return None

# contoh penggunaan dengan batas 9
a = -1
b = 0
eps = 0.001
bisection(a, b, eps, N=9)


    