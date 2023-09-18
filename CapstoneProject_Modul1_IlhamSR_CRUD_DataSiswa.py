# Data siswa
data_siswa = [
    {"NIS": 101, "Nama": "Sinta", "Kelas": 'JCDS', "Nama Lecturer" : "Muhammad Reza", "Nomor Telepon": "08123456798", "Email Siswa" : "sinta@gmail.com", "Nilai Akhir": 90},
    {"NIS": 102, "Nama": "Zee", "Kelas": 'JCDM', "Nama Lecturer" : "Fikri Hasan","Nomor Telepon": "08123456799", "Email Siswa" : "zee@gmail.com","Nilai Akhir": 95},
    {"NIS": 103, "Nama": "Bob", "Kelas": 'JCWD', "Nama Lecturer" : "Aji Setiadji","Nomor Telepon": "08123456800", "Email Siswa" : "bob@gmail.com","Nilai Akhir": 89},
    {"NIS": 104, "Nama": "Yogi", "Kelas": 'JCDS', "Nama Lecturer" : "Muhammad Reza","Nomor Telepon": "08964895781", "Email Siswa" : "yogi@gmail.com","Nilai Akhir": 92},
    {"NIS": 105, "Nama": "Ambar", "Kelas": 'JCWD', "Nama Lecturer" : "Aji Setiadji","Nomor Telepon": "089987651923", "Email Siswa" : "ambar@gmail.com","Nilai Akhir": 96}
]

# Fungsi untuk mencari data siswa berdasarkan NIS
def cari_data_siswa(nis_cari):
    for siswa in data_siswa:
        if siswa['NIS'] == nis_cari:
            return siswa
    return None

# Fungsi untuk menampilkan data siswa dalam format tabel
def tampilkan_data_siswa(data=None):
    if not data:
        data = data_siswa

    while True:
        print("\n=============== Menu Tampilkan Data Siswa ===============")
        print("1. Tampilkan Data Siswa Tanpa Pengurutan")
        print("2. Mengurutkan Berdasarkan NIS")
        print("3. Mengurutkan Berdasarkan Nama")
        print("4. Mengurutkan Berdasarkan Kelas")
        print("5. Cari Data Siswa")
        print("6. Kembali ke Menu Utama")

        submenu = input("Pilih submenu [1-6]: ")

        if submenu == "1":
            tampilkan_data_siswa_tanpa_pengurutan(data)
        elif submenu == "2":
            urutkan_data_siswa_nis(data)
        elif submenu == "3":
            urutkan_data_siswa_nama(data)
        elif submenu == "4":
            urutkan_data_siswa_kelas(data)
        elif submenu == "5":
            cari_data_siswa_menu(data)
        elif submenu == "6":
            break
        else:
            print("Pilihan tidak valid. Tolong pilih submenu yang benar.")

# Fungsi untuk menampilkan data siswa tanpa pengurutan
def tampilkan_data_siswa_tanpa_pengurutan(data):
    print("\nData Siswa Tanpa Pengurutan:")
    print()
    # Tampilkan header tabel
    print('+--------------------------------------------------------------------------------------------------------------------+')
    print(f"| {'NIS':<5} | {'Nama':<15} | {'Kelas':<10} | {'Nomor Telepon':<15} | {'Email Siswa':<20} | {'Nama Lecturer':<20} | {'Nilai Akhir':<10} |")
    print("-" * 117)  # Perbarui panjang garis pemisah

    # Tampilkan data siswa dalam bentuk tabel
    for siswa in data:
        nis = siswa['NIS']
        nama = siswa['Nama']
        kelas = siswa['Kelas']
        nomor_telepon = siswa['Nomor Telepon']
        email_siswa = siswa['Email Siswa']
        nama_lecturer = siswa['Nama Lecturer']
        nilai_akhir = siswa['Nilai Akhir']
        print(f"| {nis:<5} | {nama:<15} | {kelas:<10} | {nomor_telepon:<15} | {email_siswa:<20} | {nama_lecturer:<20} | {nilai_akhir:<10} |")
        print('+', '-' * 113, '+')

