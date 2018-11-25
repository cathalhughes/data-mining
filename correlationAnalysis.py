import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Datasets/relevant_data/cleanedDataset_full_no_normalisation.csv', index_col = 0)

#print(data.info())

data.FTR = data.FTR.astype('str')

print(data.head())
print(data.info())
output = pd.DataFrame(index = data.index)
for col, col_data in data.iteritems():
		if col_data.dtype == object:
			col_data = pd.get_dummies(col_data, prefix = col)
		output = output.join(col_data)


print(output.head())

#output.corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1).to_excel('pearson.xlsx')
#output.corr(output['DiffLP']) #.style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1).to_excel('DiffLP.xlsx')



##plt.imsave("pearsonCorrelation.png", cor)
#print(data['FTR'].corr(data['DiffLP']))

# plot correlated values
plt.rcParams['figure.figsize'] = [16, 6]

fig, ax = plt.subplots(nrows=1, ncols=3)

ax=ax.flatten()

cols = ['HTP', 'ATP', 'ATGD']
colors=['#415952', '#f35134', '#243AB5', '#243AB5']
j=0

for i in ax:
    if j==0:
        i.set_ylabel('HTGD')
    i.scatter(output[cols[j]], output['HTGD'], color=colors[j])
    i.set_xlabel(cols[j])
    i.set_title('Pearson: %s'%output.corr().loc[cols[j]]['HTGD'].round(2)+' Spearman: %s'%output.corr(method='spearman').loc[cols[j]]['HTGD'].round(2))
    j+=1

plt.show()