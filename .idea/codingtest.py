# #1 합계 집합
# while True:
#     n = int(input())
#     nset = []
#
#     if n == 0:
#         break
#
#     for _ in range(n):
#         a = int(input())
#         nset.append(a)
#     answer = []
#     nset = sorted(nset)
#     for i in nset:
#         for j in nset:
#             for k in nset:
#                 for l in nset:
#                     if i!= j and i!= k and j!= k:
#                         if i + k + j == l:
#                             answer.append(l)
#     print(max(answer) if answer != [] else 'no solution')
from sympy import intersection

#2 언어의 연결#
# T = int(input())
# for i in range(T):
#     M, N = map(int, input().split())
#     M_list = []
#     N_list = []
#     new_list = []
#     for _ in range(M):
#         a = input().strip()
#         M_list.append(a)
#     for _ in range(N):
#         a = input().strip()
#         N_list.append(a)
#     for j in range(M):
#         for k in range(N):
#             new_list.append(M_list[j]+N_list[k])
#     new_set = set(new_list)
#
#     print(f'Case {i+1}: {len(new_set)}')


# # 3 UFC
# T = int(input())
# for i in range(T):
#     N = int(input())
#     for j in range(0, 2**N, -1):



# 6. 맥도날드 목초지
# import math
# T = int(input())
# for i in range(T):
#     R, P = input().split()
#     R = int(R)
#     P = round(float(P),2)

#9 게놈
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     for _ in range(N):
#         a, b = input()
#
