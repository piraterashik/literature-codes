
import math

def compare_dictionaries(d1, d2):
    score = 0
    total = 0
    for key in d1:
        total += d1[key]
    for key in d2:
        for i in range(d2[key]):
            if key in d1:    
                score = score + math.log(d1[key]/total)
            else:
                score = score + math.log(.5/total)
           
    if score == 0:
        score = math.log(.5/100) 
    return score
    



def clean_text(txt):
    
    """ Inputs a string of text and 'cleans'
    the text following the provided requirements """
        
    txt = txt.replace('.','')
    txt = txt.replace(',','')
    txt = txt.replace('?','')
    txt = txt.replace('!','')
    txt = txt.replace(':','')
    txt = txt.replace('!','')
    txt = txt.replace('"','')
    txt = txt.lower()
    
    return txt.split(' ')

def stem(word):
    if word[-1] == 's':
        if word[-3:] == 'ers':
            word = word[:-3]
        elif word[-3:] == 'ies':
            word = word[:-3]
        elif word[-5:] == 'ships':
            word = word[:-5]
        elif word[-5:] == 'ments':
            word = word[:-5]
        elif word[-4:] == 'ings':
            word = word[:-4]
        elif word[-4:] == 'ness':
            if word[-6:] == 'liness':
                word = word[:-6]
            else:
                word = word[:-4]
        else:
            word = word[:-1]
    elif word[-3:] == 'ing':
      if len(word) > 4:
         if word[-4] == word[-5]:
             word = word[:-4]
      else:
          word = word[:-3]
    elif word[-2:] == 'er':
        word = word[:-2]
    elif word[-3:] == 'ful':
        word = word[:-3]
    elif word[-2:] == 'al':
        word = word[:-2]
    elif word[-4:] == 'ment':
        word = word[:-4]
    elif word[-2:] == 'ly':
        word = word[:-2]
            
    elif word[-4:] == 'ship':
        word = word[:-4]
    elif word[-4:] == 'wise':
        word = word[:-4]
    
    # x = ['a','e','i','o','u','y','w']
    # if word[-1] in x:
    #     word = word[:-1]
    return word
    

def sample_file_read(filename):
       """A function that demonstrates how to read a
       Python dictionary from a file.
       """
       f = open(filename, 'r')    # Open for reading.
       d_str = f.read()           # Read in a string that represents a dict.
       f.close()

       d = dict(eval(d_str))      # Convert the string to a dictionary.

       print("Inside the newly-read dictionary, d, we have:")
       print(d)
      
def sample_file_write(filename):
        """A function that demonstrates how to write a
        Python dictionary to an easily-readable file.
        """
        d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
        f = open(filename, 'w')      # Open file for writing.
        f.write(str(d))              # Writes the dictionary to the file.
        f.close()   
        
    


