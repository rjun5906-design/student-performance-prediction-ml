# Data Dictionary

## Dataset Information

**Dataset Name:** UCI Student Performance Dataset (Mathematics)

**Source:** UCI Machine Learning Repository

**Target Variable:** G3 (Final Grade)

**Instances:** 395

**Features:** 33

---

# Demographic Variables

| Variable | Description                     |
| -------- | ------------------------------- |
| school   | Student's school                |
| sex      | Student's sex                   |
| age      | Student's age                   |
| address  | Home address type (urban/rural) |

---

# Social Variables

| Variable | Description                     |
| -------- | ------------------------------- |
| famsize  | Family size                     |
| Pstatus  | Parent cohabitation status      |
| Medu     | Mother's education              |
| Fedu     | Father's education              |
| Mjob     | Mother's job                    |
| Fjob     | Father's job                    |
| guardian | Student's guardian              |
| famrel   | Quality of family relationships |
| freetime | Free time after school          |
| goout    | Going out with friends          |
| Dalc     | Workday alcohol consumption     |
| Walc     | Weekend alcohol consumption     |
| health   | Current health status           |
| romantic | Romantic relationship status    |

---

# School-Related Variables

| Variable   | Description                 |
| ---------- | --------------------------- |
| reason     | Reason for choosing school  |
| traveltime | Home-to-school travel time  |
| studytime  | Weekly study time           |
| schoolsup  | Extra educational support   |
| famsup     | Family educational support  |
| paid       | Extra paid classes          |
| activities | Extracurricular activities  |
| nursery    | Attended nursery school     |
| higher     | Desire for higher education |
| internet   | Internet access at home     |
| absences   | Number of school absences   |

---

# Academic Variables

| Variable | Description                   |
| -------- | ----------------------------- |
| failures | Number of past class failures |
| G1       | First period grade            |
| G2       | Second period grade           |
| G3       | Final grade (Target Variable) |

---

# Interpretation Notes

The dataset contains demographic, social, school-related, and academic factors associated with student performance. These variables can be used to investigate relationships between student characteristics, behaviors, family background, and academic outcomes.

---

# Modeling Note

The target variable for this project is G3 (final grade). The variables G1 and G2 are highly correlated with G3 and may introduce target leakage when developing early-warning prediction models. Models should be evaluated carefully when including or excluding these variables.
