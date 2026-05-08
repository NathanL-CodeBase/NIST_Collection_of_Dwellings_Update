"""
Purpose: Reads AHS 2021 dwelling characteristic CSVs produced by manufacured_house_us_rep.py
         and prints weighted-average summary tables by housing type (apartment, attached,
         detached, mobile home).
Author: Nathan Lima
Created: 2023-05-03
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd

_config_path = Path(__file__).resolve().parent.parent / "data_config.json"
if not _config_path.exists():
    raise FileNotFoundError(
        f"data_config.json not found at {_config_path}. "
        "Copy data_config.template.json to data_config.json and update the paths."
    )
with open(_config_path) as f:
    _cfg = json.load(f)

DATA_DIR = Path(_cfg["data_dir"])
RESULTS_DIR = Path(_cfg["results_dir"])
OUTPUT_DATA_DIR = RESULTS_DIR / "output_data"

# Enter the number of rows wanted
ap = 6  # number of apartments
at = 6  # number of attached homes
de = 5  # number of detached homes
mh = 1  # number of manufactured homes

apartment = pd.read_csv(OUTPUT_DATA_DIR / "ahs21_apartment_characteristics.csv")
apartment = apartment[apartment['year_built'] == 6].drop(['count', 'running_%'], axis=1)
apartment = apartment.reset_index(drop=True).head(ap)

attached = pd.read_csv(OUTPUT_DATA_DIR / "ahs21_attached_characteristics.csv")
attached = attached[attached['year_built'] == 6].drop(['count', 'running_%'], axis=1)
attached = attached.reset_index(drop=True).head(at)

detached = pd.read_csv(OUTPUT_DATA_DIR / "ahs21_detached_characteristics.csv")
detached = detached[detached['year_built'] == 6].drop(['count', 'running_%'], axis=1)
detached = detached.reset_index(drop=True).head(de)

mobile_home = pd.read_csv(OUTPUT_DATA_DIR / "ahs21_mobile_home_characteristics.csv")
mobile_home = mobile_home[mobile_home['year_built'] == 6].drop(['count', 'running_%'], axis=1)
mobile_home = mobile_home.reset_index(drop=True).head(mh)

print('apartment')
print(apartment.groupby(['UNITSIZE', '#_of_units'])['weight'].sum())
print('attached')
print(attached.groupby('UNITSIZE')['weight'].sum())
print('detached')
print(detached.groupby('UNITSIZE')['weight'].sum())
print('mobile_home')
print(mobile_home.groupby('UNITSIZE')['weight'].sum())
