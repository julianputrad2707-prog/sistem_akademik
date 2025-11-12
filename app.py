from models.siswa import Siswa
from models.guru import Guru
from models.admin import Admin
from models.laporan import Laporan

print("\n===== PENGUJIAN SISTEM AKADEMIK SEKOLAH =====")

# 1. PENGUJIAN FILE SISWA
print("\n--- PENGUJIAN KELAS SISWA ---")

# Membuat objek siswa
s1 = Siswa("S01", "Tasya", "X RPL 1")
s2 = Siswa("S02", "Bila", "X RPL 1")
s3 = Siswa("S03", "El", "X RPL 1")

# Menampilkan data siswa
print("Data Siswa:")
for s in [s1, s2, s3]:
    s.tampilkan_data()

# 2. PENGUJIAN FILE GURU
print("\n--- PENGUJIAN KELAS GURU ---")

# Membuat objek guru
guru1 = Guru("G01", "Pak Budi", "Matematika")
guru2 = Guru("G02", "Bu Sari", "Bahasa Inggris", jabatan_tambahan="Pembina OSIS")

# Menambah nilai siswa
guru1.tambah_nilai("S01", 85)
guru1.tambah_nilai("S02", 90)
guru2.tambah_nilai("S01", 80)
guru2.tambah_nilai("S02", 88)
guru2.tambah_nilai("S03", 75)

# Menambah absensi siswa
guru1.tambah_absensi("S01", "Hadir")
guru1.tambah_absensi("S02", "Alpha")
guru2.tambah_absensi("S03", "Hadir")

# Melihat nilai dan absensi
print("Data Guru dan Nilai:")
for g in [guru1, guru2]:
    g.tampilkan_data()

# 3. PENGUJIAN FILE ADMIN
print("\n--- PENGUJIAN KELAS ADMIN ---")

admin = Admin()

# Menambah guru ke data admin
admin.tambah_guru(guru1)
admin.tambah_guru(guru2)

# Menambah pegawai
admin.tambah_pegawai("Pak Darto", "Petugas Kebersihan")
admin.tambah_pegawai("Bu Tini", "Administrasi")

# Menambah jadwal pelajaran
admin.tambah_jadwal("Senin", "07.00-08.30", "Matematika", "X RPL 1", "Pak Budi")
admin.tambah_jadwal("Selasa", "09.00-10.30", "Bahasa Inggris", "X RPL 1", "Bu Sari")

# Menampilkan data guru, pegawai, dan jadwal
print("Data Guru:")
for g in admin.data_guru:
    print(f"{g.nama} - {g.mapel} - Jabatan tambahan: {g.jabatan_tambahan}")

print("\nData Pegawai:")
for p in admin.data_pegawai:
    print(f"{p['nama']} - Jabatan: {p['jabatan']}")

print("\nData Jadwal:")
for j in admin.jadwal_pelajaran:
    print(f"{j['hari']} {j['jam']} - {j['mapel']} ({j['kelas']}) oleh {j['guru']}")

# 4. PENGUJIAN FILE LAPORAN
print("\n--- PENGUJIAN KELAS LAPORAN ---")

laporan = Laporan()

# --- Rapor ---
print("\nMembuat Rapor Siswa:")
laporan.buat_rapor("S01", "Tasya", "X RPL 1", admin.data_guru)
laporan.buat_rapor("S02", "Bila", "X RPL 1", admin.data_guru)
laporan.buat_rapor("S03", "El", "X RPL 1", admin.data_guru)

print("Data Rapor:")
for r in laporan.lihat_semua_rapor():
    print(f"{r['nama']} - Rata-rata: {r['rata_rata']} - Predikat: {r['predikat']} - {r['keterangan']}")

# --- SPP ---
print("\nMenambah Data SPP:")
laporan.tambah_spp("S01", "Tasya", 300000, "Januari")
laporan.tambah_spp("S02", "Bila", 300000, "Januari", "Sudah Bayar")
laporan.tambah_spp("S03", "El", 300000, "Januari")

laporan.ubah_status_spp("S01", "Januari", "Sudah Bayar")

print("Data SPP:")
for spp in laporan.lihat_spp():
    print(f"{spp['nama']} - {spp['bulan']} - Rp{spp['jumlah']} ({spp['status']})")

# --- Gaji ---
print("\nMenambah Data Gaji:")
laporan.tambah_gaji("G01", "Pak Budi", 5000000)
laporan.tambah_gaji("G02", "Bu Sari", 5000000, tunjangan=500000, jabatan_tambahan="Pembina OSIS")

laporan.ubah_gaji("G01", gaji_pokok_baru=5200000)

print("Data Gaji Guru:")
for g in laporan.lihat_gaji():
    print(f"{g['nama']} - Total Gaji: Rp{g['total_gaji']} (Tunjangan: Rp{g['tunjangan']})")

# --- Hapus Data ---
print("\nMenghapus Beberapa Data:")
laporan.hapus_rapor("S03")
laporan.hapus_spp("S03", "Januari")
laporan.hapus_gaji("G01")

print("Data Setelah Dihapus:")
print("Rapor:", [r["nama"] for r in laporan.lihat_semua_rapor()])
print("SPP:", [s["nama"] for s in laporan.lihat_spp()])
print("Gaji:", [g["nama"] for g in laporan.lihat_gaji()])

