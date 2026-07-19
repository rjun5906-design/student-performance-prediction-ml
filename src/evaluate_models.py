from typing import Dict, Sequence

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


def eval_reg(
    y_true: Sequence[float],
    y_pred: Sequence[float],
) -> Dict[str, float]:
    """
    Calculate common regression evaluation metrics.
    """

    true_values = np.asarray(y_true, dtype=float)
    predicted_values = np.asarray(y_pred, dtype=float)

    if true_values.size == 0 or predicted_values.size == 0:
        raise ValueError("y_true and y_pred cannot be empty.")

    if true_values.shape != predicted_values.shape:
        raise ValueError(
            "y_true and y_pred must have the same shape."
        )

    if not np.all(np.isfinite(true_values)):
        raise ValueError(
            "y_true contains missing or infinite values."
        )

    if not np.all(np.isfinite(predicted_values)):
        raise ValueError(
            "y_pred contains missing or infinite values."
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
