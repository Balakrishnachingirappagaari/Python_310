import random

def join():
    words=["Balakrishna","SDE","Siemens","Bangalore"]
    sentance=' '.join(words)
    print(sentance)
    
def split():
    words="Balakrishna"
    anotherWords="Balakrishna SDE Siemens Bangalore"
    split=list(words)
    anothersplit=anotherWords.split('x')
    print (split)
    print(anothersplit)
    
def randomnumbers():
    x=random.randrange(0,10)
    print(x)
    
def create100randomnumbers():
    for x in range(3):
        print(random.uniform(0,5))
    
create100randomnumbers()    
#join()
#split()
#randomnumbers()
