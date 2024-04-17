def IEV_read(iev):
    with open(iev, 'r') as file:
        iev_data = file.read().split()
        int_array = [int(item) for item in iev_data]
    return int_array
def iev_calc(data):
    offspring = (1 * data[0] + 1 * data[1] + 1 * data[2] + 0.75 * data[3] + 0.5 * data[4] + 0 * data[5]) * 2
    return offspring
print(iev_calc(IEV_read('rosalind_iev.txt')))
