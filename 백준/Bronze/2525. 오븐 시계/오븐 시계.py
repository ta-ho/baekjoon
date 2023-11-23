start_time = list(map(int, input().split()))
start_time_hour = start_time[0]
start_time_minute = start_time[1]
cooking_time_minute = int(input())

start_time_minute_transformed = start_time_hour * 60 + start_time_minute
end_time_minute = start_time_minute_transformed + cooking_time_minute
end_time_hour = end_time_minute // 60 % 24 # '% 24' => 24시간제 적용
print(end_time_hour, end_time_minute % 60)