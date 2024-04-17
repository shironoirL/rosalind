def read_fasta_to_dict(filename):
    """
    Читает файл FASTA и возвращает словарь, где ключи - идентификаторы, а значения - последовательности ДНК.

    :param filename: путь к файлу FASTA
    :return: словарь с идентификаторами и последовательностями
    """
    fasta_dict = {}
    current_key = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_key = line[1:]
                fasta_dict[current_key] = ""
            else:
                if current_key:
                    fasta_dict[current_key] += line

    return fasta_dict