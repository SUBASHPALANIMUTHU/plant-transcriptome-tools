import sys
from Bio import SeqIO

def main(fasta_file):
    print("Transcript_ID\tLength")
    for record in SeqIO.parse(fasta_file, "fasta"):
        print(f"{record.id}\t{len(record.seq)}")

if __name__ == "__main__":
    main(sys.argv[1])
