import random
def testBinSearchClosest():
    db = random.sample(range(500),100)
    print("Binary search closest function test")
    db.sort()
    print(db)
    for _ in range(10):
        key = random.randrange(500)
        index = binSearchClosest(db, key)
        print("The closest value to", key, ":", db[index], "at index", index)

def binSearchClosest(db, key):
    db.sort()
    i, result, min = 0, 0, key + 1
    if key in db:
        result = db.index(key)
    else:
        if len(db) == 0:
            return None
        for i in range(0, len(db)):
            if (abs(db[i] - key)) < min:
                min = abs(db[i] - key)
                result = i
    return result

binSearchClosest([],3)
