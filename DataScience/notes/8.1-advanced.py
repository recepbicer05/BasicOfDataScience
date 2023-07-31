
# Gelişmiş Fonksiyonel Keşifçi Veri Analizi (ADVANCED FUNCTIONAL EDA)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

def check_df(dataframe, head=5):
    print("######### Shape #########")
    print(dataframe.shape)
    print("######### Types #########")
    print(dataframe.dtypes)
    print("######### Head #########")
    print(dataframe.head(head))
    print("######### Tail #########")
    print(dataframe.tail(head))
    print("######### NA #########")
    print(dataframe.isnull().sum())
    print("######### Quantiles #########")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)
df1= sns.load_dataset("tips")
check_df(df1)
