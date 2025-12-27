# IMPC Phenotype Image Analysis

## Project Overview
This project explores gene–phenotype associations using publicly available data from the International Mouse Phenotyping Consortium (IMPC). 
It combines **data extraction, ontology inspection, and automated image analysis** to produce reproducible results.

## Data Source
- IMPC public portal (https://www.mousephenotype.org/)
- Gene-level phenotype data (MP ontology)
- Associated images (histology, lacZ, X-ray)

## Methods
1. **IMPC data extraction**: Python scripts query the REST/Solr API to retrieve gene-phenotype records and image metadata.
2. **Image analysis**: ImageJ/Fiji macros quantify features in microscopy images (cell counts, morphology) from IMPC or sample datasets.
3. **Python orchestration**: Automates macro execution, collects results, and generates summary statistics.

## Limitations
- No animal handling performed.
- Analysis is based on publicly available images and metadata.
- Results are exploratory; no causal claims are made.

## Folder Structure
- `data/`: raw and processed data
- `notebooks/`: Jupyter notebooks for exploration
- `scripts/`: Python scripts for queries and automation
- `imagej_macros/`: reproducible ImageJ macros
- `results/`: tables and figures
# impc-phenotype-image-analysis
