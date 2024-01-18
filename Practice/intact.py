# Words count sequentially.

def stopWords(text, k):
    # Write your code here
    words = text.split()
    word_count = {}
    stop_words_list = []

    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

        stop_words_list = [word for word, count in word_count.items() if count >= k]

    return stop_words_list

ts = "the brown fox jumped over the brown dog and runs away to the brown house"
k = 2
print(stopWords(ts, k))
