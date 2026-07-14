# Scaling Plan

## Session 12: Numerical Variables

## Purpose

The purpose of this scaling plan is to decide which numerical variables should be scaled before machine-learning models are trained. Scaling is important because some models are sensitive to the size and range of numeric features.

## Numeric Variable Review

The dataset was reviewed using the following Python code:

```python
num_cols = df.select_dtypes(include="number").columns.tolist()
print(df[num_cols].agg(["min", "max", "mean"]).T)
```

This code identified all numeric columns and summarized their minimum, maximum, and mean values.

## Why Scaling Is Needed

Some numeric variables may have different ranges. For example, one variable may range from 0 to 4, while another may range from 0 to 100. Models that use distances, gradients, or coefficients can be affected by these differences.

## Models That Need Scaling

1. Logistic Regression
   - Scaling helps optimization converge more reliably.

2. Linear Regression
   - Scaling improves stability, especially when regularization is used.

3. K-Nearest Neighbors (KNN)
   - Distance-based models require scaling so larger-value variables do not dominate.

4. Support Vector Machine (SVM)
   - SVM depends on distances and margins, making scaling important.

5. Neural Networks
   - Scaled inputs improve gradient-based learning.

## Models That Usually Do Not Require Scaling

1. Decision Tree
   - Uses threshold splits and is generally unaffected by scale.

2. Random Forest
   - Collection of decision trees and usually does not require scaling.

3. Gradient Boosting
   - Tree-based boosting models generally do not require scaling.

## Recommended Pipeline Approach

- Use StandardScaler for Logistic Regression, Linear Regression, KNN, SVM, and Neural Networks.
- Do not apply scaling for Decision Tree, Random Forest, or Gradient Boosting unless needed for a specific experiment.
- Use scikit-learn Pipelines to prevent data leakage.
- Fit the scaler only on training data.
- Apply the fitted scaler to validation and test data.

## Final Recommendation

Scaling should be included for Logistic Regression, Linear Regression, KNN, SVM, and Neural Networks. Scaling is not required for Decision Tree, Random Forest, or Gradient Boosting models. Separate preprocessing pipelines should be used so that each model receives the appropriate preprocessing.