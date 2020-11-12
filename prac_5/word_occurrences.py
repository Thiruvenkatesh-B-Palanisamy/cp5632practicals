word_count_dict = {}
text = input("Text").split()
for word in text:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
print(word_count_dict)
text = list(word_count_dict.keys())
text.sort()
length_align = max(len(word) for word in text)
for word in text:
    print("{:{}} : {}".format(word, length_align, word_count_dict[word]))



