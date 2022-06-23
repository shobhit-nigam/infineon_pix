import nltk    #NLP algorithms
import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk import FreqDist

url = "https://www.infineon.com/"
html_obj = urlopen(url).read()
raw_data = BeautifulSoup(html_obj, 'html.parser').get_text()
# print(raw_data)
print("len of initial words =", len(raw_data))
tokens = nltk.word_tokenize(raw_data)


html_words = ['https', 'http', 'display', 'button', 'hover',
             'color', 'background', 'height', 'none', 'target',
             'WebPage', 'reload', 'fieldset', 'padding', 'input',
            'select', 'textarea', 'html', 'form', 'cursor',
            'overflow', 'format', 'italic', 'normal', 'truetype',
            'before', 'name', 'label', 'float', 'title', 'arial', 'type',
            'block', 'audio', 'inline', 'canvas', 'margin', 'serif', 'menu',
            'woff', 'content', 'fixed', 'media', 'position', 'relative', 'hidden',
            'width', 'clear', 'body', 'standard', 'expandable', 'helvetica',
            'fullwidth', 'embed', 'expandfull', 'fullstandardwidth', 'left', 'middle',
            'iframe', 'rgba', 'selected', 'scroll', 'opacity',
            'center', 'false', 'right']

generic_words = ['Overview', 'Solutions']

eliminate_words = html_words + generic_words

final_words = []

for w in tokens:
    if w.isalpha() and w not in eliminate_words:
        final_words.append(w)

print("len of final words =", len(final_words))

text = nltk.Text(final_words)

freqdist_obj = FreqDist(text)
freqdist_obj.plot(10)
