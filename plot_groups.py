import pandas as pd
import matplotlib.pyplot as plt
import random
#create data frame that has the result of the MDS plus the cluster numbers and titles
df = pd.read_excel('workbook_list_match.xlsx') 

#group by cluster
groups = df.groupby('GroupNbr')
uni_grp=df['GroupNbr'].unique()
#generating random colors for pplot
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(len(uni_grp))]

# set up plot
fig, ax = plt.subplots(figsize=(17, 17)) # set size
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

#iterate through groups to layer the plot
#note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
for name, group in groups:
    #print(name)
    ax._get_lines.get_next_color()
    ax.plot(group.GroupNbr, group.Item, marker='*', linestyle='', ms=16, 
            label=name, color=color[name -1 ], 
            mec='none')
    #ax.scatter( group.GroupNbr,group.Item)
    #ax.set_aspect('auto')
    ax.tick_params(\
       axis= 'x',          # changes apply to the x-axis
      which='both',      # both major and minor ticks are affected
       bottom='off',      # ticks along the bottom edge are off
      top='off',         # ticks along the top edge are off
      labelbottom='off')
    ax.tick_params(\
        axis= 'y',         # changes apply to the y-axis
        which='both',      # both major and minor ticks are affected
        left='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
       labelleft='off')
    
    
ax.legend(numpoints=1)  #show legend with only 1 point
#add label in x,y position with the label as the film title
for i in range(len(df)):
     ax.text(df.loc[df.index[i], 'GroupNbr'], df.loc[df.index[i], 'Item'], df.loc[df.index[i], 'Item'], size=8)  

plt.savefig('snap.png', dpi=200)
#plt.show() #show the plot
