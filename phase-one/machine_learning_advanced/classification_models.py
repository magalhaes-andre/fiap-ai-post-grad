import pandas as pd
df = pd.read_csv(r"C:\Users\arfdd\coding\post-grad\phase-one\machine_learning_advanced\fruits.csv")
print(df.head())

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

df['Fruit Categories'] = label_encoder.fit_transform(df['Fruit'])

print(df.head())

dum_df = pd.get_dummies(df, columns=["Fruit"])

dum_df.to_csv("fruits_with_dummies.csv")

# Jupyter Notebooks with examples:
# https://github.com/FIAP/Pos_Tech_DTAT/blob/4adb2f888cacb37fa813674e3ec2e970c63d3c20/Aula%2001/Notebooks/Introdu%C3%A7%C3%A3o_a_modelos_de_classifica%C3%A7%C3%A3o.ipynb    