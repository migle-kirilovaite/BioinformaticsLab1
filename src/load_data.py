import os
from Bio import SeqIO


def load_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append((record.id, str(record.seq)))
    return sequences


def load_all_viruses(directory):
    mammalian_viruses = {}
    bacterial_viruses = {}

    for filename in os.listdir(directory):
        if filename.endswith(".fasta"):
            file_path = os.path.join(directory, filename)
            viruses = load_fasta(file_path)

            if filename.startswith("mamalian"):
                mammalian_viruses.update(viruses)
            elif filename.startswith("bacterial"):
                bacterial_viruses.update(viruses)

    return mammalian_viruses, bacterial_viruses


