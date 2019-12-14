import random

class MarkovChain(object):

    def __init__(self, fileName='MarKovChain/DataFiles/LovePoems.txt'):
        self.dictionary = {}
        self.open_file = open (fileName)
        self.words = self.splitWordsInFile()
        self.word_size = len(self.words)
        self.createDictionary()


    def splitWordsInFile(self):
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words
    
    
    def triples(self):
        if len(self.words) < 3:
            return
        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])
                
    def createDictionary(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.dictionary:
                self.dictionary[key].append(w3)
            else:
                self.dictionary[key] = [w3]
                    
    def generateText(self, size=100):
        seed = random.randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.dictionary[(w1, w2)])
        gen_words.append(w2)
        poem=' '.join(gen_words).lower()
        return poem[:poem.rfind('.')]
def resourceSelector(id):
    switcher={
            'love':"MarKovChain/DataFiles/LovePoems.txt",
            'math':"MarKovChain/DataFiles/MathPoems.txt",
            'misfit':"MarKovChain/DataFiles/MisFitPoems.txt"
                }
    func=switcher.get(id,"./DataFiles/MisFitPoems.txt")
    return func    
    