print("----Kelompok 5----")
print("----Management Memory----")
RAM = float (input ("Masukan kapasitas RAM : "))
SisOP = float (input ("Masukan Sistem Operasi : "))
digunakan = float (input ("Masukan memori yang terpakai : "))

tidakterpakai = RAM - (SisOP + digunakan)

print ("RAM yang tak terpakai", tidakterpakai)