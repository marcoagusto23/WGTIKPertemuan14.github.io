def read_data(filename):
    data_barang = []
    f = open(filename, 'r')
    for line in f:
        row = line.split()
        produksi = [int(i) for i in row[-8:][::2]]
        penjualan = [int(i) for i in row[-8:][1::2]]
        if len(row) > 9:
            row[0] = row[0] + ' ' + row[1]
        data_barang.append({row[0]: [produksi, penjualan]})
    return data_barang

def peningkatan(data):
    daftar_increase = []
    for item in data:
        for k, v in item.items():
            L = item[k][0]
            if all(x<y for x, y in zip(L, L[1:])) == True:
                daftar_increase.append(k)
    return daftar_increase

def report(data, nama):
    for item in data:
        for k, v in item.items():
            if k == nama:
                L = item[k][1]
                mean = sum(L)/len(L)
                return mean

def main():
    while True:
        data = read_data('input.txt')
        print('Selamat datang di dasbor gudang!\nApa yang ingin anda lakukan?\n1. Cek peningkatan produksi\n2. Cek report produk\n3. Keluar')
        uInput = input('Pilihan anda: ')
        if uInput == '1':
            result = peningkatan(data)
            if result == []:
                print('Tidak ada barang yang mengalami peningkatan produksi secara konstan')
            else:
                print(result)
            input('Tekan apapun untuk melanjutkan...')
        elif uInput == '2':
            print('Barang mana yang ingin anda cek?\nPilihan: ')
            for item in data:
                print(*item.keys())
            uItemPilih = input('Ketikkan salah satu nama dari barang yang tersedia di atas (case sensitive): ')
            print(f'Rata-rata penjualan untuk item {uItemPilih}: {report(data, uItemPilih)}')
            input('Tekan apapun untuk melanjutkan...')
        elif uInput == '3':
            exit()
        else:
            return 'Ada kesalahan dalam input anda.'

main()
