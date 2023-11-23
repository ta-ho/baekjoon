song_and_average = list(map(int, input().split()))
num_song = song_and_average[0]
average = song_and_average[1]
num_melody = num_song * (average-1) + 1
print(num_melody)