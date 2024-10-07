# def find_coding_regions(sequence):
#     start_codon = "ATG"
#     stop_codons = ["TAA", "TAG", "TGA"]
#     regions = []
#
#     for i in range(len(sequence) - 2):
#         if sequence[i:i+3] == start_codon:
#             for j in range(i + 3, len(sequence) - 2, 3):
#                 codon = sequence[j:j+3]
#                 if codon in stop_codons:
#                     regions.append((i, j + 3))
#                     break
#     return regions

def find_coding_regions(sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    regions = []

    start_positions = []

    for i in range(len(sequence) - 2):
        codon = sequence[i:i + 3]

        if codon == start_codon:
            start_positions.append(i)

        elif codon in stop_codons:
            if start_positions:
                furthest_start = start_positions[-1]
                regions.append((furthest_start, i + 3))

            start_positions.clear()

    return regions

def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in reversed(sequence)])

def filter_short_regions(regions, min_length=100):
    return [(start, stop) for start, stop in regions if stop - start >= min_length]
