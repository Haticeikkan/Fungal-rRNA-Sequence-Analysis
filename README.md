# Fungal-rRNA-Sequence-Analysis

<img src="Resimler/Fungal-rRNA-Sequence-Analysis.png">
<br>
<p>Mantarların tanımlanması için ribozomal RNA bölgelerinden 18S, 28S ve ITS bölgeleri kullanılmaktadır. Ancak bunlardan ITS dizisi tür düzeyinde tanımlama için aynı türün bireyleri arasındaki farklılığının az, değişik türler arasındaki farklılığının fazla olması nedeniyle altın standart olarak kullanılmasını sağlamıştır.<p>

<p>Ökaryotik canlılarda bu gen bölgesi 18S small subunit (SSU), 28S large subunit (LSU) ve 5.8S subunit oluşmaktadır. Bu üç gen kompleksi arasında onları birbirinden ayıran ITS bölgeleri bulunur. ITS1 ve ITS2 bölgeleri türler arasında değişiklikler göstermektedir.<p>
<img src="Resimler/Ribozomal_DNA_gen_kompleksi.png"> <br>
Resim 1: Ribozomal DNA gen kompleksi <br>

<p>Ancak bazı durumlarda bu gen bölgeleri yeterli gelmeyebilir. Bu gibi durumlarda farklı bölgelerde değerlendirilmeye alınmaktadır. Bu çalışmada da ITS bölgelerinin yanı sıra 18S rRNA ve 28S rRNA bölgeleri değerlendirmeye alınmıştır. <p>

<p>Güvenilir bir tanımlama yapmak için National Center for Biotechnology Information (NCBI)'ın referans sequence dosyalarının olduğu RefSeq Targeted Loci Project Fungi (Fungi FTP: https://ftp.ncbi.nlm.nih.gov/refseq/TargetedLoci/Fungi/) dizilerini Biopython  kütüphanesiyle analiz edildi.<p>

## Gereklilikler
- [Visual Studio Code](https://code.visualstudio.com/download) <br>
- [Biopython](https://github.com/biopython) <br>
- [Blast+](https://blast.ncbi.nlm.nih.gov/doc/blast-news/2023-BLAST-News.html) 

## 1. Adım: Convert to Fasta
<p>Sekans Analiz cihazından veriler .fasta uzantılı olarak çıkmaktadır. NCBI'den referans alınan veriler ise .gbff uzantılıdır. Bu yüzden referans alacağımız dosyaları .fasta formatına çevrilmiştir.<p>

## 2. Adım: Fungal-rRNA-Sequence-Analysis
<p>Sequence Analiz burada yapılmıştır. Öncelikle Biopython ve Blast+ indirilip kurulmalıdır. Daha sonra aynı dizinde Fungal-rRNA-Sequence-Analysis adında bir klasör oluşturulup kodlar bu klasör içinde yazılmıştır. Klasör içinde ayrıca Turler(Referans alınacak suşların bulunduğu klasör) ve Fastalar(Analizi yapılacak .fasta dosyaları) adlı klasör oluşturulup gereken dosyalar konularak analiz yapılmaktadır.Analiz yapılırken benzerlik oranı en yüksek 5 tür yazdırılmıştır.<p>

### Örnek Çıktılar
<img src="Resimler/Ornek1.png"> <br>
Resim 2: Örnek 1
<p> <p>
<img src="Resimler/Ornek2.png"> <br>
Resim 3: Örnek 2
<p> <p>
<img src="Resimler/Ornek3.png"> <br>
Resim 4: Örnek 3

#### NOT: Referance-Sequence-Analysis Dosyası
Bu dosya Blast veritabanını kullanarak analiz yapmaktadır.