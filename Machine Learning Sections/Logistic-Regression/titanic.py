import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.ioff()

df = pd.read_csv('titanic_train.csv')
# sns.boxplot(x='Pclass', y='Age', data=df, hue='Embarked')

plt.show()
