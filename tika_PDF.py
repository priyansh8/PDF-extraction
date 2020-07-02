from tika import parser # pip install tika
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import re
import spacy
from os import path
from glob import glob


def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

listOfDoc = find_ext('C:\\Users\\user\\Desktop\\Resources\\Documents\\',"pdf")

scanlist = []

for g in range(0,len(listOfDoc)):
    try:
        p=listOfDoc[g]
        raw = parser.from_file(p)
        fulldoc=raw['content']

        fulldoc = fulldoc.replace('\n',' ')
        fulldoc = re.sub(r' +',' ', fulldoc)
        docarr = sent_tokenize(fulldoc)

        if len(fulldoc)==0:
            print("No Text Extracted Require OCR")
       

        li3 = []
        for i in docarr:
            if(re.findall("issue price", i, re.IGNORECASE)):
                li3.append(i)
        print(" ")
        print(" ")
        print("DOCUEMNT ",listOfDoc[g])
       
        for i in li3:
            print(i)

    except:
        print("Exception occured in doc ",g)
