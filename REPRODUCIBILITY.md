# Reproducibility Guide

This guide describes how to reproduce the repository-level derived tables and manuscript-facing assets. The raw OSD-679 image payload is not redistributed in this repository.

## 1. Prepare the environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For GPU training, install the PyTorch build that matches your CUDA version before installing the remaining requirements.

## 2. Obtain the raw data

Download the OSD-679 image payload through NASA GeneLab / the Open Science Data Repository according to the dataset access instructions.

This repository expects a local OSD-679-style directory layout. The released manifests contain relative image paths and do not include the raw OCT images.

## 3. Verify required local inputs

The reproducibility-bundle script expects local metadata and result files such as:

```text
metadata/image_age_mapping.csv
outputs/paper1/supplementary/tables/Supplementary_Table_S1_Cohort_Characteristics_and_Sample_Counts.csv
outputs/paper1/supplementary/tables/Supplementary_Table_S2_Control_Model_Performance_3Fold_CV.csv
outputs/paper1/supplementary/tables/Supplementary_Table_S9_CrossValidation_Split_Definitions_Rat_IDs.csv
outputs/paper1/tables/table3_backbone_ablation_mainpaper.csv
```

If these files are missing, regenerate the upstream metadata, training, evaluation, and paper-table outputs before building the release bundle.

## 4. Rebuild the release bundle

```bash
python3 scripts/paper/build_reproducibility_bundle.py
```

The output folder is:

```text
reproducibility/osd679_age_prediction_release/
```

Expected outputs include:

- `Supplementary_Data_1_Image_to_Age_Mapping.xlsx`
- `Supplementary_Data_2_Benchmark_Splits_and_Results.xlsx`
- `Supplementary_Data_3_Qualitative_Examples.xlsx`
- CSV companion files
- `bundle_manifest.json`
- bundle-level `README.md`

## 5. Primary analysis logic

The primary RAG analysis should use the image-only RETFound-LoRA model trained on controls only.

Recommended sequence:

```text
OSD-679 OCT images
        ↓
Rat/eye/day OCT bags
        ↓
RETFound-LoRA + attention MIL
        ↓
Predicted retinal age
        ↓
RAG and DeltaRAG
        ↓
Group separation and biomarker association analyses
```

## 6. Interpretation limits

The current results support RAG as a continuous retinal stress-recovery phenotype. They do not support DeltaRAG as a strong binary HLS classifier.

Biomarker-input age models should remain exploratory and should not be used for biomarker-discovery claims if the same biomarkers are later correlated with RAG.
