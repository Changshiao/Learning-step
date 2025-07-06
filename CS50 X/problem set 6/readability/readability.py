from cs50 import get_string
import re
text=get_string("Text:")
sentences = re.split(r'[.!?]', text)
num_sentences = len(sentences) - 1
words = re.findall(r'\b\w+\b', text)
num_words = len(words)
S = num_sentences
L=sum(c.isalpha() for c in text)
W = num_words
Le=L/W*100
Se=S/W*100
print(W)
print(S)
print(L)
index = round(0.0588 * Le - 0.296 * Se - 15.8)
if index<1:
    print("Before Grade 1")
elif index>16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
