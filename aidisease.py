import pymysql


class Disease():
    def __init__(self, name, mainSymp, nSymp):
        self.name = name
        self.mainSymp = mainSymp
        self.nSymp = nSymp
        self.nAns = []


# ## fetch data from junction table
# ## connection work
# conn = pymysql.connect(host='localhost', user='root', password='', db='HealthSystem')
# a = conn.cursor()
# ##end connection work

# ## Query
# sql = 'SELECT D.disease_name, S.symptom_name FROM diseases AS D JOIN disease_symptoms_bridgetable AS DC ON D.disease_id = DC.disease_id JOIN symptoms AS S ON S.symptom_id = DC.symptom_id'
# a.execute(sql)
# data = a.fetchall()

# for x in range(0, 3):
#     print ("We're on time %d" % (x))

# MainSymp : symp1, symp2....
listofAllsymp = {
    "Deep Cough": ["ear Pain", "sore Swelling", "change in Voice", "difficulty in breathing"],
    "Jaw Pain": ["sore Throat", "teeth Loose", "painful Chewing"],
    "MainSymp3": ["weakness", "fever", "cheek swelling", "other", "other2"],
    'lung problems': ['cough with blood', 'shortness of breath'],
    'skin problems': ['redness of face', 'moles on skin'],
    'Diarrhea': ['watery stool', 'vomiting', 'abdominal cramps', 'belly pain'],
    'eating or weight problems': ['W', 'fever']
}
# Populate Disease objects
dArray = []
i = 0
for k, v in listofAllsymp.items():
    dArray.append(Disease("D"+str(i), k, v))
    print(dArray[i].name, dArray[i].mainSymp, dArray[i].nSymp)
    i = i + 1
print()

# ASK SYMPTOMS
for d in dArray:
    ans = input("Answer with  'y'  or  'n'\nDo you have/feel " + str(d.name)+" > ")

    if ans == "y":
        for n in d.nSymp:
            # print(n)
            NSans = input("\nDo you have/feel "+str(n)+" : ")
            if NSans == 'y':
                d.nAns.append(NSans)

for docDetail in dArray:
    print(docDetail.name,docDetail.mainSymp,docDetail.nSymp,docDetail.nAns)
print()

# Calculate percentage of symptom occurance
symp_per = {}
for dp in dArray:
    ansSize = len(dp.nAns)
    tsymp = len(dp.nSymp)

    per = (ansSize / tsymp) *100
    symp_per[dp.name] = per
    
print(symp_per)

