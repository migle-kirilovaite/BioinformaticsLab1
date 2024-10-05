import os
from Bio import SeqIO


def load_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append((record.id, str(record.seq)))  # Store ID and sequence
    return sequences


def load_all_fastas(directory):
    mammalian_sequences = {}
    bacterial_sequences = {}

    for filename in os.listdir(directory):
        if filename.endswith(".fasta"):
            file_path = os.path.join(directory, filename)
            sequences = load_fasta(file_path)

            if filename.startswith("mamalian"):
                for record_id, sequence in sequences:
                    mammalian_sequences[record_id] = sequence
            elif filename.startswith("bacterial"):
                for record_id, sequence in sequences:
                    bacterial_sequences[record_id] = sequence

    return mammalian_sequences, bacterial_sequences

