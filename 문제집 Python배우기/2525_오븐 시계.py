'''
문제
KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다. 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다.

또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.

훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

입력
첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

출력
첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

예제 입력 1 
14 30
20
예제 출력 1 
14 50

예제 입력 2 
17 40
80
예제 출력 2 
19 0

예제 입력 3 
23 48
25
예제 출력 3 
0 13
'''

# try1: 시간과 분을 따로 계산
'''
start_time = list(map(int, input().split()))
start_time_hour = start_time[0]
start_time_minute = start_time[1]

cooking_time_minute_raw = int(input())
cooking_time_hour = cooking_time_minute_raw // 60
cooking_time_minute = cooking_time_minute_raw % 60

end_time_hour = start_time_hour + cooking_time_hour
end_time_minute = start_time_minute + cooking_time_minute

if end_time_hour >= 24:
    if end_time_minute >= 60:
        print((end_time_hour - 24 + (end_time_minute // 60)), end_time_minute % 60)
    else:
        print((end_time_hour - 24), end_time_minute)
else:
    if end_time_minute >= 60:
        if end_time_hour + (end_time_minute // 60) >= 24:
            print((end_time_hour + (end_time_minute // 60) - 24), end_time_minute % 60)
        else:
            print((end_time_hour + (end_time_minute // 60)), end_time_minute % 60)
    else:
        print(end_time_hour, end_time_minute)
'''

# 과연 이게 제일 효율적인 코드가 맞는가... => no

# try2: 시간과 분을 한 번에 계산
start_time = list(map(int, input().split()))
start_time_hour = start_time[0]
start_time_minute = start_time[1]
cooking_time_minute = int(input())

start_time_minute_transformed = start_time_hour * 60 + start_time_minute
end_time_minute = start_time_minute_transformed + cooking_time_minute
end_time_hour = end_time_minute // 60 % 24 # '% 24' => 24시간제 적용
print(end_time_hour, end_time_minute % 60)