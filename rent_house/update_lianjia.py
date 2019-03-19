#-*- 


from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db1 = client["copy"]
myset1 = db1['lianjia']

db2 = client['update']
myset2 = db2["lianjia"]

house_infos = myset1.find({},{'_id':0})

# myset2.create_index('addr')
for data in house_infos:
    for key, value in data.items():
        infos = {"addr":key, "infos":value}
        
        myset2.save(infos)



# house_infos

