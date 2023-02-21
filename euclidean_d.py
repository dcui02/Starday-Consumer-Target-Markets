# Start with a df of the primary attributes of the CDP binary profiles
# which are listed below (note that some might be spelled differently in the code below):
# age_20_24
# age_25_34
# age_35_44
# age_45_54
# children_ages_2_or_younger
# children_ages_3_5
# children_ages_6_9
# children_ages_10_14
# children_ages_15_17
# household_makeup_self
# household_makeup_with_other_adults_only
# household_makeup_with_children
# annual_household_income_70k_99k
# annual_household_income_100k_199k
# annual_household_income_200k
# location_density_urban
# location_density_suburb
# location_density_rural

# you'll use the imput from the formula to recreate a consumer
# profile and then you can compare that new profile to the CDP_binary_df dataframe
# with the euclidean distance function. Code for this is at the bottom - it will have to be updated.
import pandas as pd
import numpy as np

'main primary demographics sheet'
p_demo = pd.read_csv('/Users/davidcui02/Downloads/CDP_primary_demographics_v1.csv')

## first create this binary sheet
# create a new DataFrame with only the required columns

CDP_binary_df = p_demo[['id', 'age', 'children_ages_2_or_younger',
                        'children_ages_3_5', 'children_ages_6_9', 'children_ages_10_14',
                        'children_ages_15_17', 'household_makeup',
                        'annual_household_income',
                        'location_density']]
# create a new column for each age group and set the values to 1 if the age is in that group, else 0
CDP_binary_df['age_20-24'] = np.where(CDP_binary_df['age'] == '20-24', 1, 0)
CDP_binary_df['age_25-34'] = np.where(CDP_binary_df['age'] == '25-34', 1, 0)
CDP_binary_df['age_35-44'] = np.where(CDP_binary_df['age'] == '35-44', 1, 0)
CDP_binary_df['age_45-54'] = np.where(CDP_binary_df['age'] == '45-54', 1, 0)

# drop the original 'age' column
CDP_binary_df.drop('age', axis=1, inplace=True)

# set the values in the columns for children ages to 1 if there are children in that age group, else 0
CDP_binary_df['children_ages_2-or-younger'] = np.where(CDP_binary_df['children_ages_2_or_younger'] == 'y', 1, 0)
CDP_binary_df['children_ages_3-5'] = np.where(CDP_binary_df['children_ages_3_5'] == 'y', 1, 0)
CDP_binary_df['children_ages_6-9'] = np.where(CDP_binary_df['children_ages_6_9'] == 'y', 1, 0)
CDP_binary_df['children_ages_10-14'] = np.where(CDP_binary_df['children_ages_10_14'] == 'y', 1, 0)
CDP_binary_df['children_ages_15-17'] = np.where(CDP_binary_df['children_ages_15_17'] == 'y', 1, 0)

# drop the original children columns
CDP_binary_df.drop('children_ages_2_or_younger', axis=1, inplace=True)
CDP_binary_df.drop('children_ages_3_5', axis=1, inplace=True)
CDP_binary_df.drop('children_ages_6_9', axis=1, inplace=True)
CDP_binary_df.drop('children_ages_10_14', axis=1, inplace=True)
CDP_binary_df.drop('children_ages_15_17', axis=1, inplace=True)

# set the values in the columns for household makeup
CDP_binary_df['household_makeup_self'] = np.where(CDP_binary_df['household_makeup'] == 'self', 1, 0)
CDP_binary_df['household_makeup_With other adults only'] = np.where(CDP_binary_df['household_makeup'] ==
                                                                    'With other adults only', 1, 0)
CDP_binary_df['household_makeup_With children'] = np.where(CDP_binary_df['household_makeup'] == 'With children', 1, 0)

# drop the original 'household_makeup' column
CDP_binary_df.drop('household_makeup', axis=1, inplace=True)

# set the values in the columns for annual income
CDP_binary_df['annual_household_income_$70,000 - $99,000'] = np.where(CDP_binary_df['annual_household_income'] ==
                                                            '$70,000 - $99,000-24', 1, 0)
CDP_binary_df['annual_household_income_$100,000 - $199,000'] = np.where(CDP_binary_df['annual_household_income'] ==
                                                              '$100,000 - $199,000-34', 1, 0)
CDP_binary_df['annual_household_income_$200,000+'] = np.where(CDP_binary_df['annual_household_income'] == '$200,000+', 1, 0)

