from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from trainingdataloader import training_data
import numpy as np

class KNNClassifier:
    def __init__(self, training_data, n_neighbors=3, test_size=0.2, random_state=42):
        self.X = np.array([i[0].features for i in training_data])
        self.y = np.array([i[1] for i in training_data])
        self.n_neighbors = n_neighbors
        self.test_size = test_size
        self.random_state = random_state
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=self.test_size, random_state=self.random_state)
        self.knn = KNeighborsClassifier(n_neighbors=self.n_neighbors)
        self.y_pred = None

    def train(self):
        self.knn.fit(self.X_train, self.y_train)

    def test(self):
        self.y_pred = self.knn.predict(self.X_test)
        return self.y_pred

    def predict(self, exercise):
        self.result = self.knn.predict(exercise.features)

    def evaluate(self):
        if self.y_pred is None:
            raise ValueError("Call 'predict()' method before evaluating.")
        print(classification_report(self.y_test, self.y_pred))
        print(confusion_matrix(self.y_test, self.y_pred))

if __name__ == "__main__":
    knn_classifier = KNNClassifier(training_data)
    knn_classifier.train()
    knn_classifier.test()
    knn_classifier.evaluate()