import pandas as pd

data = pd.read_csv('Datasets/final_dataset_project_full_no_normalisation.csv')
#test_data = pd.read_csv('Datasets/test_project_full_new_normalisation.csv')
print(data.head())

def drop_irrelevant_data(data): 
	data = data[data.MW > 3]
	#test_data = test_data[test_data.MW > 3]

	data.drop(['Unnamed: 0','HomeTeam', 'AwayTeam', 'Date', 'MW', 'HTFormPtsStr', 'ATFormPtsStr', 'FTHG', 'FTAG',
	           'HTGS', 'ATGS', 'HTGC', 'ATGC','HomeTeamLP', 'AwayTeamLP','HTFormPts','ATFormPts',
	           'HM4','HM5','AM4','AM5','HTLossStreak5','ATLossStreak5','HTWinStreak5','ATWinStreak5',
	           'HTWinStreak3','HTLossStreak3','ATWinStreak3','ATLossStreak3'],1, inplace=True)

	# test_data.drop(['Unnamed: 0','HomeTeam', 'AwayTeam', 'Date', 'MW', 'HTFormPtsStr', 'ATFormPtsStr', 'FTHG', 'FTAG',
	#            'HTGS', 'ATGS', 'HTGC', 'ATGC','HomeTeamLP', 'AwayTeamLP','HTFormPts','ATFormPts',
	#            'HM4','HM5','AM4','AM5','HTLossStreak5','ATLossStreak5','HTWinStreak5','ATWinStreak5',
	#            'HTWinStreak3','HTLossStreak3','ATWinStreak3','ATLossStreak3'],1, inplace=True)
	return data #, test_data

#, cleaned_test_data = 
cleaned_data = drop_irrelevant_data(data)


def get_dataset_stats(data):

	total_matches = data.shape[0]
	number_of_features = data.shape[1] - 1
	number_homewins = len(data[data.FTR == 'H'])
	win_rate = (float(number_homewins) / (total_matches)) * 100

	return total_matches, number_of_features, number_homewins, win_rate

total_matches, number_of_features, number_homewins, win_rate = get_dataset_stats(cleaned_data)

print ("Total number of matches: {}".format(total_matches))
print ("Number of features: {}".format(number_of_features))
print ("Number of matches won by home team: {}".format(number_homewins))
print ("Win rate of home team: {:.2f}%".format(win_rate))

cleaned_data.to_csv('Datasets/relevant_data/cleanedDataset_full_no_normalisation.csv')
#cleaned_test_data.to_csv('Datasets/relevant_data/cleanedTestDataset_full_new_normalisation.csv')



