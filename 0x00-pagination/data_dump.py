#!/usr/bin/env python3
'''script to dump data into a file'''

import requests

url = 'https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240819T131641Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a6ea56996a450152e26b4698f784095948a9ee2c8448f0d59f22f7b0575185e9'

# send a GET request to the url
response = requests.get(url)

# check if the request was successful
if response.status_code == 200:
    # open a file in write-binary mode
    with open('Popular_Baby_Names.csv', 'wb') as file:
        # write the content of the response to the file
        file.write(response.content)
    print('data saved successfully to Popular_Baby_Names.csv')
else:
    print(f'failed to fetch data. status code {response.status_code}')
