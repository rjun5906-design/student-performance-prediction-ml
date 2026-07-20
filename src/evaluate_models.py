"""
Reusable evaluation functions for regression and classification models.
"""

from typing import Dict, Sequence, Optional
from numbers import Real

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)


def eval_reg(
    y_true: Sequence[float],
    y_pred: Sequence[float],
) -> Dict[str, float]:
    """
    Calculate regression metrics:
    MAE, RMSE, and R².
    """

    true_values = np.asarray(y_true, dtype=float)
    predicted_values = np.asarray(y_pred, dtype=float)

    if true_values.size == 0 or predicted_values.size == 0:
        raise ValueError("y_true and y_pred cannot be empty.")

    if true_values.shape != predicted_values.shape:
        raise ValueError(
            "y_true and y_pred must have the same shape."
        )

    mse = mean_squared_error(
        true_values,
        predicted_values,
    )

    return {
        "MAE": float(
            mean_absolute_error(
                true_values,
                predicted_values,
            )
        ),
        "RMSE": float(np.sqrt(mse)),
        "R2": float(
            r2_score(
                true_values,
                predicted_values,
            )
        ),
    }


def eval_clf(
    y_true: Sequence,
    y_pred: Sequence,
    y_proba: Optional[Sequence[Real]] = None,
) -> dict[str, float]:
    """
    Evaluate binary classification predictions.

    Class convention:
    1 = at-risk student
    0 = student not currently classified as at risk
    """

    if len(y_true) != len(y_pred):
        raise ValueError(
            "y_true and y_pred must contain the same number of observations."
        )

    if len(y_true) == 0:
        raise ValueError(
            "The evaluation arrays must not be empty."
        )

    if y_proba is not None and len(y_true) != len(y_proba):
        raise ValueError(
            "y_true and y_proba must contain the same number of observations."
        )

    results = {
        "accuracy": float(
            accuracy_score(y_true, y_pred)
        ),
        "precision": float(
            precision_score(
                y_true,
                y_pred,
                zero_division=0,
            )
        ),
        "recall": float(
            recall_score(
                y_true,
                y_pred,
                zero_division=0,
            )
        ),
        "f1": float(
            f1_score(
                y_true,
                y_pred,
                zero_division=0,
            )
        ),
    }

    if y_proba is not None:
        results["roc_auc"] = float(
            roc_auc_score(
                y_true,
                y_proba,
            )
        )

    return results