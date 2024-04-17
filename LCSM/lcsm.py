from CommonFunctions import read_fasta_to_dict
values = list(read_fasta_to_dict('rosalind_lcsm.txt').values())
import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
@timing_decorator
def longest_common_substring(strings):
    def lcs_two_strings(str1, str2):
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        longest = 0
        lcs_end_pos = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > longest:
                        longest = dp[i][j]
                        lcs_end_pos = i - 1
                else:
                    dp[i][j] = 0

        return str1[lcs_end_pos - longest + 1: lcs_end_pos + 1]

    common_substring = strings[0]

    for string in strings[1:]:
        common_substring = lcs_two_strings(common_substring, string)
        if not common_substring:
            break

    return common_substring
