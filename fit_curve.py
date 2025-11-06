
import numpy as np
import pandas as pd

def fit_and_score(csv_path):
    df = pd.read_csv(csv_path)
    x_data = df['x'].values
    y_data = df['y'].values
    N = len(df)
    t = np.linspace(6, 60, N)

    theta = 0.490777338
    M = 0.0213825022
    X = 54.8999932

    x_pred = (t*np.cos(theta) - np.exp(M*np.abs(t))*np.sin(0.3*t)*np.sin(theta) + X)
    y_pred = (42 + t*np.sin(theta) + np.exp(M*np.abs(t))*np.sin(0.3*t)*np.cos(theta))
    L1_total = np.sum(np.abs(x_data - x_pred) + np.abs(y_data - y_pred))
    L1_per_point = L1_total / N
    return L1_total, L1_per_point

if __name__ == '__main__':
    L1_total, L1_per_point = fit_and_score('xy_data.csv')
    print('L1_total:', L1_total)
    print('L1_per_point:', L1_per_point)
