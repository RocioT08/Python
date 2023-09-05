import random
import statistics as st
import enum
import pandas as pd

class ControlStructuresEngine2:
    def bubble_sort(self, dictionary):
        sorted_list = list(dictionary.items())
        n = len(sorted_list)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if sorted_list[j][1] < sorted_list[j + 1][1]:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        return sorted_list

    def doEx1(self):
        print("#F#")

        numbers = [12, 75, 150, 180, 145, 525, 50]
        for number in numbers:
            if number > 500:
                break
            if number > 150:
                continue
            if number % 5 == 0:
                print(number)

        print("#G#")
        cars = {
            "2000": 19000, "2001": 19853, "2002": 19000, "2003": 7845, "2004": 17896,
            "2005": 23098, "2006": 19000, "2007": 19853, "2008": 19000, "2009": 7845,
            "2010": 17896, "2011": 23098, "2012": 19000, "2013": 19853, "2014": 19000,
            "2015": 7845, "2016": 17896, "2017": 23098, "2018": 19000, "2019": 19853,
            "2020": 19000, "2021": 7845, "2022": 17896, "2023": 23098
        }

        prices = [cars[str(year)] for year in range(2005, 2011)]
        mean = st.mean(prices)
        print("Mean for models from 2005 to 2011:", mean)

        print("#H#")
        student_marks = {
            "Andrés": 85,
            "Natalia": 92,
            "Cris": 78,
            "Marlon": 95,
            "Fer": 88
        }

        print(self.bubble_sort(student_marks))


        print("#I#")
        fruits = ["mango", "orange", "berry"]

        for fruit in fruits:
            if fruit == "orange":
                continue
            print(fruit)

    def demonstrateMatchCase(self):
        # matching the cases of an integer variable
        user_input = 50
        match user_input:
            case 20:
                print("You selected 20!")
            case 30:
                print("You selected 30!")
            case 40:
                print("You selected 40!")
            case 50:
                print("You selected 50!")

        # matching the cases of an integer variable with the pipe operator to combine multiple matches
        user_input = 30
        match user_input:
            case 20:
                print("You selected 20!")
            case 30 | 40:
                print("You selected 30 or 40!")
            case 50:
                print("You selected 50!")

        # matching the cases of a string variable
        user_input = "exit".lower()
        match user_input:
            case "run":
                print("The code is running.")
            case "pause":
                print("Code execution is paused.")
            case "exit":
                print("The code is exiting")

        # matching the partial cases of an integer variable and including a default case.
        user_input = 400
        match int(str(user_input)[0]):
            case 2:
                print("You selected 20!")
            case 3:
                print("You selected 30!")
            case 4:
                print("You selected 40!")
            case _:
                print("You selected an invalid input!")

        # matching the structure of collection with match-case.
        collection1 = [7, 8, 9, 10]
        collection1 = [7]
        match collection1:
            case [a]:
                print("Only one item:", [a])
            case [a, b]:
                print("Two items:", [a, b])
            case [a, b, *rest]:
                print("More than two items: ", [a,b, rest])

        # matching the data type.
        value = 400
        match value:
            case int() | float() as value:
                print("numeric")
            case str() as value:
                print("String")
            case _:
                print("Unacceptable Data Type")

        # match-case guarded with if.
        student = {'name': 'Kate', 'grade': 90, 'courses': 16}
        match student:
            case {'name': name, 'courses': courses, 'grade': grade} if courses > 15 and grade >= 90:
                print(name, ": Exceptional")
            case {'name': name, 'courses': courses, 'grade': grade} if grade >= 90:
                print(name, ": Good")
            case _:
                print(name, "No current award")

class SummaryOpts(enum.Enum):
    Average = 1
    AverageByOver = 2
    Sum = 3
    SumByOver = 4

class cricket:
    def __init__(self):
        self.overs = []
        for i in range(5):
            self.overs.append(self.over())

        self.perfectScore = []
        for i in range(5):
            self.perfectScore.append(self.over(True))

    def over(self, isIdealScore=False):
        if isIdealScore:
            return [6, 6, 6, 6, 6, 6]

        ran_num = [random.randint(0, 6) for i in range(6)]
        return ran_num

    def cricSummary(self, scores, opts):

        if opts not in SummaryOpts:
            print('Invalid Operation!')

        match opts:
            case SummaryOpts.Average:
                return(sum([sum(over) for over in scores]) / (len(scores) * 6))
            case SummaryOpts.AverageByOver:
                return st.mean([sum(over) for over in scores])
            case SummaryOpts.Sum:
                return(sum([sum(over) for over in scores]))
            case SummaryOpts.SumByOver:
                return([sum(over) for over in scores])



cs_engine = ControlStructuresEngine2()

#cs_engine.doEx1()
#cs_engine.demonstrateMatchCase()

game = cricket()
#print(game.__dict__)
#print(game.cricSummary(game.overs, SummaryOpts.Sum))
#print(game.cricSummary(game.overs, SummaryOpts.AverageByOver))
#print(game.cricSummary(game.overs, SummaryOpts.SumByOver))
#print(game.cricSummary(game.overs, SummaryOpts.Average))
#print(game.cricSummary(game.overs, "APPLE"))


####################PANDAS######################
class pandasEngine():
    def loadData(self):
        self.mallC = pd.read_csv('D:\TSOM\PData\Mall_Customers.csv')
        print(self.mallC.to_string())

pe = pandasEngine()
pe.loadData()