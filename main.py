from src.load_data import load_all_viruses
from src.find_regions import find_coding_regions, reverse_complement, filter_short_regions

def main():
    directory = "data/"
    mammalian_sequences, bacterial_sequences = load_all_viruses(directory)

    print("Processing Mammalian Sequences:")
    for record_id, sequence in mammalian_sequences.items():
        regions_forward = find_coding_regions(sequence)
        regions_reverse = find_coding_regions(reverse_complement(sequence))

        all_regions = regions_forward + regions_reverse
        filtered_regions = filter_short_regions(all_regions)


    print("\nProcessing Bacterial Sequences:")
    for record_id, sequence in bacterial_sequences.items():
        regions_forward = find_coding_regions(sequence)
        regions_reverse = find_coding_regions(reverse_complement(sequence))

        all_regions = regions_forward + regions_reverse
        filtered_regions = filter_short_regions(all_regions)

if __name__ == '__main__':
    main()