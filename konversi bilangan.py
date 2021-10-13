# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:37:25 2021

@author: User
"""
import sys
pilih = 0
while pilih ==0:

    print("---PROGRAM KONVERSI BILANGAN---")
    print("1. -> Desimal ke Biner\t\n2. -> Biner ke Desimal\t\n3. -> Exit\t")

    pilih1 = int(input("Silahkan pilih Menu : "))
    if pilih1 == 1 :
       desimal = int(input("Masukkan Bilangan Desimal : "))
       hasil = ""
       while (desimal) != 0:
           hasil += ("%d" % (desimal % 2))
           desimal //=2
           hasilakhir = ""
           for i in range(len(hasil)-1,-1,-1):
               hasilakhir += hasil[i]
               print("Nilai Binernya Adalah : ",hasilakhir)
    elif pilih1 == 2 :
        biner = input("Masukkan Bilangan Biner : ")
        desimal = 0 
        pangkat = len(biner)-1

        for i in range(len(biner)):
            idesimal = int(biner[i]) *2 ** pangkat
            desimal += idesimal
            pangkat -= 1
        print("Bilangan Desimalnya Adalah : ",desimal)
    
    elif pilih1 ==3 :
        print("Terima Kasih sudah menggunakan Program ini !") 
        sys.exit(0)
