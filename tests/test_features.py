import numpy as np
import sys
sys.path.append(r"C:\Users\suhai\bandgap-predictor")

from matminer.featurizers.composition import ElementProperty
from pymatgen.core import Composition

def formula_to_features(formula_list):
    featurizer = ElementProperty.from_preset("magpie")
    rows = []
    for formula in formula_list:
        try:
            comp = Composition(formula)
            features = featurizer.featurize(comp)
            rows.append(features)
        except:
            rows.append([0] * len(featurizer.feature_labels()))
    return np.array(rows)

def test_feature_shape():
    X = formula_to_features(["Rb2Te", "CdCl2"])
    assert X.shape[0] == 2
    assert X.shape[1] > 100

def test_invalid_formula_returns_zeros():
    X = formula_to_features(["INVALID123"])
    assert X.shape[0] == 1
    assert np.sum(X) == 0