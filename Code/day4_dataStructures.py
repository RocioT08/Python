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
        pass


ds_engine = DataStructureEngine()
ds_engine.demonstrateLists()
#ds_engine.demonstrateTuples()

