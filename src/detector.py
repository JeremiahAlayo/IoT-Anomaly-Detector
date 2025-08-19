import pandas as pd
from sklearn.ensemble import IsolationForest

def fit_isoforest(df: pd.DataFrame, feature_cols):
    X = df[feature_cols].fillna(0)
    model = IsolationForest(random_state=42)
    model.fit(X)
    return model

def score(model, df: pd.DataFrame, feature_cols):
    X = df[feature_cols].fillna(0)
    labels = model.predict(X)          # 1 = normal, -1 = anomaly
    scores = model.decision_function(X) * -1  # higher = more anomalous
    out = df.copy()
    out["anomaly_label"] = (labels == -1).astype(int)
    out["anomaly_score"] = scores
    return out
