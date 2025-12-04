import sys
from Bio import SeqIO

def clean_header(header):
    return header.replace(" ", "_").split("|")[0]

def main(fasta):
    records = []
    for record in SeqIO.parse(fasta, "fasta"):
        record.id = clean_header(record.id)
        record.description = ""
        records.append(record)

    out = fasta.replace(".fasta", "_clean.fasta")
    SeqIO.write(records, out, "fasta")
    print(f"Clean FASTA saved as: {out}")

if __name__ == "__main__":
    main(sys.argv[1])
