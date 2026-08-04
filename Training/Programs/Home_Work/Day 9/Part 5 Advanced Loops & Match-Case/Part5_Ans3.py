action ="refund" 
days =12
match action:
    case "refund"|"return" if days <=14:
     print("Approved")  
    case "refund" | "return":
      print( "Window Expired") 
    case _:
      print("Connecting to operator...")

