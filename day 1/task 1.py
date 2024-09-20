import nltk
# The noun should be in the capital letter
sentence = 'I Love Cat and I Love dog and I Love Eagle'
is_noun = lambda pos: pos[:2] == 'NN'
tokenized = nltk.word_tokenize(sentence)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
print(nouns)
#for nouns
#if item[0] in "aeiou"-->
#sentence=sentence.replace(nouns[0], '(A Or An)'+nouns[0])
# print(sentence)
vowels = 'AEIOUaeiou'
for word in nouns:
    if word[0] in vowels:
        sentence = sentence.replace(word, 'an ' + word)
    else:
        sentence = sentence.replace(word, 'a ' + word)
print(sentence)