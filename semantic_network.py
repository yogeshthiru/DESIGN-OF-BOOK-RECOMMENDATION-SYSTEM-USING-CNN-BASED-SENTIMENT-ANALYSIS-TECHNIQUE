# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:17:39 2019
D:/project/datasets/main/test.txt
@author: Yogesh
"""
import nltk 
from itertools import product
from nltk.corpus import state_union
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.corpus import wordnet 
import statistics 

 
stop_words = set(stopwords.words('english')) 

 
sentences= ['pleasure', 'gifted', 'happy', 'absolutely', 'love', 'never',  'brilliant', 'eating', 'aliveVelvet', 'face', 'become', 'good', 'even', 'flirting', 'happens', 'says', "n't", 'want', 'hear', 'get', 'heated', 'drift', 'Then', 'change', 'velvet', 'different', 'wants', 'starts', 'head', 'around', 'released', 'help', 'deal', 'outside', 'club', 'read', 'hook', 'start', 'visits', 'old', 'mysterious', 'annual', 'take', 'shadowy',  'invited', 'leave', 'soon', 'deeper', 'ever', 'expectedI', 'loved', 'moved', 'right', 'along', 'brisk', 'kept', 'turning', 'appealing', 'nature', 'liked', 'developed', 'recommend', 'enjoys', 'shifter/monster', 'definitely', 'look', 'hooked', 'beginning', 'running', 'past', 'trying', 'alive', 'blaming', 'takes', 'finds', 'wanting', 'keep', 'safe', 'finally', 'stop', 'grief', 'Is', 'Read', 'find', 'handyThis', 'huge', 'true', 'tissues', 'ready', 'cried', 'laughed', 'smiled', 'felt', 'anger', 'reading', 'awesome', 'fantastic', 'beautiful', 'tragic', 'totally', 'favorite', 'feel', 'really','much', 'expected', 'say', 'halfway', 'finish', 'sweet', 'emotional', 'humor', 'many', 'short', 'small', 'repeated', 'like', 'easy', "'s", 'essentially', 'came', 'hating', 'give', 'redeeming', 'mean', 'bella', 'irrelatable', 'main', 'differently', 'Do', 'hate', 'overhyped', 'disappointed', 'gross', 'also', 'great', 'super', 'annoying', 'problematic', 'literally', 'watches', 'girl', 'cool', 'romantic', 'review', 'saying', 'born', 'raised', 'Not', 'french', 'anytime', 'beloved', 'little', 'sentimental', 'usually', 'accurateBut', 'brought', 'made', 'almost', 'mesaying', 'pronounced', 'kitchen', 'cornbread', 'call', 'tell', 'middle', 'supposed', 'mix', 'Moving', 'onNeedless', 'stepped', 'back', 'found', 'literary', 'fell', 'hard', 'storyline', 'best', 'make', 'cajun', 'magic', 'protected', 'took', 'storms', 'battling', 'guilt', 'suffer', 'amazing', 'pushing', 'together', 'staring', 'punching', 'heartThe', 'riveting', 'scorching', 'away', 'gon', 'ask', 'moving', 'slow', 'exhaustingAdored', 'finishedI', 'need', 'thank', 'gracing', 'bringing',  'booksbut', 'makes', 'spent', 'indeed', 'sweeping', 'chased', 'ex-lover',  'typical', 'well', 'mother', 'relate', 'grow', 'thinks', 'begins', 'ignite', 'inside', 'frightens', 'antagonistic', 'believe', 'wear', 'yoga']
sentences1=['jumbo', 'even', 'looking', 'went', 'big','fails', 'get', 'goes', 'crow', 'mis', 'understood', 'residing', 'felt', 'missing', 'left', 'unfinished', 'tied', 'completely', 'donot like', 'wayTwilight', 'saga', 'read', 'early', 'teen', 'reread', 'mean', 'bella', 'totally', 'irrelatable', 'necessary', 'female', 'seriously', 'lay', 'middle', 'forest', 'dumped', 'many', 'describedOk', 'dude', 'not','eyesThis', 'loads', 'crapSeriously', 'considering', 'rome', 'good', 'ever', "n't", 'believe', 'put', 'stunk', "'s", 'worse', 'continued', 'reading', 'dumb', 'always', 'avid',  'worst', 'againThis', 'reads', 'horribly', 'cliched', 'forced', 'string', 'awkward', 'seems', 'rich', 'complex', 'almost', 'text', 'descriptive', 'little', 'weird', 'narration', 'unsubtle', 'plainly', 'stated', 'theatrically', 'cheesy', 'similar', 'sparse', 'prose', 'purely', 'masturbatory', 'unpopular', 'author', 'thoroughly', 'convinced', 'dare', 'flood', 'undiscovered', 'loud', 'comedic', 'full', 'fail', 'write', 'better', 'saddened', 'bad',  'thought', 'used', 'hardest', 'afford', 'ironically','poorly',  'Even', "'ve", 'happen', 'add', 'numerous', 'less', 'glowing', 'already', 'received', 'maybe', 'validate', 'virtual', 'negative', 'opinionThe', 'basic', 'entire', 'inner', 'animus', 'expand', 'understanding', 'Unfortunately', 'real', 'quickly', 'blurs', 'live', 'bad', 'write/tell', 'probably', 'rather', 'watch', 'father', 'take','tiresome', 'shower', 'murmured', 'blindly', 'terrible', 'whole','boring', 'nightmareThe', 'ugly', 'crapI', 'prepared', 'remotely', 'interested', 'titillated', 'sheep', 'chick', 'nasty', 'far', 'guy', 'tired', 'third', 'possessed', 'pull', 'broke', 'first', 'decided', 'handful', 'obscure', 'etc', 'include', 'back', 'ai', 'worthless','waste', 'standard', 'validating', 'also', 'second', 'reviews', 'buying/readingShame', 'meThe', 'best', 'makes', 'reader', 'new', 'describe', 'mountainous', "'m", 'sure', 'insulting', 'muslim', 'attentionEither', 'absolute', 'intially', 'never', 'buy', 'advertised', 'came', 'looked', 'hard', 'follow', 'impossible', 'idiot', 'wrote', 'readers', 'hatred','unrealistic','harsh']

f=open("D:/project/datasets/main/te.txt")
for x in f:
    focus_sentence = x.strip()
    c=focus_sentence.split()
    d=[]
    out=[]
    
    tokenized = c 
    for i in tokenized:
        wordsList = nltk.word_tokenize(i) 
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        d.extend(tagged)
        #print(d)
        k=[]
    for i in range(0,len(d)):

        if d[i][1]=='VB':
            k.append(d[i][0])
        if d[i][1]=='VBD':
            k.append(d[i][0])
        if d[i][1]=='VBG':
            k.append(d[i][0]) 
        if d[i][1]=='VBN':
            k.append(d[i][0])
        if d[i][1]=='VBP':
            k.append(d[i][0])
        if d[i][1]=='VBZ':
            k.append(d[i][0])
        if d[i][1]=='JJ':
            k.append(d[i][0])
        if d[i][1]=='JJR':
            k.append(d[i][0])
        if d[i][1]=='JJS':
            k.append(d[i][0])
        if d[i][1]=='RB':
            k.append(d[i][0])
        if d[i][1]=='RBR':
            k.append(d[i][0])
        if d[i][1]=='RBS':
            k.append(d[i][0])
        if d[i][1]=='RP':
            k.append(d[i][0])
    print("\nTagged words of current review")        
    print(k)
    eater=[0]
    allsyns1 = set(ss for word in sentences for ss in wordnet.synsets(word))
    allsyns2 = set(ss for word in k for ss in wordnet.synsets(word))
    allsyns3 = set(ss for word in sentences1 for ss in wordnet.synsets(word))
    out=[]
    mut=[]
    for s1,s2 in product(allsyns1, allsyns2):
        best=wordnet.wup_similarity(s1, s2)
        if(best==None):
            best=0
        else:
            best=best
        best=best*100
        rounds=int(best)
        if(rounds>80):
            da=s2
            sog=da.name().split(".")[0].replace('_',' ')
            out.append(sog)
            #print(rounds)
            #gg.append(s2)
            eater.append(rounds)
            
    #print(f)
    #print(out)
    #print(gg)        
    #print(eater)
    x3 = statistics.mean(eater)
    print("Mean is :", x3) 
    
    
    
    meater=[0]
    for s1,s2 in product(allsyns3, allsyns2):
        gest=wordnet.wup_similarity(s1, s2)
        if(gest==None):
            gest=0
        else:
            gest=gest
        gest=gest*100
        roundt=int(gest)
        if(roundt>80):
            sa=s2
            hog=da.name().split(".")[0].replace('_',' ')
            mut.append(hog)             
            #f.append(s2)
            #print(roundt)
            meater.append(roundt)
    #print(meater)
    #print(f)
    #print(mut)
    x1 = statistics.mean(meater)
    print("Mean is :", x1)
    
    if(x1>x3):
        #str1=" "
        new_path = 'D:/project/datasets/main/tagging/type2.1.txt'
        new_days = open(new_path,'a')
        new_days.write(focus_sentence+"\n"+"\n")
        #sentences1.extend(k)
        for i in out:
            if i not in sentences1:
                sentences1.append(i) 
       
        print(focus_sentence)
        print("type2-It's a negative review")
        
    else:
        #str2=" "
        new_path1 = 'D:/project/datasets/main/tagging/type1.1.txt'
        new_days1 = open(new_path1,'a')
        new_days1.write(focus_sentence+"\n")
        #sentences.extend(k)
        for j in mut:
            if j not in sentences:
                sentences.append(j) 
        
        print(focus_sentence)
        print("type1-It's a positive review")
    
    out.clear()
    mut.clear()
    d.clear()
    k.clear()
    eater.clear()
    meater.clear()
        
        
print("...........................COMPLETED.......................................")               
print("\nPositive Tagged words\n")     
print(sentences)
print("\nNegative Tagged words\n")
print(sentences1)  

  
   
    
        
        
    
    
    
        
       

