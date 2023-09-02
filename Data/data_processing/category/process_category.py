import pandas as pd

'''
Receives:
- category_step1.csv
    - incls. Neighbourhood code
    - incls. comma-separated categories

Exports:
- category.csv
    - incls. Neighbourhood code with unique category on each line
'''

FILE_PATH = "Data/data_processing/category/category_step1.csv"
EXPORT_PATH = "scripts/seeding/seeding_data/category.csv"

df = pd.read_csv(FILE_PATH)

df_primary = df[['code', 'categories']].copy()
df_primary['categories'] = df_primary['categories'].str.split(",")
df_primary = df_primary.explode('categories')
df_primary.to_csv(EXPORT_PATH)

print("Category.csv succesfully generated.")