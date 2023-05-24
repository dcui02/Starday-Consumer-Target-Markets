import pandas as pd

responder = {
    'nan': 'respondent_id'
}

customID = {
    'nan': 'custom_data_ID'
}

type_hello_world = {
    'Open-Ended Response': 'hello_world'
}

respondent_age = {
    'Response': 'age'
}

grocery_shopper = {
    'Response': 'primary_grocery_shopper',
    'Other (please specify)': 'other_grocery_shopper'
}

annual_income = {
    'Response': 'household_income'
}

living_location = {
    'Response': 'us_region'
}

gender = {
    'Response': 'gender_identity',
    'Not listed (please specify)': 'gender_other'
}

education = {
    'Response': 'highest_level_eductation'
}

living_location_size = {
    'Response': 'self_reported_location_density'
}

zipcode = {
    'Open-Ended Response': 'zip_code'
}

supplements = {
    'Open-Ended Response': 'open_end_supplements'
}

healthy_food_products = {
    'Open-Ended Response': 'open_end_food_product_for_health'
}

sustainable_foods = {
    'Response': 'attitude_towards_sustainable_foods'
}

home_recipe = {
    'Open-Ended Response': 'open_end_cooked_recipe'
}

restaurant_dish = {
    'Open-Ended Response': 'open_end_new_restaurant_dish'
}

new_snack = {
    'Open-Ended Response': 'open_end_new_snack'
}

money_spent_on_groceries = {
    'Response': 'last_wk_grocery_spend'
}

side_dish = {
    'Open-Ended Response': 'open_end_side_dish'
}

travel_location = {
    'Open-Ended Response': 'traveled_in_past_2_yrs'
}

food_rec_source = {
    'Response': 'last_food_discovery',
    'Other (please specify)': 'open_end_other_food_discovery'
}

social_media = {
    'Response': 'social_media_preference',
    'Other (please specify)': 'other_social_media_pref'
}

plant_based_opinion = {
    'Response': 'attitude_towards_plant_based_products'
}

habeya = {
    'Open-Ended Response': 'habeya_location'
}

good_or_bad_response = {
    'nan': 'result'
}

# household makeup question
household_makeup = {
    'I live by myself': 'live_with_self',
    'I live with a roommate or roommates': 'live_with_roommate',
    'I live with a partner or spouse': 'live_with_partner_or_spouse',
    'I live with children': 'live_with_children',
    'I live with my parents or in-laws': 'live_with_parents_or_inlaws',
    'Other (please specify)': 'live_with_other_family_adults'
}

# age_of_children question
age_of_children = {
    '2 years old or younger': 'children_ages_2_or_younger',
    '3-5': 'children_ages_3_5',
    '6-9': 'children_ages_6_9',
    '10-14': 'children_ages_10_14',
    '15-17': 'children_ages_15_17',
    '18 years old or older': 'children_ages_18_plus',
    'There are no children in my household.': 'no_children'
}

# ethnicity question
ethnicity = {
    'White or Caucasian': 'race_white_caucasian',
    'Black or African American': 'race_black_african_american',
    'American Indigenous or Alaska Native': 'race_american_indigenous_alaskan_native',
    'East Asian': 'race_east_asian',
    'South Asian': 'race_south_asian',
    'Native Hawaiian or Other Pacific Islander': 'race_native_hawaiian_pacific_islander',
    'Latinx': 'race_latinx',
    'Prefer not to disclose': 'race_not_provided',
    'Not listed (please specify)': 'race_other'
}

# relationship status question
relationship_status = {
    'Single': 'relationship_single',
    'Dating/In a relationship': 'relationship_dating',
    'Married': 'relationship_married',
    'Divorced/Separated': 'relationship_divorced_separated',
    'Not listed (please specify)': 'relationship_other'
}

# employment status question
employment_status = {
    'Full-time employed': 'work_full_time',
    'Student': 'work_student',
    'Part-time employed': 'work_part_time',
    'Homemaker': 'work_homemaker',
    'On paid family leave': 'work_paid_family_leave',
    'Taking time off from working': 'work_taking_time_off',
    'Unemployed': 'work_unemployed',
    'Not listed (please specify)': 'other_employment'
}

