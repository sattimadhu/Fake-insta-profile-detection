import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def predict_profile(profile_data):
    prediction = model.predict([profile_data])
    if prediction[0]==0:
        return 'Real'
    else:
        return 'Fake'
def accuracy(test,pred):
    return accuracy_score(test,pred)

# reading data from datasets fake.json and real.json
fake=pd.read_json('data\\fakeProfiles.json')
real=pd.read_json('data\\realProfiles.json')

# combining the datasets
data=pd.concat([fake, real], ignore_index=True)

# splitting features and labels
X=data[['userFollowerCount', 'userFollowingCount', 'userBiographyLength',
          'userMediaCount', 'userHasProfilPic', 'userIsPrivate',
          'usernameDigitCount', 'usernameLength']]
y=data[['isFake']]

# splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

# model=LogisticRegression()
#training the model
model=DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred=model.predict(X_test)
print(accuracy(y_test,y_pred)*100)

