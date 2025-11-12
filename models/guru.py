class Guru:
    def __init__(self, id_guru, nama, mapel, jabatan_tambahan=None):
        self.id_guru = id_guru
        self.nama = nama
        self.mapel = mapel
        self.jabatan_tambahan = jabatan_tambahan
        self.nilai_siswa = {}  # {id_siswa: nilai}
        self.absensi = {}      # {id_siswa: 'Hadir'/'Alpha'}

    # CRUD Nilai
    def tambah_nilai(self, id_siswa, nilai):
        self.nilai_siswa[id_siswa] = nilai

    def ubah_nilai(self, id_siswa, nilai_baru):
        if id_siswa in self.nilai_siswa:
            self.nilai_siswa[id_siswa] = nilai_baru

    def hapus_nilai(self, id_siswa):
        if id_siswa in self.nilai_siswa:
            del self.nilai_siswa[id_siswa]

    def lihat_nilai(self):
        return self.nilai_siswa

    # CRUD Absensi
    def tambah_absensi(self, id_siswa, status):
        self.absensi[id_siswa] = status

    def lihat_absensi(self):
        return self.absensi

    def tampilkan_data(self):
        print(f"\nData Guru: {self.nama} ({self.mapel})")
        for id_siswa, nilai in self.nilai_siswa.items():
            absen = self.absensi.get(id_siswa, "-")
            print(f"- Siswa {id_siswa}: Nilai = {nilai}, Absensi = {absen}")
