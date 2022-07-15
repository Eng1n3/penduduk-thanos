from function import PendudukThanos

if __name__ == "__main__":
    banyak_hari = int(input("Masukkan banyak hari: "))
    penduduk_thanos = PendudukThanos(banyak_hari)
    print(penduduk_thanos.hari_berjalan())
