#import libarary
import numpy as np
import matplotlib.pyplot as plt

#masukkan nilai selang, galat, dan Maximum Iterasi
fungsi_x = input("\nMasukkan persamaan fungsi x: ")
a = float(input("Masukkan nilai xn-1: "))  # a = xn-1 atau x0
b = float(input("Masukkan nilai xn: "))  # b = xn atau x
galat = float(input("Masukkan nilai galat: "))
MaxIterasi = int(input("Masukkan nilai maksimum iterasi: "))

def f(x):
    return eval(fungsi_x) #masukkan f(x)

## ALGORITMA SECANT
#   1. Diasumsikan 2 nilai tebakan awal, yaitu x0 dan x1
#   2. Rumus xn+1 adalah c = b-(f(b)*(b-a))/(f(b)-f(a))
#   3. Jika |xn+1 - xn| < galat, iterasi selesai, solusi hampiran akar adalah xr+1

def secant(f, a , b, MaxIterasi):
    print("\n--------------------------------------------------------------------------------------------------")
    print("| n |    xn-1    |    xn    |     xn+1   |   |xn - xn-1| |    f(xn-1)  |   f(xn)   |    f(xn+1)  |")
    print("--------------------------------------------------------------------------------------------------")
    for i in range(MaxIterasi):
        c = b-(f(b)*(b-a))/(f(b)-f(a))    # c = xn+1 atau x2
        print('|{:3}|{:=12.5f}|{:=10.5f}|{:=12.5f}|{:=15.6f}|{:>13.5f}|{:>11.5f}|{:>13.5f}|'.format(i+1, a, b, c, abs(b-a), f(a), f(b), f(c)))
        
        #print(i+1, "\t", format(a,".5f"), "\t", format(b,".5f"), "\t", format(c,".5f"),"\t", format(abs(b-a),".9f"), "\t", format(f(a),".5f"), "\t", format(f(b),".5f"), "\t", format(f(c),".5f"))
        if abs(b-a) < galat:
            break
        else:
            a = b
            b = c
    else:
        print("Sudah memenuhi batas iterasi maksimum!")
    return c

jawaban = secant(f, a, b, MaxIterasi)

print("--------------------------------------------------------------------------------------------------")
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