# drop the original 'annual_household_income' column
CDP_binary_df.drop('annual_household_income', axis=1, inplace=True)

# set the values in the columns for location density
CDP_binary_df['location_density_urban'] = np.where(CDP_binary_df['location_density'] == 'urban', 1, 0)
CDP_binary_df['location_density_suburb'] = np.where(CDP_binary_df['location_density'] == 'suburban', 1, 0)
CDP_binary_df['location_density_rural'] = np.where(CDP_binary_df['location_density'] == 'rural', 1, 0)

# drop the original 'location_density' column
CDP_binary_df.drop('location_density', axis=1, inplace=True)

CDP_binary_df

# create group breakdowns
# under 35
CDP_binary_df['u35'] = np.where((CDP_binary_df['age_20-24'] == 1) |
                                (CDP_binary_df['age_25-34'] == 1)
                                , 1, 0)
# under 45
CDP_binary_df['u45'] = np.where((CDP_binary_df['age_20-24'] == 1) |
                                (CDP_binary_df['age_25-34'] == 1) |
                                (CDP_binary_df['age_35-44'] == 1)
                                , 1, 0)
# over 24
CDP_binary_df['o24'] = np.where((CDP_binary_df['age_25-34'] == 1) |
                                (CDP_binary_df['age_35-44'] == 1) |
                                (CDP_binary_df['age_45-54'] == 1)
                                , 1, 0)
# over 34
CDP_binary_df['o34'] = np.where((CDP_binary_df['age_35-44'] == 1) |
                                (CDP_binary_df['age_45-54'] == 1)
                                , 1, 0)
# under 35, lives w/ self
CDP_binary_df['u35_LWS'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                     (CDP_binary_df['age_25-34'] == 1)) &
                                    (CDP_binary_df['household_makeup_self'] == 1)
                                    , 1, 0)
# under 45, lives w/ self
CDP_binary_df['u45_LWS'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                     (CDP_binary_df['age_25-34'] == 1) |
                                     (CDP_binary_df['age_35-44'] == 1)) &
                                    (CDP_binary_df['household_makeup_self'] == 1)
                                    , 1, 0)
# over 24, lives w/ self
CDP_binary_df['o24_LWS'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                     (CDP_binary_df['age_35-44'] == 1) |
                                     (CDP_binary_df['age_45-54'] == 1)) &
                                    (CDP_binary_df['household_makeup_self'] == 1)
                                    , 1, 0)
# over 34, lives w/ self
CDP_binary_df['o34_LWS'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                     (CDP_binary_df['age_45-54'] == 1)) &
                                    (CDP_binary_df['household_makeup_self'] == 1)
                                    , 1, 0)
# under 35, lives w/ adults only
CDP_binary_df['u35_LWA'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                     (CDP_binary_df['age_25-34'] == 1)) &
                                    (CDP_binary_df['household_makeup_With other adults only'] == 1)
                                    , 1, 0)
# under 45, lives w/ adults only
CDP_binary_df['u45_LWA'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                     (CDP_binary_df['age_25-34'] == 1) |
                                     (CDP_binary_df['age_35-44'] == 1)) &
                                    (CDP_binary_df['household_makeup_With other adults only'] == 1)
                                    , 1, 0)
# over 24, lives w/ adults only
CDP_binary_df['o24_LWA'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                     (CDP_binary_df['age_35-44'] == 1) |
                                     (CDP_binary_df['age_45-54'] == 1)) &
                                    (CDP_binary_df['household_makeup_With other adults only'] == 1)
                                    , 1, 0)
# over 34, lives w/ adults only
CDP_binary_df['o34_LWA'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                     (CDP_binary_df['age_45-54'] == 1)) &
                                    (CDP_binary_df['household_makeup_With other adults only'] == 1)
                                    , 1, 0)
# under 35, lives w/ kids
CDP_binary_df['u35_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                     (CDP_binary_df['age_25-34'] == 1)) &
                                    (CDP_binary_df['household_makeup_With children'] == 1)
                                    , 1, 0)
# under 45, lives w/ kids
CDP_binary_df['u45_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                     (CDP_binary_df['age_25-34'] == 1) |
                                     (CDP_binary_df['age_35-44'] == 1)) &
                                    (CDP_binary_df['household_makeup_With children'] == 1)
                                    , 1, 0)
