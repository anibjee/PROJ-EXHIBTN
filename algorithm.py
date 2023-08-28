import numpy as np
from sklearn.neighbors import KNeighborsClassifier

class KNNClassifier:
    def __init__(self, k=3):
        self.k = k
        self.model = KNeighborsClassifier(n_neighbors=k)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X_test):
        return self.model.predict(X_test)

class RankingAlgorithm:
    def __init__(self):
        pass

    def rank_items(self, items, scores):
        ranked_items = [item for _, item in sorted(zip(scores, items), reverse=True)]
        return ranked_items

X_train = [[2019, 1000000], [2020, 1200000], [2018, 800000], [2021, 1500000]]
y_train = ['F34', 'M34', 'A34', 'S23']

knn = KNNClassifier(k=2)
knn.fit(X_train, y_train)

items = ['F34', 'M34', 'A34', 'S23']
sales_scores = [1000, 1800, 1200, 1500]

ranking_algo = RankingAlgorithm()
ranked_items = ranking_algo.rank_items(items, sales_scores)

print("KNN Predictions:", knn.predict([[2017, 900000], [2023, 1400000]]))
print("Ranked Items:", ranked_items)