# health and wellness question
health_and_wellness = {
    'I exercise to feel more energized': 'exercise_energized',
    'I exercise to feel less stress': 'exercise_less_stress',
    'I exercise to decrease risk of illness': 'exercise_decrease_illness',
    'I exercise to decrease risk or heal from an injury': 'exercise_heal_from_injury',
    'I exercise to maintain or increase my strength and/or conditioning': 'exercise_strength_conditioning',
    'I exercise to maintain or increase my flexibility and/or mobility': 'exercise_increase_flexibility_mobility',
    'I exercise to maintain or increase my muscle mass': 'exercise_increase_muscle',
    'I exercise to lose weight': 'exercise_lose_weight',
    'I exercise to train for something specific': 'exercise_training',
    'I don’t exercise': 'exercise_none',
    'Not listed (please specify)': 'exercise_other'
}

# health concerns question
health_concerns = {
    'Gut/microbiome health': 'health_concern_gut_microbiome',
    'Brain/cognitive performance (focus, energy, mood)': 'health_concern_brain_cognitive',
    'Stress management/relief': 'health_concern_stress_mgmt',
    'Sleep management': 'health_concern_sleep_mgmt',
    'Skin health': 'health_concern_skin',
    'Hormonal health': 'health_concern_hormonal',
    'Sexual wellness': 'health_concern_sexual_wellness',
    'Cardiovascular health': 'health_concern_cardiovascular',
    'Immunity': 'health_concern_immunity',
    'Bone/joint health': 'health_concern_bone_joint',
    'Oral/dental health': 'health_concern_oral_dental',
    'Ocular/vision health': 'health_concern_ocular_vision',
    'Hair/scalp health': 'health_concern_hair_scalp',
    'Muscle health/maintenance': 'health_concern_muscle_maintenance',
    'Weight management': 'health_concern_weight_mgmt',
    'I don’t consider any health concerns or priorities when grocery shopping.': 'health_concern_none',
    'Other (please specify)': 'health_concern_other'
}

# diet question
diet_restrictions = {
    'Vegan': 'diet_vegan',
    'Plant-based': 'diet_plant_based',
    'Vegetarian': 'diet_vegetarian',
    'Pescatarian': 'diet_pescatarian',
    'Ketogenic Diet': 'diet_keto',
    'Low Carb': 'diet_low_carb',
    'Low Fat': 'diet_low_fat',
    'High Protein': 'diet_high_protein',
    'Low/No Sugar': 'diet_low_no_sugar',
    'Low FODMAP': 'diet_low_fodmap',
    'Gluten Free': 'diet_gluten_free',
    'Non-GMO': 'diet_non_gmo',
    'Organic/All Natural': 'diet_organic_all_natural',
    'Soy Free': 'diet_soy_free',
    'Whole30': 'diet_whole30',
    'Dairy Free': 'diet_dairy_free',
    'Flexitarian': 'diet_flexitarian',
    'Alkaline diet': 'diet_alkaline',
    'Anti Inflammatory': 'diet_anti_inflammatory',
    'Allergen-free': 'diet_allergen_free',
    'Intuitive eating': 'diet_intuitive_eating',
    'Sustainable diet': 'diet_sustainable_diet',
    'Low Histamine': 'diet_low_histamine',
    'Beegan': 'diet_beegan',
    'Diabetic Friendly': 'diet_diabetic_friendly',
    'Not listed (please specify)': 'diet_other'
}

# cooking habits question
cooking_habits = {
    'None, I don’t cook at home': 'cooking_habits_none',
    'I make a detailed list once a week': 'cooking_habits_list_once_per_wk',
    'I tend to cook the same meals over and over again': 'cooking_habits_cook_same_meals',
    'I have a rotation of staples and occasionally add something new': 'cooking_habits_occasionally_something_new',
    'I decide what to make on a daily basis': 'cooking_habits_decide_by_day',
    'I cook based on what I have in my house': 'cooking_habits_cook_what_i_have',
    'Other (please specify)': 'cooking_habits_other'
}

