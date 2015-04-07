"""Usage: address4forensics.py (-L|-P|-C) [-b <offset> | --partition-start <offset>] [-B [-s <bytes>]] [-l <address>] [-p <address>] [-c <address> -k <sectors> -r <sectors> -t <tables> -f <sectors>]
        
 
Arguments:
    TEXT  Message to be printed
    offset  the offset
    bytes  the bytes
    address  the address

Options:
    --count=N  number of times the message will be output
    --caps  convert the text to upper case
    --partition-start <offset>  same as -b
    -b <offset>  physical address of the start of the partition
    -s <bytes>  bytes per sectors
    -l <address>  logical address
    -p <address>  physical-known address
    -c <address>  cluster-known address
    -k <sectors>  number of sectors per cluster
    -r <sectors>  number of reserved sectors in partition
    -t <tables>  number of FAT tables
    -f <sectors>  length of each FAT table in SECTORS
"""

# Docopt is a library for parsing command line arguments
from docopt import docopt

if __name__ == '__main__':
   
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__)

    # Count is a mandatory option, caps is optional
    #count = int(arguments['--count'])
    #caps = arguments['--caps']

    print(arguments)

    if arguments['-L'] == True:
        if arguments['-b']:
            if arguments['-p']:
                result = int(arguments['-p'])-int(arguments['-b'])
                print(result)
    elif arguments['-P'] == True:
        if arguments['-b']:
            result = int(arguments['-b'])+((int(arguments['-c'])-2)*int(arguments['-k']))+int(arguments['-r'])+(int(arguments['-t'])*int(arguments['-f']))
            print(result)
            
    
    #for i in range(count):
        # In the definition, we expect one or more TEXT parameters
        # Each parameter is a word, or a text in quotes: "something like this"
        # If the user forgets about the quote, the program would print only "something"
        # Thus, we merge all the specified parameters with space
        #text = ' '.join(arguments['TEXT'])
        #if(caps):
            #print text.upper()
        #else:
            #print text
