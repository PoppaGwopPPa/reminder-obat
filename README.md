 Reminder Minum Obat

Aplikasi web sederhana untuk membantu mengingat jadwal konsumsi obat harian. Dibangun menggunakan **Flask**, **SQLite**, dan **Docker**, serta dilengkapi fitur notifikasi visual dan suara saat waktu minum obat tiba.

 Fitur Utama

 Tambah, edit, dan hapus data obat
 Notifikasi waktu minum obat berbasis jam lokal browser
 notifikasi suara menggunakan JavaScript
 Siap dijalankan menggunakan Docker dan Docker Compose Tampilan responsif dengan Tailwind CSS

Tampilan Antarmuka

> Tambahkan screenshot nanti di sini:
- Form Tambah Obat
- Tabel Obat
- Notifikasi + Suara

 Teknologi yang Digunakan

| Teknologi     | Keterangan                         |
|---------------|-------------------------------------|
| Python        | Bahasa backend                     |
| Flask         | Framework web ringan               |
| SQLite        | Database lokal ringan              |
| Tailwind CSS  | Styling antarmuka web              |
| JavaScript    | Notifikasi waktu + audio           |
| Docker        | Containerisasi aplikasi            |


 Struktur Direktori
reminder-obat/
├── app.py
├── init_db.py
├── database.db
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── templates/
│ ├── index.html
│ └── edit.html
├── static/
│ └── alarm.mp3

Akses di browser:
http://localhost:5000

Jalankan dengan Docker
docker-compose up --build

Nama: Bintang Bimantara Putra
NIM : 32602300019
Mata Kuliah: Cloud Computing
Dosen Pengampu: Sam Farisa Chaerul Haviana, ST., M.Kom



