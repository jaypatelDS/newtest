import pymongo

client = pymongo.MongoClient("mongodb+srv://jaypatel93:jayH38387@jaydemo1.rlpurkb.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "jay",
    "email" : "jaykumarhpatel99@gmail.com",
    "surname" : "Patel"
}
db1 = client ['mongotest']
coll = db1['test']
coll.insert_one(d )

