def solution(genres, plays):
    from collections import defaultdict
    answer = []
    album_list = []
    album_count = len(genres)
    play_count_for_genre = defaultdict(lambda : 0)
    for i in range(album_count):
        album_list.append([i,0,genres[i],plays[i]])
        play_count_for_genre[genres[i]] += plays[i]
    for i in range(album_count):
        album_list[i][1] = play_count_for_genre[album_list[i][2]]
    
    sorted_album_list = sorted(album_list,key=lambda e: (-e[1],-e[3],e[0]))
    
    current_ganre = [sorted_album_list[0][2]]
    current_count = 0
    for i in range(album_count):
        if current_ganre == sorted_album_list[i][2]:
            if current_count < 2:
                current_count += 1
                answer.append(sorted_album_list[i][0])
        else:
            current_ganre = sorted_album_list[i][2]
            current_count = 1
            answer.append(sorted_album_list[i][0])

    return answer

def solution2(genres, plays):
    from collections import defaultdict
    play_numbers = defaultdict(lambda : 0)
    items = []
    for i in range(0,len(genres)):
        play_numbers[genres[i]] += plays[i]
        tmp = [genres[i], plays[i], i]
        items.append(tmp)

    for i in range(0, len(genres)):        
        items[i].append(play_numbers[genres[i]])

    target = sorted(items, key = lambda item: (-item[3], -item[1], item[2]))
    answer = []
    tmp = ['', 0]
    for i in range(0, len(target)):
        if target[i][0] == tmp[0]:
            tmp[1] += 1
            if tmp[1] > 2:
                continue
        else:
            tmp[0] = target[i][0]
            tmp[1] = 1
        answer.append(target[i][2])           
    return answer

solution(["classic","classic","classic","classic","pop"],	[500,150,800,800,2500])
