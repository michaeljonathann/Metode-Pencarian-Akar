#import libarary
import numpy as np
import matplotlib.pyplot as plt

#masukkan nilai selang, galat, dan Maximum Iterasi
fungsi_x = input("\nMasukkan persamaan fungsi x: ")
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
galat = float(input("Masukkan nilai galat: "))
MaxIterasi = int(input("Masukkan nilai maksimum iterasi: "))

def f(x):
    return eval(fungsi_x) #masukkan f(x)

## ALGORITMA BISECTION
#   1. c = (a+b)/2
#   2. Jika |b-c| <= galat, maka iterasi berhenti dan c adalah akar persamaan
#   3. Jika f(b)*f(c) <= 0, maka a=c lainnya b=c

def bisection(f, a, b, MaxIterasi):
    if f(a)*f(b) > 0:
        print("Tidak memiliki akar persamaan!")
    else:
        print("\n-----------------------------------------------------------------------------")
        print("| n |    a    |    b    |    c    |   |b-c|   |   f(a)  |   f(b)  |   f(c)  |")
        print("-----------------------------------------------------------------------------")
        for i in range(MaxIterasi):
            c = (a+b)/2
            print('|{:3}|{:=9.5f}|{:=9.5f}|{:=9.5f}|{:=11.6f}|{:=9.5f}|{:>9.5f}|{:>9.5f}|'.format(i+1, a, b, c, abs(b-c), f(a), f(b), f(c)))

            if abs(b-c) <= galat:
                break
            elif f(b)*f(c) <= 0:
                a=c
            else:
                b=c
        else:
            print("Sudah memenuhi batas iterasi maksimum!")
        return c

jawaban = bisection(f, a, b, MaxIterasi)

print("-----------------------------------------------------------------------------")
print("\nAkar persamaannya adalah", jawaban)
print("\nDengan nilai galat: ", galat)

x = np.linspace(a, b, 100)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, f(x), 'b')
ax.text(jawaban-0.01, 0.1, jawaban)
ax.plot(x, np.zeros(x.shape), 'r--')
ax.grid()
plt.show()
