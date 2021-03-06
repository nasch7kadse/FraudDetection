# -*- coding: utf-8 -*-
# Copyright 2014-now Equitania Software GmbH - Pforzheim - Germany
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from FraudAPI.fraud_predictor.utils import parse_yaml, get_model_name
from build_model import create_model
import os
import pandas as pd
import joblib


def start_predictor(parameter_list: dict):
    dataframe = convert_parameter_list_to_numpy(parameter_list)
    model_path = get_model_name("../../model/input/creditcard.csv")
    if not os.path.exists(model_path):
        create_model()

    # Starting parameters
    regression_model = joblib.load(model_path)
    prediction = regression_model.predict(dataframe)
    return prediction


def convert_parameter_list_to_numpy(parameter_list: dict):
    dataframe = {}
    for key, value in parameter_list.items():
        dataframe[key] = [float(value)]
    return pd.DataFrame(dataframe)
