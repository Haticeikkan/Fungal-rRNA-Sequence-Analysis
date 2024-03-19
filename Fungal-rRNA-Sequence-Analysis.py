#Bu kod Bursa Uludağ Üniversitesi Tıp Fakültesi Tıbbi Mikrobiyoloji BAP TGA:2023-1313 Projesi kapsamında geliştirilmiştir.
#Bu kodu geliştirenler Ayşen İKKAN ve Hatice İKKAN :)

#Gerekli kütüphaneler kullanıldı.
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import os
import sys

# Referans suşlarının bulunduğu klasör
reference_folder = r"D:\Fungal-rRNA-Sequence-Analysis\Türler"

# BLAST için kullanılacak veritabanı
database = "nt"

# Referans suşlarını okuma
reference_sequences = []
for file_name in os.listdir(reference_folder):
    if file_name.endswith(".fasta"):
        file_path = os.path.join(reference_folder, file_name)
        with open(file_path, "r") as ref_handle:
            for record in SeqIO.parse(ref_handle, "fasta"):
                reference_sequences.append(record)

# Analiz edilecek .fasta dosyasını buraya yazınız.
query_file = r"D:\Fungal-rRNA-Sequence-Analysis\Fastalar\68842.fasta"

# BLAST sonuçlarının analiz edileceği eşik değerleri
min_identity = 96  # Minimum eşleşme yüzdesi
min_align_length = 95  # Minimum hizalama uzunluğu

# Dosyadaki her .fasta dosyası için BLAST yapma
with open(query_file, "r") as handle:
    query_sequence = SeqIO.read(handle, "fasta")
    print("Analiz Edilen Dosya: ", query_file)
    
    found_match = False  # En az bir eşleşme bulunduğunu belirten değişken
            
    for reference_sequence in reference_sequences:
        result_handle = NCBIWWW.qblast("blastn", database, query_sequence.seq, alignments=5, descriptions=5)
        blast_record = NCBIXML.read(result_handle)
        
        print("En Yüksek Benzerlik Oranına Sahip 5 Eşleşme:")
        count = 0
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                identity = hsp.identities / hsp.align_length * 100
                align_length = hsp.align_length
                        
                if identity >= min_identity and align_length >= min_align_length:
                    count += 1
                    print(f"\nHit {count}:")  # Sırası
                    print("Hit ID:", alignment.hit_id)  # Eşleşme Kimliği
                    print("Hit Description:", alignment.hit_def)  # Eşleşme Açıklaması
                    print("Hit E-Value:", hsp.expect)  # Eşleşme E-Değeri
                    print("Alignment Length:", align_length)  # Hizalama uzunluğu
                    print("Percentage Identity:", identity)  # Benzerlik yüzdeliği
                    print("Query Length:", blast_record.query_letters) # Sorgu dizisinin uzunluğu 
                    print("Subject Length:", len(reference_sequence))  # Referans dizisinin uzunluğu
                    print("Query Start:", hsp.query_start)  # Sorgu dizisinin hizalanmış başlangıç pozisyonu
                    print("Query End:", hsp.query_end)  # Sorgu dizisinin hizalanmış bitiş pozisyonu
                    print("Subject Start:", hsp.sbjct_start)  # Referans dizisinin hizalanmış başlangıç pozisyonu
                    print("Subject End:", hsp.sbjct_end)  # Referans dizisinin hizalanmış bitiş pozisyonu
                    print("Query Coverage:", hsp.align_length / blast_record.query_letters * 100)  # Sorgu dizisinin hizalama boyunca kapsama yüzdesi 
                    print("Percentage Identity (PID):", hsp.identities / hsp.align_length * 100)  # Tanımlama yüzdeliği
                    print("Number of Identical Matches:", hsp.identities)  # Bire bir eşleşme sayısı
                    print("Number of Mismatches:", hsp.align_length - hsp.identities - hsp.gaps)  # Hizalama boyunca farklılık gösteren nükleotid sayısı
                    print("Number of Gaps:", hsp.gaps)  # Hizalama boyunca açık bırakılan boşluk sayısı
                    print("Bit Score:", hsp.bits)  # HSP'nin bit puanı
                    print("-----------------")
                    found_match = True  # En az bir eşleşme bulundu
                    
                    if count == 5:
                        break
            if count == 5:
                break
        if count == 5:
            break
    
    if not found_match:
        print("Tanımlanamadı: Bu kriterlere uyan bir eşleşme bulunamadı.")

print("Program sonlandırıldı.")
sys.exit()