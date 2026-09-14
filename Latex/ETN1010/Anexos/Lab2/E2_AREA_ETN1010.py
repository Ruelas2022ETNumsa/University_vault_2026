# Step 1: Import necessary libraries
from sklearn import datasets                          # Load dataset
from sklearn.model_selection import train_test_split  # Split data
from sklearn.neighbors import KNeighborsClassifier    # KNN model
from sklearn.metrics import accuracy_score            # Evaluate performance
import pandas as pd                                   # For better visualization

# Step 2: Load the Iris dataset
iris = datasets.load_iris()

# Step 3: Convert dataset into a Pandas DataFrame for better visualization
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Show first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(iris_df.head(), "\n")

# Step 4: Define features (X) and labels (y)
X = iris.data   # Features: petal/sepal length & width
y = iris.target  # Labels: 0 = setosa, 1 = versicolor, 2 = virginica

# Step 5: Split data into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Show the number of samples in each set
print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}\n")

# Step 6: Create and train the KNN model
modelo = KNeighborsClassifier(n_neighbors=3)  # Use k=3 neighbors
modelo.fit(X_train, y_train)                  # Train the model

# Step 7: Make predictions on test data
y_pred = modelo.predict(X_test)

# Step 8: Show actual vs. predicted labels
result_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
result_df['Actual_Species']    = result_df['Actual'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
result_df['Predicted_Species'] = result_df['Predicted'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print("Actual vs. Predicted Labels:\n", result_df.head(), "\n")

# Step 9: Evaluate model accuracy
precision = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {precision * 100:.2f}%")