# grocery store questions
grocery_store = {
    'Trader Joe’s': 'grocery_store_trader_joes',
    'Albertsons Safeway': 'grocery_store_albertsons',
    'Bashas/AJs/Food City': 'grocery_store_bashas',
    'Central Market': 'grocery_store_central_market',
    'Fresh Market': 'grocery_store_fresh_market',
    'Giant': 'grocery_store_giant',
    'Giant Eagle': 'grocery_store_giant_eagle',
    'Haggen': 'grocery_store_haggen',
    'Harmons': 'grocery_store_harmons',
    'HEB': 'grocery_store_heb',
    'Key Food': 'grocery_store_key_food',
    'Kroger (Ralphs, Marianos, Smiths, Frys, Fred Meyer, King Scoopers, JayC, Bakers)': 'grocery_store_kroger',
    'Market Basket': 'grocery_store_market_basket',
    'Meijer': 'grocery_store_meijer',
    'Nugget Markets': 'grocery_store_nuggest_markets',
    'Publix': 'grocery_store_publix',
    'Schnucks': 'grocery_store_schnucks',
    'Spartan Nash': 'grocery_store_spartan_nash',
    'Stater Bros': 'grocery_store_stater_bros',
    'Stop & Shop': 'grocery_store_stop_and_shop',
    'Wakefern/ShopRite': 'grocery_store_wakerfern_shoprite',
    'Wegmans': 'grocery_store_wegmans',
    'Club Grocer (Costco, BJs, Sam’s Club, etc.)': 'grocery_store_club_grocer',
    'Target': 'grocery_store_target',
    'Walmart': 'grocery_store_walmart',
    'Sprouts': 'grocery_store_sprouts',
    'Whole Foods': 'grocery_store_whole_foods',
    'My local natural store': 'grocery_store_local_natural_store',
    'My local farmers market': 'grocery_store_local_farmers_market',
    'My local co-op': 'grocery_store_local_coop',
    'I did not shop for groceries in-person in the last month.': 'grocery_store_no_grocery_shopping',
    'Other (please specify)': 'grocery_store_other'
}

# online grocery store question
online_grocery_store = {
    'Amazon Fresh': 'online_grocery_store_amazon_fresh',
    'Amazon': 'online_grocery_store_amazon',
    'Thrive Market': 'online_grocery_store_thrive',
    'Walmart Online': 'online_grocery_store_walmart',
    'Target Online': 'online_grocery_store_target',
    'Kroger Online': 'online_grocery_store_kroger',
    'Safeway/Albertsons Online': 'online_grocery_store_albertsons',
    'Instacart': 'online_grocery_store_instacart',
    'Shipt': 'online_grocery_store_shipt',
    'Peapod': 'online_grocery_store_peapod',
    'FreshDirect': 'online_grocery_store_freshdirect',
    'Whole Foods Online': 'online_grocery_store_whole_foods',
    'Hy-Vee Online': 'online_grocery_store_hyvee',
    'Giant Eagle Online': 'online_grocery_store_giant_eagle',
    'Club Grocer Online (Costco, BJs, Sam’s Club, etc)': 'online_grocery_store_club',
    'GoPuff': 'online_grocery_store_gopuff',
    'Foxtrot': 'online_grocery_store_foxtrot',
    'Bubble Goods': 'online_grocery_store_bubble_goods',
    'I did not shop for groceries online in the last month.': 'online_grocery_store_none',
    'Other (please specify)': 'online_grocery_store_other'
}

