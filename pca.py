import pandas as pd
import sklearn
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

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

    # consulting the shape of the training data (717, 13) 5 rows and 14 columns
    print(X_train.shape)
    print(y_train.shape)

    # PCA no selecciona 3 de tus 13 variables originales; las transforma. Crea 3 nuevas variables artificiales que son combinaciones lineales de todas las anteriores, diseñadas para capturar la mayor cantidad de información posible.

    # create the variance matrix of the training data
    # n_components = min(n_muestras, n_features)
    pca = PCA(n_components=3)
    pca.fit(X_train)

    #  batch create a new instance of IncrementalPCA with 3 components and a batch size of 10. This means that the data will be processed in batches of 10 samples at a time, which can be useful for large datasets that do not fit into memory all at once.
    ipca = IncrementalPCA(n_components=3, batch_size=10)
    ipca.fit(X_train)


    # range generate the number from 0 and quantity of components, in this case 3. The explained_variance_ratio_ attribute of the PCA object returns an array containing the percentage of variance explained by each of the selected components. By plotting this array against the range of components, we can visualize how much information is retained as we increase the number of components.
     # gráfica: componentes 1, 2 y 3 en el eje X
    plt.plot(
        range(1, len(pca.explained_variance_ratio_) + 1),
        pca.explained_variance_ratio_,
        marker='o',
    )

    # the title of the plot is set to 'Explained variance ratio by principal component', which indicates that the plot shows how much of the total variance in the data is explained by each principal component.
    plt.xlabel('Principal component')
    plt.ylabel('Explained variance ratio')
 
    # En Codespaces no hay pantalla: guardamos la imagen ANTES de show()
    plt.savefig('pca_varianza.png')
    plt.show()
