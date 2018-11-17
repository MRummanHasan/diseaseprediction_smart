import pymysql
from scipy.spatial import distance
user_location = [2,3]
user_price = 500

class Disease():
    def __init__(self, name, mainSymp, nSymp):
        self.name = name
        self.mainSymp = mainSymp
        self.nSymp = nSymp
        self.nAns = []


# fetch data from junction table
# connection work
conn = pymysql.connect(host='localhost', user='root',
                       password='', db='HealthSystem')
a = conn.cursor()
# end connection work

# Query
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
    'Eating or Weight Problems': ['W', 'fever']
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
    ans = input("Answer with  'y'  or  'n'\nDo you have/feel " +                str(d.name)+" > ")
    if ans == "y":
        for n in d.nSymp:
            # print(n)
            NSans = input("\nDo you have/feel "+str(n)+" : ")
            if NSans == 'y':
                d.nAns.append(NSans)

# print details
for docDetail in dArray:
    print(docDetail.name, docDetail.mainSymp, docDetail.nSymp, docDetail.nAns)
print()

# Calculate percentage of symptom occurance
symp_percent = {}
for dp in dArray:
    ansSize = len(dp.nAns)
    tsymp = len(dp.nSymp)
    per = (ansSize / tsymp) * 100
    symp_percent[dp.name] = per
print(symp_percent)

Doc_to_dept = {
    'ENT': ['D0', 'D1'],
    'General': ['flu', 'D3'],
    'Cancer': ['oral', 'D4'],
    'Skin': ['D5', 'D6'],
    'Dentist': ['D7', 'D8'],
    'OPD': ['D0', 'D3'],
    'Psychology': ['D2', 'D4']
}

# Check Department
def check_depart(symp_percent,Doc_to_dept):
    inverse = [(value, key) for key, value in symp_percent.items()]
    highVal = max(inverse)[0]
    print(highVal, "high index")

    # key at highest value
    highValKey = list(symp_percent.keys())[list(symp_percent.values()).index(highVal)]
    print(highValKey, "name")

    for dtdk, dtdv in Doc_to_dept.items():
        print(dtdv)
        if dtdv.__contains__(highValKey):
            print("success this depart: ")
            return dtdk
        else:
            return 'General'

thisdepart = check_depart(symp_percent,Doc_to_dept)


# thisdepart = "ENT"
sql = 'SELECT doc_name,doc_dept,doc_TimeTo, doc_timeFrom,doc_location,doc_price FROM doctor WHERE doc_dept = '+'"'+thisdepart+'"'
a.execute(sql)
data = a.fetchall()

class Doctor():
    def __init__(self, name, dept, timeTo, timeFrom, location,price):
        self.name = name
        self.dept = dept
        self.timeTo = timeTo
        self.timeFrom = timeFrom
        self.location = location
        self.price = price
# distance cost of hospitals
dist_of_Hosp = {
    'Nazimabad Hospital' : [5,2],
    'Johar Hospital' : [2,4],
    'DHA Hospital' : [3,8],
    'Saddar Skin Hospital' : [5,5]
}

AllhospCord = []
# Populate Doctor objects
docObjArray = []
for eachdoc in data:
    docObjArray.append(Doctor(eachdoc[0], eachdoc[1] ,eachdoc[2], eachdoc[3], eachdoc[4],eachdoc[5]))
    #       name,  dept,  timeTo,  timeFrom,  location,   price
    print(eachdoc[0], eachdoc[1] ,eachdoc[2], eachdoc[3], eachdoc[4],eachdoc[5])
    
    # Contraints for location
    hosp_cord = dist_of_Hosp[eachdoc[4]]
    print(hosp_cord)

    user_points = (user_location[0], user_location[1], 0)
    hosp_points = (hosp_cord[0], hosp_cord[1], 0)
    dst = distance.euclidean(user_points, hosp_points)
    print(dst)
    AllhospCord.append(dst)
    print()

indexof_hospCord =  AllhospCord.index(min(AllhospCord))
print("Nearest Hospital is: ",docObjArray[indexof_hospCord].location)

