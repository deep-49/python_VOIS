fees={}

def pay(sid,amount):
    fees[sid]=amount

def getFee(sid):
    return fees[sid]