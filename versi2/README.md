# mysqltomongo: versi 2
Aplikasi difokuskan agar aplikasi dapat melakukan migrasi semua table pada sebuah database MySQl ke database MongoDB, proses deteksi jumlah table dilakukan dengan memanfaatkan metadata SQL.

## Requirement
* Python 3.X
* MySQl Connector Python: pip install mysql-connector-python
* Mongo Connector Python: pip install pymongo

## Cara Penggunaan
* Import exampledb.sql ke server mysql
* Configurasi koneksi mysql server pada file mysqltomongodb-v2.sql
* Jalankan server MongoDB
* Eksekuasi aplikasi dengan: python mysqltomongodb-v2.sql

## Referensi
*M. N. Y. Utomo, "Pengembangan Model Migrasi Database Relational ke NoSQL Memanfaatkan Metadata SQL," Jurnal Teknologi Elekterika, vol. 17, no. 2, pp. 1-6, 2020.*\
Jurnal URL: [Article](http://jurnal.poliupg.ac.id/index.php/JTE/article/view/2212) 

