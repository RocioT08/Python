import random

class ControlStructuresEngine:
    # THESE ARE METHODS DEFINED AT THE CLASS LEVEL
    def demonstrateBasicFunctions(self):
        ran_list = [round(random.uniform(10, 100)) for x in range(10)]
        print(ran_list)
        print('The Total of Numbers in ran_list: ' + str(sum(ran_list)))

        #[S1, S2, S3..... S10]
        names = ["S" + str(x) for x in range(1, 11)]
        print(names)

        marks = zip(names,ran_list)
        print(list(marks))

    def demonstrateIfElifElse(self):
        #Generate two random numbers
        x = random.normalvariate(50,2)
        y = random.uniform(10,100)

        if(x > y):
            print('X is greater than Y')
        elif(x == y):
            print('X is Y')
        else:
            print('Y is greater than X')

        if (x > y): print('X is greater than Y')

        print('X is greater than Y') if (x > y) else print('X is NOT greater than Y')

    def demonstrateForLoop(self):
        ran_nums = [round(random.uniform(10, 100)) for x in range(10)]

        for x in ran_nums:
            if(x > 50): print(x)

        ran_nums_gt_50 = [x for x in ran_nums if x>50 ]
        print(ran_nums_gt_50)

        str1 = "Pablo Riuz"
        for x in str1:
            if(str.isupper(x)): print(x)

        str_UC = [x for x in str1 if str.isupper(x)]
        print(str_UC)

        str1_iter = iter(str1)
        print(next(str1_iter))
        print(next(str1_iter))
        print(next(str1_iter))
        print(next(str1_iter))

        list1 = [1,3,5,7,9]
        for x in list1:
            print(x)
            if x == 5: continue
            print(x)

        for x in list1:
            print(x)
            if x == 5: break
            print(x)

        list2 = list(range(5, 50, 5))
        print(list2)
        print(range(5, 50, 5))

        for x in range(5, 50, 5):
            print(x)
            if x == 25: continue
            print(x)

        print('####')
        for x in range(5, 75, 5):
            print(x/2)
        else:
            print('The for loop ended')
            print('Was it ended by the break?')

    def get_the_two_max_numbers(self,numbers):
        numbers.sort(reverse=True)
        return(numbers[:2])

    def get_the_two_max_numbers2(self,numbers):
        num1 = 0
        num2 = 0
        for x in numbers:
            if(x > num1): num1 = x
            elif (x > num2): num2 = x
        return([num1, num2])

    def generateMultiTable(self, number):
        return([number*x for x in range(11) ])
        """
        for i in range(1, 11):
            table = number * i
            print(table) """

    def doEx1(self):
        print("#Q1#")
        numbers = [round(random.uniform(10, 100)) for x in range(10)]
        print(self.get_the_two_max_numbers(numbers))
        print(self.get_the_two_max_numbers2(numbers))

        print("")
        print("#Q2#")
        random_numbers = [round(random.uniform(1, 100)) for x in range(20)]

        sum_even = 0
        sum_odd = 0

        for x in random_numbers:
            if x % 2 == 0:
                sum_even += x
            else:
                sum_odd += x

        print("Random Numbers:", random_numbers)
        print("Sum of Even Numbers:", sum_even)
        print("Sum of Odd Numbers:", sum_odd)

        sum_even = sum([x for x in random_numbers if x % 2 == 0])
        sum_odd = sum([x for x in random_numbers if x % 2 != 0])

        print("Sum of Even Numbers:", sum_even)
        print("Sum of Odd Numbers:", sum_odd)

        print()
        print("#C#")
        student = [
            {"id": 2, "first_name": "John", "last_name": "Quick", "subjects": ["English", "Python"], "score": [87, 93]},
            {"id": 3, "first_name": "Paul", "last_name": "Kenedy", "subjects": ["English", "C++", "Math"],
             "score": [85, 76, 90]},
            {"id": 4, "first_name": "Ricki", "last_name": "Morty", "subjects": ["C++", "Math"], "score": [67, 74]}]

        sumMath = 0
        countStudent = 0

        for i in student:
            if 'Math' in i["subjects"]:
                sumMath += i["score"][i["subjects"].index('Math')]
                countStudent += 1

        print(sumMath / countStudent)

        print()
        print("#D#")
        print(self.generateMultiTable(3))

        print("#E#")

        i = 1
        user_nums = []
        while(i <=5):
            num = int(input())
            user_nums.append(num)
            i += 1

        print(user_nums)




#THIS IS A FUNCTION DEFINED AT THE MODULE LEVEL
def mySampleFunction(a, b):
    return(a * b / 9000)

cs_engine = ControlStructuresEngine()

#cs_engine.demonstrateBasicFunctions()
#cs_engine.demonstrateIfElifElse()
#cs_engine.demonstrateForLoop()
cs_engine.doEx1()
#mySampleFunction(6,8)