import copy
import random

import numpy
import pandas as pd

class AggEngine():
    def loadMallData(self):
        self.mallC = pd.read_csv('D:\TSOM\PData\Mall_Customers.csv')
        self.mallC.columns = ['CustomerID', 'Gender', 'Age', 'Annual_Income_k_USD', 'Spending_Score']
        print(self.mallC.to_string())

    def loadData(self):
        self.cod = pd.read_csv('D:\TSOM\RData\cod.csv')
        print(self.cod.to_string())

    def perc(self,a, q):
        return(numpy.percentile(a,q))

    def demonstrateAgg(self):
        self.loadData()
        print("###column sums###")
        print(self.cod.agg('sum'))
        print("###column means###")
        print(self.cod[["intensity","prevalence","depth","weight","length"]].agg('mean'))

        print("###row sums###")
        """axis{0 or ‘index’, 1 or ‘columns’}, default 0
        If 0 or ‘index’: apply function to each column. If 1 or ‘columns’: apply function to each row.
        """
        print(self.cod[["weight", "length"]].agg('sum', axis=1))

        """
        Mean - df.agg('mean')
        Median - df.agg('median')
        Mode - df.agg('mode')
        Sum - df.agg('sum')
        Count - df.agg('count')
        Max - df.agg('max')
        Min - df.agg('min')
        Standard Deviation - df.agg('std')
        Variance - df.agg('var')
        Skewness - df.agg('skew')
        Kurtosis - df.agg('kurt')
        """
        print(self.cod[["depth", "weight", "length"]].agg(['sum','mean','min','max','std']))
        print(self.cod[["depth", "weight", "length"]].agg(['sum', 'mean', 'min', 'max', 'std']).rename(index={
            'sum':"sum_of_column", "mean":"mean_of_column", "min":"min_of_column", "max":"max_of_column","std":"sd_of_column"
        }))

        print(self.cod[["depth", "weight", "length"]].agg(lambda x : self.perc(x,0.75)))

        print(self.cod.agg({"depth": ['min','max'], "weight": 'sum',"length": 'mean'}))

        print(self.cod.groupby('area').agg({"depth": ['min', 'max','mean'], "weight":['min', 'max','mean'], "length": ['min', 'max','mean']}).to_string())
        sum_df = self.cod.groupby('area').agg({"depth": ['min', 'max', 'mean'], "weight": ['min', 'max', 'mean'],
                                            "length": ['min', 'max', 'mean']})

        print(self.cod[["area","depth"]].groupby('area').agg(['min', 'max', 'mean']).reset_index())

        df1 = pd.DataFrame({
            "m1": [45, 67, 87, 34,65],
            "m2": [76, 45, 87, 90,74],
            "m3": [67,89,34,67,88]
        }, index=["S1","S2","S3","S4","S5"])

        print("####DF1####")
        print(df1)

        print()
        print("offer 3 bonus points")
        df2 = df1.transform(lambda x : x+3)
        print(df2)

        print()
        df2[["total", "avg"]] = df2.agg(['sum', 'mean'], axis=1)
        print()
        print(df2)

        def add3(x):
            return x+3

        def add5(x):
            return x+5

        print()
        print("offer 3 and 5 bonus points")
        df3 = df1.transform([add3, add5])
        print(df3)

        print()
        print(df1.apply([add3,add5]))

        print()
        df1["class"] = ["A","A","B","B","B"]

        print(df1)
        print()
        df4 = copy.deepcopy(df1)
        df4[["total", "avg"]] = df4[["m1","m2","m3"]].agg(['sum', 'mean'], axis=1)
        print(df4)
        print()


        df4["class_avg"] = df4.groupby('class')['avg'].transform('mean')
        print(df4)
        print()

    def doEx1(self):
        self.loadMallData()

        self.mallC["Age_Group"] = pd.cut(self.mallC.Age,bins = 4, labels=["A","B","C","D"])
        print(self.mallC)
        print(self.mallC.groupby(["Gender", "Age_Group"]).agg({'Annual_Income_k_USD':['mean','min','max'],
                                                               'Spending_Score':['mean','min','max']}))

        self.mallC["Spending_Score_By_Gender"] = self.mallC.groupby('Gender')['Spending_Score'].transform('mean')
        print(self.mallC.to_string())

    def demonstrateMerge(self):
        marks1 = pd.DataFrame({'name':["S"+str(x) for x in range(1,11)],
                               'm1': [random.randint(10,100) for y in range(10)],
                               'm2': [random.randint(10,100) for y in range(10)],
                               'm2': [random.randint(10,100) for y in range(10)],
                               'class':['A','B','A','A','B','B','C','C','D','D']})



        classD = pd.DataFrame({'class': ['A','B','C','D'],
                               'teacher':['Maria','Pablo','Lois','Adnan'],
                               'subject':['Data','Decision','Business','Maths']})
        print(marks1)
        print(classD)

        marks2 = marks1.merge(classD, how='inner',on='class')
        print(marks2)



a_engine = AggEngine()
#a_engine.demonstrateAgg()
#a_engine.doEx1()
a_engine.demonstrateMerge()