# grocery purchase question
grocery_purchase = {
    'Gluten-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/cfca865a-4736-4fb1-8912-043c547388f6.png': 'grocery_purchase_gluten_free',
    'Paleo https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/51091a5d-e8a5-4ed9-8e3d-b9654031a125.png': 'grocery_purchase_paleo',
    'Raw https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/0a782582-11c4-4ae6-8397-df6b9d47f9d4.png': 'grocery_purchase_raw',
    'Vegan https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/f462b444-6573-46ea-92ae-fb36f5ed6c67.png': 'grocery_purchase_vegan',
    'Vegetarian https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/846e3ee6-3cb3-467f-bf62-34118fdf9229.png': 'grocery_purchase_vegetarian',
    'AIP Diet https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/f9e8cd8c-e2d7-41fc-a42a-c5c9204d70c5.png': 'grocery_purchase_aip_diet',
    'Low FODMAP https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/5fa5967e-010f-4a1d-9d18-c95ff1cb836e.png': 'grocery_purchase_low_fodmap',
    'Ketogenic https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/b918ca55-2464-43eb-8a3f-40753987dc62.png': 'grocery_purchase_ketogenic',
    'Organic https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/85342485-1c89-421b-863c-92e3b69d38fe.png': 'grocery_purchase_organic',
    'Whole30 Compatible https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/7575ac26-88a3-4d1e-a14a-92119843402b.png': 'grocery_purchase_whole30',
    'Alcohol-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/2f3338ed-6f06-42ea-968b-deb670a707b7.png': 'grocery_purchase_alcohol_free',
    'Caffeine-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/4c1ce9df-8eab-48b8-91fd-392442f3c43a.png': 'grocery_purchase_caffeine_free',
    'Cholesterol-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/ec18d418-201d-4ac6-ae31-f9f3d28a0007.png': 'grocery_purchase_cholesterol_free',
    'Contains Probiotics https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/9913a985-52de-4335-84f0-15a6fcf273ec.png': 'grocery_purchase_contains_probiotics',
    'Dairy-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/d91afeca-98aa-492d-92ae-baf4f390ed74.png': 'grocery_purchase_dairy_free',
    'Dye- and Color Additive-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/010f6241-b3c3-4030-a947-92d36dfd308b.png': 'grocery_purchase_dye_color_free',
    'High Fiber https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/06ee7dde-96ec-4e08-97c0-05dd78a5350d.png': 'grocery_purchase_high_fiber',
    'High in Protein https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/f3225ba3-cec4-49ba-82ff-39361c9dfaa5.png': 'grocery_purchase_high_protein',
    'Low-Fat https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/2eb6820e-2b2c-4ca6-b1a7-2e01c7c1ab31.png': 'grocery_purchase_low_fat',
    'Low-Glycemic https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/3aaa46bb-0881-4a72-b6e3-a99f8fa93ac2.png': 'grocery_purchase_low_glycemic',
    'No Added Sugar or Sweeteners https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/71db6e31-c44e-4052-8c1b-a84d112ad152.png': 'grocery_purchase_no_added_sugar',
    'No Antibiotics / Synthetic Hormones https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/da22d7ed-33a5-4b88-8d52-b563bb189e46.png': 'grocery_purchase_no_antibiotics',
    'No Sulfites / Sulphur Dioxide https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/436738a4-de73-462e-9a63-4ef8a8f94b9c.png': 'grocery_purchase_no_sulfites',
    'Nut-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/06c27b22-72a8-4dad-bdb0-0ac4e343b787.png': 'grocery_purchase_nut_free',
    'Peanut-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/1e61b218-0415-4fa9-92f1-52bf2d0ecc7a.png': 'grocery_purchase_peanut_free',
    'Pesticide-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/1f1a61a2-07b8-4df5-9e41-9d07212c6fa4.png': 'grocery_purchase_pesticide_free',
    'Preservative-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/563dba10-bda1-44ae-b406-152c8e2a2388.png': 'grocery_purchase_preservative_free',
    'Salt-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/bf020a3a-8e80-40ca-b322-f5e96633a7c0.png': 'grocery_purchase_salt_free',
    'Soy-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/a88844ae-5fd0-4103-9f36-f553f1f10451.png': 'grocery_purchase_soy_free',
    'Sugar-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/25634e35-68c7-4279-bdb7-a94f1359cb12.png': 'grocery_purchase_sugar_free',
    'Yeast-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/0a816c5d-e65d-4f46-85f3-f43ffc9950da.png': 'grocery_purchase_yeast_free',
    'Non-GMO https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/1f945a81-53a8-4097-9ee9-760987b810b8.png': 'grocery_purchase_non_gmo',
    'Big 8 Allergen-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/2f0af677-3125-499e-bac0-6e83cc413b7d.png': 'grocery_purchase_big_8_allergen_free',
    'Grain-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/4b337084-0db8-4448-b628-64d5e509ed84.png': 'grocery_purchase_grain_free',
    'Plant-Based https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/d5708f50-8ba2-42aa-99a4-fd3c53fce766.png': 'grocery_purchase_plant_based',
    'Low-Sodium https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/e31668a1-2968-453b-a0f9-3fa34dfdb31a.png': 'grocery_purchase_low_sodium',
    'Low Sugar https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/0f4642a2-bce9-44b8-ac0b-638c1f7004e7.png': 'grocery_purchase_low_sugar',
    'Other (please specify)': 'grocery_purchase_other'
}