# over 24, lives w/ kids
CDP_binary_df['o24_LWK'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                     (CDP_binary_df['age_35-44'] == 1) |
                                     (CDP_binary_df['age_45-54'] == 1)) &
                                    (CDP_binary_df['household_makeup_With children'] == 1)
                                    , 1, 0)
# over 34, lives w/ kids
CDP_binary_df['o34_LWK'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                     (CDP_binary_df['age_45-54'] == 1)) &
                                    (CDP_binary_df['household_makeup_With children'] == 1)
                                    , 1, 0)
# kids under 6
CDP_binary_df['ku6'] = np.where((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                (CDP_binary_df['children_ages_3-5'] == 1),
                                1, 0)
# kids under 10
CDP_binary_df['ku10'] = np.where((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                 (CDP_binary_df['children_ages_3-5'] == 1) |
                                 (CDP_binary_df['children_ages_6-9'] == 1),
                                 1, 0)
# kids under 15
CDP_binary_df['ku15'] = np.where((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                 (CDP_binary_df['children_ages_3-5'] == 1) |
                                 (CDP_binary_df['children_ages_6-9'] == 1) |
                                 (CDP_binary_df['children_ages_10-14'] == 1),
                                 1, 0)
# kids over 2
CDP_binary_df['ko2'] = np.where((CDP_binary_df['children_ages_3-5'] == 1) |
                                (CDP_binary_df['children_ages_6-9'] == 1) |
                                (CDP_binary_df['children_ages_10-14'] == 1) |
                                (CDP_binary_df['children_ages_15-17'] == 1),
                                1, 0)
# kids over 5
CDP_binary_df['ko5'] = np.where((CDP_binary_df['children_ages_6-9'] == 1) |
                                (CDP_binary_df['children_ages_10-14'] == 1) |
                                (CDP_binary_df['children_ages_15-17'] == 1),
                                1, 0)
# kids over 9
CDP_binary_df['ko9'] = np.where((CDP_binary_df['children_ages_10-14'] == 1) |
                                (CDP_binary_df['children_ages_15-17'] == 1),
                                1, 0)
# kids single age group
CDP_binary_df['ksingleage'] = np.where(CDP_binary_df['children_ages_2-or-younger'] +
                                       CDP_binary_df['children_ages_3-5'] +
                                       CDP_binary_df['children_ages_6-9'] +
                                       CDP_binary_df['children_ages_10-14'] +
                                       CDP_binary_df['children_ages_15-17'] == 1,
                                       1, 0)
# kids multiple age groups
CDP_binary_df['kmultiage'] = np.where((CDP_binary_df['children_ages_2-or-younger'] +
                                       CDP_binary_df['children_ages_3-5'] +
                                       CDP_binary_df['children_ages_6-9'] +
                                       CDP_binary_df['children_ages_10-14'] +
                                       CDP_binary_df['children_ages_15-17']) >= 2,
                                      1, 0)
# old and young kids
CDP_binary_df['koldandyoungage'] = np.where((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                            (CDP_binary_df['children_ages_3-5'] == 1) &
                                            (CDP_binary_df['children_ages_10-14'] == 1) |
                                            (CDP_binary_df['children_ages_15-17'] == 1),
                                            1, 0)
# at least 2 young kids
CDP_binary_df['2yk'] = np.where(CDP_binary_df['children_ages_2-or-younger'] +
                                CDP_binary_df['children_ages_3-5'] +
                                CDP_binary_df['children_ages_6-9'] >= 2,
                                1, 0)
# at least 2 old kids
CDP_binary_df['2ok'] = np.where(CDP_binary_df['children_ages_6-9'] +
                                CDP_binary_df['children_ages_10-14'] +
                                CDP_binary_df['children_ages_15-17'] >= 2,
                                1, 0)
# under 35, high income
CDP_binary_df['u35_HI'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                    (CDP_binary_df['age_25-34'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$200,000+'] == 1)
                                   , 1, 0)
# under 45, high income
CDP_binary_df['u45_HI'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                    (CDP_binary_df['age_25-34'] == 1) |
                                    (CDP_binary_df['age_35-44'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$200,000+'] == 1)
                                   , 1, 0)
# over 24, high income
CDP_binary_df['o24_HI'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                    (CDP_binary_df['age_35-44'] == 1) |
                                    (CDP_binary_df['age_45-54'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$200,000+'] == 1)
                                   , 1, 0)
# over 34, high income
CDP_binary_df['o34_HI'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                    (CDP_binary_df['age_45-54'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$200,000+'] == 1)
                                   , 1, 0)
# under 35, med income
CDP_binary_df['u35_MI'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                    (CDP_binary_df['age_25-34'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1)
                                   , 1, 0)
# under 45, med income
CDP_binary_df['u45_MI'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                    (CDP_binary_df['age_25-34'] == 1) |
                                    (CDP_binary_df['age_35-44'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1)
                                   , 1, 0)
# over 24, med income
CDP_binary_df['o24_MI'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                    (CDP_binary_df['age_35-44'] == 1) |
                                    (CDP_binary_df['age_45-54'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1)
                                   , 1, 0)
# over 34, med income
CDP_binary_df['o34_MI'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                    (CDP_binary_df['age_45-54'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1)
                                   , 1, 0)
# under 35, low income
CDP_binary_df['u35_LI'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                    (CDP_binary_df['age_25-34'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1)
                                   , 1, 0)
# under 45, low income
CDP_binary_df['u45_LI'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                    (CDP_binary_df['age_25-34'] == 1) |
                                    (CDP_binary_df['age_35-44'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1)
                                   , 1, 0)
# over 24, low income
CDP_binary_df['o24_LI'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                    (CDP_binary_df['age_35-44'] == 1) |
                                    (CDP_binary_df['age_45-54'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1)
                                   , 1, 0)
# over 34, low income
CDP_binary_df['o34_LI'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                    (CDP_binary_df['age_45-54'] == 1)) &
                                   (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1)
                                   , 1, 0)
# urban, with kids
CDP_binary_df['urb_LWK'] = np.where((CDP_binary_df['location_density_urban'] == 1) &
                                    (CDP_binary_df['household_makeup_With children'] == 1)
                                    , 1, 0)
# suburb, with kids
CDP_binary_df['suburb_LWK'] = np.where((CDP_binary_df['location_density_suburb'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# rural, with kids
CDP_binary_df['rural_LWK'] = np.where((CDP_binary_df['location_density_rural'] == 1) &
                                      (CDP_binary_df['household_makeup_With children'] == 1)
                                      , 1, 0)
# urban, no kids
CDP_binary_df['urb_nok'] = np.where((CDP_binary_df['location_density_urban'] == 1) &
                                    (CDP_binary_df['household_makeup_With children'] == 0)
                                    , 1, 0)
# suburb, no kids
CDP_binary_df['suburb_nok'] = np.where((CDP_binary_df['location_density_suburb'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# rural, no kids
CDP_binary_df['rural_nok'] = np.where((CDP_binary_df['location_density_rural'] == 1) &
                                      (CDP_binary_df['household_makeup_With children'] == 0)
                                      , 1, 0)
# under 35, high income, with kids
CDP_binary_df['u35_HI_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# under 35, high income, no kids
CDP_binary_df['u35_HI_nok'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# under 45, high income, with kids
CDP_binary_df['u45_HI_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# under 45, high income, no kids
CDP_binary_df['u45_HI_nok'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# over 24, high income, with kids
CDP_binary_df['o24_HI_LWK'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# over 24, high income, no kids
CDP_binary_df['o24_HI_nok'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# over 34, high income, with kids
CDP_binary_df['o34_HI_LWK'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# over 34, high income, no kids
CDP_binary_df['o34_HI_nok'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# under 35, med income, with kids
CDP_binary_df['u35_MI_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# under 35, med income, no kids
CDP_binary_df['u35_MI_nok'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# under 45, med income, with kids
CDP_binary_df['u45_MI_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# under 45, med income, no kids
CDP_binary_df['u45_MI_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# over 24, med income, with kids
CDP_binary_df['o24_MI_LWK'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# over 24, med income, no kids
CDP_binary_df['o24_MI_nok'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# over 34, med income, with kids
CDP_binary_df['o34_MI_LWK'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# over 34, med income, no kids
CDP_binary_df['o34_MI_nok'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# under 35, low income, with kids
CDP_binary_df['u35_LI_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# under 35, low income, no kids
CDP_binary_df['u35_LI_nok'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# under 45, low income, with kids
CDP_binary_df['u45_LI_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# under 45, low income, no kids
CDP_binary_df['u45_LI_LWK'] = np.where(((CDP_binary_df['age_20-24'] == 1) |
                                        (CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# over 24, low income, with kids
CDP_binary_df['o24_LI_LWK'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# over 24, low income, no kids
CDP_binary_df['o24_LI_nok'] = np.where(((CDP_binary_df['age_25-34'] == 1) |
                                        (CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# over 34, low income, with kids
CDP_binary_df['o34_LI_LWK'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 1)
                                       , 1, 0)
# over 34, low income, no kids
CDP_binary_df['o34_LI_nok'] = np.where(((CDP_binary_df['age_35-44'] == 1) |
                                        (CDP_binary_df['age_45-54'] == 1)) &
                                       (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                       (CDP_binary_df['household_makeup_With children'] == 0)
                                       , 1, 0)
# urban, high income
CDP_binary_df['urban_HI'] = np.where((CDP_binary_df['location_density_urban'] == 1) &
                                     (CDP_binary_df['annual_household_income_$200,000+'] == 1)
                                     , 1, 0)
# suburb, high income
CDP_binary_df['suburb_HI'] = np.where((CDP_binary_df['location_density_suburb'] == 1) &
                                      (CDP_binary_df['annual_household_income_$200,000+'] == 1)
                                      , 1, 0)
# rural, high income
CDP_binary_df['rural_HI'] = np.where((CDP_binary_df['location_density_rural'] == 1) &
                                     (CDP_binary_df['annual_household_income_$200,000+'] == 1)
                                     , 1, 0)
# urban, med income
CDP_binary_df['urban_MI'] = np.where((CDP_binary_df['location_density_urban'] == 1) &
                                     (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1)
                                     , 1, 0)
# suburb, med income
CDP_binary_df['suburb_MI'] = np.where((CDP_binary_df['location_density_suburb'] == 1) &
                                      (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1)
                                      , 1, 0)
# rural, med income
CDP_binary_df['rural_MI'] = np.where((CDP_binary_df['location_density_rural'] == 1) &
                                     (CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1)
                                     , 1, 0)
# urban, low income
CDP_binary_df['urban_LI'] = np.where((CDP_binary_df['location_density_urban'] == 1) &
                                     (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1)
                                     , 1, 0)
# suburb, low income
CDP_binary_df['suburb_LI'] = np.where((CDP_binary_df['location_density_suburb'] == 1) &
                                      (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1)
                                      , 1, 0)
# rural, low income
CDP_binary_df['rural_LI'] = np.where((CDP_binary_df['location_density_rural'] == 1) &
                                     (CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1)
                                     , 1, 0)
# urban, young kids
CDP_binary_df['urban_yk'] = np.where((CDP_binary_df['location_density_urban'] == 1) &
                                     ((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                      (CDP_binary_df['children_ages_3-5'] == 1))
                                     , 1, 0)
# suburb, young kids
CDP_binary_df['suburb_yk'] = np.where((CDP_binary_df['location_density_suburb'] == 1) &
                                      ((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                       (CDP_binary_df['children_ages_3-5'] == 1))
                                      , 1, 0)
# rural, young kids
CDP_binary_df['rural_yk'] = np.where((CDP_binary_df['location_density_rural'] == 1) &
                                     ((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                      (CDP_binary_df['children_ages_3-5'] == 1))
                                     , 1, 0)
# urban, tweens
CDP_binary_df['urban_mk'] = np.where((CDP_binary_df['location_density_urban'] == 1) &
                                     ((CDP_binary_df['children_ages_6-9'] == 1) |
                                      (CDP_binary_df['children_ages_10-14'] == 1))
                                     , 1, 0)
# suburb, tweens
CDP_binary_df['suburb_mk'] = np.where((CDP_binary_df['location_density_suburb'] == 1) &
                                      ((CDP_binary_df['children_ages_6-9'] == 1) |
                                       (CDP_binary_df['children_ages_10-14'] == 1))
                                      , 1, 0)
# rural, tweens
CDP_binary_df['rural_mk'] = np.where((CDP_binary_df['location_density_rural'] == 1) &
                                     ((CDP_binary_df['children_ages_6-9'] == 1) |
                                      (CDP_binary_df['children_ages_10-14'] == 1))
                                     , 1, 0)
# urban, old kids
CDP_binary_df['urban_ok'] = np.where((CDP_binary_df['location_density_urban'] == 1) &
                                     (CDP_binary_df['children_ages_15-17'] == 1)
                                     , 1, 0)
# suburb, old kids
CDP_binary_df['suburb_ok'] = np.where((CDP_binary_df['location_density_suburb'] == 1) &
                                      (CDP_binary_df['children_ages_15-17'] == 1)
                                      , 1, 0)
# rural, old kids
CDP_binary_df['rural_ok'] = np.where((CDP_binary_df['location_density_rural'] == 1) &
                                     (CDP_binary_df['children_ages_15-17'] == 1)
                                     , 1, 0)
# high income, young kids
CDP_binary_df['HI_yk'] = np.where((CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                  ((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                   (CDP_binary_df['children_ages_3-5'] == 1))
                                  , 1, 0)
# med income, young kids
CDP_binary_df['MI_yk'] = np.where((CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                  ((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                   (CDP_binary_df['children_ages_3-5'] == 1))
                                  , 1, 0)
# low income, young kids
CDP_binary_df['LI_yk'] = np.where((CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                  ((CDP_binary_df['children_ages_2-or-younger'] == 1) |
                                   (CDP_binary_df['children_ages_3-5'] == 1))
                                  , 1, 0)
# high income, tweens
CDP_binary_df['HI_mk'] = np.where((CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                  ((CDP_binary_df['children_ages_6-9'] == 1) |
                                   (CDP_binary_df['children_ages_10-14'] == 1))
                                  , 1, 0)
# mid income, tweens
CDP_binary_df['MI_mk'] = np.where((CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                  ((CDP_binary_df['children_ages_6-9'] == 1) |
                                   (CDP_binary_df['children_ages_10-14'] == 1))
                                  , 1, 0)
# low income, tweens
CDP_binary_df['LI_mk'] = np.where((CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                  ((CDP_binary_df['children_ages_6-9'] == 1) |
                                   (CDP_binary_df['children_ages_10-14'] == 1))
                                  , 1, 0)
# high income, old kids
CDP_binary_df['HI_ok'] = np.where((CDP_binary_df['annual_household_income_$200,000+'] == 1) &
                                  (CDP_binary_df['children_ages_15-17'] == 1)
                                  , 1, 0)
# mid income, old kids
CDP_binary_df['MI_ok'] = np.where((CDP_binary_df['annual_household_income_$100,000 - $199,000'] == 1) &
                                  (CDP_binary_df['children_ages_15-17'] == 1)
                                  , 1, 0)
# low income, old kids
CDP_binary_df['LI_ok'] = np.where((CDP_binary_df['annual_household_income_$70,000 - $99,000'] == 1) &
                                  (CDP_binary_df['children_ages_15-17'] == 1)
                                  , 1, 0)
# urban or suburn
CDP_binary_df['urban_suburb'] = np.where((CDP_binary_df['location_density_rural'] == 1) |
                                         (CDP_binary_df['location_density_suburb'] == 1)
                                         , 1, 0)
# build Euclidean distance table
# create dataset of profile relationships
from scipy.spatial import distance

# create dictlist
CDP_profile_relationships_dict_list = []

# iterate through each row in the binary table
for idx, row in CDP_binary_df.iterrows():
    # save the ID
    ID_1 = row['id']
    # save the array
    profile_array_1 = row.iloc[1:].to_numpy()
    # iterate through binary table for distance comparison
    for index, relationship_row in CDP_binary_df.iloc[(idx + 1):, :].iterrows():
        # save the ID of the new rows
        ID_2 = relationship_row['id']
        # create second array for comparison
        profile_array_2 = relationship_row.iloc[1:].to_numpy()
        # calculate the euclidean distance between each array
        e_distance = distance.euclidean(profile_array_1, profile_array_2)
        # create dictionary row
        new_row = {"ID_1": ID_1, "ID_2": ID_2, "e_distance": e_distance}
        # save row into dictlist
        CDP_profile_relationships_dict_list.append(new_row.copy())

# create dataframe of results
CDP_profile_relationships = pd.DataFrame(CDP_profile_relationships_dict_list)

# add a percentile column
CDP_profile_relationships['distance_percentile'] = (
            (CDP_profile_relationships.e_distance - CDP_profile_relationships.e_distance.min()) /
            (CDP_profile_relationships.e_distance.max() - CDP_profile_relationships.e_distance.min()))

CDP_profile_relationships
