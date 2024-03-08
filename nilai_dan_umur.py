print("Selamat datang di Form Pendaftaran Universitas")

nama = input("Nama: ")
tempat_lahir = input("Tempat Lahir: ")
tanggal_lahir = input("Tanggal Lahir (DD/MM/YYYY): ")
tahun_lahir = input("Tahun Lahir (YYYY): ")
nilai_bing = float(input("Nilai Bahasa Inggris: "))
nilai_mtk = float(input("Nilai Matematika: "))
nilai_bindo = float(input("Nilai Bahasa Indonesia: "))
jenis_kelamin = input("Jenis Kelamin (Laki-laki/Perempuan): ")

rata_rata_nilai = (nilai_bing + nilai_mtk + nilai_bindo) / 3
print("\nData yang telah diinput:")
print(f"Nama: {nama}")
print(f"Tempat Lahir: {tempat_lahir}")
print(f"Tanggal Lahir: {tanggal_lahir}")
print(f"Tahun Lahir: {tahun_lahir}")
print(f"Nilai Bahasa Inggris: {nilai_bing}")
print(f"Nilai Matematika: {nilai_mtk}")
print(f"Nilai Bahasa Indonesia: {nilai_bindo}")
print(f"Jenis Kelamin: {jenis_kelamin}")

if rata_rata_nilai >= 80 and jenis_kelamin.lower() == "laki-laki":
    print("\nSaran Jurusan: Jurusan Teknik Informatika")
elif rata_rata_nilai >= 80 and jenis_kelamin.lower() == "perempuan":
    print("\nSaran Jurusan: Jurusan Sistem Informasi")
else:
    print("\nSaran Jurusan: Jurusan Desain Komunikasi Visual (DKV)")
