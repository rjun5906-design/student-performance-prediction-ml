# Encoding Plan

## Project

Predicting Student Academic Success Using Interpretable Machine Learning

## Session

Session 11: Categorical Variables

## Purpose

This encoding plan documents how categorical variables will be converted into numeric features for machine learning. Most machine learning algorithms require numeric input, so categorical variables must be encoded before model training.

The encoding strategy depends on whether each categorical variable is nominal, binary, or ordinal.

## Encoding Rules

### Binary Variables

Variables with only two categories will be encoded as 0/1.

Examples:

* yes = 1
* no = 0

### Nominal Variables

Variables with more than two categories and no natural order will use one-hot encoding.

Example:

* Mjob
* Fjob
* reason
* guardian

### Ordinal Variables

Variables with meaningful ordered levels will remain numeric.

Examples:

* Medu
* Fedu
* traveltime
* studytime
* health

## Encoding Decisions

| Variable   | Type    | Encoding |
| ---------- | ------- | -------- |
| school     | Binary  | 0/1      |
| sex        | Binary  | 0/1      |
| address    | Binary  | 0/1      |
| famsize    | Binary  | 0/1      |
| Pstatus    | Binary  | 0/1      |
| schoolsup  | Binary  | 0/1      |
| famsup     | Binary  | 0/1      |
| paid       | Binary  | 0/1      |
| activities | Binary  | 0/1      |
| nursery    | Binary  | 0/1      |
| higher     | Binary  | 0/1      |
| internet   | Binary  | 0/1      |
| romantic   | Binary  | 0/1      |
| Mjob       | Nominal | One-Hot  |
| Fjob       | Nominal | One-Hot  |
| reason     | Nominal | One-Hot  |
| guardian   | Nominal | One-Hot  |

## Reflection Question

Ordinal encoding can mislead a model when categories do not have a true natural order.

For example, assigning job categories such as teacher, health, services, and other numerical values creates a false ranking that does not exist.

One-hot encoding is more appropriate for unordered categories because it avoids introducing artificial distances between categories.
student-performance-prediction-ml
└── notebooks