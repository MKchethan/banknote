## load the train and test split
## train algo
## save the metrices, params
import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import RandomForestClassifier
from get_data import read_params
import argparse
import joblib
import json


def eval_metrics(actual, pred):
    accuracy = accuracy_score(actual, pred)
    return accuracy

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    max_depth = config["estimators"]["RandomForestClassifier"]["params"]["max_depth"]
    n_estimators = config["estimators"]["RandomForestClassifier"]["params"]["n_estimators"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    rfc = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=random_state)
    rfc.fit(train_x, train_y)

    predicted_qualities = rfc.predict(test_x)

    (accuracy) = eval_metrics(test_y, predicted_qualities)

    print("Random Forest (max_depth=%f, n_estimators=%f):" % (max_depth, n_estimators))
    print("  Accuracy: %s" % accuracy)

 ###################################################################

    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f:
        scores = {
            "Accuracy": accuracy
        }
        json.dump(scores, f, indent=4)

    with open(params_file, "w") as f:
        params = {
            "max_depth": max_depth,
            "n_estimators": n_estimators,
        }
        json.dump(params, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(rfc, model_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)