# Fungsi untuk menampilkan menu pencarian data siswa
def cari_data_siswa_menu(data):
    while True:
        print("\n=============== Menu Pencarian Data Siswa ===============")
        print("1. Cari berdasarkan NIS")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Kelas")
        print("4. Kembali ke Menu Tampilkan Data Siswa")

        submenu = input("Pilih submenu pencarian [1-4]: ")

        if submenu == "1":
            nis_cari = input("Masukkan NIS yang ingin dicari: ")
            if not nis_cari.isdigit():
                print("NIS harus berupa angka.")
                continue

            nis_cari = int(nis_cari)
            hasil_pencarian = cari_data_siswa(nis_cari)

            if hasil_pencarian:
                tampilkan_data_siswa_tanpa_pengurutan([hasil_pencarian])
            else:
                print("Data siswa dengan NIS tersebut tidak ditemukan.")
        elif submenu == "2":
            nama_cari = input("Masukkan Nama yang ingin dicari: ")
            if not nama_cari.isalpha():
                print("Nama harus berupa huruf.")
                continue

            hasil_pencarian = cari_data_siswa_berdasarkan_nama(nama_cari, data)

            if hasil_pencarian:
                tampilkan_data_siswa_tanpa_pengurutan(hasil_pencarian)
            else:
                print("Data siswa dengan Nama tersebut tidak ditemukan.")
        elif submenu == "3":
            kelas_cari = input("Masukkan Kelas yang ingin dicari: ")
            if not kelas_cari.isalpha():
                print("Kelas harus berupa huruf.")
                continue

            hasil_pencarian = cari_data_siswa_berdasarkan_kelas(kelas_cari, data)

            if hasil_pencarian:
                tampilkan_data_siswa_tanpa_pengurutan(hasil_pencarian)
            else:
                print("Data siswa dengan Kelas tersebut tidak ditemukan.")
        elif submenu == "4":
            break
        else:
            print("Pilihan tidak valid. Tolong pilih submenu pencarian yang benar.")

# Fungsi pencarian data siswa berdasarkan NIS
def cari_data_siswa(nis_cari):
    for siswa in data_siswa:
        if siswa['NIS'] == nis_cari:
            return siswa

# Fungsi pencarian data siswa berdasarkan Nama
def cari_data_siswa_berdasarkan_nama(nama_cari, data):
    hasil_pencarian = []
    for siswa in data:
        if siswa['Nama'].lower() == nama_cari.lower():
            hasil_pencarian.append(siswa)
    return hasil_pencarian

# Fungsi pencarian data siswa berdasarkan Kelas
def cari_data_siswa_berdasarkan_kelas(kelas_cari, data):
    hasil_pencarian = []
    for siswa in data:
        if siswa['Kelas'].lower() == kelas_cari.lower():
            hasil_pencarian.append(siswa)
    return hasil_pencarian

# Fungsi untuk mengurutkan data siswa berdasarkan NIS
def urutkan_data_siswa_nis(data=None):
    if not data:
        print("Belum Ada Data Siswa.")
        return

    data_siswa_urut = sorted(data, key=lambda x: x['NIS'])
    print("\nData Siswa (Urut berdasarkan NIS):")
    tampilkan_data_siswa_tanpa_pengurutan(data_siswa_urut)

# Fungsi untuk mengurutkan data siswa berdasarkan Nama
def urutkan_data_siswa_nama(data=None):
    if not data:
        print("Belum Ada Data Siswa.")
        return

    data_siswa_urut = sorted(data, key=lambda x: x['Nama'])
    print("\nData Siswa (Urut berdasarkan Nama):")
    tampilkan_data_siswa_tanpa_pengurutan(data_siswa_urut)

