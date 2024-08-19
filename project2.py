import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Step 1: Data Collection
# Generating a sample dataset
np.random.seed(0)

data = pd.DataFrame({
    'age': np.random.randint(20, 80, 100),
    'gender': np.random.choice(['male', 'female'], 100),
    'bmi': np.random.normal(25, 5, 100),
    'blood_pressure': np.random.normal(120, 10, 100),
    'cholesterol': np.random.normal(200, 30, 100),  # Fixed typo here
    'family_history': np.random.choice([0, 1], 100),  # 0: No, 1: Yes
    'disease': np.random.choice([0, 1], 100)  # 0: No disease, 1: Disease present
})

# Display the first few rows of the dataset
print("Sample Data:")
print(data.head())

# Step 2: Data Preprocessing
# Handle missing values separately for numeric and categorical columns
data.fillna({
    'age': data['age'].mean(),
    'bmi': data['bmi'].mean(),
    'blood_pressure': data['blood_pressure'].mean(),
    'cholesterol': data['cholesterol'].mean(),
    'family_history': data['family_history'].mode()[0],
    'gender': data['gender'].mode()[0]
}, inplace=True)

# Encode categorical variables
data['gender'] = data['gender'].map({'male': 0, 'female': 1})

# Separate features and target
X = data.drop('disease', axis=1)
y = data['disease']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 3: Feature Selection
# (For simplicity, we are using all features)

# Step 4: Model Development
# Creating a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Step 5: Cross-Validation
# Performing cross-validation
# Make sure to scale X before cross-validation
X_scaled = scaler.fit_transform(X)
cv_scores = cross_val_score(model, X_scaled, y, cv=5)

print("\nCross-Validation Results:")
print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Score: {cv_scores.mean():.2f}")

# Step 6: Hyperparameter Tuning
param_grid = {
    'C': [0.1, 1, 10],
    'solver': ['liblinear', 'saga']
}

# Initialize GridSearchCV
grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5, scoring='accuracy')

# Fit the grid search
grid_search.fit(X_train, y_train)

# Display the best parameters and best score from grid search
print("\nHyperparameter Tuning Results:")
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best CV Score: {grid_search.best_score_:.2f}")
