import sys
from Bio import SeqIO

def gc_content(seq):
    seq = seq.upper()
    g = seq.count("G")
    c = seq.count("C")
    valid = sum(seq.count(n) for n in "ATGC")
    return ((g + c) / valid) * 100 if valid > 0 else 0

def main(fasta):
    print("Transcript_ID\tGC_Content(%)")
    for record in SeqIO.parse(fasta, "fasta"):
        print(f"{record.id}\t{gc_content(record.seq):.2f}")

if __name__ == "__main__":
    main(sys.argv[1])
