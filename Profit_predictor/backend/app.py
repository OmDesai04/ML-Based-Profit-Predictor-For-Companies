import sys
import joblib
import numpy as np
import pandas as pd  

model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

rnd, admin, market = map(float, sys.argv[1:4])

X_input = pd.DataFrame([[rnd, admin, market]], columns=['R&D Spend', 'Administration', 'Marketing Spend'])

X_scaled = scaler.transform(X_input)
pred = model.predict(X_scaled)

print(pred[0])