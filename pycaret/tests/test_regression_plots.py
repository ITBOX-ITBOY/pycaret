import os, sys

sys.path.insert(0, os.path.abspath(".."))

import pandas as pd
import pytest
import pycaret.regression
import pycaret.datasets

def test():
    # loading dataset
    data = pycaret.datasets.get_data('juice')
    assert isinstance(data, pd.core.frame.DataFrame)

    # init setup
    reg1 = pycaret.regression.setup(data, target='Purchase', log_experiment=True, silent=True, html=False, session_id=123, fold=2)
    
    model = pycaret.regression.create_model('rf')

    available_plots = [
        "parameter",
        "residuals",
        "error",
        "cooks",
        "rfe",
        "learning",
        "manifold",
        "vc",
        "feature",
        "feature_all",
    ]

    for plot in available_plots:
        pycaret.regression.plot_model(model, plot=plot)

    models = [pycaret.regression.create_model('et'), pycaret.regression.create_model('xgboost')]

    available_shap = ["summary", "correlation", "reason"]

    for model in models:
        for plot in available_shap:
            pycaret.regression.interpret_model(model, plot=plot)

    assert 1 == 1
    
if __name__ == "__main__":
    test()
