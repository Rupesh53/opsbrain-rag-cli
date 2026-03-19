from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Dummy training (replace later with real logs)
X = np.array([
    [10, 2],
    [50, 5],
    [100, 8],
    [20, 3],
])
y = np.array([4, 6, 9, 5])

model = RandomForestRegressor()
model.fit(X, y)

def predict_quality(query, chunks):
    features = [[len(query), chunks]]
    print(f"Length of query {len(query)}")
    print(f"chunks {chunks}")
    return float(model.predict(features)[0])