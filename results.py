import pandas as pd
from sklearn import linear_model

class Analysis:
    def __init__(self, budget, genre, n, v, l, plot):
        self.budget = budget
        self.genre = genre
        self.n = n
        self.v = v
        self.l = l
        self.plot = plot

    def data(self):
        data = pd.read_csv('FinalMovieUpdatedAgain2.csv')
        genre = []
        for i in range(len(data)):
            temp = data['Genre'][i].split(" ")
            mapped = list(map(int, temp))
            genre.append(mapped)
        desired_genre = []
        for i in range(len(genre)):
            set2 = set(genre[i])
            set1 = set(self.genre)
            if set1.issubset(set2):
                desired_genre.append(i)

        newdata = data[data.index.isin(desired_genre)]
        return newdata

    def rating(self):
        data = pd.read_csv('FinalMovieUpdatedAgain2.csv')
        genre = []
        for i in range(len(data)):
            temp = data['Genre'][i].split(" ")
            mapped = list(map(int, temp))
            genre.append(mapped)
        desired_genre = []
        for i in range(len(genre)):
            set2 = set(genre[i])
            set1 = set(self.genre)
            if set1.issubset(set2):
                desired_genre.append(i)
        newdata = data[data.index.isin(desired_genre)]
        X = newdata[['Nudity', 'Violence', 'Language', 'Budget', 'Plot Sentiment']]
        Y = newdata[['IMDB Rating']]
        regr = linear_model.LinearRegression()
        regr.fit(X, Y)
        arr = [self.n, self.v, self.l, self.budget, self.plot]
        result = str(regr.predict([arr]))[2:-2]
        return round(float(result), 2)


