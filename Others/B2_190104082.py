# ID: 190104082
# Date: 22/12/2022
# Group: B2
# Online: 2

import re
while True:
    

    inputStr=input("Input String:")




    if (re.match("c[a-z]*_[0-9][0-9]+",inputStr)):
        print("String follows the pattern.")
    else:
        print("String does not folloe the pattern.")
    
    

