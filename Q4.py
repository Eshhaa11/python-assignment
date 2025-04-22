def char_frequency(word):
    freq = {}
    for letter in word:
        if letter in freq:
            freq[letter] = freq[letter] + 1
        else:
            freq[letter] = 1
    print(freq)

char_frequency("hello")
