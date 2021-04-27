print("------------------------------------------------------")
print("Fungsi Untuk Menentukan Bilangan Prima Dari 2 Bilangan")
print("------------------------------------------------------")
up = input("Masukkan nilai batas atas  : ")
up = int(up)
down = input("Masukkan nilai batas bawah : ")
down = int(down)
print ("Bilangan prima antara ",down, " dan ",up," adalah :")
a = up
b = down
for c in range (b,a+1):
    if c >1: 
        for i in range(2,c):
            if(c%i) == 0:
                break
        else:
            print(c)
           
print("------------------------------------------------------")