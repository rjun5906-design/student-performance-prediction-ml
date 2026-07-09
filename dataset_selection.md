# Dataset Selection

## Chosen Dataset

The selected dataset for this project is the **UCI Student Performance Dataset**.

## Dataset Source

The dataset is available from the **UCI Machine Learning Repository**.

Dataset URL:

https://archive.ics.uci.edu/dataset/320/student+performance

## Dataset Description

The UCI Student Performance Dataset contains student information related to academic performance in secondary education. It includes demographic, social, school-related, and academic variables. The main target variable for this project is **G3**, which represents the student's final grade.

## Target Variable

**G3 — Final Grade**

The value of G3 ranges from 0 to 20.

## Machine Learning Task Types

This dataset is appropriate for both regression and classification.

For regression, the model can predict the numerical final grade, G3.

For classification, the G3 variable can be converted into categories such as:

- Pass / Fail
- Low / Medium / High Performance
- At-Risk / Not At-Risk

## Reason for Selection

This dataset is a strong choice for the project because it is public, structured, and small enough for classroom use in Google Colab. It supports both regression and classification, which allows students to compare different machine learning algorithms using the same dataset.

One important modeling issue is that G1 and G2 are strongly related to G3. These variables may create target leakage if the goal is early prediction before final grades are known.

## License

The dataset is available under the **Creative Commons Attribution 4.0 International License (CC BY 4.0).**

## Citation

Cortez, P., & Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance.

UCI Machine Learning Repository. Student Performance Dataset.