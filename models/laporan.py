class Laporan:
    def __init__(self):
        self.rapor_siswa = []   
        self.data_spp = []      
        self.data_gaji = []     

    # BAGIAN RAPOR (Nilai Siswa)
    def buat_rapor(self, id_siswa, nama, kelas, daftar_guru):
        nilai_mapel = {}

        # Ambil nilai dari semua guru
        for guru in daftar_guru:
            if id_siswa in getattr(guru, "nilai_siswa", {}):
                nilai_mapel[guru.mapel] = guru.nilai_siswa[id_siswa]

        if not nilai_mapel:
            print(f"[!] Tidak ada nilai ditemukan untuk siswa {nama} ({id_siswa}).")
            return False

        rata2 = sum(nilai_mapel.values()) / len(nilai_mapel)
        predikat = self.hitung_predikat(rata2)
        keterangan = "Lulus" if rata2 >= 70 else "Tidak Lulus"

        # cek apakah rapor sudah ada -> update, bukan duplikat
        for r in self.rapor_siswa:
            if r["id_siswa"] == id_siswa:
                r.update({
                    "nama": nama,
                    "kelas": kelas,
                    "nilai_mapel": nilai_mapel,
                    "rata_rata": rata2,
                    "predikat": predikat,
                    "keterangan": keterangan
                })
                print(f"[i] Rapor untuk {nama} ({id_siswa}) di-update.")
                return True

        # jika belum ada
        self.rapor_siswa.append({
            "id_siswa": id_siswa,
            "nama": nama,
            "kelas": kelas,
            "nilai_mapel": nilai_mapel,
            "rata_rata": rata2,
            "predikat": predikat,
            "keterangan": keterangan
        })
        print(f"[i] Rapor untuk {nama} ({id_siswa}) dibuat.")
        return True

    def lihat_semua_rapor(self):
        return list(self.rapor_siswa)

    def lihat_rapor_siswa(self, id_siswa):
        for r in self.rapor_siswa:
            if r["id_siswa"] == id_siswa:
                return r
        return None

    def hapus_rapor(self, id_siswa):
        awal = len(self.rapor_siswa)
        self.rapor_siswa = [r for r in self.rapor_siswa if r["id_siswa"] != id_siswa]
        berhasil = len(self.rapor_siswa) < awal
        if berhasil:
            print(f"[i] Rapor siswa {id_siswa} dihapus.")
        return berhasil

    def hitung_predikat(self, nilai):
        if nilai >= 90:
            return "A"
        elif nilai >= 80:
            return "B"
        elif nilai >= 70:
            return "C"
        elif nilai >= 60:
            return "D"
        else:
            return "E"

    # BAGIAN SPP SISWA
    def tambah_spp(self, id_siswa, nama, jumlah, bulan, status="Belum Bayar"):
        self.data_spp.append({
            "id_siswa": id_siswa,
            "nama": nama,
            "bulan": bulan,
            "jumlah": jumlah,
            "status": status
        })
        print(f"[i] SPP ditambahkan: {nama} {bulan} Rp{jumlah} ({status})")
        return True

    def lihat_spp(self):
        return list(self.data_spp)

    def ubah_status_spp(self, id_siswa, bulan, status_baru):
        for spp in self.data_spp:
            if spp["id_siswa"] == id_siswa and spp["bulan"] == bulan:
                spp["status"] = status_baru
                print(f"[i] Status SPP {spp.get('nama','(nama?)')} bulan {bulan} diubah menjadi {status_baru}.")
                return True
        print(f"[!] Data SPP untuk {id_siswa} bulan {bulan} tidak ditemukan.")
        return False

    def hapus_spp(self, id_siswa, bulan):
        awal = len(self.data_spp)
        self.data_spp = [
            spp for spp in self.data_spp
            if not (spp["id_siswa"] == id_siswa and spp["bulan"] == bulan)
        ]
        berhasil = len(self.data_spp) < awal
        if berhasil:
            print(f"[i] SPP siswa {id_siswa} bulan {bulan} dihapus.")
        return berhasil

    # BAGIAN GAJI GURU / PEGAWAI
    def tambah_gaji(self, id_guru, nama, gaji_pokok, tunjangan=0, jabatan_tambahan=None):
        total_gaji = gaji_pokok + tunjangan
        self.data_gaji.append({
            "id_guru": id_guru,
            "nama": nama,
            "gaji_pokok": gaji_pokok,
            "tunjangan": tunjangan,
            "jabatan_tambahan": jabatan_tambahan,
            "total_gaji": total_gaji
        })
        print(f"[i] Gaji ditambahkan: {nama} Rp{total_gaji} (pokok {gaji_pokok} + tunjangan {tunjangan})")
        return True

    def lihat_gaji(self):
        return list(self.data_gaji)

    def ubah_gaji(self, id_guru, gaji_pokok_baru=None, tunjangan_baru=None):
        for g in self.data_gaji:
            if g["id_guru"] == id_guru:
                if gaji_pokok_baru is not None:
                    g["gaji_pokok"] = gaji_pokok_baru
                if tunjangan_baru is not None:
                    g["tunjangan"] = tunjangan_baru
                g["total_gaji"] = g["gaji_pokok"] + g["tunjangan"]
                print(f"[i] Gaji {g['nama']} diperbarui: total Rp{g['total_gaji']}")
                return True
        print(f"[!] Data gaji untuk id_guru {id_guru} tidak ditemukan.")
        return False

    def hapus_gaji(self, id_guru):
        awal = len(self.data_gaji)
        self.data_gaji = [g for g in self.data_gaji if g["id_guru"] != id_guru]
        berhasil = len(self.data_gaji) < awal
        if berhasil:
            print(f"[i] Data gaji untuk id_guru {id_guru} dihapus.")
        return berhasil
