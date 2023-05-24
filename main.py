import pandas as pd
import tabulardata
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# models
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier

# Read the original CSV file, with the 1st row of questions showing
questions_csv = pd.read_csv('/Users/davidcui02/Desktop/input.csv', header=None)

original_csv = pd.read_csv('/Users/davidcui02/Desktop/input.csv')

questions_csv.drop(questions_csv.columns[[1, 2, 3, 4, 5, 6, 7]], axis=1, inplace=True)

original_csv.drop(['Collector ID',
                   'Start Date',
                   'End Date',
                   'IP Address',
                   'Email Address',
                   'First Name',
                   'Last Name'], axis=1, inplace=True)

# remove leading/trailing spaces in columns
questions_csv.iloc[0] = [value.strip() if isinstance(value, str) else value for value in questions_csv.iloc[0]]
original_csv.columns = [value.strip() if isinstance(value, str) else value for value in original_csv.columns]

# save the first row as a list
headers = original_csv.columns.to_list()

# loop through the columns
for i in range(1, len(headers)):
    # check if the word starts with "Unnamed"
    if headers[i].startswith('Unnamed'):
        # replace the word with the previous word in the list
        headers[i] = headers[i - 1]

# update the first row with new column names
questions_csv.columns = headers

# create curr_question variable
curr_question = ''
output = pd.DataFrame()
open_responses = pd.DataFrame()
null_columns = pd.DataFrame()
# create a loop that goes through numbers that represent each column index
for i in range(0, len(questions_csv.columns)):
    curr_question = questions_csv.columns[i]
    # check to see if the current column is the same as the last column, indicated we already handled that question
    if curr_question == questions_csv.columns[i - 1]:
        # if we handled it already, update the current question variable
        # curr_question = questions_csv.columns[i]
        # continue onto the next item in the loop
        continue
    # if we haven't handled this question yet
    else:
        # check to see if this isn't a question (indicated by a blank second row)
        if pd.isnull(original_csv.iloc[0][i]):
            # output = pd.concat([output, nan_question(curr_question, questions_csv)], axis=1)
            # open_responses = pd.concat([open_responses, nan_question(curr_question, questions_csv)], axis=1)
            null_columns = pd.concat([null_columns, tabulardata.nan_question(curr_question, questions_csv)], axis=1)
        # check to see if this is a single-select question
        elif original_csv.iloc[0][i] == 'Response':
            # if it is single select, check to see if there is a option to list something not available
            if original_csv.iloc[0][i + 1] in ['Not listed (please specify)', 'Other (please specify)']:
                output = pd.concat([output, tabulardata.response_question(curr_question, questions_csv)], axis=1)
                open_responses = pd.concat(
                    [open_responses, tabulardata.other_notlisted_column(curr_question, questions_csv)], axis=1)
            # if it's a regular single select, then handle that way
            else:
                # handle w/ single select
                output = pd.concat([output, tabulardata.response_question(curr_question, questions_csv)], axis=1)
        elif original_csv.iloc[0][i] == 'Open-Ended Response':
            # handle by taking the value (similar to nan question)
            open_responses = pd.concat([open_responses, tabulardata.open_ended_question(curr_question, questions_csv)],
                                       axis=1)
        # otherwise it must be a multi-select answer
        else:
            # handle with multi-select
            output = pd.concat([output, tabulardata.multiple_answer_question(curr_question, original_csv)], axis=1)
    # update current question
    curr_question = questions_csv.columns[i]

output.drop(['live_with_other_family_adults',
             'race_other',
             'relationship_other',
             'other_employment',
             'exercise_other',
             'health_concern_other',
             'diet_other',
             'cooking_habits_other',
             'grocery_store_other',
             'online_grocery_store_other',
             'grocery_purchase_other',
             'grocery_purchase_cert_other',
             'grocery_product_other',
             'plant_based_other_issues'], axis=1, inplace=True)


output.to_csv('/Users/davidcui02/Desktop/output.csv', index=False)
open_responses.to_csv('/Users/davidcui02/Desktop/open_responses.csv', index=False)



