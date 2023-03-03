import pandas as pd
import numpy as np
import euclidean_d

'primary demographics sheet'
p_demo = pd.read_csv('/Users/davidcui02/Downloads/CDP_primary_demographics_v1.csv')

'profile relationships sheet'
p_relationships = pd.read_csv('/Users/davidcui02/Downloads/CDP_profile_relationships.csv')
'print(p_relationships)'

"""
'problem 1: When trying to build out our target market (i.e. collection of consumer profiles), ' 
    'I have a population size in mind that I want to reach and a specific profile that ' 
    'I believe suits the market best. I want to know which profiles I should add to my target market ' 
    'to reach the population I want to market to. (i.e. find the profiles that are most similar to the ' 
    'target profile until I reach the population I’m after)'
'Input Example: cdp_profile_id = ‘101756’ & population_size = 1,500,000'
'Output Example: A list of the CDP_Profiles that are the most closely related to 101756 ' 
    'which will bring the total population of the target market up to 1.5M'
"""

"""
General idea: greedy algorithm
    - Take input id and calculate Euclidean distance between it and all the other profiles
    - smaller the distance = more similar 
    - sort the profiles by shortest to longest distance to the input id profile
    - add the profiles with the shortest distance to the output list until the target population is reached

How to calculate Euclidean distance between profiles? 
    - use e_distance from p_relationships csv?
    - turn the attributes into some numerical version (get_dummies?)
    - how to weigh these attributes?  
Use group_population_est to fill up population?
"""


# takes in list of target IDs, desired population, and a dataframe
def building_market(target_id, population, dataframe):
    # output list of profiles
    target_profiles = []
    CDP_profile_relationships = euclidean_d.create_euclidean_distance_table(dataframe)
    # filter the CDP_profile_relationships dataframe so that it only contains rows that contain the target IDs
    filtered_df = CDP_profile_relationships.loc[(CDP_profile_relationships['ID_1'].isin(target_id))
                                                | (CDP_profile_relationships['ID_2'].isin(target_id))]
    # sort the rows by smallest to largest e_distance
    sorted_df = filtered_df.sort_values(by='e_distance')
    # subtract the initial population of the target IDs from the population
    population = population - dataframe.loc[dataframe['id'].isin(target_id), 'group_population_est'].sum()
    # iterate through the sorted dataframe and add profiles to the target list
    for index, row in sorted_df.iterrows():
        # grab the correct ID (meaning the one that isn't in the target_ids list)
        if row['ID_1'] in target_id:
            profile_id = row['ID_2']
        else:
            profile_id = row['ID_1']
        # grab the population estimate from the cdp profiles
        population_est_total = dataframe.loc[dataframe['id'] == profile_id, 'group_population_est'].values[0]
        # if the population is negative then end the for loop
        # if not,
        # check if population has been exceeded, if not add the target profile into the output list
        # and subtract the current profile's estimated group population from the population
        if population <= 0:
            break
        else:
            target_profiles.append(profile_id)
            population -= population_est_total
    return target_profiles


"""
When trying to expand our target market, I have a list of profiles that are currently included in our market 
    (sometimes expressed in aggregate) - I want to find the profiles that are 
    most similar to my target market but not presently included that will add x number of consumers to my market.
Input Example: Age 25-44, No kids, urban or suburban, income below $200k - increase population by 100k
Output Example: What is the population of the given attributes as well as a list of 
    the CDP_Profiles that are the most closely related to aggregated 
    profile description that will raise of total population by 100k
"""

"""
General Idea:
    - turn input into a profile
    - What is the population of the given attributes: 
        find number of profiles that match the attributes in the input profile (add up group_population_est)
        - i.e. there are 50 profile groups that are between age 25-44 or x amount of people from gen pop that fit
            - this attribute 
    - use algorithm in problem 1 to find list of profiles that are most similar to target market 
"""


# helper functions that creates rows that will be added to a dataframe
def create_rows(dataframe, age_range, household_makeup, kids_under_2, kids_3_5,
                kids_6_9, kids_10_14, kids_15_17, income_range, location_density):
    for age in age_range:
        # create rows for each age range
        for income in income_range:
            # create rows for each income range
            new_row = pd.DataFrame({'id': [dataframe['id'].max() + 1],
                                    'age': [age],
                                    'household_makeup': [household_makeup],
                                    'children_ages_2_or_younger': [kids_under_2],
                                    'children_ages_3_5': [kids_3_5],
                                    'children_ages_6_9': [kids_6_9],
                                    'children_ages_10_14': [kids_10_14],
                                    'children_ages_15_17': [kids_15_17],
                                    'annual_household_income': [income],
                                    'location_density': [location_density],
                                    'population_perc': [0],
                                    'group_population_est': [0]})
            dataframe = pd.concat([dataframe, new_row], ignore_index=True)
    return dataframe


