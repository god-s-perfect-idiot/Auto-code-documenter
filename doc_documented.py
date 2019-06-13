import time
from subprocess import call

filename=""
linecount=0
content=[]
funcs=[]
param=[]
param_unformatted=[]
ret=[]

def clear():

'''
Function
Inputs: none
Outputs: none
'''



    call(["clear"])

def welc():

'''
Function
Inputs: none
Outputs: none
'''



    clear()
    print("\n\n\t\t----------------------------------- \n\n\t\t\tDOCUMENTER \n\n\t\t-----------------------------------")
    time.sleep(1)
    clear()

def analyse():

'''
Function
Inputs: none
Outputs: none
'''



    global linecount,content,filename

    clear()
    filename=input("Enter Python file name: ")
    if(filename[-3:]!=".py"):
        filename=filename+".py"
    f=open(filename)
    linecount=sum(1 for line in open(filename))
    for i in range(linecount):
        line=f.readline()
        content.append(line)
    f.close()

def trim():

'''
Function
Inputs: none
Outputs: none
'''


    
    global content
    
    clear()
    for i in range(linecount):
        if(content[i][-1:]=="\n"):
            content[i]=content[i][:-1]

def untrim():

'''
Function
Inputs: none
Outputs: none
'''


    
    global content

    clear()
    for i in range(linecount):
        content[i]=content[i]+"\n"

def find_params(name):

'''
Function
Inputs: name
Outputs: none
'''



    global param,param_unformatted
    
    params=""

    name=list(name)
    for i in range(len(name)):
        if(name[i]=="("):
            start=i+1
        if(name[i]==")"):
            end=i
    for i in range(start,end):
        params+=name[i]
    params_formatted=params.split(",")
    if(params==""):
        params="none"
    param.append(params_formatted)
    param_unformatted.append(params)

def find_rets(name,start,end):

'''
Function
Inputs: name,start,end
Outputs: none
'''


    
    global ret

    rets=[]
    
    i=start
    while(i<end):
        s=content[i].split()
        if(s!=[]):
            if(s[0]=="return"):
                rets.append(s[1:])
        i=i+1  
    ret.append(rets)    
     

def functs():

'''
Function
Inputs: none
Outputs: none
'''


    
    global funcs
    
    clear()
    for i in range(linecount):
        if(content[i][:3]=="def"):
            funcs.append([content[i][3:-1],i])
            find_params(content[i][3:-1])

    for i in range(len(funcs)):
        if i!= len(funcs)-1:
            find_rets(funcs[i][0],funcs[i][1],funcs[i+1][1])
        else:
            find_rets(funcs[i][0],funcs[i][1],linecount)

def modify():

'''
Function
Inputs: none
Outputs: none
'''


    
    for i in range(len(funcs)):
        ret_st=""
        for j in  range(len(ret[i])):            
            ret_s=""
            for k in range(len(ret[i][j])):
                ret_s=ret_s+ret[i][j][k]
            if(j<len(ret[i])-1):
                ret_st=ret_st+ret_s+" and "
            else:
                ret_st=ret_st+ret_s
        if(ret[i]==[]):
            ret_st="none"
        if(len(ret[i])>1):
            ret_st=ret_st+"\nMutliple exits from function\n"    
        content[funcs[i][1]]=content[funcs[i][1]]+"\n\n'''\nFunction\nInputs: "+param_unformatted[i]+"\n"+"Outputs: "+ret_st+"\n'''\n\n"

def writeback():

'''
Function
Inputs: none
Outputs: none
'''


    
    name=filename[:-3]+"_documented"+".py"
    f=open(name,"w+")
    for i in range(linecount):
        f.write(content[i])
    f.close()      

welc()
analyse()
trim()
functs()
modify()
untrim()
writeback()
