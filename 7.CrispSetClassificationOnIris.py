import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# Crisp Set boundaries for petal length
def classify_petal_length(row):
    if row['petal length (cm)'] < 2.5:
        return 'Setosa'
    elif 2.5 <= row['petal length (cm)'] <= 5.0:
        return 'Versicolor'
    else:
        return 'Virginica'

# Apply the classification
iris_df['Crisp Set'] = iris_df.apply(classify_petal_length, axis=1)

# Display the resulting classification
print(iris_df[['petal length (cm)', 'Crisp Set']])
