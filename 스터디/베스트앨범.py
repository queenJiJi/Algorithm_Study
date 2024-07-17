from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_dic = defaultdict(list)
    
    # genre_dic = [(장르, 플레이횟수)]
    for i,val in enumerate(genres):
        genre_dic[val].append((i,plays[i]))

    # 장르별 총 플레이횟수
    total_play = {}
    
    for genre, songs in genre_dic.items():
        total = 0
        for song in songs:
            # song: (곡의 인덱스 ,재생횟수)의 튜플형태
            total += song[1]
        total_play[genre] = total

    # 장르별 총 플레이 횟수를 내림차순으로 정렬
    sorted_genres = sorted(total_play.keys(), key=lambda genre: total_play[genre], reverse=True)
    print(sorted_genres)
    
    # 각 장르별로 재생횟수가 많은 순서대로 정렬
    for genre in sorted_genres:
        sorted_songs = sorted(genre_dic[genre], key=lambda x:(-x[1],x[0])) # x[1]을 기준으로 내림차순 정렬, x[1]이 같다면 x[0]을 기준으로 오름차순
        answer.extend(song[0] for song in sorted_songs[:2])
    return answer



print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))