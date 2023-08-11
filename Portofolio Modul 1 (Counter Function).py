# SYNTAX PEMANGGILAN FUNCTION COUNTER
from collections import Counter

#CONTOH PENGGUNAAN COUNTER
from collections import Counter
List = ['a', 'b', 'b', 'c', 'a', 'r', 'g', 'r', 'd']
print (Counter(List))

#CONTOH PENGGUNAAN LEN
List = ['a', 'b', 'b', 'c', 'a', 'r', 'g', 'r', 'd']
print (len(List))

# SYNTAX DASAR COUNTER
Counter()

# CONTOH PENGGUNAAN COUNTER PADA STRING
Contoh_String = 'Selamat datang di dunia!'
print(Counter(Contoh_String))

# CONTOH PENGGUNAAN COUNTER PADA INTERGER
Contoh_Interger = 1,2,3,4,5
print(Counter(Contoh_Interger))

# CONTOH PENGGUNAAN COUNTER PADA FLOAT
Contoh_Float = 12.4, 25.1, 54.8, 12.4, 12.2, 15.7, 54.8
print(Counter(Contoh_Float))

# CONTOH PENGGUNAAN COUNTER PADA RANGE
Contoh_Range = range(0,5)
print(Counter(Contoh_Range))

# CONTOH PENGGUNAAN COUNTER PADA LIST
Contoh_List = ['Abigail', 'Sarah', 'Dini', 'Dwi', 'Sarah', 'Dini', 'Roy']
print(Counter(Contoh_List))

# CONTOH PENGGUNAAN COUNTER PADA TUPLE
Contoh_Tuple = ('Abigail', 'Sarah', 'Dini', 'Dwi', 'Sarah', 'Dini', 'Roy')
print(Counter(Contoh_Tuple))

# CONTOH PENGGUNAAN COUNTER PADA DICTIONARY
Contoh_Dictionary = {'a':4, 'b':7, 'c':5}
print(Counter(Contoh_Dictionary))
Contoh_Dictionary2 = {'Nama': 'Sarah', 'Umur' : 26, 'Status' : 'Menikah'}
print(Counter(Contoh_Dictionary2))

# CONTOH PENGGUNAAN COUNTER PADA SET
Contoh_Set = {'Abigail', 'Sarah', 'Dini', 'Dwi', 'Sarah', 'Dini', 'Roy'}
print(Counter(Contoh_Set))

#Contoh 1
#Data sebagai berikut:
Data_Penjualan_Toko_A= {'Kopi': 56, 'Teh': 100, 'Lainnya': 400}
Data_Penjualan_Toko_B= {'Kopi': 13, 'Teh': 95, 'Matcha': 30, 'Lainnya': 275}

#Ingin mengetahui total penjualan di toko A dan toko B
Total_Penjualan_Toko_A = Counter(Data_Penjualan_Toko_A)
Total_Penjualan_Toko_B = Counter(Data_Penjualan_Toko_B)
Total_Penjualan_Toko_A.update(Total_Penjualan_Toko_B)
for i,j in Total_Penjualan_Toko_A.items():
    print(f'Total penjualan {i} di Toko A maupun Toko B sebanyak {j} buah')

#Contoh 2
#Data Sebagai berikut:
Dic1 = {'a' : 2, 'b' : 4, 'x' : 7, 'd' : 1, 'w' : 6}
Dic2 = {'e' : 6, 'd' : 13, 'r' : 2, 's' : 1,}

#Ingin mengetahui urutan dari terbesar ke terkecil masing-masing list
Counter_1 = Counter(Dic1)
Counter_2 = Counter(Dic2)
Counter.most_common(Counter_1)
Counter.most_common(Counter_2)
for i,j in Counter_1.items():
    print(f'Jumlah elemen {i} sebanyak {j} buah')
for a,b in Counter_2.items():
    print(f'Jumlah elemen {a} sebanyak {b} buah')