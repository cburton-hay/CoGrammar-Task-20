# ======= Working with the spaCy ===== #
import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("house")

print(word1.similarity(word2))
print(word1.similarity(word3))
print(word1.similarity(word4))
print(word2.similarity(word3))
print(word2.similarity(word4))
print(word3.similarity(word4))

print("Comparison of cat apple monkey banana car dog lorry house")

tokens = nlp("cat apple monkey banana car dog lorry house")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, (token1.similarity(token2)))

"""
Although all of these words are nouns, their similarity is based on what they actually are.
Animals have haigh similarity, transport has high similarity, fruits have high similarity.
I was expecting house and cat to have a high similarity as a cat that stays indoors can be called a house cat.

On small, there were mant user warning e.g. UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
Although it appeared to run quicker, it did not have the information required for an accurate comparison.
The results of the token comparisons differ greatly. In small lorry and banana have over 0.6 similarit but in medium is less that 0.2.
"""     

sentence_to_compare = "Why is my cat on the car?"
sentences = ["Where did my dog go?",
"Hello, there is my car."
"I've lost my car in my car.", 
"I'd like my boat back.",
"I will name my dog Diana.",
"Why is my cat on the car?"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + ": " + str(similarity))

