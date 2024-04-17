# A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.
#
# A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v
#  and head w
#  is represented by (v,w)
#  (but not by (w,v)
# ). A directed loop is a directed edge of the form (v,v)
# .
#
# For a collection of strings and a positive integer k
# , the overlap graph for the strings is a directed graph Ok
#  in which each string is represented by a node, and string s
#  is connected to string t
#  with a directed edge when there is a length k
#  suffix of s
#  that matches a length k
#  prefix of t
# , as long as s≠t
# ; we demand s≠t
#  to prevent directed loops in the overlap graph (although directed cycles may be present).
#
# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
#
# Return: The adjacency list corresponding to O3
# . You may return edges in any order.

def parse_fasta_file(file_path):
    with open(file_path, 'r') as file:
        fasta_data = file.read()
    return parse_fasta(fasta_data)
def parse_fasta(fasta_data):
    entries = fasta_data.strip().split('>')
    identifiers = []
    sequences = []
    for entry in entries:
        if entry:
            lines = entry.splitlines()
            identifiers.append(lines[0])
            sequences.append(''.join(lines[1:]))
    return identifiers, sequences
def overlap(a, b, k):
    return a[-k:] == b[:k]
def build_overlap_graph(sequences, k):
    graph = {}
    n = len(sequences)
    for i in range(n):
        graph[i] = []
        for j in range(n):
            if i != j and overlap(sequences[i], sequences[j], k):
                graph[i].append(j)
    return graph
def format_output(overlap_graph, identifiers):
    formatted_output = []
    for i in overlap_graph:
        for j in overlap_graph[i]:
            formatted_output.append(f"{identifiers[i]} {identifiers[j]}")
    return formatted_output
identifiers, sequences = parse_fasta_file('rosalind_grph.txt')
overlap_graph = build_overlap_graph(sequences, 3)
output = format_output(overlap_graph, identifiers)
for i in output:
    print(i)
