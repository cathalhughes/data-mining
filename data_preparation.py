from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv('Datasets/relevant_data/cleanedDataset.csv', index_col = 0)
# test_data = pd.read_csv('Datasets/relevant_data/cleanedTestDataset.csv', index_col = 0)

# data = pd.read_csv('Datasets/final_dataset_project.csv')
# test_data = pd.read_csv('Datasets/test_project.csv')


#data.drop(['Unnamed: 0'])

def get_target_label_for_data(data):
	attributes = data.drop(['FTR'],1)
	target_label = data['FTR']

	return attributes, target_label

def get_home_not_home(data):
	data['FTR'] = data.FTR.apply(only_hw)

	attributes = data.drop(['FTR'],1)
	target_label = data['FTR']

	return attributes, target_label


def only_hw(string):
    if string == 'H':
        return 'H'
    else:
        return 'NH'


# attributes, target_label = get_target_label_for_data(data)

# test_attributes , test_target_label = get_target_label_for_data(test_data)

def standardise_data(attributes):
	columns = [['HTGD','ATGD','HTP','ATP','DiffLP']]
	for column in columns:
		attributes[column] = scale(attributes[column])
	
	attributes.HM1 = attributes.HM1.astype('str')
	attributes.HM2 = attributes.HM2.astype('str')
	attributes.HM3 = attributes.HM3.astype('str')
	attributes.AM1 = attributes.AM1.astype('str')
	attributes.AM2 = attributes.AM2.astype('str')
	attributes.AM3 = attributes.AM3.astype('str')
	
	return attributes

# attributes = standardise_data(attributes)

# test_attributes = standardise_data(test_attributes)

def convert_categorical_variables(attributes):
	output = pd.DataFrame(index = attributes.index)
	for col, col_data in attributes.iteritems():
			if col_data.dtype == object:
				print(col_data)
				col_data = pd.get_dummies(col_data, prefix = col)
			output = output.join(col_data)

	return output

# attributes = convert_categorical_variables(attributes)
# print ("Processed feature columns ({} total features):\n{}".format(len(attributes.columns), list(attributes.columns)))

# print ("\nFeature values:")
# print(attributes.head())

# print(test_target_label)

def split_data(data, test_data):
	attributes, target_label = get_target_label_for_data(data)
	test_attributes , test_target_label = get_target_label_for_data(test_data)
	attributes = standardise_data(attributes)
	test_attributes = standardise_data(test_attributes)
	attributes = convert_categorical_variables(attributes)
	test_attributes = convert_categorical_variables(test_attributes)

	return attributes, test_attributes, target_label, test_target_label



data = pd.read_csv('Datasets/relevant_data/cleanedDataset_full_no_normalisation.csv', index_col = 0)
#test_data = pd.read_csv('Datasets/relevant_data/cleanedTestDataset.csv', index_col = 0)

def convert_categorical_variables1(attributes):
	output = pd.DataFrame(index = attributes.index)
	for col, col_data in attributes.iteritems():
			if col_data.dtype == object and col != 'FTR':
				# print(col_data)
				col_data = pd.get_dummies(col_data, prefix = col)
			output = output.join(col_data)

	return output

#test = pd.concat([data, test_data], ignore_index=True)
#print(len(test_data))
#data = standardise_data(data)

# cols = ['HTP', 'ATP', 'HM1_D', 'HM1_D','HM1_D','AM1_D','AM3_L','AM3_W', 'HTGD','ATGD','DiffFormPoints','DiffLP','FTR']
cols = ['HTP','ATP', 'HM1', 'HM2', 'HM3', 'AM1', 'AM2', 'AM3','HTGD','ATGD','DiffFormPts','DiffPts','DiffLP', 'FTR']
data = data[cols]

#data = convert_categorical_variables1(data)
data = data.drop(['HM1', 'HM2', 'HM3', 'AM1', 'AM2', 'AM3'], 1)
#data['HTP'].hist(bins=10)
#plt.xlabel("HTP")
#plt.show()
print(data)

data.to_csv('Datasets/relevant_data/forBayes2_no_normalisation.csv')

'''
Both of these techniques have their drawbacks. If you have outliers in your data set, normalizing your data will certainly scale the “normal” data to a very small interval. And generally, most of data sets have outliers. When using standardization, your new data aren’t bounded (unlike normalization).
'''

