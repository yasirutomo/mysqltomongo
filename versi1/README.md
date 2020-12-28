# mysqltomongo: versi 1
Aplikasi difokuskan pada kemampuan migrasi 1 table pada database MySQl menjadi sebuah collection di database MongoDB

## Requirement
* Python 3.X
* MySQl Connector Python: pip install mysql-connector-python
* Mongo Connector Python: pip install pymongo

## Cara Penggunaan
* Import exampledb.sql ke server mysql
* Configurasi koneksi mysql server pada file mysqltomongodb-v1.sql
* Jalankan server MongoDB
* Eksekuasi aplikasi dengan: python mysqltomongodb-v1.sql

## Referensi
*M. N. Y. Utomo and R. Nur, "Migrasi Table Basis Data Relasional ke Collection Basis Data NoSQL dengan Teknik Transformasi Data," Seminar Nasional Hasil Penelitian & Pengabdian Kepada Masyarakat, SNP2M 2020, pp. 23-28, 2020.*\
Paper URL: [Article](http://jurnal.poliupg.ac.id/index.php/snp2m/article/view/2381)

