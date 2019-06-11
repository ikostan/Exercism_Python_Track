def proteins(strand):

    amino_acids = {'AUG': ['Methionine'],
                   'UUUUUC': ['Phenylalanine'],
                   'UUAUUG': ['Leucine'],
                   'UCUUCCUCAUCG': ['Serine'],
                   'UAUUAC': ['Tyrosine'],
                   'UGUUGC': ['Cysteine'],
                   'UGG': ['Tryptophan'],
                   'STOP': ['UAA', 'UAG', 'UGA']}

    codons = amino_acids.keys()
    stop = False
    stop_i = 0
    strand_temp = [strand[n: n + 3] for n in range(0, len(strand), 3)]

    # test stops translation
    for i, s in enumerate(strand_temp):
        if s in amino_acids['STOP']:
            stop = True
            stop_i = i
            break

    result = []

    if stop:

        # if stop codon at end
        if strand[-3:] in amino_acids['STOP']:

            strand_temp = strand_temp[:-1]

            for c in codons:
                for t in strand_temp:
                    # transfer amino_acids key into list of codons
                    if t in [c[i:i + 3] for i in range(0, len(c), 3)]:
                        result += amino_acids[c]

        # if stop codon at beginning
        elif strand[:3] in amino_acids['STOP']:
            return result

        # if stop codon in the middle
        else:
            strand_temp = strand_temp[0:stop_i]

            for s in strand_temp:
                for c in codons:
                    if s in [c[i:i + 3] for i in range(0, len(c), 3)]:
                        result += amino_acids[c]

    else:
        for s in strand_temp:
            for c in codons:
                if s in [c[i:i+3] for i in range(0, len(c), 3)]:
                    result += amino_acids[c]

    return result

