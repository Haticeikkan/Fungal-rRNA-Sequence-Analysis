# Bu kod Bursa Uludağ Üniversitesi Tıp Fakültesi Tıbbi Mikrobiyoloji BAP TGA:2023-1313 Projesi kapsamında geliştirilmiştir.
# Geliştiriciler: Ayşen İKKAN ve Hatice İKKAN :)
# Bu kod NCBI RefSeq Targeted Loci Project kapsamında Referans Sekanslarla analiz yapmaktadır.

#Gerekli kütüphaneler kullanıldı.
from Bio import SeqIO, SearchIO
import subprocess
import os
import sys

# Referans suşlarının bulunduğu klasör
reference_folder = r"C:\Fungal-rRNA-Sequence-Analysis\Turler"

# Oluşturulacak my_database.fasta dosyasının yolu ve adı
my_database_file = os.path.join(reference_folder, "my_database.fasta")

# Eğer my_database.fasta dosyası yoksa oluştur
if not os.path.exists(my_database_file):
    # Birleştirilecek .fasta dosyalarının adları
    fasta_files = ["18S_rRNA.fasta", "28S_rRNA.fasta", "ITS.fasta"]

    # my_database.fasta dosyasını oluşturma ve birleştirme
    with open(my_database_file, "w") as output_handle:
        for fasta_file in fasta_files:
            file_path = os.path.join(reference_folder, fasta_file)
            with open(file_path, "r") as input_handle:
                for record in SeqIO.parse(input_handle, "fasta"):
                    SeqIO.write(record, output_handle, "fasta")

    print("my_database.fasta dosyası oluşturuldu.")
else:
    print("my_database.fasta dosyası zaten mevcut.")

# BLAST veritabanını oluşturma komutu
makeblastdb_cmd = f"makeblastdb -in {my_database_file} -dbtype nucl"

# BLAST veritabanını oluşturma işlemini çalıştırma
try:
    subprocess.run(makeblastdb_cmd, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("BLAST veritabanı oluşturma işlemi başarısız oldu:", e)
    sys.exit(1)

# Analiz edilecek .fasta dosyasının buraya yazınız.
query_file = r"C:\Fungal-rRNA-Sequence-Analysis\Fastalar\A.fasta"

# BLAST sonuçlarının analiz edileceği eşik değerleri
min_identity = 96  # Minimum eşleşme yüzdesi
min_align_length = 95  # Minimum hizalama uzunluğu

# BLAST için kullanılacak veritabanı dosyası
database = my_database_file

# BLAST komutu
blast_cmd = f"blastn -out blast_output.xml -outfmt 5 -num_alignments 5 -query {query_file} -db {database}"

# BLAST işlemini çalıştırma
try:
    subprocess.run(blast_cmd, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("BLAST işlemi başarısız oldu:", e)
    sys.exit(1)

# BLAST sonuçlarını okuma ve analiz etme
blast_records = SearchIO.parse("blast_output.xml", "blast-xml")

for blast_record in blast_records:
    print("En Yüksek Benzerlik Oranına Sahip 5 Eşleşme:")
    count = 0
    for hit in blast_record:
        for hsp in hit:
            identity = hsp.ident_num / hsp.aln_span * 100
            align_length = hsp.aln_span

            if identity >= min_identity and align_length >= min_align_length:
                count += 1
                print(f"\nHit {count}:")  # Sırası
                print("Hit ID:", hit.id)  # Eşleşme Kimliği
                print("Hit Description:", hit.description)  # Eşleşme Açıklaması
                print("Hit E-Value:", hsp.evalue)  # Eşleşme E-Değeri
                print("Alignment Length:", align_length)  # Hizalama uzunluğu
                print("Percentage Identity:", identity)  # Benzerlik yüzdeliği
                print("Query Length:", hsp.query_span)  # Sorgu dizisinin uzunluğu
                print("Subject Length:", hsp.hit_span)  # Referans dizisinin uzunluğu
                print("Query Start:", hsp.query_start)  # Sorgu dizisinin hizalanmış başlangıç pozisyonu
                print("Query End:", hsp.query_end)  # Sorgu dizisinin hizalanmış bitiş pozisyonu
                print("Subject Start:", hsp.hit_start)  # Referans dizisinin hizalanmış başlangıç pozisyonu
                print("Subject End:", hsp.hit_end)  # Referans dizisinin hizalanmış bitiş pozisyonu
                print("-----------------")
                if count == 5:
                    break
        if count == 5:
            break

    if not count:
        print("Tanımlanamadı: Bu kriterlere uyan bir eşleşme bulunamadı.")

print("Program sonlandı.")