# Fungsi untuk mengurutkan data siswa berdasarkan Kelas
def urutkan_data_siswa_kelas(data=None):
    if not data:
        print("Belum Ada Data Siswa.")
        return

    data_siswa_urut = sorted(data, key=lambda x: x['Kelas'])
    print("\nData Siswa (Urut berdasarkan Kelas):")
    tampilkan_data_siswa_tanpa_pengurutan(data_siswa_urut)


# Fungsi untuk menambahkan data siswa baru
def tambah_data_siswa():
    while True:
        nis = input("Masukkan NIS Siswa: ")

        if not nis.isdigit() or len(nis) != 3 or not nis.startswith('1'):
            print("NIS harus berupa angka, dimulai dengan '1', dan memiliki 3 digit.")
            continue

        nis = int(nis)

        if any(siswa["NIS"] == nis for siswa in data_siswa):
            print("NIS sudah ada dalam data. Tambahkan NIS yang berbeda.")
            continue

        nama = input("Masukkan Nama Siswa: ").title()
        if not nama.replace(" ", "").isalpha():
            print("Nama Siswa harus berupa huruf.")
            continue

        kelas = input("Masukkan Kelas Siswa: ").upper()
        if not kelas.isalpha():
            print("Kelas harus berupa huruf.")
            continue

        nomor_telepon = input("Masukkan Nomor Telepon: ")
        if nomor_telepon.startswith('08') and nomor_telepon.isdigit() and len(nomor_telepon) <= 13:
            pass
        else:
            print("Nomor Telepon tidak valid. Pastikan dimulai dengan '08', inputan berupa angka, dan kurang dari atau sama dengan 13 digit")
            continue

        email_siswa = input("Masukkan Email Siswa: ")
        nama_lecturer = input("Masukkan Nama Lecturer: ").title()
        if not nama_lecturer.replace(" ", "").isalpha():
            print("Nama Lecturer harus berupa huruf.")
            continue

        while True:
            nilai_akhir = input("Masukkan Nilai Akhir: ")
            if not nilai_akhir.replace('.', '', 1).isdigit():
                print("Nilai Akhir harus berupa angka.")
                continue

            nilai_akhir = int(nilai_akhir)
            if 0 <= nilai_akhir <= 100:
                break
            else:
                print("Nilai Akhir harus berada dalam rentang 0 hingga 100.")
                continue

        siswa_baru = {
            "NIS": nis,
            "Nama": nama,
            "Kelas": kelas,
            "Nomor Telepon": nomor_telepon,
            "Email Siswa": email_siswa,
            "Nama Lecturer": nama_lecturer,
            "Nilai Akhir": nilai_akhir
        }

        data_siswa.append(siswa_baru)
        print("Data Siswa Berhasil Ditambahkan!")
        break

