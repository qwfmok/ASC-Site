# s = """'Python' is a "Programming language"
# that lets you work quickly
# and
# integrate systems more effectively."""
# print(s)

# 단어 개수 세서 최빈값 구함
# word = input().upper()
# word_sorted = sorted(word)
#
# for i in word_sorted:
#
# bul = int(input())
# room, gap = 1, 6
# for i in range(1, bul+1):
#     if i < 8:
#         if i == 2:
#             room += 1
#             gap += 6
#         else:
#             continue
#     else:
#         if i
#
#
# print(room)

# import sys
# import time

# # 입력 데이터 수
# n = 100000  # 10만 번 입력
#
# print(f"{n}개의 입력을 받아 시간 측정")

# # ==== input() 테스트 ====
# start = time.time()
# for _ in range(n):
#     temp = input()
# end = time.time()
# print(f"input() 사용 시간: {end - start:.4f}초")
#
#
# # ==== sys.stdin.readline() 테스트 ====
# print("이제 sys.stdin.readline() 테스트 시작!")
# start = time.time()
# for _ in range(n):
#     temp = sys.stdin.readline()
# end = time.time()
# print(f"sys.stdin.readline() 사용 시간: {end - start:.4f}초")

# import sys
#
# n = int(sys.stdin.readline())
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)

# N, M = map(int, input().split())
# baguni = [i for i in range(1, N+1)]
# for i in range(1, M+1):
#     fir ,sec = map(int, input().split())
#     baguni[fir-1:sec] = baguni[fir-1:sec][::-1]
# print(*baguni)

# string_list = list(input())
# alpha = list('abcdefghijklmnopqrstuvwxyz')
# for i in string_list:
#     for j in alpha:
#         if i == j:
#             alpha.pop(alpha.index(j))
#             alpha.insert(alpha.index(j), alpha.index(j))
#         else:
#             alpha.pop(alpha.index(j))
#             alpha.insert(alpha.index(i), -1)
#
# print(alpha)
# # index 오류, pop과 insert 동시에 하면 위험, 코드의 의도를 모르겠음

# word = input()
# alpha = list('abcdefghijklmnopqrstuvwxyz')
#
# for ch in alpha:
#     print(word.find(ch), end=' ')

# N = int(input())
# for _ in range(N):
#     num, S = input().split()
#     for j in S:
#         print(j*int(num), end='')
#     print()

# alphabet_list= ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# string = input().upper()
# hap = 0
# for i in string:
#
#
# print(hap)

# alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#
# alpha_to_index = {ch: i for i, group in enumerate(alphabet_list) for ch in group}
#
# word = input()
# hap = 0
# for i in word:
#     hap = hap + alpha_to_index[i] + 3
# print(hap)

# N = int(input())
#
# for i in range(1,10):
#     print(f'{N} * {i} = {N*i}')

# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self, val):
#         self.value += val
#
# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val
#
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100
#
# # print(chr(ord('a')) == 'a')
#

