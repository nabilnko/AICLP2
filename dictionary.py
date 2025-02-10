original_text = "Hi,This is Nabil Kowsar Orbe.I study in Green University of Bangladesh."
spllited_words = original_text.split()
word_count = {}
for word in spllited_words:  
    word_count[word] = word_count.get(word, 0) + 1  
print(word_count)
