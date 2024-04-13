# Problem
# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

# An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

# Given: A DNA string s
#  of length at most 1 kbp in FASTA format.

# Return: Every distinct candidate protein string that can be translated from ORFs of s
# . Strings can be returned in any order.

codon_table = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}
def translate_to_protein(codon):
    protein = None
    if len(codon) == 3 and codon_table.has_key(codon):
        protein = codon_table[codon]
    return protein

def rnaTranscription(s):
    return s.replace('T', 'U')

def openReadingFrame(s):
    results = []
    indexes = [] 
    l = len(s)
    for i in range(l):
        protein = codon_table(s[i:i+3])
        if protein and protein == 'M':
            indexes.append(i)
    for i in indexes:
        stop = False
        proteinString = ''

        for j in range(i,l,3):
            protein = codon_table(s[j:j+3])

            if not protein:
                break

            elif protein == 'Stop':
                stop = True
                break

            proteinString += protein

        if stop:
            results.append(proteinString)
    return results

data = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
print(openReadingFrame(rnaTranscription(data)))