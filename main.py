from google.colab import drive
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


drive.mount('/content/drive')
file_path = '/content/drive/MyDrive/vgsales.csv'

df = pd.read_csv(file_path)

df.drop('Name', axis = 1, inplace = True)
df = pd.get_dummies(df, columns = ['Platform', 'Genre'], drop_first = True)
publisher_count = df['Publisher'].value_counts()
df['Publisher'] = df['Publisher'].map(publisher_count)
df.rename(columns = {'Publisher' : 'Publisher_encoded'}, inplace = True)
df.dropna(inplace = True)
print(df)

X = df.drop(columns = ['EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Rank'])
y = df['Global_Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)
x_scale = StandardScaler()
y_scale = StandardScaler()
y_train_reshaped = y_train.values.reshape(-1, 1)
X_train_scaled = x_scale.fit_transform(X_train)
y_train_scaled = y_scale.fit_transform(y_train_reshaped)
model = LinearRegression ()
model.fit(X_train_scaled, y_train_scaled)
predictions_reshaped = model.predict(x_scale.transform(X_test)).reshape(-1, 1)
y_pred = y_scale.inverse_transform(predictions_reshaped)
print(y_pred)
print(f'r2_score : {r2_score(y_test, y_pred.flatten())}')
print(f'mse : {mean_squared_error(y_test, y_pred.flatten())}')
print(f'mae : {mean_absolute_error(y_test, y_pred.flatten())}')
