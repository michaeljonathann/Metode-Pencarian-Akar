#import libarary
import numpy as np
import matplotlib.pyplot as plt

#masukkan nilai galat, dan Maximum Iterasi
fungsi_f_x = input("\nMasukkan persamaan fungsi f(x): ")
fungsi_g_x = input("Masukkan persamaan fungsi g(x): ")
a = float(input("Masukkan nilai x0: "))  # a = x0 atau xr
galat = float(input("Masukkan nilai galat: "))
MaxIterasi = int(input("Masukkan nilai maksimum iterasi: "))

def f(x):
    return eval(fungsi_f_x) #masukkan f(x)

def g(x):
    return eval(fungsi_g_x) 

## ALGORITMA ITERASI TITIK TETAP
#   1. Definisikan xr+1 = g(xr)
#   2. Asumsikan nilai awal x0, sehingga diperoleh barisan nilai x0,x1,x2,x3,... yang diharapkan konvergen ke akarnya
#   3. Jika |xr+1 - xr| < galat, iterasi selesai, solusi hampiran akar adalah xr+1

def titik_tetap(g, a, MaxIterasi):
    print("\n----------------------------------------")
    print("| n |     xr   |   xr+1  | |xr+1 - xr| |")
    print("----------------------------------------")
    for i in range(MaxIterasi):
        b = g(a)    # b = xr+1
        print('|{:3}|{:=10.5f}|{:=9.5f}|{:>13.5f}|'.format(i+1, a, b, abs(b-a)))
        
        #print(i+1, "\t", format(a,".5f"), "\t", format(b,".5f"), "\t", format(abs(b-a),".9f"))
        if abs(b-a) < galat:
            break
        else:
            a = b
    else:
        print("Sudah memenuhi batas iterasi maksimum!")
    return b

jawaban = titik_tetap(g, a, MaxIterasi)

print("----------------------------------------")
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


