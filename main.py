from google.colab import drive
import pandas as pd


drive.mount('/content/drive')
file_path = '/content/drive/MyDrive/vgsales.csv'

df = pd.read_csv(file_path)

df.drop('Name', axis = 1, inplace = True)
df = pd.get_dummies(df, columns = ['Platform', 'Genre'], drop_first = True)
publisher_count = df['Publisher'].value_counts()
df['Publisher'] = df['Publisher'].map(publisher_count)
df.rename(columns = {'Publisher' : 'Publisher_encoded'}, inplace = True)
print(df.head())
