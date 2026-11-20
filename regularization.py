import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression
from skLearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

from skLearn.model_selection import train_test_split
from sklearn.metrics import mean_squeared_error

if  __name__ == "__main__":
    dataset = pd.read_csv('./data/whr2017.csv')
    print(dataset.describe())
    
