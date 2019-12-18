import tensorflow as tf
import numpy as np
import pandas as pd

from m4_evaluation_metrices import *
from glob import glob


def read_raw_data(file_path):
    df = pd.read_csv(file_path)
    try:
        del df['V1']
    except Exception as e:
        print('No headers row to remove, will continue..')
    
    return df.values

def evaluate_point_predictions(train_data, test_data, point_predcitions):
    errors = []

    for sample_x, sample_y, sample_prediction in zip(train_data, test_data, point_predcitions):
        sample_x = sample_x[~np.isnan(sample_x)]

        errors.append(m4_mase(sample_x, sample_y, sample_prediction))

    return np.array(errors).mean()

def evaluate_intervals_predictions(train_data, test_data, lower_predcitions, upper_predcitions):
    acd_coverage = []
    msis_errors = []

    samples = zip(train_data, test_data, lower_predcitions, upper_predcitions)

    for sample_x, sample_y, sample_lower_prediction, sample_upper_prediction in samples :
        sample_x = sample_x[~np.isnan(sample_x)]

        acd_coverage.append(acd(sample_y, sample_lower_prediction, sample_upper_prediction))
        msis_errors.append(msis(sample_x, sample_y, sample_lower_prediction, sample_upper_prediction))

    return np.array(acd_coverage).mean(), np.array(msis_errors).mean()



train_data = read_raw_data('Dataset/Hourly-train.csv')
test_data = read_raw_data('Dataset/Hourly-test.csv')

groups = ['SSY']

for group in groups:
    print(f'===============Evaluation results for {group}===============')
    
    models = glob(f'{group}/*/')

    for model_path in models:
        print(f'==== For model {model_path}')

        point_predcitions = read_raw_data(f'{model_path}/point.csv')
        lower_predcitions = read_raw_data(f'{model_path}/lower.csv')
        upper_predcitions = read_raw_data(f'{model_path}/upper.csv')
        

        mase_err = evaluate_point_predictions(train_data, test_data, point_predcitions)
        print(f'Point Predcition MASE {mase_err}')

        acd_err, msis_err = evaluate_intervals_predictions(train_data, test_data, lower_predcitions, upper_predcitions)
        print(f'Interval Predcition ACD {acd_err}')
        print(f'Interval Predcition MSIS {msis_err} \n')

        