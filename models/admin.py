class Admin:
    def __init__(self):
        self.data_guru = []
        self.data_pegawai = []
        self.jadwal_pelajaran = []

    def tambah_guru(self, guru):
        self.data_guru.append(guru)

    def tambah_pegawai(self, nama, jabatan):
        self.data_pegawai.append({"nama": nama, "jabatan": jabatan})

    def tambah_jadwal(self, hari, jam, mapel, kelas, guru):
        self.jadwal_pelajaran.append({
            "hari": hari,
            "jam": jam,
            "mapel": mapel,
            "kelas": kelas,
            "guru": guru
        })