# certified grocery product question
grocery_purchase_cert = {
    'Certified Gluten-Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/9e860e59-e707-4ab5-8270-c94310322fd6.png': 'grocery_purchase_cert_gluten_free',
    'Certified Organic https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/67b5a6fa-2656-4715-b6b9-b92cc28f8f90.png': 'grocery_purchase_cert_organic',
    'Certified Vegan https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/528d0758-ee70-4758-a866-586bc52e7132.png': 'grocery_purchase_cert_vegan',
    'Certified Fairly Traded https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/a633c4f7-d5ac-4391-9931-46c73f1296f1.png': 'grocery_purchase_cert_fairly_traded',
    'Non-GMO Project Verified https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/d8fb83d0-958d-480c-80f6-add2b96fe5fb.png': 'grocery_purchase_cert_non_gmo_project',
    'Whole30 Approved https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/706e9185-7fba-4014-97a3-dcf313a05c15.png': 'grocery_purchase_whole30_approved',
    'Certified Kosher https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/dd78da23-f9d3-4216-b7a6-594fa4b84836.png': 'grocery_purchase_cert_kosher',
    'Certified Glyphosate Residue Free https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/4cee12fe-faff-4f61-b44c-cf7ecce78e56.png': 'grocery_purchase_cert_glyphosate_residue_free',
    'Certified Biodynamic https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/e7e55390-849b-4ece-97aa-bda197e0f7e5.png': 'grocery_purchase_cert_biodynamic',
    'Certified B Corporation https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/c0183389-be6b-44f1-bebd-808e0f6f50ae.png': 'grocery_purchase_cert_b_corp',
    'Leaping Bunny Certified https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/fed90bfe-d586-440e-8b8b-010cce755230.png': 'grocery_purchase_leaping_bunny_cert',
    'Certified Halal https://surveymonkey-assets.s3.amazonaws.com/survey/509126465/rte/6cd2c9cc-96aa-43e3-a351-7f552f3311e3.png': 'grocery_purchase_cert_halal',
    'Monash University Low FODMAP Certified https://surveymonkey-assets.s3.amazonaws.com/survey/508764373/rte/fecac568-f0a1-4754-8544-83457adb616b.png': 'grocery_purchase_monash_university_low_fodmap',
    'Other (please specify)': 'grocery_purchase_cert_other'
}

