# PERTEMUAN 03 - Tugas Latihan 1 - Selsasa, 28 September 2021
# M. IQBAL ZAYYAN ABIYYU_12210720_Kelas:12.1A.39
# CARA 2
def nilaiTerbesar(bil1, bil2, bil3, bil4):
    if bil1 < bil2 or bil1 < bil3 or bil1 < bil4:
        print("Bilangan Terbesar: ", bil1)
    elif bil2 < bil1 or bil2 < bil3 or bil2 < bil4:
        print("Bilangan Terbesar: ", bil2)
    elif bil3 < bil1 or bil3 < bil2 or bil3 < bil4:
        print("Bilangan Terbesar: ", bil3)
    else:
        print("Bilangan Terbesar: ", bil4)


nilaiTerbesar(60, 20, 100, 40)
nilaiTerbesar(20, 40, 60, 100)
nilaiTerbesar(100, 20, 40, 60)
nilaiTerbesar(40, 100, 20, 60)
