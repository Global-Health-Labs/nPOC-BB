# Risk Evaluation

## Overview

The nPOC-BB was originally developed at GHL as the front-end of a prototype diagnostic test system called NAATOS. Therefore, the design inputs for the nPOC-BB are a subset of the design inputs for NAATOS, and the Risk Evaluation for the nPOC-BB is excerpted from the larger NAATOS Risk Evaluation.

You can also [download a tabular version of this Risk Evaluation Table in the ```*.csv``` format](./nPOC-BB_risk.csv).

## Lookup Matrices

### Risk Level - Probability (P1 x P2 = P)

{{ read_csv("docs/inputs/lookup_probability.csv") }}

### Risk Level - Risk Level (S x P = Risk)

{{ read_csv("docs/inputs/lookup_risk.csv") }}

## Risk Evaluation Table

{{ read_csv("docs/inputs/nPOC-BB_risk.csv", na_filter = False) }}
