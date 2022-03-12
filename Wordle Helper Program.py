#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random


# In[2]:


data=pd.read_csv(r"C:\Users\User\Desktop\Wordle.txt")


# In[3]:


#data=data[~data['which'].str.contains("s")]
#data


# In[4]:


word_list=[]
list_words=[]
data_words=[]
#data_words=[data['which'][i] for i in range(len(data))]
clean_data_words=[]


for i in range(len(data)):
    m=list(data['which'][i])
    for i in m:
        if not m[-1]=='s':
            data_words.append(m)


k=[]
for i in range(len(data)):
    m=list(data['which'][i])
    word_list.append(m)
    list_words.append(word_list)
    
for i in range(len(data_words)):
    word=''.join(data_words[i])
    if word in clean_data_words:
        pass
    else:
        clean_data_words.append(word)
        
        
        
        


# In[5]:


go_first=random.choice(data_words)

go_first


# In[6]:



def wordle_game():
    
                
    go_first=random.choice(clean_data_words)
    print("let's start the game. You can start with this word  "+go_first)
    a=int(input(' 1 to continue, 0 to stop'))
    if a==1:
        print(guess_matches())
    
        
    


# In[7]:


def input_letters():
    a1, b1=input("if you matched with something, type the letter and the position, space-separated").split(' ')
    a2,b2=input("For the machine's help, enter a word that did not match with anything (including position)")
    b1=int(b1)
    b2=input(b2)
    flag_str='s'
    for i in range(len(list_words)):
        for j in word_list[i]:
            if word_list[i][b1]==a1 and word_list[i][b2]!=a2:
                answer=''.join(word_list[i])
                if flag_str!=answer:
                    print("This is one suggestion we can provide. You should guess which one it is among these wisely!")
                    print(answer)
                    flag_str=answer


# In[14]:


def guess_matches():
    t=[]
    final=0
    no_quant=1
    while final!=5:
        ans=input("Did you match with something? (Y/N)")
        if ans=='Y':
            print(input_letters())
            final+=1
        elif ans=='N' and no_quant<2:
            go_again=random.choice(clean_data_words)
            print("Here you can try again with this word "+go_again)
            no_quant+=1
            continue
        elif ans=='N' and no_quant==2:
            pair_1, pair1_2=input("Input space separated characters and numbers of a word that didn't match with anything").split(' ')
            pair_2, pair2_2=input("Input space separated characters and numbers of another word that didn't match with anything").split(' ')
            pair_3, pair3_2=input("Input space separated characters and numbers of another word that didn't match with anything").split(' ')
            
            pair1_2=int(pair1_2)
            pair2_2=int(pair2_2)
            pair3_2=int(pair3_2)
            flag_str='s'
            for i in range(len(list_words)):
                for j in word_list[i]:
                    if word_list[i][pair1_2-1]!=pair_1 and word_list[i][pair2_2]!=pair_2 and  word_list[i][pair3_2]!=pair_3: 
                        answer=''.join(word_list[i])
                        if flag_str!=answer:
                            print("This is one suggestion we can provide. You should guess which one it is among these wisely!")
                            print(answer)
                            flag_str=answer
        if final==5:
            print("That's all the help I can provide you for now! You should guess yourself now else the game would be no fun!")
           
    
    
    
    #a2, b2=input("Did you match with anything else?If yes, then type the letter and the position in the same format. If not then write the same letter you matched with and the position, again please!").split(' ')
    #b2=int(b2)
    #a3, b3=input("For the machine's help")
    #flag_str='s'
    #for i in range(len(list_words)):
        #for j in word_list[i]:
            #if word_list[i][b1]==a1 and word_list[i][b2]==a2:
                #answer=''.join(word_list[i])
                #if flag_str!=answer:
                    #print(answer)
                    #flag_str=answer
                


# In[ ]:


wordle_game()


# In[ ]:





# In[ ]:





# In[ ]:




