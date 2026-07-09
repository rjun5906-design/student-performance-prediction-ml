# Cleaning Checklist

## Project

Student Performance Prediction Using Machine Learning

## Session

Session 10: Missing Values and Duplicates

## Summary

The dataset was checked for missing values and duplicate rows as part of Session 10. The missing-value check showed that all columns have zero missing values. The duplicate-row check also showed zero duplicate rows.

## Missing Values

### Python Code Used

```python
df.isna().sum()
```

### Result

No missing values were found in the dataset.

### Decision

No imputation is needed.

### Reason

Because every column has zero missing values, replacing or estimating values would be unnecessary and could introduce artificial patterns into the data.

## Duplicate Rows

### Python Code Used

```python
df.duplicated().sum()
```

### Result

No duplicate rows were found.

### Decision

No duplicate rows need to be removed.

### Reason

Because the duplicate count is zero, the dataset does not contain repeated records that could bias model training or evaluation.

## Recommendation

No cleaning action is required for missing values or duplicate rows at this stage. The dataset can move forward to preprocessing and feature engineering. However, this result should still be documented because confirming that no cleaning is needed is an important part of a reproducible data-quality workflow.

## Reflection Question

### Question

Why is documenting "no cleaning needed" just as important as documenting cleaning steps?

### Answer

Documenting "no cleaning needed" is important because it confirms that the dataset was actually checked for data-quality problems. If no missing values or duplicate rows are found, this result should still be recorded so that future readers understand why no imputation or duplicate removal was performed.

This improves reproducibility because another researcher can see the exact reason cleaning was not applied. It also improves transparency because the decision is based on evidence from the data, not assumption. In this project, the missing-value count was 0 and the duplicate-row count was 0, so no cleaning action was required for these two issues.
