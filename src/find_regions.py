def find_coding_regions(sequence):
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}

    valid_pairs = []

    start_positions = []

    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i + 3]

        if codon == start_codon:
            start_positions.append(i)

        elif codon in stop_codons:
            furthest_valid_start = None

            for start in reversed(start_positions):
                has_stop_in_between = any(
                    sequence[j:j + 3] in stop_codons for j in range(start + 3, i, 3)
                )

                if not has_stop_in_between:
                    furthest_valid_start = start
                    break

            if furthest_valid_start is not None:
                valid_pairs.append((furthest_valid_start, i + 3))

            start_positions = [s for s in start_positions if s > i]

    return valid_pairs

def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in reversed(sequence)])

def filter_short_regions(regions, min_length=100):
    return [(start, stop) for start, stop in regions if stop - start >= min_length]
