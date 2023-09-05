import copy
import random


class DataStructureEngine:
    def demonstrateLists(self):
        list1 = [5,6,10,[45, 60]]
        list2 = list((10,20,30,40,50,random.uniform(10,100),random.uniform(10,100)))

        print(list1)
        print(list2)

        print(list1[0]) #Item 1 - Index 0
        print(list1[0:3]) #Items 1,2,3 - Index [0,3)
        print(list1[:3]) #Items 1,2,3 - Index [0,3)
        print(list1[2:])  # Items 3,4 - Index [2,3]


        print(list1[-1])  # Items 4 - Index 3
        print(list1[:-1])  # Items 1,2,3 - Index [0,-1)
        print(list1[1:-1])  # Items 2,3 - Index [1,-1)
        print(list1[1:-2])  # Items 2 - Index [1,-2)

        print(list1[-1:])  # Items 4 - Index [-1,-1]
        print(list1[-2:])  # Items 3,4 - Index [-2,-1]

        print(list1[-2:0])  # Empty List
        print(list1[-1:-3])  # Empty List
        print(list1[::-1])  # Reversed List

        print(list1[::2])  # [start:stop:step]
        print(list2[1:5:2])  # [start:stop:step]
        print(list2[::-2])  #

        name = 'Charles'
        name = 'maddam'
        print(name[::-1])

        list4 = list1+list2
        print(list4)

        list5 = [10,14,15,6,8,9,2,10,22,30]
        list6 = [x for x in list5 if x>15]
        print(list6)

        list7 = [x*10 for x in list5 if x < 10]
        print(list7)

    def demonstrateTuples(self):
        tup1 = (3,5,7,2,3,6)
        tup2 = (4,)

        print(tup1[3])
        print(tup1[1:4])

        #tup1[1] = (4,) # Error
        tup3 = tup1 + tup2
        print(tup3)

        tup3List = list(tup3)
        tup3List[1] = 9
        tup3 = tuple(tup3List)
        print(tup3)

        #in Operator
        if 3 in tup3:
            print('3 is Found in the Tuple')

        tup4 = (45, 50, 31)
        (s1Marks, s2Marks, s3Marks) = tup4

        print(s1Marks)
        tup4 += (43, 45)
        (s1Marks, s2Marks, *otherMarks) = tup4
        print(s1Marks)
        print(otherMarks)

    def doEx1(self):
        print('##### Q1 #####')
        fruits = ['Apple', 'Banana', 'Kiwi']
        fruits_copy = fruits[:]
        fruits_copy.reverse()
        print(fruits)
        fruits[1] = 'Orange'
        print(fruits)
        print(fruits_copy)

        print('##### Q2 #####')
        list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
        list1[2][2].append(7000)
        print(list1)

        list2 = [10, 20, [300, 400, [4000, 6000, 5000], 500], 30, 40]
        list2[2][2].insert(2,7000)
        print(list2)

        list2[2][2][2:3] = [7000,8000]
        print(list2)

    def doEx2(self):
        print('##### Q1 #####')
        employee_details = [(1, "AA", 100), (1, "BB", 1001), (1, "cc", 1002)]
        employee2 = employee_details[1]
        print(employee2)
        print(employee2[1])

    def demonstrateSets(self):
        set_purchase1 = {"phone","laptop","iron","pen","tv","lamp"}
        set_purchase2 = {"phone","laptop","tv","book","ruler","water bottle"}

        print(set_purchase1)
        print(set_purchase2)

        for i in set_purchase1:
            print("I bought a/an",i)

        print("phone" in set_purchase1)

        set_purchase2.add("toy")
        print(set_purchase2)

        set_purchase2.update({"toy","spoon"})
        print(set_purchase2)

        set_purchase2.remove("toy")
        print(set_purchase2)

        set2_purchase22 = set_purchase2
        set2_purchase22.add("toy")

        print(set_purchase2)

        set_unionPurchase = set_purchase1.union(set_purchase2)
        print(set_unionPurchase)

        #set_purchase1.update(set_purchase2)
        set_intersectPurchase = set_purchase1.intersection(set_purchase2)
        print(set_intersectPurchase)

        set_diff1Purchase = set_purchase1.difference(set_purchase2)
        print(set_diff1Purchase)

        set_symDiffPurchase = set_purchase1.symmetric_difference(set_purchase2)
        print(set_symDiffPurchase)

    def demonstrateDicts(self):
        dict1 = {
            "S1": 99,
            "S2": 67,
            "S3": 88,
            "S4": 96,
            "S5": 50
        }

        print(dict1)
        dict1.update({"S6": 50})
        dict1.update({"S5": 50})
        dict1.update({"S5": 60})
        print(dict1)

        dict1["S1"] = 89
        print(dict1)

        dict1.pop("S5")
        print(dict1)




ds_engine = DataStructureEngine()
#ds_engine.demonstrateLists()
#ds_engine.demonstrateTuples()
#ds_engine.doEx1()
#ds_engine.doEx2()
#ds_engine.demonstrateSets()
ds_engine.demonstrateDicts()