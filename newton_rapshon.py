#import libarary
import numpy as np
import matplotlib.pyplot as plt

#masukkan nilai galat, dan Maximum Iterasi
fungsi_x = input("\nMasukkan persamaan fungsi x: ")
turunan_fungsi_x = input("Masukkan turunan fungsi x: ")
a = float(input("Masukkan nilai x0: "))  # a = x0 atau xn
galat = float(input("Masukkan nilai galat: "))
MaxIterasi = int(input("Masukkan nilai maksimum iterasi: "))

def f(x):
    return eval(fungsi_x) #masukkan f(x)

def df(x):
    return eval(turunan_fungsi_x) #masukkan turunan dari f(x)

## ALGORITMA NEWTON RAPSHON
#   1. Hitung turunan dari f(x)
#   2. Asumsikan nilai awal x0, sehingga diperoleh barisan nilai x0,x1,x2,x3,... yang diharapkan konvergen ke akarnya
#   3. Rumus xn+1 adalah b = a-(f(a)/df(a))
#   4. Jika |xn+1 - xn| < galat, iterasi selesai, solusi hampiran akar adalah xr+1

def newton_rapshon(f, df, a, MaxIterasi):
    print("\n--------------------------------------------------------------")
    print("| n |    xn    |   xn+1  |  f(xn)  |   f'(xn)  | |xn+1 - xn| |")
    print("--------------------------------------------------------------")
    for i in range(MaxIterasi):
        b = a-(f(a)/df(a))  # b = xn+1
        print('|{:3}|{:=10.5f}|{:=9.5f}|{:=9.5f}|{:=11.5f}|{:>13.5f}|'.format(i+1, a, b, f(a), df(a), abs(b-a)))
        
        #print(i+1, "\t", format(a,".5f"), "\t", format(b,".5f"), "\t", format(f(a),".5f"), "\t", format(df(a),".5f"), "\t", format(abs(b-a),".9f"))
        if abs(b-a) < galat:
            break
        else:
            a = b
    else:
        print("Sudah memenuhi batas iterasi maksimum!")
    return b

jawaban = newton_rapshon(f, df, a, MaxIterasi)

print("--------------------------------------------------------------")
print("\nAkar persamaannya adalah", jawaban)
print("\nDengan nilai galat: ", galat)

x = np.linspace(0, a, 100)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, f(x), 'b')
ax.text(jawaban-0.01, 0.1, jawaban)
ax.plot(x, np.zeros(x.shape), 'r--')
ax.grid()
plt.show()