# grocery product question (q31)
grocery_product = {
    'Biodegradable https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/17ce1f27-302d-4512-a176-447be5d32e87.png': 'grocery_purchase_biodegradable',
    'BPA-Free https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/50822fee-1019-4497-b863-8153cb10d35b.png': 'grocery_purchase_bpa_free',
    'Compostable https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/7ecfacef-03f0-4f8e-96b6-06d3322009ec.png': 'grocery_purchase_compostable',
    'Cruelty-Free https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/5cb9bb7d-bf4b-4edc-a27b-1aba855cad6c.png': 'grocery_purchase_cruelty_free',
    'Made in USA https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/f0d446f7-6d22-4a0a-83cf-4ec296e20b05.png': 'grocery_purchase_made_in_usa',
    'Nontoxic https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/0d089861-5eee-455a-97f6-6c6cf05cd141.png': 'grocery_purchase_non_toxic',
    'Recycled Packaging https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/93d2a11d-b18c-4a34-a8df-f03e1cd2d5ab.png': 'grocery_purchase_recycled_packaging',
    'Sourced Direct From Farmers https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/b52b68d3-5c2c-4157-b7b2-e1dbae26db48.png': 'grocery_purchase_sourced_direct_farmers',
    'Ethically Sourced https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/cd02c63d-8d94-44a3-a968-9b9c6c48b64c.png': 'grocery_purchase_ethically_sourced',
    'Woman-Founded Business https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/64870c24-3c1b-4a38-a9b8-3b4b54a9847d.png': 'grocery_purchase_woman_founded_business',
    'Sustainably Farmed https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/47cc005a-5940-4a35-99e1-8859b2d2824e.png': 'grocery_purchase_sustainably_farmed',
    'Regenerative https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/adc9ebcf-ced5-49c6-8190-81b6cd22f5d0.png': 'grocery_purchase_regenerative',
    'Recyclable https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/f91393c9-8f5c-4f30-8b92-f668cdb7cd01.png': 'grocery_purchase_recyclable',
    'Plastic-Free https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/a25a1f31-f30d-4b1c-b70e-1f46c5743989.png': 'grocery_purchase_plastic_free',
    'BIPOC Founded https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/28ed9dd6-a670-4a24-b2ff-bfe08a7f9ac8.png': 'grocery_purchase_bipoc_founded',
    'Upcycled https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/2f54c35b-16a9-4ed5-9727-578d57a23194.png': 'grocery_purchase_upcycled',
    'Supports Charity https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/7c4b2666-c0c0-47b6-8abf-a44dffd62bca.png': 'grocery_purchase_supports_charity',
    'Low-Waste https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/701eb9bc-7bba-402d-8131-5769049d5822.png': 'grocery_purchase_low_waste',
    'LGBTQIA+ Founded https://surveymonkey-assets.s3.amazonaws.com/survey/508656311/rte/07ecffa2-1464-475b-96fa-7eceed2ce050.png': 'grocery_purchase_lgtqia_founded',
    'Other (please specify)': 'grocery_product_other'
}

# plant based frustration question
plant_based = {
    'Plant-based options are expensive': 'plant_based_expensive',
    'Plant-based options don’t taste good/could taste better': 'plant_based_bad_taste',
    'Plant-based options have bad texture': 'plant_based_bad_texture',
    'Plant-based options are hard to find in my local grocery store': 'plant_based_hard_to_find',
    'There aren’t enough plant-based protein options': 'plant_based_not_enough_protein_options',
    'Plant-based products aren’t high enough in protein': 'plant_based_not_enough_protein',
    'Plant-based products are too processed': 'plant_based_too_processed',
    'Plant-based products include ingredients I don’t like or want to eat': 'plant_based_do_not_like',
    'I have no frustrations when it comes to plant-protein products': 'plant_based_no_frustrations',
    'Other (please specify)': 'plant_based_other_issues'
}

