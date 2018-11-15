import io

# MainSymp : symp1, symp2....
listAllsymp = [['   Deep Cough   ',  '  Ear Pain  ',  '  Sore Swelling  ',  '  Change in Voice  ',  '   Difficulty in breathing   '],
               ['   Jaw Pain   ',  '  Sore Throat  ',  '  Teeth Loose  ',  '  Painful Chewing  '],
               ['   MainSymp3   ',  '  weakness  ',  '   fever   ','   cheek swelling   ',  '   other   '],
               ['   MainSymp4   ',  '   s1   ',  '   s2   ']]

for i in listAllsymp:
    for j in i:
        print(j)

# Populate MainSymptoms
# Output : [['Deep Cough'], ['Jaw Pain'], ['MainSymp3'], ['MainSymp4']]
quesList = []
i = 0
for ms in listAllsymp:
    # print(listAllsymp[i][0:1])
    quesList.append(listAllsymp[i][0:1])
    i = i+1
print(quesList)
# print()
ms = 0
aaa = []
print(ms)
aaa.append(str(listAllsymp[ms][0]))
index = quesList.index(aaa)  # index of MS
print(index)

eachdataset = 0
for q in quesList:
    
    ans = input("Answer with  'y'  or  'n'  \nDo you have/feel "+str(q)[1:-1].strip()+" : ")
    print()
    if ans ==  "y":
        for i in listAllsymp:
            for j in i:
                print(j,str(q)[1:-1],"xxxxxxxxxxx")
                if j == str(q)[1:-1]:
                    j =  'yes'
                    print(j,"--------------")


        # find index of MS(deepCOugh) from listAllsymp, pick Allsymptoms; insert Allsymtom to QuestionList
        for MS in listAllsymp:
            print(MS[0], str(q)[2:-2])

            if MS[0] == str(q)[2:-2]:
                ns = 1

                for NS in MS:
                    try:
                        if ns < len(MS):
                            allsymp = listAllsymp[eachdataset][ns]
                            ns = ns + 1
                            index = quesList.index(aaa)  # index of MS
                            print(ms)
                            # insert after index of MS, Allsympton of MS
                            quesList.insert(index+1, allsymp)
                            print("===== symp added to questionlist", ns)
                            # print("ms ki iteration", ms)
                            ms = ms + 1
                    except:
                        pass
                print("---finalilist-----", quesList, "-----------")
                eachdataset = eachdataset + 1
                print(eachdataset, "Allsymplist")
            else:
                pass
    else:
        pass


# count of symptom listAllsymp
# print(len(listAllsymp[0]))
# only symptoms
# i = 0
# for ms in listAllsymp:
#     print(listAllsymp[i][1:])
#     i = i+1


# find index of MS(deepCOugh) from listAllsymp, pick Allsymptoms; insert Allsymtom to QuestionList
# ms = 0
# for MS in listAllsymp:
#     print(MS[0],str(quesList[ms])[2:-2])

#     if MS[0] == str(q)[2:-2]:
#         print(MS, "------")
#         ns = 1
#         for NS in MS:
#             if ns < len(MS):
#                 allsymp = listAllsymp[0][ns]
#                 ns = ns + 1
#             # insert after index of MS, Allsympton of MS
#                 quesList.insert(index+1, allsymp)
#                 print("======yes symp added to question")

#         print(quesList,"*****finallist*****")
#     ms = ms + 1
