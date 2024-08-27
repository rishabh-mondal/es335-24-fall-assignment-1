import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import pandas as pd
import os
import numpy as np

def plot_waveform(X: pd.DataFrame, y: pd.Series, num_rows: int = 3, num_cols: int = 2) -> None:
    """
    Plots the waveform for each activity class
    :param X: The input features extracted from MakeDataset.py
    :param y: The labels for the input features extracted from MakeDataset.py
    :param num_rows: Number of rows in the plot
    :param num_cols: Number of columns in the plot
    """
    columns = [f'axis_{axis}_{i}' for axis in ['x', 'y', 'z'] for i in range(500)]
    df = pd.DataFrame(X.reshape((X.shape[0], -1)), columns=columns)
    df['activity_class'] = y
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))
    axes = np.ravel(axes)
    activity_classes = df['activity_class'].unique()
    activity_classes.sort()
    
    activity = {1:"WALKING",2:"WALKING_UPSTAIRS",3:"WALKING_DOWNSTAIRS",4:"SITTING",5:"STANDING",6:"LAYING"}
    
    for i, activity_class in enumerate(activity_classes):
        activity_df = df[df['activity_class'] == activity_class].drop('activity_class', axis=1)
        activity_mean = activity_df.mean()
        axes[i].plot(activity_mean)
        axes[i].set_xticks([])
        axes[i].set_title(f'Waveform for Activity Class {activity[activity_class]}')
        axes[i].set_xlabel('Time')
        axes[i].set_ylabel('Acceleration')
    
    plt.tight_layout()
    plt.show()
    plt.savefig('waveform_plot.png')
