from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_excel("workbook_list_match.xlsx") 
#df['Item']=df['Item'].apply(lambda i: (' '.join(i.split('-'))).upper())
#df['Item']=df['Item'].apply(lambda i: (' '.join(i.split('/'))))
#df['Item']=df['Item'].apply(lambda i: (' '.join(i.split('_'))))
comment_words = ' '
stopwords = set(STOPWORDS) 

for val in df.GroupNbr: 
    val = 'Group'+str(val)
    #val = str(val) 
    tokens = val.split() 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower()           
    for words in tokens:
        comment_words = comment_words + words + ' '
        
wordcloud = WordCloud(width = 1000, height = 1000, collocations=False,
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
                         
plt.figure(figsize = (17, 17), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
plt.savefig('wordcloud.png', dpi=200)