# question: what if household has multiple children? are children even account for in this

# explanations of variables:
# int: age_range_minimum: minimum age of desired target market
# int: age_range_maximum: maximum age of desired target market
# only 4 ranges for age in our dataset (20-24, 25-34, 35-44, 45-54)
# string: makeup_of_household: (3 options) "self" "With other adults only" or "With children"
# int: density_of_location: (3 options) "urban" "suburb" or "rural"
# int: income_min: minimum income of desired target market
# int: income_max: maximum income of desired target market
# only 3 ranges for income in our dataset (70k-99k, 100k-199k, 200k+)
# string: has_kids_under_2, has_kids_3_5, has_kids_6_9, has_kids_10_14, has_kids_15_17 either going to be 'n' or 'y'
# to stay consistent with the csv
def expand_market(age_range_minimum, age_range_maximum, makeup_of_household, has_kids_under_2, has_kids_3_5,
                  has_kids_6_9, has_kids_10_14, has_kids_15_17, density_of_location, income_min,
                  income_max, population_increase):
    # checking that each input is correct
    # Validate age_range_minimum
    if not isinstance(age_range_minimum, int):
        return "age_range_minimum should be an integer"
    if age_range_minimum < 20 or age_range_minimum > 54:
        return "age_range_minimum should be between 20 and 54"

    # Validate age_range_maximum
    if not isinstance(age_range_maximum, int):
        return "age_range_maximum should be an integer"
    if age_range_maximum < 20 or age_range_maximum > 54:
        return "age_range_maximum should be between 20 and 54"

    # Validate makeup_of_household
    valid_makeup_of_household_input = ["self", "With other adults only", "With children"]
    if makeup_of_household not in valid_makeup_of_household_input:
        return "makeup_of_household should be one of: self, With other adults only, With children"

    # Validate has_kids_under_2, has_kids_3_5, has_kids_6_9, has_kids_10_14, has_kids_15_17
    valid_has_kids_input = ["y", "n"]
    if not all(x in valid_has_kids_input for x in [has_kids_under_2, has_kids_3_5,
                                                   has_kids_6_9, has_kids_10_14, has_kids_15_17]):
        return "has_kids_* variables should be 'y' or 'n'"

    # Validate density_of_location
    valid_density_of_location_input = ["urban", "suburb", "rural"]
    if density_of_location not in valid_density_of_location_input:
        return "density_of_location should be one of: urban, suburb, rural"

    # Validate income_min
    if not isinstance(income_min, int):
        return "income_min should be an integer"

    # Validate income_max
    if not isinstance(income_max, int):
        return "income_max should be an integer"

    # Validate population_increase
    if not isinstance(population_increase, int):
        return "population_increase should be an integer"

    # first filter out rows in p_demo that aren't in the desired household_makeup
    # then filter out rows in p_demo that aren't in the desired location_density
    filtered_df = p_demo.loc[(p_demo['household_makeup'] == makeup_of_household) &
                             (p_demo['location_density'] == density_of_location) &
                             (p_demo['children_ages_2_or_younger'] == has_kids_under_2) &
                             (p_demo['children_ages_3_5'] == has_kids_3_5) &
                             (p_demo['children_ages_6_9'] == has_kids_6_9) &
                             (p_demo['children_ages_10_14'] == has_kids_10_14) &
                             (p_demo['children_ages_15_17'] == has_kids_15_17)]

    # create boolean to helps determine where the age range is
    # min_age_range_20_24 = (age_range_minimum >= '20')
    min_age_range_25_34 = (age_range_minimum >= 25)
    min_age_range_35_44 = (age_range_minimum >= 35)
    min_age_range_45_54 = (age_range_minimum >= 45)

    max_age_range_20_24 = (age_range_maximum <= 24)
    max_age_range_25_34 = (age_range_maximum <= 34)
    max_age_range_35_44 = (age_range_maximum <= 44)
    # max_age_range_45_54 = (age_range_maximum <= '54')

    # if the minimum age range is greater than 45 then it can't be in any of other 3 age ranges so filter those out
    if min_age_range_45_54:
        filtered_df = p_demo.loc[p_demo['age'] == '45-54']
    # if above isn't true then check if min age is above 35, if it is then filter those not in top 2 age ranges
    elif min_age_range_35_44:
        filtered_df = p_demo.loc[(p_demo['age'] == '35-44') & (p_demo['age'] == '45-54')]
    # if above two conditions aren't true then check if min age is above 25, if it is then filter out
    # those in 20-24 age range
    elif min_age_range_25_34:
        filtered_df = p_demo.loc[p_demo['age'] != '20-24']

    # now basically repeat above but with the maximum age now
    # if the maximum age range is less than 24, then it can't be any of other 3 higher age ranges so filter those out
    if max_age_range_20_24:
        filtered_df = p_demo.loc[p_demo['age'] == '20-24']
    # if above isn't true then check if max age is below 34, if it is then filter those not in bottom 2 age ranges
    elif max_age_range_25_34:
        filtered_df = p_demo.loc[(p_demo['age'] == '20-24') & (p_demo['age'] == '25-34')]
    # if above two conditions aren't true then check if max age is below 44, if it is then filter out
    # those in 45-54 age range
    elif max_age_range_35_44:
        filtered_df = p_demo.loc[p_demo['age'] != '45-54']

    # create booleans to help determine what the income range is
    # min_income_70k_99k = (income_min >= 70000)
    min_income_100k_199k = (income_min >= 100000)
    min_income_200k = (income_min >= 200000)

    max_income_100k_199k = (income_max <= 199000)
    max_income_70k_99k = (income_max <= 99000)

    # if the minimum income is above 200k then filter those out that make less
    if min_income_200k:
        filtered_df = p_demo.loc[p_demo['annual_household_income'] == '$200,000+']
    # if above isn't true then check if the minimum income is above 100k,
    # it is then filter out those that make 70k to 90k
    elif min_income_100k_199k:
        filtered_df = p_demo.loc[p_demo['annual_household_income'] != '$70,000 - $99,000']

    # do the same as above but with maximum income now
    # if the maximum income is below 99k then filter those out that make more
    if max_income_70k_99k:
        filtered_df = p_demo.loc[p_demo['annual_household_income'] == '$70,000 - $99,000']
    # if above isn't true then check if the maximum income is below 199k, if it is then filter
    # those out that make more than 200k
    elif max_income_100k_199k:
        filtered_df = p_demo.loc[p_demo['annual_household_income'] != '$200,000+']

    # after filtering the data set, gets the sum of the group_population_est
    # represents the population of the given attributes
    market_population = filtered_df['group_population_est'].sum()

    # specify the age range bins
    # (20-24, 25-34, 35-44, 45-54)
    # the first interval is [20,25), which includes ages from 20 to 24 (inclusive of 20, but exclusive of 25).
    # the second interval is [25,35), which includes ages from 25 to 34 (inclusive of 25, but exclusive of 35).
    # the third interval is [35,45), which includes ages from 35 to 44 (inclusive of 35, but exclusive of 45).
    # the fourth interval is [45,55), which includes ages from 45 to 54 (inclusive of 45, but exclusive of 55).
    bins = [20, 25, 35, 45, 55]
    labels = ['20-24', '25-34', '35-44', '45-54']

    # create a categorical variable for the input age range using pd.cut()
    age_range = pd.cut([age_range_minimum, age_range_maximum], bins=bins, labels=labels)

    # convert the categorical variable to a list of age ranges
    age_range = age_range.dropna().unique().tolist()

    # define the income ranges
    ranges = [pd.Interval(left=70000, right=99000),
              pd.Interval(left=100000, right=199000),
              pd.Interval(left=200000, right=float('inf'))]

    # create a boolean mask to determine which ranges the input income falls into
    mask = pd.Series(False, index=range(len(ranges)))
    for r in ranges:
        if income_max >= r.left and income_min <= r.right:
            mask[ranges.index(r)] = True

    # determine the income ranges that the input income falls into
    income_range = []
    for i in range(len(ranges)):
        if mask[i]:
            income_range.append('$' + str(int(ranges[i].left)) + ' - $' + (
                'inf' if pd.isna(ranges[i].right) else str(int(ranges[i].right))))

    # create new rows based on the input criteria
    new_rows = create_rows(p_demo, age_range, makeup_of_household, has_kids_under_2, has_kids_3_5,
                           has_kids_6_9, has_kids_10_14, has_kids_15_17, income_range, density_of_location)

    # convert the new_rows dictionary to a dataframe
    new_df = pd.DataFrame.from_dict(new_rows)

    # concatenate the new dataframe with the existing p_demo dataframe
    new_p_demo = pd.concat([p_demo, new_df], ignore_index=True)

    # creates list of IDs of only the profiles of the aggregate marget that were added to p_demo
    # id_list = new_p_demo.loc[new_p_demo['id'] >= [p_demo['id'].max() + 1], 'id'].tolist()
    added_ids = new_p_demo.iloc[len(p_demo):]['id'].tolist()

    # use building market function to get list of a list of
    # the CDP_Profiles that are the most closely related to aggregated
    # profile description that will raise of total population by the intended amount
    output_list = building_market(added_ids, population_increase, new_p_demo)

    # market_population is the group_population_est of those that meet the aggregate profile
    # output_list is a list of CDP_profiles
    return market_population, output_list
