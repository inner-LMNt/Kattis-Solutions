import sys

for line in sys.stdin:
    alphabet_length, word_length = map(int, line.split())

    alphabet_length += 1
    max_arrangements = alphabet_length ** word_length # sample space

    # dp[i][j] = number of tight words of length `i` ending with letter `j`
    dp = [[0 for _ in range(alphabet_length)] for _ in range(word_length)]

    # Base case: all words of length 1 are tight
    for i in range(alphabet_length):
        dp[0][i] = 1

    if alphabet_length == 1 or alphabet_length == 2:
        print(100)
        continue
    else:
        for i in range(1, word_length):
            for j in range(alphabet_length):
                if j == 0: # first letter
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1] # can be appended from 2 previous letters
                elif j == alphabet_length - 1: # last letter
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] # can be appended from 2 previous letters
                else: # middle letters
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1] # can be appended from 3 previous letters

    # Sum up all tight words of length `word_length`
    tight_words = 0
    for i in range(alphabet_length):
        tight_words += dp[-1][i]

    print(100 * tight_words / max_arrangements)