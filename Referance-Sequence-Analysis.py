# Bu kod Bursa Uludağ Üniversitesi Tıp Fakültesi Tıbbi Mikrobiyoloji BAP TGA:2023-1313 Projesi kapsamında geliştirilmiştir.
# Geliştiriciler: Ayşen İKKAN ve Hatice İKKAN :)
# Bu kod Blast veritabanını kullanarak analiz yapmaktadır.

#Gerekli kütüphaneler
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO

# Sorgu dizisi dosyasını açma
query_file = r"D:\ALSU\Fungal-rRNA-Sequence-Analysis\Fastalar\A.fasta"

# Dosyadan sorgu dizisini okuma
with open(query_file, "r") as handle:
    query_sequence = SeqIO.read(handle, "fasta")

# BLAST işlemi
result_handle = NCBIWWW.qblast("blastn", "nt", query_sequence.seq)

# BLAST sonuçlarını analiz etme
blast_record = NCBIXML.read(result_handle)

# En yüksek 5 eşleşme oranını yazdırma
print("Top 5 Best Hits:")
print("-----------------")
for i, alignment in enumerate(blast_record.alignments[:5], 1):
    print(f"Hit {i}")
    print("Hit ID:", alignment.hit_id)
    print("Hit Description:", alignment.hit_def)
    print("Hit E-Value:", alignment.hsps[0].expect)
    print("Alignment Length:", alignment.hsps[0].align_length)
    print("Percentage Identity:", alignment.hsps[0].identities / alignment.hsps[0].align_length * 100)
    
    # BLAST sonuçlarında bulunan ek değerleri yazdırma
    for hsp in alignment.hsps:
        print("qlen:", hsp.align_length)
        print("slen:", hsp.align_length)
        print("length:", hsp.align_length)
        print("qstart:", hsp.query_start)
        print("qend:", hsp.query_end)
        print("sstart:", hsp.sbjct_start)
        print("send:", hsp.sbjct_end)
        print("qcovs:", (hsp.query_end - hsp.query_start + 1) / len(query_sequence) * 100)
        print("pident:", hsp.identities / hsp.align_length * 100)
        print("nident:", hsp.identities)
        print("mismatch:", hsp.align_length - hsp.identities - hsp.gaps)
        print("gaps:", hsp.gaps)
        print("bitscore:", hsp.bits)
        print("-----------------")
    
# Döngüyü bitir (ilk 5 eşleşme işlendikten sonra)