map_of_questions = {
    'Respondent ID': responder,
    'Custom Data 1': customID,
    'Type: “Hello world”': type_hello_world,
    'What is your age?': respondent_age,
    'Who is the primary grocery shopper for your household?': grocery_shopper,
    "What's your annual household income?": annual_income,
    'Which part of the United States do you live?': living_location,
    'Which of the following describes your household? Select all that apply.': household_makeup,
    'If there are children in your household, what are their age ranges? Select all that apply.': age_of_children,
    'Which ethnicities do you identify with? Select all that apply.': ethnicity,
    'What is your relationship status? Select all that apply.': relationship_status,
    'What is your current employment status? Select all that apply.': employment_status,
    'How do you identify?': gender,
    'What is the highest level of education you have achieved?': education,
    'What best describes your living environment?': living_location_size,
    'What zip code do you live in? (5-digit zip code)': zipcode,
    'Which best describes your relationship to exercise? Select all that apply.': health_and_wellness,
    'Which of the following health concerns or priorities do you actively consider when grocery shopping? Select your top 3.': health_concerns,
    'Name a supplement you purchased in the last 3 months that relates to one of your top 3 health concerns or priorities.What was it (brand and product), which health priority it relates to, and explain why you purchased it?': supplements,
    'Name a food or beverage product you purchased in the last 3 months that supports one of your top 3 health concerns or priorities.What was it (brand and product), which health priority it relates to, explain why you purchased it, and what you enjoyed (or did not) about it?': healthy_food_products,
    'Which, if any, diets or restrictions do you or someone in your household currently, or did in the last 3 months, follow? Select all that apply.': diet_restrictions,
    'Which of the following describes your attitudes towards sustainable foods (foods that are grown in a manner that limits their negative impact on the environment and the communities that produce them)?': sustainable_foods,
    'Which of following best describes your meal planning or cooking style in the last 3 months? Select all that apply.': cooking_habits,
    'Name a new recipe that you cooked at home in the last 3 months.What was it (name, type of dish, cuisine), how did you find it, and describe what you enjoyed (or did not) about it?': home_recipe,
    'Name a new restaurant dish that you ate in the last 3 months.What was it (dish name, type, cuisine), why did you order it, what restaurant, and describe what you enjoyed (or did not) about it?': restaurant_dish,
    'In the last month, which stores did you shop in-person to buy groceries? Select all that apply.': grocery_store,
    'In the last month, which online stores/services did you shop to buy groceries? Select all that apply.': online_grocery_store,
    'Name a new snack food product that you bought and tried in the last 3 months. What was it (product and brand), why did you buy it, from where, and describe what you enjoyed (or did not) about it?': new_snack,
    'How much money did you spend on groceries last week?': money_spent_on_groceries,
    'Name a new food product that you bought and tried as a meal or part of a meal in the last 3 months.What was it (product and brand), why did you buy it, from where, and describe what you enjoyed (or did not) about it?': side_dish,
    'Which of the following describe grocery products you purchased in the last month? Select all that apply.': grocery_purchase,
    'Which of the following certifications do grocery products that you purchased in the last month have? Select all that apply.': grocery_purchase_cert,
    'Which of the following characteristics describe grocery products you purchased in the last month? Select all that apply.': grocery_product,
    'What places, if any, outside of the United States (City, Country) did you travel to in the last 2 years?': travel_location,
    'Thinking about the last new food product, dish, or recipe you discovered or tried, how did you find out about it?': food_rec_source,
    'In the last week, which social media platform did you spend the most time on?': social_media,
    'Which of the below best describes your attitude towards plant-based protein?': plant_based_opinion,
    'When it comes to plant-based protein products, what, if any, are your primary frustrations? Select up to three.': plant_based,
    'Habeya is a high protein crunchy “topper” made from crispy chickpeas, herbs, and spices.Where would you expect to find Habeya in your local grocery store? Include aisle, location, or other products you would expect it to be nearby.': habeya,
    'is_good_response': good_or_bad_response
}

# for the other/notlisted column of a response question
def other_notlisted_column(question, csv_file):
    # Turn header row into a list
    list_of_all_columns = csv_file.iloc[0].tolist()

    # Get the index of the question
    question_index = list_of_all_columns.index(question)

    # Extract the column of answers
    answers_column = csv_file.iloc[1:, question_index + 1].fillna('')

    current_question_map = map_of_questions[question]

    # Create a new DataFrame for the column
    new_csv = pd.DataFrame(answers_column)

    # get the key-value in the question map for whatever the original column is called
    column_name = current_question_map.get('Other (please specify)') or current_question_map.get(
        'Not listed (please specify)')

    # replace the original column name with the key value
    output_csv = new_csv.replace('Other (please specify)', column_name).replace('Not listed (please specify)',
                                                                                column_name)
    output_csv.columns = output_csv.iloc[0]

    # Drop the first row (header)
    output_csv = output_csv[1:]

    return output_csv


