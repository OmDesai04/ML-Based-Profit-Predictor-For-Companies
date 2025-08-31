import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb

file_path = './1000_Companies.csv'
data = pd.read_csv(file_path)

# Ensure a stable, explicit output directory for figures
fig_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'figures'))
os.makedirs(fig_dir, exist_ok=True)

X = data[["R&D Spend", "Administration", "Marketing Spend"]]
y = data["Profit"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, "scaler.pkl")

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0, random_state=42),
    "Lasso": Lasso(alpha=0.01, random_state=42),
    "SVR": SVR(),
    "Decision Tree": DecisionTreeRegressor(max_depth=5, random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=200, max_depth=5, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=200, max_depth=3, random_state=42),
    "AdaBoost": AdaBoostRegressor(n_estimators=200, random_state=42),
    "XGBoost": xgb.XGBRegressor(objective="reg:squarederror", n_estimators=300, random_state=42)
}

def evaluate(model, name):
    # Fit a fresh clone of the model
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    cv = cross_val_score(model, X_scaled, y, cv=5).mean()

    return {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2 Score": r2, "CV Score": cv}, y_pred, model

results = {}
predictions = {}
best_score = float("-inf")
best_model_name = None
best_model_trained = None

for name, model in models.items():
    metrics, y_pred, trained_model = evaluate(model, name)
    results[name] = metrics
    predictions[name] = y_pred
    
    score = metrics["R2 Score"] + metrics["CV Score"]
    if score > best_score:
        best_score = score
        best_model_trained = trained_model
        best_model_name = name

# Optionally refit best model on all available data for final export
best_model_trained.fit(X_scaled, y)
joblib.dump(best_model_trained, "best_model.pkl")

print("\nModel Performance Summary:")
for name, metrics in results.items():
    print(f"\n🔹 {name}")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
print(f"\n Best Model: {best_model_name} (Combined Score: {best_score:.4f})")

plt.figure(figsize=(10,5))
sns.barplot(x=list(results.keys()), y=[results[k]["R2 Score"] for k in results])
plt.title("R² Score Comparison")
plt.xticks(rotation=45)
plt.ylabel("R² Score")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "r2_score_comparison.png"))
plt.close()

y_pred_best = predictions[best_model_name]
residuals = y_test - y_pred_best

plt.figure(figsize=(8,4))
sns.histplot(residuals, bins=20, kde=True)
plt.title("Residual Distribution of Best Model")
plt.xlabel("Residuals")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "residual_plot.png"))
plt.close()

plt.figure(figsize=(6,6))
sns.scatterplot(x=y_test, y=y_pred_best)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red')
plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title("Actual vs Predicted Profit")
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, "actual_vs_predicted.png"))
plt.close()

print("\nSaved figures to:")
print(os.path.join(fig_dir, "r2_score_comparison.png"))
print(os.path.join(fig_dir, "residual_plot.png"))
print(os.path.join(fig_dir, "actual_vs_predicted.png"))