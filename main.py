import pandas as pd
import numpy as np
from euclidean_d import CDP_profile_relationships

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


def building_market(target_id, population):
    target_profiles = []
    filtered_df = CDP_profile_relationships.loc[(CDP_profile_relationships['ID_1'] == target_id)
                                                | (CDP_profile_relationships['ID_2'] == target_id)]
    sorted_df = filtered_df.sort_values(by='e_distance')

    # iterate through the sorted dataframe and add profiles to the target list
    for index, row in sorted_df.iterrows():
        profile_id = row['ID_1'] if row['ID_2'] == target_id else row['ID_2']
        population_est_total = p_demo.loc[p_demo['id'] == profile_id, 'group_population_est'].values[0]

        # check if adding this profile's group_population_est will exceed the population limit
        if population_est_total <= population:
            target_profiles.append(profile_id)
            population -= population_est_total

        # if adding this profile's population_est_total will exceed the population limit, break the loop
        if population <= 0:
            break

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

# should return list with profiles 100001 and 100002
print(building_market(100000, 286000))
