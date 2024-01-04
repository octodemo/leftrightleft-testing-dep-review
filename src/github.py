import requests
import logging

class Client:
    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        }

    def get_diff(self, compare_url):
        response = requests.get(compare_url, headers=self.headers)
        if response.status_code == 200:
            logging.info("Successfully retrieved diff")
            return response.text
        else:
            e = f"Error retrieving diff.  Response: {response.json()}"
            logging.error(e)
            raise Exception(e)
        
    def add_comment(self, comment_url, comment):
        data = {"body": comment}
        response = requests.post(comment_url, headers=self.headers, json=data)
        if response.status_code == 201:
            logging.info("Successfully added comment")
        else:
            e = f"Error adding comment. Response: {response.json()}"
            logging.error(e)
            raise Exception(e)