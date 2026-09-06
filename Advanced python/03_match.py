# **** MATCH CASE **** 
# Python 3.10 introduced the match statment, which is similar to the switch statement found in other programming language. 

# The basic syntax of the match statement involves matching a variable against several cases using the case keyword.

def http_status(status):
 match status:
    case 200:
        return "ok"
    case 404:
        return "Not Found"
    case 500:
        return "Internal Server Error"
    case _:
        return "unknown stnatus"
    
 # Usage
 print(http_status(200)) #output: OK

        