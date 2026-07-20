# Session 17: Correlation Analysis Interpretation

## Summary

The correlation analysis shows that G2 and G1 have the strongest relationships with G3. G2 has a correlation of 0.904868 with G3, while G1 has a correlation of 0.801468. These results indicate very strong positive associations between earlier grades and the final grade. The strongest negative correlation is failures (-0.360415), suggesting that students with more past failures tend to have lower final grades.

## Interpretation

G2 has the strongest positive correlation with G3, followed by G1. This is expected because G1, G2, and G3 represent student performance at different stages of the same course. Students who perform well earlier in the course generally continue to perform well on the final grade.

Failures has the strongest negative correlation with G3 (-0.360415), indicating that students with a history of failing courses tend to earn lower final grades. Other variables such as parental education (Medu and Fedu) show weaker positive relationships, while age, going out with friends, and travel time show modest negative relationships.

Correlation measures association, not causation. These results do not prove that any variable directly causes higher or lower grades.

## Recommendation

Develop two modeling scenarios:

1. **Full-Information Model**
   - Include G1 and G2.
   - Appropriate when earlier grades are already available.
   - Likely to produce the highest predictive accuracy.

2. **Early-Warning Model**
   - Exclude G1 and G2.
   - Appropriate when identifying at-risk students before those grades exist.
   - Avoids temporal leakage and provides a more realistic prediction setting.

The strong correlations of G1 and G2 are valuable, but they may create a leakage concern if used in an early-warning model because those grades would not yet be available at the time predictions are made.