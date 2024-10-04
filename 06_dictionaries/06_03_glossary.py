# this code will make a python glossary 

python_glossary = {'Boolean'  : "True or False",
                   'String' : 'the value of this is letters or words',
                   'Int' : "the value of this is numbers without decimals",
                   'Float' : 'the value of this is numbers with decimals',
                   'If statement' : "will check if something is true before call it's block of code"}

key_list = list(python_glossary.keys())

for key in key_list:
    print ("\n" + key) 
    if key == 'Boolean':
        print (':' + python_glossary['Boolean'])
    elif key == 'String':
         print (':' + python_glossary['String'])
    elif key == 'Int':
         print (':' + python_glossary['Int'])
    elif key == 'Float':
         print (':' + python_glossary['Float'])
    elif key == 'If statement':
         print (':' + python_glossary['If statement'])



    
    
