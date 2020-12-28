# mysqltomongo
MySQLtoMongo merupakan aplikasi untuk melakukan migrasi database dari MySQl ke database MongoDB. Aplikasi ini dibangun menggunakan bahasa pemograman Python versi 3.X.

## Requirement
* Python 3.X
* MySQl Connector Python: pip install mysql-connector-python
* Mongo Connector Python: pip install pymongo

## Versions
Pengembangan dilakukan secara bertahap dan di bedakan menjadi beberapa versi:

### Version 1
Pengembangan aplikasi migrasi versi 1 difokuskan pada kemampuan migrasi 1 table pada database MySQl menjadi sebuah collection di database MongoDB. Pengembangan versi 1 ini dilakukan berdasarkan penelitian:\\
*M. N. Y. Utomo and R. Nur, "Migrasi Table Basis Data Relasional ke Collection Basis Data NoSQL dengan Teknik Transformasi Data," Seminar Nasional Hasil Penelitian & Pengabdian Kepada Masyarakat, SNP2M 2020, pp. 23-28, 2020.*\\
Paper URL: [Article](http://jurnal.poliupg.ac.id/index.php/snp2m/article/view/2381)

### Version 2
Pengembangan aplikasi migrasi versi 2 dengan fokus agar aplikasi dapat melakukan migrasi semua table pada sebuah database MySQl ke database MongoDB, proses deteksi jumlah table dilakukan dengan memanfaatkan metadata SQL. Pengembangan ini merujuk penelitian:\\
*M. N. Y. Utomo, "Pengembangan Model Migrasi Database Relational ke NoSQL Memanfaatkan Metadata SQL," Jurnal Teknologi Elekterika, vol. 17, no. 2, pp. 1-6, 2020.*\\
Jurnal URL: [Article](http://jurnal.poliupg.ac.id/index.php/JTE/article/view/2212) 