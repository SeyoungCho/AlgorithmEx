# 탈락 조건 1. 중복 단어 말한 사람 2. 규칙에 어긋나는 단어 말한 사람

def solution(n, words):
    answer = [0, 0]
    used_words = [words[0]]
    for i, word in enumerate(words[1:]):
        if len(word) == 1 or word[0] != words[i][-1] or word in used_words:
            answer[0] = (i + 1) % n + 1
            answer[1] = (i + 1) // n + 1
            break
        used_words.append(word)
    return answer