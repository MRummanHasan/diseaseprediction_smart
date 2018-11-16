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
########################     OR    #####################
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

Doc_to_dept = {
    'ENT': ['D0','D1'],
    'General': ['flu','D3'],
    'Cancer': ['oral','D4'],
    'Skin': ['D5','D6'],
    'D4': ['D7','D8'],
    'D5': ['D0','D3'], 
    'D6': ['D2','D4']
}

# Check Department
inverse = [(value, key) for key, value in symp_per.items()]
highVal = max(inverse)[0]
print (highVal, "high index")

# key at highest value
highValKey = list(symp_per.keys())[list(symp_per.values()).index(highVal)]
print(highValKey, "name")

for dtdk,dtdv in Doc_to_dept.items():
    print(dtdv)
    if dtdv.__contains__(highValKey):
        print("success this depart: ", dtdk)
        break
    else:
        print("no suc")
print("\nhmmm")

