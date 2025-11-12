class Siswa:
    def __init__(self, id_siswa, nama, kelas):
        self.id_siswa = id_siswa
        self.nama = nama
        self.kelas = kelas

    def tampilkan_data(self):
        print(f"ID: {self.id_siswa}, Nama: {self.nama}, Kelas: {self.kelas}")
