# this will clean up the code of 06_03 and add to the glossary

python_glossary = {'Boolean'  : "True or False",
                   'String' : 'the value of this is letters or words',
                   'Int' : "the value of this is numbers without decimals",
                   'Float' : 'the value of this is numbers with decimals',
                   'If statement' : "will check if something is true before call it's block of code",
                   'elif' : 'will check if soemthing else is true before calling its block of code',
                   'else' : "if the  if statement doesn't fire this will instead",
                   'for loop' : 'will continue to print something as long as items remain',
                   'print' : 'this will print anything you put in the parenthesis',
                   'list' : 'this contains a set of strings or ints'
                   }


for key, value in python_glossary.items():
    print ('\n' + key)
    print (value)
