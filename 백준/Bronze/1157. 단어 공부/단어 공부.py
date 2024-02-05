alpha = input()
DP = [0] * 128
for char in alpha:
    DP[int(ord(char.lower()))+1] += 1
max_DP = max(DP)
max_alpha_indices = [i - 1 for i, freq in enumerate(DP) if freq == max_DP]
if len(max_alpha_indices) == 1:
    max_alpha_char = chr(max_alpha_indices[0]).upper()
    print(max_alpha_char)
else:
    print('?')