# first two columns that are the responder ID and custom data
responder_info = null_columns.iloc[:, :2]
# result column
results = null_columns.iloc[:, 2:]

# Read the CSV file
data = pd.read_csv('/Users/davidcui02/Desktop/output.csv')

# Identify columns that can be converted to int
integer_columns = []

for column in data.columns:
    try:
        if data[column].str.isnumeric().all():
            integer_columns.append(column)
    except:
        pass

# Convert identified columns to int
data[integer_columns] = data[integer_columns].astype('int')

# Create dummy variables using get_dummies()
dummy_data = pd.get_dummies(data, dtype=int)

# create final open_response csv
open_responses_final = pd.concat([responder_info, open_responses, results], axis=1)

# Reset indices of DataFrames
responder_info.reset_index(drop=True, inplace=True)
dummy_data.reset_index(drop=True, inplace=True)
results.reset_index(drop=True, inplace=True)

final = pd.concat([responder_info, dummy_data, results], axis=1)

# Save the dummy variables DataFrame to a CSV file
final.to_csv('/Users/davidcui02/Desktop/final.csv', index=False)
open_responses_final.to_csv('/Users/davidcui02/Desktop/open_responses.csv', index=False)

# train model

# prep data
data = pd.read_csv('/Users/davidcui02/Desktop/final.csv')
X = data.drop(columns=['custom_data_ID'])  # Remove 'custom_data_ID' column only
X = X.drop(columns=['result'])  # Remove 'result' column
y = data['result']

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

"""
# __________________ boost model ___________ 0.8192955589586524 
# create model
boost = HistGradientBoostingClassifier()
# fit models
boost.fit(X_train, y_train)
# make predictions
predictions_boost = boost.predict(X_test)
# report accuracy score
acc_boost = accuracy_score(predictions_boost, y_test)
print("Boost: " + str(acc_boost))
# saving model
#filename = "boost.pickle"
"""

"""
# __________________ svm model ___________ 0.6447166921898928 
# create model
svm = svm.SVC(kernel='linear')
# fit models
svm.fit(X_train, y_train)
# make predictions
predictions_svm = svm.predict(X_test)
# report accuracy score
acc_svm = accuracy_score(predictions_svm, y_test)
print("SVM: " + str(acc_svm))
# saving model
#filename = "svm.pickle"
"""

"""
# __________________ knn model ___________
# n_neighbors=5: 0.5895865237366003
# n_neighbors=10: 0.5926493108728943
# n_neighbors=20: 0.6156202143950995
# n_neighbors=25: 0.6294027565084227
# n_neighbors=40: 0.6171516079632465
# n_neighbors=50: 0.6278713629402757
# n_neighbors=100: 0.6508422664624809

# create model
# edit n to find best result
knn = KNeighborsClassifier(n_neighbors=250)
# fit models
knn.fit(X_train, y_train)
# make predictions
predictions_knn = knn.predict(X_test)
# report accuracy score
acc_knn = accuracy_score(predictions_knn, y_test)
print("KNN: " + str(acc_knn))
# saving model
#filename = "knn.pickle"
"""

"""
# __________________ lda model ___________ 0.7856049004594181
# create model
lda = LinearDiscriminantAnalysis()
# fit models
lda.fit(X_train, y_train)
# make predictions
predictions_lda = lda.predict(X_test)
# report accuracy score
acc_lda = accuracy_score(predictions_lda, y_test)
print("LDA: " + str(acc_lda))
# saving model
#filename = "lda.pickle"
"""

"""
# __________________ random forest model ___________  0.8254211332312404
# Create the random forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model to the training data
rf.fit(X_train, y_train)

# Make predictions on the test data
predictions_rf = rf.predict(X_test)

# Calculate the accuracy score
acc_rf = accuracy_score(predictions_rf, y_test)
print("Random Forest: " + str(acc_rf))
"""

"""
# --------------------------------------------------- #
pickle.dump(boost, open(filename, "wb"))

# loading saved model
model = pickle.load(open(filename, "rb"))

# applying saved model to sample dataset...
X = "some data goes here..."
y_predicted = model.predict(X)
"""
