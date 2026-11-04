import pandas as pd
import sklearn
import matplotlib.pyplot as plt

from sklearn.decomposition import KernelPCA

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    #load dataframe
    dt_heart = pd.read_csv('./data/heart.csv')

    print(dt_heart.head(5))

    dt_features = dt_heart.drop(['target'], axis=1)
    dt_target = dt_heart['target']

    dt_features = StandardScaler().fit_transform(dt_features)


    X_train, X_test, y_train, y_test = train_test_split(dt_features, dt_target, test_size=0.3, random_state=42)

    # we want 4 components to take the relevant information from the original 13 features. The kernel is set to 'poly', which means that the algorithm will use a polynomial kernel to transform the data into a higher-dimensional space before performing PCA. This can help capture non-linear relationships in the data that may not be captured by linear PCA.
    kpca = KernelPCA(n_components=4, kernel='poly')
    kpca.fit(X_train)

    dt_train = kpca.transform(X_train)
    dt_test = kpca.transform(X_test)

    # regression logistic with the solver set to 'lbfgs'. The solver is an optimization algorithm used to find the best parameters for the logistic regression model. 'lbfgs' is a popular choice for small to medium-sized datasets and is known for its efficiency and accuracy.
    logistic = LogisticRegression(solver='lbfgs')

    logistic.fit(dt_train, y_train)

    print('SCORE KPCA: ', logistic.score(dt_test, y_test))