# if the question is open-ended response
def open_ended_question(question, csv_file):
    # Turn header row into a list
    list_of_all_columns = csv_file.iloc[0].tolist()

    # Get the index of the question
    question_index = list_of_all_columns.index(question)

    # Extract the column of answers
    answers_column = csv_file.iloc[1:, question_index].fillna('')

    current_question_map = map_of_questions[question]

    # Create a new DataFrame for the column
    new_csv = pd.DataFrame(answers_column)

    column_name = current_question_map['Open-Ended Response']

    output_csv = new_csv.replace('Open-Ended Response', column_name)

    output_csv.columns = output_csv.iloc[0]

    # Drop the first row (header)
    output_csv = output_csv[1:]

    return output_csv


def response_question(question, csv_file):
    # Turn header row into a list
    list_of_all_columns = csv_file.iloc[0].tolist()

    # Get the index of the question
    question_index = list_of_all_columns.index(question)

    # Extract the column of answers
    answers_column = csv_file.iloc[1:, question_index].fillna('')

    current_question_map = map_of_questions[question]

    # Create a new DataFrame for the column
    new_csv = pd.DataFrame(answers_column)

    column_name = current_question_map['Response']

    output_csv = new_csv.replace('Response', column_name)

    output_csv.columns = output_csv.iloc[0]

    # Drop the first row (header)
    output_csv = output_csv[1:]

    return output_csv


# if the question is a 'nan' type column
def nan_question(question, csv_file):
    # Turn header row into a list
    list_of_all_columns = csv_file.iloc[0].tolist()

    # Get the index of the question
    question_index = list_of_all_columns.index(question)

    # Extract the column of answers
    answers_column = csv_file.iloc[1:, question_index].fillna('')

    current_question_map = map_of_questions[question]

    # Create a new DataFrame for the column
    new_csv = pd.DataFrame(answers_column)

    column_name = current_question_map['nan']

    output_csv = new_csv.replace('', column_name)

    output_csv.columns = output_csv.iloc[0]

    # Drop the first row (header)
    output_csv = output_csv[1:]

    return output_csv


transformed_data = []


# if it is question in which user chooses multiple answers
def multiple_answer_question(question, input_csv):
    current_question_map = map_of_questions[question]

    # Create a list to hold the transformed DataFrame rows
    transformed_rows = []

    # Append the column names to the transformed_rows list
    transformed_rows.append(list(current_question_map.values()))

    # turns the 2nd row of responses all into 1 list
    list_of_all_columns = input_csv.iloc[0].tolist()

    # what is the first answer choice of the question
    first_answer = next(iter(current_question_map))

    # finds index of first answer choice in the entire csv
    first_answer_index = list_of_all_columns.index(first_answer)

    # Get the index of the 'Other (please specify)' column
    other_column_indices = []
    for column_name in ['Other (please specify)', 'Not listed (please specify)']:
        if column_name in current_question_map.keys():
            other_column_indices.append(list(current_question_map.keys()).index(column_name))

    # Iterate over each row in the input DataFrame
    for idx, row in input_csv.iterrows():
        # Skip the first row (index 0) which contains the column names
        if idx == 0:
            continue

        # Create a list to hold the transformed row values
        transformed_row = ['0'] * len(current_question_map)

        # Iterate over the column mapping
        for key, value in current_question_map.items():
            # Check if the original column value exists in the row values
            if key in row.values:
                # Set the corresponding value in the transformed row to '1'
                transformed_row[list(current_question_map.keys()).index(key)] = '1'

        # Set the value of other column to the value from 'Other (please specify)'
        for other_column_index in other_column_indices:
            other_value = row[other_column_index + first_answer_index]
            if pd.isnull(other_value):  # Check if the value is NaN
                other_value = ''  # Set to an empty string if it's NaN
            transformed_row[other_column_index] = str(other_value)

        # Append the transformed row to the transformed_rows list
        transformed_rows.append(transformed_row)

    # Create a new DataFrame with the transformed rows
    final_df = pd.DataFrame(transformed_rows)

    # Update the index of the final DataFrame to start with 1 instead of 0
    final_df.index = final_df.index + 1

    output_csv = final_df

    output_csv.columns = output_csv.iloc[0]

    # Drop the first row (header)
    output_csv = output_csv[1:]

    return output_csv

