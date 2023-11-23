import sys

input = sys.stdin.readline
num_test = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
for i in range(len(score_list)):
    score_list[i] = score_list[i]/max_score*100
print(sum(score_list)/len(score_list))