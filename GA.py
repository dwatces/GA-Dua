#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
from google.oauth2.service_account import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import json
import requests

app = Flask(__name__)

@app.route('/create-google-analytics-account', methods=['POST'])
def create_googles = data['api_credentials']
    account_name = data['account_name']
    property_name = data['property_name']
    website_url = data['website_url']
    timezone = data['timezone']

    # Build the credentials object from the API credentials
    credentials = Credentials.from_service_account_info(api_credentials)

    # Build the Google Analytics service
    service = build('analytics', 'v3', credentials=credentials)

    try:
        # Create the Google Analytics account
        account = service.management().accountSummaries().insert(body={
            'kind': 'analytics#accountSummary',
            'name': account_name,
            'timezone': timezone
        }).execute()

        # Extract the account ID
        account_id = account['id']

        # Create the Google Analytics property
        property = service.management().webproperties().insert(accountId=account_id, body={
            'kind': 'analytics#webProperty',
            'name': property_name,
            'websiteUrl': we_analytics_account():
    # Parse the JSON data from the request
    data = json.loads(request.data)

    # Extract the API credentials, account name, property name, website URL, and timezone from the JSON data
    api_credentialbsite_url
        }).execute()

        # Extract the property ID
        property_id = property['id']

        # Create the default Google Analytics view
        view = service.management().profiles().insert(accountId=account_id, webPropertyId=property_id, body={
            'kind': 'analytics#profile',
            'name': 'All Website Data'
        }).execute()

        # Extract the view ID
        view_id = view['id']

        # Generate the Duda API URL and access token
        duda_url = 'https://api.duda.co/api/sites/multiscreen/{}/analytics'.format(data['site_id'])
        duda_token = data['duda_token']

        # Build the Duda API request payload
        duda_payload = {
            'type': 'google_analytics',
            'code': 'ga(\'create\', \'{}\'); ga(\'send\', \'pageview\');'.format(property_id)
        }

        # Send the Duda API request
        duda_response = requests.put(duda_url, headers={'Authorization': 'Bearer {}'.format(duda_token)}, json=duda_payload)

        # Check if the Duda API request was successful
        if duda_response.ok:
            # Return the account, property, and view IDs as a JSON response
            return jsonify({'account_id': account_id, 'property_id': property_id, 'view_id': view_id}), 200
        else:
            # Return the Duda API error message as a JSON response
            return jsonify({'error': 'Failed to update Duda website: {}'.format(duda_response.json())}), duda_response.status_code

    except HttpError as error:
        # Handle any errors that occur during the account creation process
        error_details = json.loads(error.content)['error']
        return jsonify({'error': error_details['message']}), error_details['code']

if __name__ == '__main__':
    app.run()

    


# In[ ]:


import requests
import json

# Define the JSON data to send in the HTTP POST request
data = {
    "credentials": {
         "type": "service_account",
          "project_id": "tidy-interface-384121",
          "private_key_id": "527f64c4d3ef0cb487114a2c02ac6f7ec87d8e9e",
          "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC2M+jD2gpagf2P\n3EIUruwa3c5Yrzp2oMgxQmLIw37fikMeps/+8tGDs1Dt13mYuSuwcZjZ4cuIXYM9\nJ8oDsVB/NccmGvpIAe8kmhtxtgutSOQ/kOW9fwIBSY6wd1tu2dxSMtRkMBgGIVbF\nh1r5QeJfJ9KdkrGLYJJK+liFYnMKOuhvZoyTI/OESCIB8/SBv1OQA86AgciSdUUZ\n1pvD+5Qx7zexEJfSokjQfu5fsn4PWxd5JIbn+ygUIkaqp+Q086rSECDw/HyVRodW\n4W9AFxqmsouG5ObyqWUwYSipUCpOb7P6mVOd121eBNICsEx+XM8GxPiC7OZvUZ/a\nBxUAFqP5AgMBAAECggEABK1gtW1inGfvnMquUhZa9oYY4tctuKegN/6Ap294UW/8\n0Nu+pWhxlzBKXK6uPwzK2bLS1g4JMekXokFkGtPpkXhtkjV5VRGipFWF7JV8J4DC\nZjzXnvWUlTigjnhj6xyx3pTSNbez2C1xKy0yOUmXEHMG4bdnMiEipETYsqTgN+QX\n0Lgdf1YwIxgj7Bn6B/mTNSbh+i+/4WrdhqejTNrmh00xq4zNgQ4U9Mf2BwrB1srb\njDYpz+e2pWRGFaCQZOFAAOXUz5s5EKdFf2HhHLgtHwbeUbsuqtSxrEaH7xd0lFar\nPsmh1Xp1CRehpLXDInJ/aj+MyIvfN61hgN8v4w7O8QKBgQD0dHoOVLpkqS4u7ukK\nCpAJPjXb1jdhuerI5YUxGvPjvTrPtWlJBu6x1QDllRHMZkH1vEcqJQU+SJ19BA7t\nvS3v3X3zbzjhJUQVXt30TNBH50pRtG2GlPYR2Y488OZNS92YuVCb70mEskRJ+75R\nKsvy0lahYZLzgtwt6AEXbIG36QKBgQC+zsmJwjd/3NP9Hls4YcBQiveQi7V1j7/P\nExoXmQqFpcNq+F35gmbNJ79EOxeNuQuwfy+378AiRUN5YRx4Bs4smcqK3sBUHA7S\n4AJXAU7fzZRDZLdqaC7YeEnTVg4ejH2DZm5hC20iULGGs2bK7MH5QAUc5KbPQJdt\nOlSLeM8RkQKBgDlLE1BIi2cMP8bAN94im5+O9RCRJGnDKUPsh0r7Bi5aK26DFioH\ndeo4Af3M8l71mH//oK4//vqaCk9CpD0UGbAeOWbUqoAaO9rGYT7gwfAYRVLg9sqU\nHxgP5UZjL5buMQGabUoeyxxOq7KrTe+4GBTRN3ybYdWw1ensdlUHGWABAoGACC2i\n08XATTmw2GOJs2P1Mz6Rl991GqHbrct6zdIgclQFiTs2A/DD6T0v5IPH4aoxxxHc\ngLzE9nMTjktMRhS8l4rL9KHRioldVUqGryX+NHeCSFUzy1rFzz9wop9IoaSR6KTm\nTECKH/NneIeN+1qkgcNttKxUPgPdua/LWeMGtRECgYB3D8MuIjIRRG4h0P848xNe\nyLfEID4D39JpWMZY1spBoqqfG3REqlXmXvl2m3Xmzrne9A7jUtEmPUOu6ugJ0fah\nj34i5dCA3eZPgeEh4uY5RZWr/8xlpzjxbE6TKRweUkjaSgPp4WtbHmolr/1/nQdw\nGKbqgfnSpm6JMyuxJgopUw==\n-----END PRIVATE KEY-----\n",
          "client_email": "test-624@tidy-interface-384121.iam.gserviceaccount.com",
          "client_id": "115704331410859531959",
          "auth_uri": "https://accounts.google.com/o/oauth2/auth",
          "token_uri": "https://oauth2.googleapis.com/token",
          "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
          "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test-624%40tidy-interface-384121.iam.gserviceaccount.com"
    },
    "view_id": account_name,
    "tracking_id": property_name,
}

# Send the HTTP POST request to the Flask app
response = requests.post("http://127.0.0.1:5000/", json=data)

# Print the response from the Flask app
print(response.json())


# In[ ]:




