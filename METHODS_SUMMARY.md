# Methods Summary

## Project framing

This repository supports Brown Norway rat OCT age-prediction experiments using RETFound-LoRA, matched CNN baselines, and manuscript-oriented reproducibility assets for the OSD-679 study.

The central scientific question is whether a retinal age model trained only on control animals can generate a retinal age gap (RAG) signal that reflects ocular stress and recovery in hindlimb suspension (HLS) animals.

## Primary model

- Backbone: RETFound NatureOCT checkpoint.
- Adaptation strategy: LoRA applied to the final RETFound blocks.
- Input unit: rat/eye/day OCT bag.
- Aggregation: attention-based multiple-instance learning over all available OCT views for each rat/eye/day.
- Training cohort: controls only.
- Evaluation cohort: out-of-fold controls plus HLS animals.
- Cross-validation: 3-fold rat-level cross-validation to avoid leakage across observations from the same animal.

## Primary derived endpoints

```text
RAG = predicted_retinal_age_days - chronological_age_days
```

```text
DeltaRAG(day) = RAG(day) - RAG(day 0)
```

DeltaRAG is computed only when a valid day-0 baseline exists for the same rat/eye.

## Main interpretation

The current analysis supports RAG as a continuous image-derived ocular stress-recovery phenotype, not as a standalone binary HLS classifier.

The strongest current biological association is recovery-phase RAG versus temporal choroidal thickness in HLS animals. DeltaRAG group separation is weak and should not be presented as a robust HLS detector.

## Recommended statistical framing

Final manuscript inference should account for repeated observations across rat, eye, and day. Recommended approaches include mixed-effects models or rat-level clustered bootstrap confidence intervals.

Example model form:

```text
biomarker ~ RAG_or_DeltaRAG + group + day + RAG_or_DeltaRAG:group + (1 | rat_id)
```

For biomarkers with strong day effects, use day-centered RAG or include day as a categorical covariate.

## Claims currently supported

- RETFound-LoRA predicts chronological age from Brown Norway rat OCT with stable out-of-fold control performance.
- RAG provides a continuous image-derived age-deviation score.
- Recovery-phase RAG is strongly associated with temporal choroidal thickness in HLS animals.
- DeltaRAG has candidate associations with choroidal/retinal thickness changes, but these require more power and external validation.

## Claims to avoid

- Do not claim that DeltaRAG is a strong HLS classifier.
- Do not claim that day-90 DeltaRAG separates HLS from controls.
- Do not use biomarker-input age models as evidence for biomarker discovery, because this creates circularity if the same biomarkers are later correlated with RAG.

## Workflow overview

```text
OSD-679 OCT images
        ↓
Rat/eye/day OCT bags
        ↓
RETFound-LoRA + attention MIL
        ↓
Predicted retinal age
        ↓
RAG / DeltaRAG
        ↓
A) HLS-vs-control separation
B) biomarker association
C) recovery-phase remodeling interpretation
```
