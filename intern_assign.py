import re
import pandas as pd
string=''
question=[]
answer_list=[]
answer=[]
newfile=[]

with open("/home/ubuntu/Desktop/Input","r")as file:
    text = file.readlines()
    #print (text)
   
    pat='.*[?=?]$'
    for i in text:
        m=re.search(pat,i)
        if(m!=None):
            question.append(i)
        else:
            answer.append(i)    
         
    for i in answer:
        string=string+i
        #print(string)
    pattern=re.compile(r"Answer:")
    matches=pattern.finditer(string)
    for match in matches:
        newfile.append(match.span())
    for i in range(len(newfile)):
        if (i==len(newfile)-1):
            
            answer_list.append(string[newfile[i][0]:])
        else:    
            answer_list.append(string[newfile[i][0]:newfile[i+1][0]])   
print(len(question))        
print(len(answer_list))   




dict = {'question': question, 'answer': answer_list}  
     
df = pd.DataFrame(dict) 
  
# saving the dataframe 
df.to_csv('output_intern.csv',index=False)
#df=pd.DataFrame()





#df['question']=question
#df['answer']=answer

#df.index+=1

#df.to_csv('output_internship.csv',index=True)
        
        
        
        
        
        

