import collections
import random
import re
import urllib.request, json

import nltk
from nltk import stem
from nltk.corpus import stopwords
import wordcloud

import pandas as pd
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


class customerAnalysisEngine():
    def __init__(self):
        self.getStopWords()

    def loadData(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        """ Load data into reviews_all. """
        self.book_data = pd.read_csv("C:\\Users\\owner\\Documents\\DataAnalitics\\Python\\project\\Data\\books_data.csv")
        self.book_review = pd.read_csv("C:\\Users\\owner\\Documents\\DataAnalitics\\Python\\project\\Data\\Books_rating.csv")

        """ To understand the structure print the head of the DataFrame. """
        print('Books Data:')
        print(self.book_data.head())
        print(self.book_data.describe(include='all'))

        print('Books Reviews:')
        print(self.book_review.head())
        print(self.book_review.describe(include='all'))


    def cleanData(self):
        """ Transform column names and run summary stats to understand the variables more.
                Ensure to print the number of rows separately. """

        self.book_data.columns = ["Title", "description", "authors", "image", "previewLink", "publisher",
                                  "publishedDate", "infoLink",
                                  "categories", "ratingsCount"]

        print(self.book_data.describe(include='all'))
        print("***Number of Rows:", len(self.book_data))
        print()

        self.book_review.columns = ["ID", "Title", "Price", "User_id", "ProfileName",
                                    "Helpfulness_Score", "Score", "Time", "Summary", "Review"]

        print(self.book_review.describe(include='all'))
        print("***Number of Rows:", len(self.book_review))
        print()

        """Merge the two Databases"""
        self.books_db = pd.merge(self.book_data, self.book_review, on="Title")

        """ Treat missing values in the Rating and ReviewText variables. 
        In this case, dropna has been chosen as the strategy.   """
        self.books_db.dropna(subset=["Title", "description", "ratingsCount", "Helpfulness_Score", "Score", "Time",
                                    "Review", "Summary"], inplace=True)
        print("***Number of Rows:", len(self.books_db))
        print()

        """ Select only the 'ReviewText',  'Rating', 'DivisionName',
         'DepartmentName', and 'ClassName' variables that would matter to the analysis. 
         Creating a new DataFrame called reviews_sub. """
        self.Books_sub = self.books_db[
            ["Title", "description", "authors", "publisher", "publishedDate",
             "categories", "ratingsCount","Price","Helpfulness_Score","Score", "Time", "Review", "Summary"]]

        print(self.Books_sub.head())
        print()
        

    def analyseRating(self):

        """Analyse the effect of numerical variables over score"""

        dataCor = self.books_db[["Price", "Score", "Time"]]
        dataCor = pd.DataFrame(dataCor)
        print(dataCor.corr())
        print(dataCor.corr(method="spearman"))
        fig = px.imshow(round(dataCor.corr(), 2), text_auto=True, color_continuous_scale='deep',
                        title='Pearson Correlation')
        fig.show()

        fig = px.imshow(round(dataCor.corr(method="spearman"), 2), text_auto=True, color_continuous_scale='deep',
                        title='Spearman Correlation')
        fig.show()

        """Displaying the frequency of rating using a histogram"""

        fig = px.histogram(self.Books_sub, x="Score")
        fig.update_traces(marker_color='darkblue',
                          marker_line_color='darkblue',
                          marker_line_width=1.5)
        fig.update_layout(title_text='Score')
        fig.show()

        dfg=self.Books_sub.groupby(['categories']).size().to_frame().sort_values([0], ascending=False).head(10).reset_index()
        print(dfg)
        fig=px.histogram(dfg, x="categories", y=0,labels={"x":"Categories","y":"Count"})
        fig.update_traces(marker_color='darkblue',
                          marker_line_color='darkblue',
                          marker_line_width=1.5)
        fig.update_layout(title_text='Categories')
        fig.show()

    def analyseSentiments(self):
        self.Books_sub['sentiment'] = ['positive' if score > 2.5 else 'negative' for score in self.Books_sub['Score']]
        print(len(self.Books_sub.sentiment == "negative"))
        print(len(self.Books_sub.sentiment == "positive"))
        self.generate_special_word_clouds('all')
        self.generate_special_word_clouds('positive')
        self.generate_special_word_clouds('negative')



    def tokenize(self, doc: str, isStemmed: bool = False) -> list:
        text = doc.lower().strip()
        tokens = re.findall(r'\b\w+\b', text)

        # Stemming
        if isStemmed:
            porterstem = stem.PorterStemmer()
            tokens = [porterstem.stem(x) for x in tokens]

        return tokens

    def getStopWords(self):
        nltk.download('stopwords')
        stopWords = set(stopwords.words('english'))
        stopWords.update({'would', 'could'})
        print(stopWords)
        self.stopWorkds = stopWords

    def generate_special_word_clouds(self, sentimentType='ALL'):
        
        corpus_txt = ""
        if (sentimentType.lower() == 'all'):
            corpus_txt = " ".join(x for x in self.Books_sub.description)
        else:
            self.Books_sub = self.Books_sub[self.Books_sub.sentiment == sentimentType]
            corpus_txt = " ".join(x for x in self.Books_sub.description)

        print(corpus_txt.head())

        tokens = self.tokenize(corpus_txt)
        tokensFiltered = [token for token in tokens if token not in self.stopWorkds]
        frequencyDict = dict(collections.Counter(tokensFiltered))

        fileName = ""
        match sentimentType.lower():
            case 'all':
                fileName = "C:\\Users\\owner\\Documents\\DataAnalitics\\Python\\AlldescriptionBooks.png"
            case 'positive':
                fileName = "C:\\Users\\owner\\Documents\\DataAnalitics\\Python\\PosdescriptionBooks.png"
            case 'negative':
                fileName = "C:\\Users\\owner\\Documents\\DataAnalitics\\Python\\NegdescriptionBooks.png"

        self.generateWordCloud(frequencyDict, fileName)

    def generateWordCloud(self, frequencies, path):
        # use this code to generate the word cloud
        cloud = wordcloud.WordCloud()
        cloud.generate_from_frequencies(frequencies)

        cloud.to_file(path)
        import matplotlib.pyplot as plt
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis('off')
        plt.figure()
        print('word clouds generated!' )


    """
    Write a function to remove all the punctuations and stop words from a given text and 
    return a string of CLEAN WORDS.
    """


    def remove_punc_stopwords(self, text: str) -> str:
        text_tokens = self.tokenize(text)
        text_tokens = [token for token in text_tokens if token not in self.stopWorkds]
        return " ".join(text_tokens)


    def runTextPredictions(self):


        """ Remove punctuations and stopwords from the text data in ReviewText and Title"""
        self.Books_sub['Title'] = [str(x) for x in self.Books_sub['Title']]
        self.Books_sub['Review'] = [str(x) for x in self.Books_sub['Review']]
        self.Books_sub['Summary'] = [str(x) for x in self.Books_sub['Summary']]
        self.Books_sub['description'] = [str(x) for x in self.Books_sub['description']]


        self.Books_sub['Title'] = self.Books_sub['Title'].apply(self.remove_punc_stopwords)
        self.Books_sub['Review'] = self.Books_sub['Review'].apply(self.remove_punc_stopwords)
        self.Books_sub['Summary'] = self.Books_sub['Summary'].apply(self.remove_punc_stopwords)
        self.Books_sub['description'] = self.Books_sub['description'].apply(self.remove_punc_stopwords)

        """ Add a new variable called sentiment; if Score is greater than 3, then sentiment = 1, else sentiment = -1 """
        self.Books_sub['sentimentScore'] = [1 if x > 2.5 else -1 for x in self.Books_sub.Score]

        """ split the dataset into two: train (85% of the obs.) and test (15% of the obs.)"""
        # reviews_sub_train =  self.reviews_sub.sample(freq=0.85)
        # reviews_sub_test =  self.reviews_sub.sample(freq=0.15)

        self.Books_sub['random_index'] = [random.uniform(0, 1) for x in range(len(self.Books_sub))]

        Books_Sub_train = self.Books_sub[self.Books_sub.random_index < 0.85][
            ['Review', 'Score', 'Title','description','sentimentScore']]
        Books_sub_test = self.Books_sub[self.Books_sub.random_index >= 0.85][
            ['Review', 'Score', 'Title','description','sentimentScore']]

        print(Books_Sub_train.head())
        print(Books_sub_test.head())

        """
        from sklearn.model_selection import train_test_split
        reviews_sub_train, reviews_sub_test = train_test_split(self.reviews_sub, test_size=0.15)
        """

        """ count vectorizer:
        Next, we will use a count vectorizer from the Scikit-learn library. This will transform the text in our dataframe 
        into a 'bag of words' model, which will contain a sparse matrix of integers. 
    
        The number of occurrences of each word will be counted and printed.
        We will need to convert the text into a bag-of-words model since the logistic regression 
    
        algorithm cannot understand text.
    
        The bag-of-words model is a popular technique in natural language processing (NLP) 
        for representing text data as numerical vectors. It is a simple and intuitive approach 
        that disregards the order and structure of words in a document and focuses solely on their 
        occurrence frequencies.
    
        """

        vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
        train_matrix = vectorizer.fit_transform(Books_Sub_train['Title'])
        test_matrix = vectorizer.transform(Books_sub_test['Title'])

        """Perform Logistic Regression"""

        lr = LogisticRegression()

        X_train = train_matrix
        print(X_train)
        X_test = test_matrix
        y_train = Books_Sub_train['sentimentScore']
        y_test = Books_sub_test['sentimentScore']

        lr.fit(X_train, y_train)
        print("Coefficients:")
        print(lr.coef_)
        print("Intercept:")
        print(lr.intercept_)

        """ Generate the predictions for the test dataset"""
        predictions = lr.predict(X_test)
        Books_sub_test['predictions'] = predictions
        print(Books_sub_test.head(30))

        """Calculate the prediction accuracy"""
        Books_sub_test['match'] = Books_sub_test['sentimentScore'] == Books_sub_test['predictions']

        print("")
        print("Prediction Accuracy Logistic Regresion Sentiment Score:")
        print(sum(Books_sub_test['match']) / len(Books_sub_test))

        lr2 = LogisticRegression()

        X_train = train_matrix
        X_test = test_matrix
        y_train2 = Books_Sub_train['Score']
        y_test2 = Books_Sub_train['Score']

        lr2.fit(X_train, y_train2)

        """ Generate the predictions for the test dataset"""
        predictions2 = lr2.predict(X_test)
        Books_sub_test['predictions_rating'] = predictions2
        print(Books_sub_test.head(30))

        Books_sub_test['match_rating'] = Books_sub_test['Score'] == Books_sub_test['predictions_rating']

        print("")
        print("Prediction Accuracy Logistic Regresion Score:")
        print(sum(Books_sub_test['match_rating']) / len(Books_sub_test))


ca_engine = customerAnalysisEngine()
ca_engine.loadData()
ca_engine.cleanData()
#ca_engine.analyseRating()
#ca_engine.analyseSentiments()
#ca_engine.generate_special_word_clouds()
#ca_engine.generateWordCloud()
ca_engine.runTextPredictions()
