def fasta_read(consdata):
    matrix = []
    current_sequence = ''
    with open(consdata, 'r') as file:
        for line in file:
            line = line.rstrip()
            if line.startswith('>'):
                if current_sequence:
                    matrix.append(current_sequence)
                    current_sequence = ''
            else:
                current_sequence += line
        if current_sequence:
            matrix.append(current_sequence)
    return matrix
def cons_problem(mtx):
    transposed_list = [list(row) for row in zip(*mtx)]
    A, T, G, C = [], [], [], []
    for i in range(len(transposed_list)):
        A.append(transposed_list[i].count('A'))
        T.append(transposed_list[i].count('T'))
        G.append(transposed_list[i].count('G'))
        C.append(transposed_list[i].count('C'))
    print('A:', *A)
    print('C:', *C)
    print('G:', *G)
    print('T:', *T)
    matrix = list(zip(A, C, G, T))
    nucleotides = ['A', 'C', 'G', 'T']

    consensus = ''
    for column in matrix:
        max_index = column.index(max(column))
        consensus += nucleotides[max_index]
    print("Consensus String:", consensus)
cons_problem(fasta_read('rosalind_cons.txt'))
