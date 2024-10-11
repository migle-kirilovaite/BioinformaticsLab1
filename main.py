from src.load_data import load_all_viruses
from src.find_regions import find_coding_regions, reverse_complement, filter_short_regions
from src.translate import translate_sequence
from src.codon_table import codontab
from src.frequencies import analyze_frequencies
from src.distance_matrix import create_distance_matrix

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

    mammalian_codon_freq, mammalian_dicodon_freq = analyze_frequencies(mammalian_protein_sequences)
    bacterial_codon_freq, bacterial_dicodon_freq = analyze_frequencies(bacterial_protein_sequences)

    codon_frequencies = {**mammalian_codon_freq, **bacterial_codon_freq}
    codon_dist_matrix, codon_ids, codon_keys = create_distance_matrix(codon_frequencies)

    dicodon_frequencies = {**mammalian_dicodon_freq, **bacterial_dicodon_freq}
    dicodon_dist_matrix, dicodon_ids, dicodon_keys = create_distance_matrix(dicodon_frequencies)

    print("\nCodon Distance Matrix:")
    print(len(codon_ids))
    for i, row in enumerate(codon_dist_matrix):
        print(f"{codon_ids[i]} " + " ".join(f"{d:.3f}" for d in row))

    print("\nDicodon Distance Matrix:")
    print(len(dicodon_ids))
    for i, row in enumerate(dicodon_dist_matrix):
        print(f"{dicodon_ids[i]} " + " ".join(f"{d:.3f}" for d in row))

if __name__ == '__main__':
    main()
