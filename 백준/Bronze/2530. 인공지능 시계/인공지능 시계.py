start_time = list(map(int, input().split()))
start_time_hour = start_time[0]
start_time_minute = start_time[1]
start_time_second = start_time[2]

# 전부 초로 변환
start_time_second_transformed = start_time_hour * 3600 + start_time_minute * 60 + start_time_second
cooking_time_second = int(input())

end_time_second = start_time_second_transformed + cooking_time_second
print((end_time_second // 3600) % 24, (end_time_second % 3600) // 60,  (end_time_second % 3600) % 60)