# import pandas as pd

# df = pd.read_csv("credit_risk_dataset.csv")

# # describe dataset
# print(df.head(5))
# # print(df.describe())
# print(df.shape)
# print(df.isnull().sum())

import pandas as pd

# Sample data
df = pd.DataFrame({'Gender': ['Male', 'Female', 'Female', 'Male', 'Other'], 'id' : [1,2,3,4,5], 'Gender12': ['Male', 'Female', 'Female', 'Male', 'Other']})

# One-Hot Encoding
df_encoded = pd.get_dummies(df, drop_first=True)  # drop_first=True removes one column to avoid multicollinearity

print(df_encoded)
