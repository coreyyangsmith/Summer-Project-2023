''' This code will scrape and download community banner images from Royale LePage'''
import os
import pandas as pd

from bs4 import BeautifulSoup
import requests
import urllib.request
import time

df = pd.read_csv('cleaned_calgary_communities.csv')
df['image_url'] = ''

# The Following URLs contain links to every Calgary community as well as a banner image for the community.
base_urls = ['https://royallepagebenchmark.ca/calgary/northeast/',
             'https://royallepagebenchmark.ca/calgary/northwest/',
             'https://royallepagebenchmark.ca/calgary/southeast/',
             'https://royallepagebenchmark.ca/calgary/southwest/']

img_dir = '../media/community_images'
os.makedirs(img_dir, exist_ok=True)

# Dummy Header to get past error 403
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537'}

# For each NAME in the communities CSV file:
for index, row in df.iterrows():
    neighborhood = row['NAME']
    neighborhood_code = row['COMM_CODE']
    neighborhood_url = neighborhood.lower().replace(' ', '-')

    for base_url in base_urls:
        # Append the neighborhood name to the base URLs to form the complete URL
        url = base_url + neighborhood_url

        # Access the community's URL
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            img_element = soup.find('img', class_='attachment-royal_large_image')

            if img_element is not None:
                # Find the source image URL
                img_url = img_element.get('data-src')
                print(f'Found source URL: {img_url}')

                # Get File Extension of Source image
                file_ext = os.path.splitext(img_url)[-1]
                
                # Construct the file name to be saved as
                img_name = f'{neighborhood_code}{file_ext}'

                # Request the source image URL with dummy header
                req = urllib.request.Request(img_url, headers=headers)
                with urllib.request.urlopen(req) as response, open(os.path.join(img_dir, img_name), 'wb') as out_file:
                    data = response.read()
                    out_file.write(data)
                print(f'Downloaded {img_name}')

                # Add the image URL to the dataframe
                df.loc[index, 'image_url'] = img_url

            else:
                print(f'!!\nNo image found on RLP for {neighborhood_url}\n')
            
            time.sleep(1) # Respectful sleeping
            break

# Save new CSV with URLs
df.to_csv('cleaned_calgary_communities_with_images.csv', index=False)