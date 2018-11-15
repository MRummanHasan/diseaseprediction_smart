import io

# MainSymp : symp1, symp2....
listofAllsymp = {
    "Deep Cough": ["ear Pain", "sore Swelling", "change in Voice", "difficulty in breathing"],
    "Jaw Pain": ["sore Throat", "teeth Loose", "painful Chewing"],
    "MainSymp3": ["weakness", "fever", "cheek swelling", "other", "other2"],
    "MainSymp4": ["s1", "s2", "s3"],
    "MainSymp5": ["s1", "s2", "s3"],
    "MainSymp6": ["s1", "s2", "s3", "s4"]
}

# Pick MainSymptoms from Allsymptom list
QuesList = []
for ms,ns in listofAllsymp.items():
    QuesList.append(ms)
# print(QuesList,"\n")
# Output: QuesList = ['Deep Cough', 'Jaw Pain', 'MainSymp3', 'MainSymp4', 'MainSymp5', 'MainSymp6']

q_index = 0
for r, v in listofAllsymp.items():
    ns = 0
    ans = input("Answer with  'y'  or  'n'\nDo you have/feel "+str(r)+" : ")
    print()
    if ans == "y":
        index = QuesList.index(r)
        if QuesList[q_index] == r:
            for NS in v:
                if ns < len(v):
                    QuesList.insert(index+1, v[ns])
                    ns = ns + 1
                    q_index = q_index + 1
    q_index = q_index + 1
print()
