import pandas as pd

data = pd.read_csv('Data/calgary_communities.csv')

data = data[data['CLASS'] == 'Residential']
data.reset_index(drop = True, inplace = True)

data = data.drop('CLASS', axis = 1)
data = data.drop('SRG', axis = 1)
data = data.drop('COMM_STRUCTURE', axis = 1)

data.to_csv('Data/cleaned_calgary_communities.csv', index = False)