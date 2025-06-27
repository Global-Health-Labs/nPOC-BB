# Risk Evaluation

## Overview

The nPOC-BB was originally developed at GHL as the front-end of a prototype diagnostic test system called NAATOS. Therefore, the design inputs for the nPOC-BB are a subset of the design inputs for NAATOS, and the Risk Evaluation for the nPOC-BB is excerpted from the larger NAATOS Risk Evaluation.

You can also [download a tabular version of this Risk Evaluation Table in the ```*.csv``` format](../tables/nPOC-BB_risk.csv).

## Lookup Matrices

### Probability

P1 (Probability of the Hazardous Situation Occurring) × P2 (Probability of the Hazardous Situation Leading to Harm) = Probability

{{ read_csv("docs/tables/lookup_probability.csv") }}

### Risk Level

S (Severity) × P (Probability) = Risk Level

{{ read_csv("docs/tables/lookup_risk.csv") }}

## Risk Evaluation Table

{{ read_csv("docs/tables/nPOC-BB_risk.csv", na_filter = False) }}
