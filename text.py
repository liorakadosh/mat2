# -*- coding: utf-8 -*-
 
def revword (word:str) -> str:
   size=len(word)-1
   newWord=""
   i=0
   while (i<=size):
      newWord=newWord+word[size-i]
      i=i+1
   return (newWord)
      
def countword()->int:
    file= open('text.txt')
    save=file.readline()
    save=save.strip()
    i=0
    total=""
    end=""
    count=1
    for line in file:
        start=line+" "
        while(i<len(start)):
            end=revword(start[0:start.find(' ')])
            end=end.strip()
            if end.lower()==save.lower():
                count=count+1
            num=len(end)+1
            start=start[num:len(start)]
            total=total+" "+end    
    return(count)
  
            
        
    
    