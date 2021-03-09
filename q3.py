'''
Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
'''

paragraph = "Hi, my name is mane si"

word_list = paragraph.split(' ')
for i in range(len(word_list)):
    for j in range(i, len(word_list)-1):
        first_word = list(word_list[i])
        actual_word = ''.join(first_word)
        first_word.sort()
        second_word = list(word_list[j+1])
        second_word.sort()
        
        if first_word == second_word:
            print(actual_word)