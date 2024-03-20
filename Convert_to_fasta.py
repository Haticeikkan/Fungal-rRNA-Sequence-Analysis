#Gerekli kütüphaneler
import gzip
from Bio import SeqIO
from urllib.request import urlopen
import os

# Linkteki dosyayı İndir
url = "https://ftp.ncbi.nlm.nih.gov/refseq/TargetedLoci/Fungi/fungi.28SrRNA.gbff.gz"
output_file = "28S_rRNA.fasta" #Dosyaya isim ver
output_folder = "D:/Fungal-rRNA-Sequence-Analysis/Turler"  # Dosyanın indirildiği yer

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
    output_path = os.path.join(output_folder, output_file)
    SeqIO.write(records, output_file, "fasta")

print(f"Veri {output_file} dosyasına {output_folder} klasörüne FASTA formatında dönüştürüldü.")

# İndirilen .gbff.gz dosyasının adı 
downloaded_file = "fungi.28SrRNA.gbff.gz"

try:
    # Dosyayı sil
    os.remove(downloaded_file)
    print(f"{downloaded_file} başarıyla silindi.") # İlk indirilen .gbff.gz uzantılı dosya gereksiz yer kaplamasın diye silindi.
except FileNotFoundError:
    print(f"{downloaded_file} bulunamadı.")
except Exception as e:
    print("Dosya silinirken bir hata oluştu:", e)