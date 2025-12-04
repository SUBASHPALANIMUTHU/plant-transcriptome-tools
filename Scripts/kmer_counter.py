import sys
from Bio import SeqIO
from collections import Counter

def get_kmers(seq, k):
    return [seq[i:i+k] for i in range(len(seq)-k+1)]

def main(fasta, k=3):
    k = int(k)
    counter = Counter()

    for record in SeqIO.parse(fasta, "fasta"):
        seq = str(record.seq).upper()
        kmers = get_kmers(seq, k)
        counter.update(kmers)

    for kmer, count in counter.items():
        print(f"{kmer}\t{count}")

if __name__ == "__main__":
    fasta = sys.argv[1]
    k = sys.argv[2] if len(sys.argv) > 2 else 3
    main(fasta, k)
