import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([500, 800, 1000, 1200, 1500]).reshape(-1, 1)
y = np.array([100, 150, 200, 240, 300])

# Train model
model = LinearRegression()
model.fit(X, y)

def predict_price(size):
    return model.predict([[size]])[0]

def get_line_data():
    y_pred = model.predict(X)
    return X.flatten().tolist(), y.tolist(), y_pred.tolist()