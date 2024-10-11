from collections import defaultdict
from src.codon_table import codontab

def get_all_amino_acids(codon_table):
    return set(codon_table.values())


def get_all_dicodons(all_amino_acids):
    return {aa1 + aa2 for aa1 in all_amino_acids for aa2 in all_amino_acids}

def codon_frequency(protein_sequence, all_amino_acids):
    codon_counter = defaultdict(int)

    for amino_acid in all_amino_acids:
        codon_counter[amino_acid] = 0

    for codon in protein_sequence:
        if codon in codon_counter:  # Ensure codon exists in counter
            codon_counter[codon] += 1

    return codon_counter


def dicodon_frequency(protein_sequence, all_amino_acids):
    dicodon_counter = defaultdict(int)
    all_dicodons = get_all_dicodons(all_amino_acids)

    for dicodon in all_dicodons:
        dicodon_counter[dicodon] = 0

    for i in range(len(protein_sequence) - 1):
        dicodon = protein_sequence[i:i + 2]
        if dicodon in dicodon_counter:
            dicodon_counter[dicodon] += 1

    return dicodon_counter


def analyze_frequencies(protein_sequences):
    all_amino_acids = get_all_amino_acids(codontab)
    codon_frequencies = {}
    dicodon_frequencies = {}

    for record_id, proteins in protein_sequences.items():
        codon_frequencies[record_id] = defaultdict(int)
        dicodon_frequencies[record_id] = defaultdict(int)

        for amino_acid in all_amino_acids:
            codon_frequencies[record_id][amino_acid] = 0

        all_dicodons = get_all_dicodons(all_amino_acids)
        for dicodon in all_dicodons:
            dicodon_frequencies[record_id][dicodon] = 0

        for protein_seq in proteins:
            codon_freq = codon_frequency(protein_seq, all_amino_acids)
            dicodon_freq = dicodon_frequency(protein_seq, all_amino_acids)

            for codon, count in codon_freq.items():
                codon_frequencies[record_id][codon] += count

            for dicodon, count in dicodon_freq.items():
                dicodon_frequencies[record_id][dicodon] += count

    return codon_frequencies, dicodon_frequencies



