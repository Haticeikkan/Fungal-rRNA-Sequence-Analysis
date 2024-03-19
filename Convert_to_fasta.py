#Gerekli kütüphaneler
import gzip
from Bio import SeqIO
from urllib.request import urlopen

# Linkteki dosyayı İndir
url = "https://ftp.ncbi.nlm.nih.gov/refseq/TargetedLoci/Fungi/fungi.28SrRNA.gbff.gz"
output_file = "28S_rRNA.fasta"

try:
    with urlopen(url) as response, open("fungi.28SrRNA.gbff.gz", 'wb') as out_file:
        out_file.write(response.read())
    print("Dosya indirildi ve kaydedildi.")
except Exception as e:
    print("Hata:", e)

# Dosyayı aç
with gzip.open("fungi.28SrRNA.gbff.gz", 'rt') as gbff_file:
    # GBFF dosyasını çözümle
    records = SeqIO.parse(gbff_file, "genbank")
    
    # Veriyi FASTA formatına dönüştür
    SeqIO.write(records, output_file, "fasta")

print(f"Veri {output_file} dosyasına FASTA formatında dönüştürüldü.")