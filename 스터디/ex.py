from collections import defaultdict

def solution(genre_play_dict):
    # Step 1: 각 장르별로 총 재생 횟수를 계산합니다.
    total_plays = {genre: sum(play for _, play in songs) for genre, songs in genre_play_dict.items()}
    print(total_plays)
    # Step 2: 장르를 총 재생 횟수가 많은 순서대로 정렬합니다.
    sorted_genres = sorted(total_plays.keys(), key=lambda genre: total_plays[genre], reverse=True)
    print(sorted_genres)
    result = []
    # Step 3: 각 장르별로 노래를 재생 횟수가 많은 순서대로 정렬합니다.
    for genre in sorted_genres:
        sorted_songs = sorted(genre_play_dict[genre], key=lambda x: (-x[1], x[0]))
        # Step 4: 각 장르별로 상위 두 개의 노래를 선택합니다.
        result.extend(song[0] for song in sorted_songs[:2])

    return result

# 예제 사용
genre_play_dict = defaultdict(list, {
    'classic': [(0, 500), (2, 150), (3, 800)],
    'pop': [(1, 600), (4, 2500)]
})

print(solution(genre_play_dict))  # 결과는 [4, 1, 3, 0]이어야 합니다.