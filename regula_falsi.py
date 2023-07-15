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

## ALGORITMA REGULA FALSI
#   1. c = b-(f(b)*(b-a)/(f(b)-f(a)))
#   2. Jika |f(c)| <= galat, maka iterasi berhenti dan c adalah akar persamaan
#   3. Jika f(a)*f(c) <= 0, maka b=c lainnya a=c

def regula_falsi(f, a, b, MaxIterasi):
    if f(a)*f(b) > 0:
        print("Tidak memiliki akar persamaan!")
    else:
        print("\n-----------------------------------------------------------------------------")
        print("| n |    a    |    b    |    c    |   |f(c)|  |   f(a)  |   f(b)  |   f(c)  |")
        print("-----------------------------------------------------------------------------")
        for i in range(MaxIterasi):
            c = b-(f(b)*(b-a)/(f(b)-f(a)))
            print('|{:3}|{:=9.5f}|{:=9.5f}|{:=9.5f}|{:=11.6f}|{:=9.5f}|{:>9.5f}|{:>9.5f}|'.format(i+1, a, b, c, abs(f(c)), f(a), f(b), f(c)))
            if abs(f(c)) <= galat:
                break
            elif f(a)*f(c) <= 0:
                b=c
            else:
                a=c
        else:
            print("Sudah memenuhi batas iterasi maksimum!")
        return c

jawaban = regula_falsi(f, a, b, MaxIterasi)

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