class TextModel:
    
    
    def __init__(self,model_name):
        """ constructs a new TextModel object by accepting
        a string model_name as a parameter and initializing
        name, words and word_lengths """
        
        self.name = model_name
        self.words = ({})
        self.word_lengths = ({})
        self.stems = ({})
        self.sentence_lengths = ({})
        self.article = ({})        
        
    
    def __repr__(self):
         """Return a string representation of the TextModel."""
         
         s = 'text model name: ' + self.name + '\n'
         s += '  number of words: ' + str(len(self.words)) + '\n'
         s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
         s += '  number of stems: ' + str(len(self.stems)) + '\n'
         s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
         s += '  number of articles: ' + str(len(self.article)) 
         return s
     
    def add_string(self,s):
         """ Analyzes the string txt and adds its pieces
       to all of the dictionaries in this text model.""" 
         temp_sentence = s.replace('?', '.')
         temp_sentence = temp_sentence.replace('!', '.')
         sentence_list = temp_sentence.split(".")
       
         
         for sent in sentence_list:
             wrd = sent.split()
             n = len(wrd)
             if n in self.sentence_lengths:
                 self.sentence_lengths[n] += 1
             elif n != 0:
                 self.sentence_lengths[n] = 1
       
         word_list = clean_text(s)
         for w in word_list:
             if w in self.words:
                 self.words[w] += 1
             else:
                 self.words[w] = 1
                
             n = len(w)
             if n in self.word_lengths:
                self.word_lengths[n] += 1
             else:
                self.word_lengths[n] = 1
        
         #for articles
                
         for w in word_list:
             if w in ['a','an','the']:
                 if w in self.article:
                     self.article[w] += 1
                 else:
                     self.article[w] = 1
                
         
       
        
        #for stems
        
         for w in word_list:
             st = stem(w)
             if st in self.stems:
                self.stems[st] += 1
             else:
                self.stems[st] = 1
         
        
    def add_file(self,filename):
        """ adds all of the text in the file
        identified by filename to the model"""
        
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = ""
        for line in f:
            text += line[:]
        
        self.add_string(text)
    
    def similarity_scores(self, other):
        score_list = [0 for x in range(5)]
        score_list[0] = compare_dictionaries(other.words, self.words)
        score_list[1] = compare_dictionaries(other.word_lengths, self.word_lengths)
        score_list[2] = compare_dictionaries(other.stems, self.stems)
        score_list[3] = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        score_list[4] = compare_dictionaries(other.article, self.article)
        
        return score_list
    
    def classify(self, source1, source2):
        score1 = self.similarity_scores(source1)
        score2 = self.similarity_scores(source2)
        
        print("Scores for ",source1.name," ",score1)
        print("Scores for ",source2.name," ",score2)
        
        s1 = 0
        
        for i in range(len(score1)):
            if score1[i] > score2[i]:
                s1 += 1
            else:
                s1 -= 1
        if s1 > 0:
            print(self.name, "is more likely to have come from ",source1.name)
        else:
            print(self.name, "is more likely to have come from ",source2.name)
        
        
    def save_model(self):  
         """ saves the TextModel object self by 
         writing its various feature dictionaries to files"""
         
         f = open(self.name + '_' + 'words', 'w')      # Open file for writing.
         f.write(str(self.words))            # Writes the dictionary to the file.
         f.close()
         f = open(self.name + '_' + 'word_lengths', 'w')   
         f.write(str(self.word_lengths)) 
         f.close()
         f = open(self.name + '_' + 'stems', 'w')   
         f.write(str(self.stems)) 
         f.close()
         f = open(self.name + '_' + 'sentence_lengths', 'w')   
         f.write(str(self.sentence_lengths)) 
         f.close()
         f = open(self.name + '_' + 'article', 'w')   
         f.write(str(self.article)) 
         f.close()
         
    def read_model(self):
        """ reads the stored dictionaries for the called TextModel
        object from their files and assigns them 
        to the attributes of the called TextModel."""
        
        f = open(self.name + '_' + 'words', 'r')   # Open for reading.
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        d = dict(eval(d_str))      # Convert the string to a dictionary.
        self.words = d
        
        f = open(self.name + '_' + 'word_lengths', 'r') 
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        d = dict(eval(d_str))
        self.word_lengths = d
        
        f = open(self.name + '_' + 'stems', 'r') 
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        d = dict(eval(d_str))
        self.stems = d
        
        f = open(self.name + '_' + 'sentence_lengths', 'r') 
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        d = dict(eval(d_str))
        self.sentence_lengths = d
        
        f = open(self.name + '_' + 'article', 'r') 
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()

        d = dict(eval(d_str))
        self.article = d
        
        
        
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')
   

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')
  

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
         

def run_tests():
    """ your docstring goes here """
    source1 = TextModel('toxic')
    source1.add_file('toxic.txt')

    source2 = TextModel('therealslimshady')
    source2.add_file('therealslimshady.txt')

    new1 = TextModel('babyonemoretime')
    new1.add_file('babyonemoretime.txt')
    new1.classify(source1, source2)

    # Add code for three other new models below.
    
    new2 = TextModel('withoutme')
    new2.add_file('withoutme.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('doiwannaknow')
    new3.add_file('doiwannaknow.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('twinkletwinkle')
    new4.add_file('twinkletwinkle.txt')
    new4.classify(source1, source2)
         
         
        
        
        
    
         
    
        
     
        
        
                 
