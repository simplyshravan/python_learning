#first uncomment below two lines and download nltk data
#import nltk
#nltk.download()

from nltk.corpus import wordnet

if not wordnet.synsets('hello'):
  print('Notenglish')
else:
  print('english')
from nltk.corpus import words
word_list = words.words()

#print(len(word_list))
#prints 236736
#print(word_list)