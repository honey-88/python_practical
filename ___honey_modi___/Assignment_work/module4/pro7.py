#Write a python program to find the longest words.

def find_longest_word(word_list):  
    longest_word = ''  
    for word in word_list:    
          print(word, len(word))  


words = input('enter a  words : ')  
word_list = words.split()  
find_longest_word(word_list)