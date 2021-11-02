"""
CP1404/CP5632 Practical
word occurrences
"""
word_counter = {}
word_list = []
maximum_word_length = 0

text = input("Text: ").lower()
split_text = text.split(" ")
for word in split_text:
    word_list.append(word)
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
sorted_list = sorted(word_list)

for word in sorted_list:
    if len(word) > maximum_word_length:
        maximum_word_length = int(len(word))

for word in sorted_list:
    print("{:{}} = {}".format(word, maximum_word_length, word_counter[word]))

