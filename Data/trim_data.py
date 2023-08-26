# takes in cleaned_calgary_communities_with_images.csv
# and drops rows that don't contain a relevant image
# saves these rows in a separate file (to be added later)
# and exports a "final" csv with our final clean data

import pandas as pd

final_data = pd.read_csv('Data/cleaned_calgary_communities_with_images.csv')
missing_data = final_data.copy()

# Drop rows with missing photos
final_data = final_data[final_data['image_url'].notna()]

missing_data = missing_data[missing_data.image_url.isin(final_data.image_url) == False]


final_data.to_csv('Data/final_calgary_communities.csv', index = False)
missing_data.to_csv('Data/missing_images.csv', index = False)