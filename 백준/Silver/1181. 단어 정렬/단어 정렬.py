n = int(input())
words = []

# 단어 입력받기
for _ in range(n):
    words.append(input())

# set으로 중복 제거
words = list(set(words))

# (단어, 단어길이) 리스트
word_len = []
for word in words:
    word_len.append((word, len(word)))

# 단어길이 오름차순, 사전순 정렬
word_len.sort(key=lambda x : (x[1], x[0]))

# 정답 출력
for word, _ in word_len:
    print(word)