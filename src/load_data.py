import os
from Bio import SeqIO

def load_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append((record.id, str(record.seq)))
    return sequences

def load_all_fastas(directory):
    all_sequences = {}
    for filename in os.listdir(directory):
        if filename.endswith(".fasta"):
            file_path = os.path.join(directory, filename)
            sequences = load_fasta(file_path)
            for record_id, sequence in sequences:
                all_sequences[record_id] = sequence
    return all_sequences
