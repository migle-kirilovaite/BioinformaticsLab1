def translate_sequence(dna_sequence, codon_table):
    dna_sequence = dna_sequence.upper()

    protein_sequence = []

    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i + 3]
        amino_acid = codon_table.get(codon)

        if amino_acid is not None:
            protein_sequence.append(amino_acid)

    return ''.join(protein_sequence)
