from collections import deque

# Sample word list
words = {"cold", "cord", "card", "ward", "warm", "word"}

def word_ladder(start, end, word_list):
    if end not in word_list or not start or not end:
        return []

    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        current_word = path[-1]

        if current_word == end:
            return path

        # Generate all possible single-letter transformations
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in word_list and next_word not in visited:
                    visited.add(next_word)
                    queue.append(path + [next_word])
    return []

# Test
start_word = "cold"
end_word = "warm"
ladder = word_ladder(start_word, end_word, words)
print("Word Ladder:", ladder)
