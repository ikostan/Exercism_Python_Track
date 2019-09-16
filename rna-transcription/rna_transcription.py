def to_rna(dna_strand):
    dna = {'G': 'C',
           'C': 'G',
           'T': 'A',
           'A': 'U'}

    return ''.join(dna[char] for char in dna_strand.upper())
