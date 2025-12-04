# Plant Transcriptome Tools

A collection of lightweight, reliable, and reproducible bioinformatics tools for plant transcriptome analysis. This repository includes a set of Python scripts commonly used in RNA-seq preprocessing, FASTA handling, expression normalization, k-mer profiling, and general transcriptomics workflows.

These tools are designed for:

- Streamlining plant transcriptomics pipelines
- Ensuring reproducibility and scalability
- Enabling straightforward analysis of high-throughput sequencing data

## Features

- **RNA-seq Preprocessing:** Quality filtering, adapter trimming, and format conversions.
- **FASTA Handling:** Filtering, deduplication, renaming, and sequence statistics.
- **Expression Normalization:** TPM, RPKM/FPKM calculations from raw counts or matrices.
- **K-mer Profiling:** Counting, filtering, and sequence pattern analysis.  
- **Transcriptome Utilities:** General-purpose tools for transcript sequences.

## Requirements

- **Python 3.7+**
- The following Python packages (install via `pip`):
  - `numpy`
  - `pandas`
  - `biopython`
  - Additional dependencies listed in each script’s header

## Installation

Clone the repository:

```bash
git clone https://github.com/SUBASHPALANIMUTHU/plant-transcriptome-tools.git
cd plant-transcriptome-tools
```

(Optional) Create a virtual environment and install common dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Each tool is a standalone Python script and can be run from the command line. For help, run:

```bash
python script_name.py --help
```

### Example commands

- **Quality filter a FASTQ:**
  ```
  python fastq_quality_filter.py -i input.fastq -o output.fastq
  ```
- **Normalize expression matrix:**
  ```
  python normalize_expression.py -i counts.txt -m TPM
  ```
- **K-mer profiling:**
  ```
  python kmer_profiler.py -i sequences.fasta -k 21
  ```

See individual script headers or usage hints for more details.

## Folder Structure

```
plant-transcriptome-tools/
├── README.md
├── scripts/
│   ├── fastq_quality_filter.py
│   ├── fasta_renamer.py
│   ├── normalize_expression.py
│   ├── kmer_profiler.py
│   └── ...
└── requirements.txt
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests to improve or extend tools, add new scripts, or suggest features.

## License

This project is licensed under the MIT License.

---

**Contact:** For questions, suggestions, or tool requests, please open an issue in this repository.
