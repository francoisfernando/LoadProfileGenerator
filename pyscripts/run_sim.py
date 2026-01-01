#!/usr/bin/env python3
from pylpg import lpg_execution, lpgdata

# Simulate the predefined household CHR01 (couple, both employed) for the year 2022
data = lpg_execution.execute_lpg_single_household(
    2023,
    lpgdata.Households.CHR05_Family_3_children_both_with_work,
    lpgdata.HouseTypes.HT20_Single_Family_House_no_heating_cooling,
    startdate="2023-01-01",
    enddate="2023-12-31",
    random_seed=3442,
    resolution="00:30:00",
)

# Extract the generated electricity load profile
electricity_profile = data["Electricity_HH1"]
print(electricity_profile)

# Resample to 15 minute resolution
profile_df = electricity_profile.resample("30min").sum().to_frame()
# profile_df = electricity_profile.to_frame()
print(profile_df)

profile_df.to_csv('/input/load_profile.csv', index_label="start_timestamp")