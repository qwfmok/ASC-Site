# https://www.acmicpc.net/problem/5086
# 4 × 3 = 12이다.
#
# 이 식을 통해 다음과 같은 사실을 알 수 있다.
#
# 3은 12의 약수이고, 12는 3의 배수이다.
#
# 4도 12의 약수이고, 12는 4의 배수이다.
#
# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.
#
# 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

# while True:
#     first, second = map(int, input().split())
#     if first == 0 and second == 0:
#         break
#     if first >= second:
#         if first % second == 0:
#             print('multiple')
#         else:
#             print('neither')
#     else:
#         if second % first == 0:
#             print('factor')
#         else:
#             print('neither')

# https://www.acmicpc.net/problem/1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

from collections import Counter

# word_dict = {}
# for ch, idx in enumerate(word):

# freq = Counter(word)
# maxi = max(freq)
# print(maxi)
# word = input().strip().upper()
# freq = {}
#
# for ch in word:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
#
# max_freq = max(freq.values())
# most_common = [ch for ch, count in freq.items() if count == max_freq]
# if len(most_common) > 1:
#     print('?')
# else:
#     print(most_common[0])


# https://www.acmicpc.net/problem/2738
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# row, col = map(int, input().split())
# matrix1 = []
# matrix2 = []
# matrix3 = []
# if 0 < row <= 100 and 0 < col <= 100:
#     for i in range(row):
#         matrix1.append(list(map(int, input().split())))
#     for i in range(row):
#         matrix2.append(list(map(int, input().split())))
#     for i in range(row):
#         row_sum = []
#         for j in range(col):
#             row_sum.append(matrix1[i][j] + matrix2[i][j])
#         matrix3.append(row_sum)
#
# for row in matrix3:
#     print(*row)
#
# matrix1 = [list(map(int, input().split())) for _ in range(row)]
# matrix3 = [[matrix1[i][j] + matrix2[i][j] for j in range(col)] for i in range(row)]
# for row in matrix3: print(*row)

# keys = input().split()
# values = map(int, input().split())
#
# x = dict(zip(keys, values))
# x = {keys:values for keys, values in x.items() if keys != 'delta' and values != 30}
# print(x)