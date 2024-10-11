from collections import defaultdict
from src.codon_table import codontab

def get_all_amino_acids(codon_table):
    return set(codon_table.values())


def codon_frequency(protein_sequence, all_amino_acids):
    codon_counter = defaultdict(int)

    for amino_acid in all_amino_acids:
        codon_counter[amino_acid] = 0

    for codon in protein_sequence:
        codon_counter[codon] += 1

    return codon_counter


def dicodon_frequency(protein_sequence, all_amino_acids):
    dicodon_counter = defaultdict(int)

    for aa1 in all_amino_acids:
        for aa2 in all_amino_acids:
            dicodon = aa1 + aa2
            dicodon_counter[dicodon] = 0

    for i in range(len(protein_sequence) - 1):  # Go through pairs of amino acids
        dicodon = protein_sequence[i:i + 2]  # Get a pair of amino acids
        dicodon_counter[dicodon] += 1

    return dicodon_counter


def analyze_frequencies(protein_sequences):
    all_amino_acids = get_all_amino_acids(codontab)
    codon_frequencies = {}
    dicodon_frequencies = {}

    for record_id, proteins in protein_sequences.items():
        codon_frequencies[record_id] = []
        dicodon_frequencies[record_id] = []

        for protein_seq in proteins:
            codon_freq = codon_frequency(protein_seq, all_amino_acids)
            dicodon_freq = dicodon_frequency(protein_seq, all_amino_acids)

            codon_frequencies[record_id].append(codon_freq)
            dicodon_frequencies[record_id].append(dicodon_freq)

    return codon_frequencies, dicodon_frequencies



