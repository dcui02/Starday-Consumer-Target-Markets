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
def create_rows(dataframe, age_range, household_makeup, income_range, location_density):
    for age in age_range:
        # create rows for each age range
        for income in income_range:
            # create rows for each income range
            new_row = pd.DataFrame({'id': [dataframe['id'].max() + 1],
                                    'age': [age],
                                    'household_makeup': [household_makeup],
                                    'children_ages_2_or_younger': ['n'],
                                    'children_ages_3_5': ['n'],
                                    'children_ages_6_9': ['n'],
                                    'children_ages_10_14': ['n'],
                                    'children_ages_15_17': ['n'],
                                    'annual_household_income': [income],
                                    'location_density': [location_density],
                                    'population_perc': [0],
                                    'group_population_est': [0]})
            dataframe = pd.concat([dataframe, new_row], ignore_index=True)
    return dataframe


# question: what if household has multiple children? are children even account for in this

# explanations of variables:
# age_range_minimum: minimum age of desired target market
# age_range_maximum: maximum age of desired target market
# only 4 ranges for age in our dataset (20-24, 25-34, 35-44, 45-54)
# makeup_of_household: (3 options) "self" "With other adults only" or "With children"
# density_of_location: (3 options) "urban" "suburb" or "rural"
# income_min: minimum income of desired target market
# income_max: maximum income of desired target market
# only 3 ranges for income in our dataset (70k-99k, 100k-199k, 200k+)
def expand_market(age_range_minimum, age_range_maximum, makeup_of_household, density_of_location, income_min,
                  income_max, population_increase):
    # first filter out rows in p_demo that aren't in the desired household_makeup
    # then filter out rows in p_demo that aren't in the desired location_density
    filtered_df = p_demo.loc[(p_demo['household_makeup'] == makeup_of_household) &
                             (p_demo['location_density'] == density_of_location)]

    # create boolean to helps determine where the age range is
    # min_age_range_20_24 = (age_range_minimum >= '20')
    min_age_range_25_34 = (age_range_minimum >= '25')
    min_age_range_35_44 = (age_range_minimum >= '35')
    min_age_range_45_54 = (age_range_minimum >= '45')

    max_age_range_20_24 = (age_range_maximum <= '24')
    max_age_range_25_34 = (age_range_maximum <= '34')
    max_age_range_35_44 = (age_range_maximum <= '44')
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

    # defining the criteria for the new rows of the aggregate profile descriptions
    household_makeup = makeup_of_household
    location_density = density_of_location

    # boolean variables and determine if an age group is apart of the input
    """
    in_20_24_group
    in_25_34_group
    in_35_44_group
    in_45_54_group
    """
    # determine the specific desired age ranges
    # if max age of input is less than 24 then it is apart of 20-24 age group
    # if min age of input is greater than 20 then it is apart of 20-24 age group
    if age_range_maximum <= 24 | age_range_minimum >= 20:
        in_20_24_group = True
    else:
        in_20_24_group = False
    # if max age of input is less than 34 then it is apart of the 25-34 age group
    # if min age of input is greater than 25 then it is apart of the 25-34 age group
    if age_range_maximum <= 34 | age_range_minimum >= 25:
        in_25_34_group = True
    else:
        in_25_34_group = False
    # if max age of input is less than 44 then it is apart of the 35-44 age group
    # if min age of input is greater than 35 then it is apart of the 35-44 age group
    if age_range_maximum <= 44 | age_range_minimum >= 35:
        in_35_44_group = True
    else:
        in_35_44_group = False
    # if max age of input is less than 54 then it is apart of the 45-54 age group
    # if min age of input is greater than 45 then it is apart of the 45-54 age group
    if age_range_maximum <= 54 | age_range_minimum >= 45:
        in_45_54_group = True
    else:
        in_45_54_group = False

    # determine which age ranges are apart of the desired group
    if in_20_24_group & in_25_34_group & in_35_44_group & in_45_54_group:
        age_range = ['20-24', '25-34', '35-44', '45-54']
    elif in_20_24_group & in_25_34_group & in_35_44_group:
        age_range = ['20-24', '25-34', '35-44']
    elif in_25_34_group & in_35_44_group & in_45_54_group:
        age_range = ['25-34', '35-44', '45-54']
    elif in_20_24_group & in_25_34_group:
        age_range = ['20-24', '25-34']
    elif in_25_34_group & in_35_44_group:
        age_range = ['25-34', '35-44']
    elif in_35_44_group & in_45_54_group:
        age_range = ['35-44', '45-54']
    elif in_20_24_group:
        age_range = ['20-24']
    elif in_25_34_group:
        age_range = ['25-34']
    elif in_35_44_group:
        age_range = ['35-44']
    elif in_45_54_group:
        age_range = ['45-54']

    # boolean variables to determine if income range is apart of the input
    """
    makes_between_70k_99k
    makes_between_100k_199k
    makes_more_200k
    """
    # determine the specific desired income ranges
    # if max income of input is less than 99000 then it is apart of the 70k-99k group
    # if min income of input is greater than 70000 then it is apart of the 70k-99k group
    if income_max <= 99000 | income_min >= 70000:
        makes_between_70k_99k = True
    else:
        makes_between_70k_99k = False
    # if max income of input is less than 199000 then it is apart of the 100k-199k group
    # if min income of input is greater than 100000 then it is apart of the 100k-199k group
    if income_max <= 199000 | income_min >= 100000:
        makes_between_100k_199k = True
    else:
        makes_between_100k_199k = False
    # if min income of input is greater than 200000 then it is apart of the 200k+ group
    if income_min >= 200000:
        makes_more_200k = True
    else:
        makes_more_200k = False

    # determine which income ranges are apart of the desired group
    if makes_between_70k_99k & makes_between_100k_199k & makes_more_200k:
        income_range = ['$70,000 - $99,000', '$100,000 - $199,000', '$200,000+']
    elif makes_between_70k_99k & makes_between_100k_199k:
        income_range = ['$70,000 - $99,000', '$100,000 - $199,000']
    elif makes_between_100k_199k & makes_more_200k:
        income_range = ['$100,000 - $199,000', '$200,000+']
    elif makes_between_70k_99k:
        income_range = ['$70,000 - $99,000']
    elif makes_between_100k_199k:
        income_range = ['$100,000 - $199,000']
    elif makes_more_200k:
        income_range = ['$200,000+']

    # create new rows based on the input criteria
    new_rows = create_rows(p_demo, age_range, household_makeup, income_range, location_density)

    # convert the new_rows dictionary to a dataframe
    new_df = pd.DataFrame.from_dict(new_rows)

    # concatenate the new dataframe with the existing p_demo dataframe
    new_p_demo = pd.concat([p_demo, new_df], ignore_index=True)

    # creates list of IDs of only the profiles of the aggregate marget that were added to p_demo
    id_list = new_p_demo.loc[new_p_demo['id'] >= [p_demo['id'].max() + 1], 'id'].tolist()

    # use building market function to get list of a list of
    # the CDP_Profiles that are the most closely related to aggregated
    # profile description that will raise of total population by the intended amount
    output_list = building_market(id_list, population_increase, new_p_demo)

    # market_population is the group_population_est of those that meet the aggregate profile
    # output_list is a list of CDP_profiles
    return market_population, output_list


