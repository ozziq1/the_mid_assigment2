# Class utama: Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")

# Subclass: MahasiswaS1 (menggunakan inheritance dari class Mahasiswa)
class MahasiswaS1(Mahasiswa):
    def __init__(self, nama, nim, jurusan, semester):
        # Memanggil constructor dari superclass Mahasiswa
        super().__init__(nama, nim, jurusan)
        self.semester = semester

    def tampilkan_info(self):
        # Memanggil method tampilkan_info dari superclass
        super().tampilkan_info()
        print(f"Semester: {self.semester}")

# Contoh penggunaan
mahasiswa1 = Mahasiswa("Dina", "210001", "Teknik Informatika")
mahasiswa1.tampilkan_info()

print("\n")

mahasiswa_s1 = MahasiswaS1("Aldo", "220002", "Teknik Elektro", 5)
mahasiswa_s1.tampilkan_info()
