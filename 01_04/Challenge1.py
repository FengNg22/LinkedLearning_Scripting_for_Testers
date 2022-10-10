#Problem description
#Find out if there are any duplicate urls used in the
#json placeholder photo data

import requests

url = 'https://jsonplaceholder.typicode.com/photos'

# get the data about the photos

# examples with authentication
# response = requests.get(url, auth=('username', 'password'))
# response = requests.get(url, headers={'Autorization': 'token'})

response = requests.get(url)


# read that data into a variable
json_data = response.json()

# create a list for storing the url of each photo
url_list = []
for photo in json_data:
    # add the url for each photo to the url_list
    url_list.append((photo['url']))


# How many items are in the url list (Should be 5000 since we have 5000 photos in our dataset)?
print(len(url_list))

# How many items are there if we turn that list into a set?
# set will remove the duplicated data
print(len(set(url_list)))


