from src.load_data import load_all_viruses
from src.find_regions import find_coding_regions, reverse_complement, filter_short_regions
from src.translate import translate_sequence
from src.codon_table import codontab


def process_sequences(sequences):
    protein_sequences = []

    for record_id, sequence in sequences.items():
        protein_sequences.extend(process_sequence(sequence))

        reverse_sequence = reverse_complement(sequence)
        protein_sequences.extend(process_sequence(reverse_sequence))

    return protein_sequences


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

    print(mammalian_protein_sequences)
    print(bacterial_protein_sequences)


if __name__ == '__main__':
    main()