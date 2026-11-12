
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dataset
X = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0],
    [1, 1],
    [0, 0],
    [1, 0],
    [0, 1]
]

y = ['Yes', 'Yes', 'Yes', 'No',
     'Yes', 'No', 'Yes', 'Yes']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Predicted Output:", y_pred)
print("Actual Output:", y_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# New prediction
print("New Prediction:", model.predict([[1, 1]])[0])
