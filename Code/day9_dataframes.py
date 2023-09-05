# import pandas as pd
import random

import numpy
import pandas
import pandas as pd

class DataFrameEngine():
    def demonstrateDataFrames(self):
        # list of strings
        Names = ['Kevin', 'Danny', 'Henry', 'Kis', 'Polar', 'Vik', 'Rog']

        # Calling DataFrame constructor on list
        df = pd.DataFrame(Names)

        NamesD = {"Names": ['Kevin', 'Danny', 'Henry', 'Kis', 'Polar', 'Vik', 'Rog']}
        df2 = pd.DataFrame(NamesD)
        print("df2")
        print(df2)

        studentsD = {"Names": ['Kevin', 'Danny', 'Henry', 'Kis', 'Polar', 'Vik', 'Rog'],
                     "Marks1": [random.uniform(10, 100) for x in range(7)],
                     "Marks2": [random.uniform(10, 100) for x in range(7)]}
        df3 = pd.DataFrame(studentsD)
        print("df3")
        print(df3)

        print(df3.Names)
        print(df3.Names[3])
        print(df3.Marks1[3])
        print(df3[["Marks1", "Marks2"]])

        print(df3.loc[1])
        print(type(df3.loc[1]))
        print(df3.loc[1:5])
        print(type(df3.loc[1:5]))

        df4 = pd.DataFrame(studentsD, index=["S" + str(x) for x in range(1, 8)])
        print(df4)

        print(df4.Marks2["S5"])
        print(df4.loc["S5"]["Marks2"])
        print(df4.loc[["S5"]].Marks2)

        print(df4.iloc[4]["Marks2"])

        print(df4[[True, True, False, True, False, True, True]])
        print(df4[df4.Marks1 + df4.Marks2 > 120])

        print("Variable Analysis")
        print(df4.head())
        print(df4.tail())
        print(df4.describe())
        print(df4.describe(include='all'))

        df4.index = ["S" + str(x) + str(x) for x in range(1, 8)]
        print(df4.head(7))

        df4.set_index("Names", inplace=True)
        print(df4)

        df4.reset_index(inplace=True)
        print(df4)

        df5 = df4.set_index("Names")
        print(df4)
        print(df5)

        print("df4")
        print(df4)
        for i, j in df4.iterrows():
            print(i, j)
            print()

        for i, j in df4.iterrows():
            if(i % 2 != 0):
                print(j["Names"]+":"+str(j["Marks1"]))
            else:
                print(j["Names"] + ":" + str(j["Marks2"]))
            print()

        for k, v in df4.items():
            print(k, v)
            print()

        for t in df4.itertuples():
            print(tuple(t))
            print()

        print([bool(random.randint(0,2)) for x in range(7)])
        df4.insert(loc = 1, column = "isMale", value = [bool(random.randint(0,2)) for x in range(7)])
        print(df4)

        df4["isDomestic"] = [random.choice([True,False]) for x in range(7)]
        print(df4)


    def loadData(self):
        self.mallC = pd.read_csv('D:\TSOM\PData\Mall_Customers.csv')
        print(self.mallC.to_string())

    def doEx1(self):
        self.loadData()
        print(self.mallC.describe(include='all'))
        print(self.mallC.head(10))
        print(self.mallC.tail(10))

    def demonstrateCategoricals(self):
        s = pd.Series(["a", "b", "c", "a"], dtype="category")
        print(s)

    def doEx2(self):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        self.loadData()
        self.mallC.columns = ['CustomerID', 'Gender', 'Age', 'Annual_Income_k_USD','Spending_Score']
        print("####Q1####")
        self.mallC["annual_income_usd"] = self.mallC.Annual_Income_k_USD * 1000
        print(self.mallC.head())

        print("####Q2####")
        print("Average Age:"+ str(self.mallC.Age.mean()) +
              " | Average Income:" + str(self.mallC.Annual_Income_k_USD.mean()) )

        print("####Q3####")
        print(self.mallC.sort_values("Annual_Income_k_USD").head(20))

        print("####Q4####")
        mallC_f_gt_40 = self.mallC[list(self.mallC.Age>=40) and list(self.mallC.Gender == 'Female')]
        print(mallC_f_gt_40)

        print("####Q5####")
        mallC_f_gt_40 = self.mallC[list(self.mallC.Age >= 40) and list(self.mallC.Gender == 'Female')]
        print(mallC_f_gt_40)

        print("####Q6####")
        self.mallC.insert(loc=6, column="spend_index", value=self.mallC.Spending_Score/self.mallC.Annual_Income_k_USD)
        print(self.mallC.head())

        print("####Q7####")
        income75 = numpy.percentile(self.mallC.Annual_Income_k_USD,0.75)
        mallCm_gt_40 = self.mallC[list(self.mallC.Age >= 40) and list(self.mallC.Gender == 'Male') and
        list(self.mallC.Annual_Income_k_USD>income75)]
        print(mallCm_gt_40)

        print("####Q8####")
        incomeQ3 = numpy.percentile(self.mallC.Annual_Income_k_USD, 0.75)
        incomeQ1 = numpy.percentile(self.mallC.Annual_Income_k_USD, 0.25)
        incomeIQR = incomeQ3-incomeQ1
        self.mallC["income_outlier"] = (list(self.mallC.Annual_Income_k_USD < incomeQ1 - 1.5*incomeIQR)
                                        or list(self.mallC.Annual_Income_k_USD < incomeQ3 + 1.5*incomeIQR))
        print(self.mallC.head())
        print(self.mallC[self.mallC.income_outlier == True])

        print("####Q9####")

        for i, j in self.mallC.iterrows():
            if(j["spend_index"]>=1 and j["Gender"]=='Female' and j["Age"]<25):
                print("Customer",j["CustomerID"]," is a Potential Female Candidate with a spend index ",round(j["spend_index"],2))

        pd.reset_option("display.max_rows")
        pd.reset_option("display.max_columns")

df_engine = DataFrameEngine()
#df_engine.demonstrateDataFrames()
#df_engine.demonstrateCategoricals()
#df_engine.doEx1()
df_engine.doEx2()