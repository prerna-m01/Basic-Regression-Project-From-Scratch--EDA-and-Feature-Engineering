from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import joblib

# Create dummy data
X, y = make_regression(
    n_samples=100,
    n_features=1,
    noise=10
)

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "regression_model.pkl")

print("Model saved successfully")