﻿from src.load_data import load_all_viruses
from src.find_regions import find_coding_regions, reverse_complement, filter_short_regions
from src.translate import translate_sequence
from src.codon_table import codontab
from src.frequencies import analyze_frequencies


def process_sequences(sequences):
    processed_sequences = {}

    for record_id, sequence in sequences.items():
        main_protein_sequences = process_sequence(sequence)
        reverse_protein_sequences = process_sequence(reverse_complement(sequence))

        processed_sequences[record_id] = main_protein_sequences + reverse_protein_sequences

    return processed_sequences


def process_sequence(sequence):
    regions = find_coding_regions(sequence)
    filtered_regions = filter_short_regions(regions)
    protein_sequences = []

    for start, stop in filtered_regions:
        dna_fragment = sequence[start:stop]
        protein_seq = translate_sequence(dna_fragment, codontab)
        protein_sequences.append(protein_seq)

    return protein_sequences


def main():
    directory = "data/"
    mammalian_sequences, bacterial_sequences = load_all_viruses(directory)

    print("Processing Mammalian Sequences...")
    mammalian_protein_sequences = process_sequences(mammalian_sequences)

    print("Processing Bacterial Sequences...")
    bacterial_protein_sequences = process_sequences(bacterial_sequences)

    # Analyze codon and dicodon frequencies for individual protein sequences
    mammalian_codon_freq, mammalian_dicodon_freq = analyze_frequencies(mammalian_protein_sequences)
    bacterial_codon_freq, bacterial_dicodon_freq = analyze_frequencies(bacterial_protein_sequences)

    # Output for verification
    print("\nMammalian Codon Frequencies (by sequence):")
    print(mammalian_codon_freq)

    print("\nBacterial Codon Frequencies (by sequence):")
    print(bacterial_codon_freq)

    print("\nMammalian Dicodon Frequencies (by sequence):")
    print(mammalian_dicodon_freq)

    print("\nBacterial Dicodon Frequencies (by sequence):")
    print(bacterial_dicodon_freq)


if __name__ == '__main__':
    main()