# Fungsi untuk mengubah data siswa
def ubah_data_siswa():
    while True:
        nis_input = input("Masukkan NIS Siswa yang ingin diubah: ")

        if not nis_input.isdigit() or len(nis_input) != 3 or not nis_input.startswith('1'):
            print("NIS harus berupa integer, dimulai dari angka '1', dan memiliki 3 digit.")
            continue

        nis = int(nis_input)
        siswa_ditemukan = cari_data_siswa(nis)

        if siswa_ditemukan:
            while True:
                nama_baru = input("Masukkan Nama Baru: ").title()
                if not nama_baru.replace(" ", "").isalpha():
                    print("Nama Siswa harus berupa huruf.")
                    continue
                else:
                    break

            while True:
                kelas_baru = input("Masukkan Kelas Baru: ").upper()
                if not kelas_baru.isalpha():
                    print("Kelas harus berupa huruf.")
                    continue
                else:
                    break

            while True:
                nomor_telepon_baru = input("Masukkan Nomor Telepon Baru: ")
                if nomor_telepon_baru.startswith('08') and nomor_telepon_baru.isdigit() and len(nomor_telepon_baru) <= 13:
                    break
                else:
                    print("Nomor Telepon tidak valid. Pastikan dimulai dengan '08' dan kurang dari atau sama dengan 13 digit.")
                    continue

            email_siswa_baru = input("Masukkan Email Siswa Baru: ")

            while True:
                nama_lecturer_baru = input("Masukkan Nama Lecturer Baru: ").title()
                if not nama_lecturer_baru.replace(" ", "").isalpha():
                    print("Nama Lecturer harus berupa huruf.")
                    continue
                else:
                    break

            while True:
                nilai_akhir_baru = input("Masukkan Nilai Akhir Baru: ")
                if not nilai_akhir_baru.replace('.', '', 1).isdigit():
                    print("Nilai Akhir harus berupa angka.")
                    continue

                nilai_akhir_baru = int(nilai_akhir_baru)

                if 0 <= nilai_akhir_baru <= 100:
                    break
                else:
                    print("Nilai Akhir harus berada dalam rentang 0 hingga 100.")
                    continue

            siswa_ditemukan["Nama"] = nama_baru
            siswa_ditemukan["Kelas"] = kelas_baru
            siswa_ditemukan["Nomor Telepon"] = nomor_telepon_baru
            siswa_ditemukan["Email Siswa"] = email_siswa_baru
            siswa_ditemukan["Nama Lecturer"] = nama_lecturer_baru
            siswa_ditemukan["Nilai Akhir"] = nilai_akhir_baru

            print("Data Siswa Berhasil Diubah!")
            return
        else:
            print(f"Tidak ada data siswa dengan NIS {nis}.")


# Fungsi untuk menghapus data siswa
def hapus_data_siswa():
    while True:
        print("\nMenu Hapus Data Siswa:")
        print("1. Hapus Data Siswa Individu")
        print("2. Hapus Semua Data Siswa")
        print("3. Kembali ke Menu Utama")
        submenu = input("Pilih submenu [1-3]: ")

        if submenu == "1":
            nis_input = input("Masukkan NIS Siswa yang ingin dihapus: ")

            if not nis_input.isdigit() or len(nis_input) != 3 or not nis_input.startswith('1'):
                print("NIS harus berupa integer, dimulai dari angka '1', dan memiliki 3 digit.")
                continue

            nis = int(nis_input)
            siswa_ditemukan = cari_data_siswa(nis)

            if siswa_ditemukan:
                data_siswa.remove(siswa_ditemukan)
                print(f"Data Siswa dengan NIS {nis} Berhasil Dihapus.")
            else:
                print(f"Tidak ada data siswa dengan NIS {nis}.")
        elif submenu == "2":
            while True:
                konfirmasi = input("Anda yakin ingin menghapus semua data siswa? (Y/N): ").strip().upper()
                if konfirmasi == "Y":
                    data_siswa.clear()
                    print("Semua Data Siswa Berhasil Dihapus.")
                    break
                elif konfirmasi == "N":
                    print("Penghapusan semua data siswa dibatalkan.")
                    break
                else:
                    print("Pilihan hanya bisa Y atau N. Silakan coba lagi.")
        elif submenu == "3":
            break
        else:
            print("Pilihan tidak valid. Tolong pilih submenu yang benar.")

# Main program
while True:
    print('********************************************************')
    print('')
    print(' Nama    : Ilham Syaeful Reza')
    print(' Topik   : Program CRUD Data Siswa Sekolah Digital')
    print(' Kelas   : Job Connector Data Science (Batch 2 Bandung)')
    print("\n=============== Menu Utama ===============")
    print("1. Tampilkan Data Siswa")
    print("2. Tambah Data Siswa")
    print("3. Ubah Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Keluar")
    pilihan = input("Pilih menu [1-5]: ")

    if pilihan == "1":
        tampilkan_data_siswa()
    elif pilihan == "2":
        tambah_data_siswa()
    elif pilihan == "3":
        ubah_data_siswa()
    elif pilihan == "4":
        hapus_data_siswa()
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini. Semoga harimu menyenangkan!")
        break
    else:
        print("Pilihan tidak valid. Tolong pilih menu yang benar.")