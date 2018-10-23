def revSentence(sentence):
    
    words = sentence.split(" ")
    revsen = []
    aa=[]
    for idx in range(len(words)-1, -1, -1):
        revsen += [words[idx]]
    return " ".join(revsen)
    '''
    words = sentence.split()
    print (words)
    print type(reversed(words))
    sentence_rev = " ".join(reversed(words))
    print sentence_rev
    '''
sentence = "The quick brown fox jumped over the lazy dog."
#sentence = "hello world"
print revSentence(sentence)