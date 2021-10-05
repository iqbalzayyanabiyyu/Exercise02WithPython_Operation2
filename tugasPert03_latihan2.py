# PERTEMUAN 03 - Tugas Latihan 2 - Selsasa, 28 September 2021
# M. IQBAL ZAYYAN ABIYYU_12210720_Kelas:12.1A.39
# CARA 2
def jmlKelereng(kelerengAldi):
    kelerengBudi = kelerengAldi - 15
    kelerengAnto = 2 * (kelerengAldi + kelerengBudi)
    kelerengAgung = (kelerengAldi + kelerengBudi + kelerengAnto) - 5

    print("Jumlah Kelereng Budi: ", kelerengBudi)
    print("Jumlah Kelereng Anto: ", kelerengAnto)
    print("Jumlah Kelereng Agung: ", kelerengAgung)


jmlKelereng(int(input("Jumlah Kelereng Aldi: ")))
