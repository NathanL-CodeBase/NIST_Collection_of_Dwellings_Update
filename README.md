# A Collection of Dwellings to Represent the U.S. Housing Stock (2024 Update)

Python scripts for processing American Housing Survey (AHS) and Residential Energy Consumption Survey (RECS) data to characterize the U.S. residential dwelling stock.

## Overview

This repository contains analysis scripts developed in support of NIST TN 2329, "A Collection of Dwellings to Represent the U.S. Dwelling Stock: 2024 Update." The scripts process publicly available federal housing survey data (RECS 2020, AHS 2021) to produce weighted distributions of dwelling characteristics used to select representative prototypes for building energy and indoor air quality modeling.

Key capabilities:

- Weighted characteristic distributions from RECS 2020 and AHS 2021 survey data
- Cross-survey comparison (AHS vs. RECS)
- Square-footage-weighted averages
- Dwelling type and characteristic visualizations (Bokeh, matplotlib)
- Manufactured housing and air leakage analysis
- Historical data processing (RECS 1997)

## Disclaimer

Certain commercial equipment, instruments, software, or materials are identified in this repository in order to specify the experimental and analytical procedures adequately. Such identification is not intended to imply recommendation or endorsement of any product or service by NIST, nor is it intended to imply that the materials or equipment identified are necessarily the best available for the purpose.

## Repository Structure

```
NIST_Collection_of_Dwellings_Update/
├── scripts/                          # Analysis and processing scripts
│   ├── ahs21_weighted_average.py         # Weighted averages for AHS 2021 data
│   ├── ahs_recs_data_comparison.py       # AHS and RECS cross-survey comparison
│   ├── characteristic_distribution.py    # Dwelling characteristic distributions
│   ├── collectionofdwelling_piechart.py  # Pie charts of dwelling type data
│   ├── manufacured_house_us_rep.py       # Manufactured housing analysis
│   ├── nist_housing_visualization.py     # Interactive housing data visualization
│   ├── nist_housing_viz_fixed.py         # Updated housing visualization
│   ├── recs20_sqft_weighted_average.py   # RECS 2020 square-footage weighted averages
│   ├── recs_characteristic_distribution.py          # RECS dwelling characteristic distributions
│   ├── recs_characteristic_distribution_test(ahs).py  # RECS vs. AHS validation
│   ├── recs_characteristic_distribution_test(year).py # Year-over-year comparison
│   ├── update_values_recs97.py           # RECS 1997 data processing
│   ├── us_air_leakage_distribution.py    # U.S. air leakage distribution analysis
│   └── wap_calc.py                       # Weatherization Assistance Program calculations
│
├── data/                             # Data directory (not committed; see data_config.json)
│   ├── raw/                          # Immutable source data (RECS, AHS CSV files)
│   ├── processed/                    # Derived data files
│   └── metadata/                     # Data dictionaries and documentation
│
├── results/                          # Analysis outputs (not committed)
│   ├── figures/                      # Generated plots
│   ├── tables/                       # Summary tables
│   └── output_data/                  # Processed output files
│
├── environment.yaml                  # Conda environment specification
├── data_config.json                  # Local data paths (gitignored)
├── data_config.template.json         # Template for data configuration
├── CODEMETA.yaml                     # NIST Software Portal metadata
├── CODEOWNERS                        # Repository ownership
├── LICENSE.md                        # NIST software licensing statement
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone git@github.com:NathanL-CodeBase/NIST_Collection_of_Dwellings_Update.git
cd NIST_Collection_of_Dwellings_Update
```

### 2. Create the Conda Environment

```bash
conda env create -f environment.yaml
conda activate cod
```

### 3. Configure Data Paths

```bash
cp data_config.template.json data_config.json
```

Edit `data_config.json` and set the paths for your machine:

```json
{
  "data_dir": "C:/Users/YourName/path/to/data",
  "results_dir": "C:/Users/YourName/path/to/results"
}
```

`data_config.json` is listed in `.gitignore` and should not be committed. Use `data_config.template.json` as a reference when setting up on a new machine.

## Data Sources

Download the following public datasets and place them under `data/raw/`:

- **RECS 2020**: [EIA Residential Energy Consumption Survey](https://www.eia.gov/consumption/residential/) — `recs2020_public_v2.csv`
- **AHS 2021**: [U.S. Census American Housing Survey](https://www.census.gov/programs-surveys/ahs.html) — `household.csv`

## Usage

Activate the conda environment and run scripts from the repository root:

```bash
conda activate cod

# Dwelling characteristic distributions from RECS 2020
python scripts/characteristic_distribution.py

# Square-footage-weighted averages
python scripts/recs20_sqft_weighted_average.py

# AHS vs. RECS comparison
python scripts/ahs_recs_data_comparison.py
```

## Citation

If you use this code or data in your research, please cite:

Lima, Nathan M. (2024), A Collection of Dwellings to Represent the U.S. Housing Stock (2024 Update) Associated Python Scripts, National Institute of Standards and Technology, https://doi.org/10.18434/mds2-3488

**Related Publication:**

Lima NM, Persily AK, Emmerich SJ (2025) A Collection of Dwellings to Represent the U.S. Dwelling Stock: 2024 Update. (National Institute of Standards and Technology, Gaithersburg, MD), NIST Technical Note (TN) NIST TN 2329. https://doi.org/10.6028/NIST.TN.2329

## Contact

- **PI:** Nathan Lima
- **NIST Organizational Unit:** Engineering Laboratory
- **Division:** Building Energy and Environment Division
- **Group:** Indoor Air Quality and Ventilation Group
- **Email:** nathan.lima@nist.gov

## Acknowledgments

This research was conducted at the National Institute of Standards and Technology (NIST) as part of the [Indoor Air Quality and Ventilation Group](https://www.nist.gov/el/beed/indoor-air-quality-ventilation). Andrew K. Persily and Steven J. Emmerich served as project advisers.

## License

This software was developed by employees of the National Institute of Standards and Technology (NIST), an agency of the Federal Government, and is being made available as a public service. See [LICENSE.md](LICENSE.md) for the full NIST licensing statement.

---

For questions or issues, please open an issue on the GitHub repository or contact the project authors.
