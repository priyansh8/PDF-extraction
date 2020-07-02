from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
import re
import spacy
from os import path
from glob import glob 
from tika import parser

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
            if(re.findall("secure", i, re.IGNORECASE)):
                li3.append(i)

        print("DOCUEMNT ",listOfDoc[g])

        sp=fulldoc.split(".")

        z=0
        sentence=[]

        pNOI=0
        pSenior=0
        for i in li3:
            i=i.split(" ")
            a=0
            b=0
            c=0
            f=0
            r=0
            x=""
            
            for j in i:
                j=j.lower()
                if j=="status":
                    r=1
                    x=x+j+" "
                if j=="notes":
                    f=1
                    x=x+j+" "
                if j=="senior":
                    a=1
                    x=x+j+" "
                if j=="secured" or j=="unsecured":
                    b=1
                    x=x+j+" "
                if j=="subordianted" or j=="unsubordinated":
                    c=1
                    x=x+j+" "

            if (a+b+c+f+r)>=2:
                sentence.append(x)
                
                z=1
                print(" ")

        count_key=[]
        g=0
        sent=""
        fg=0
        for i in sentence:
            a=0
            b=0
            c=0
            f=0
            r=0
            i=i.split(" ")
            for j in i:
                j=j.lower()
                if j=="status":
                    r=1
                        
                if j=="notes":
                    f=1
                        
                if j=="senior":
                    a=1
                        
                if j=="secured" or j=="unsecured":
                    b=1
                        
                if j=="subordianted" or j=="unsubordinated":
                    c=1
            count_key.append(a+b+c+f+r)
            if b==1 and c==1:
                print(i)
                xc=0
                kj=0
                lk=0
                
                for x in i:
                    x=x.lower()
                    
                    if x=="secured":
                        xc=1
                    if x=="unsecured":
                        xc=2

                    
                    if x=="unsubordinated":
                        kj=1
                    if x=="subordinated":
                        kj=2
                    if x=="senior":
                        lk=1

                if kj==1:
                    if lk==1:
                        print("Seniority- Senior Unsubordinated")
                        pSenior=1
                    else:
                        print("Seniority- Unsubordinated")
                        pSenior=1
                if kj==2:
                    if lk==1:
                        print("Seniority- Senior subordinated")
                        pSenior=1
                    else:
                        pSenior=1
                        print("Seniority- Subordinated")

                if xc==1:
                    print("NOI- Secured")
                    pNOI=1
                if xc==2:
                    print("NOI- Unsecured")
                    pNOI=1
                                              
                
                fg=1
                break
            
            if (a+b+c+f+r)>g:
                sent=i
                g=a+b+c+f+r
        if fg==0:
            #print(sent)
            xc=0
            kj=0
            lk=0
            for x in sent:
                    x=x.lower()
                    
                    if x=="secured":
                        xc=1
                    if x=="unsecured":
                        xc=2

                    
                    if x=="unsubordinated":
                        kj=1
                        
                    if x=="subordinated":
                        kj=2
                    if x=="senior":
                        lk=1
                
            if kj==0 and lk==1:
                print("Seniority- Senior")
                pSenior=1
            elif kj==1:
                print("Seniority- Unsubordinated")
                pSenior=1
            elif kj==2:
                print("Seniority- Subordinated")
                pSenior=1

            if xc==1:
                print("NOI- Secured")
                pNOI=1
            if xc==2:
                print("NOI- Unsecured")
                pNOI=1
                               
                
        if z==0 or pSenior==0:
            a=0
            b=0
            c=0
            f=0
            r=0
            w=0
            #print("full extraction")
            for i in sp:
                i=i.split(" ")
                x=""
                for j in i:
                    j=j.lower()
                    if j=="debt":
                        w=1
                        
                    if j=="status" or j=="status:":
                        r=1
                        
                    if j=="notes":
                        f=1
                        
                    if j=="senior":
                        
                        if a==0:
                            print("Seniority- Senior")
                        a=1
                        
                    if j=="secured" or j=="unsecured":
                        
                        if b==0 and pNOI==0:
                            print("NOI- ",j)
                        b=1
                    if j=="subordianted" or j=="unsubordinated":
                        
                        if c==0:
                            print("Seniority- ",j)
                        c=1
                                  
               
    except:
        print("Exception occured in doc ",g)

    
