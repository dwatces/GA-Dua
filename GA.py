#!/usr/bin/env python





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

    




