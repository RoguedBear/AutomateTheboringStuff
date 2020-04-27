import time, sys
indent = 0
indentIncreasing = True

try:
    while True: 
        print (' ' * indent, end='')
        print('******', end='\r')
        
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
                print( ' ' * indent, end='\r')

        else:
            indent -= 1
            print(' ' * (26 - indent), end='\r')
            if indent == 0:
                indentIncreasing = True
                
except KeyboardInterrupt:
    sys.exit()
