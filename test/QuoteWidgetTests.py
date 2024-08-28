import unittest
from unittest.mock import patch
import requests
import sys
import os
"""
Name: QuoteWidgetTests.py
Descrptions: Verifies the Quote Widget methods are properly communicating with API calls
Verifies: getQuote happy, alternative, and error paths
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))) 
from QuoteWidget import QuotesWidget 

class TestQuotesAPI(unittest.TestCase):
    def setUp(self):
        self.zen_quotes_api = QuotesWidget()
    
    #Happy Path 
    @patch('requests.get')
    def test_get_quote_success(self, mock_get):
        mock_response = {
            "json.return_value": [
                {
                    "q": "MockQuote",
                    "a": "MockPerson"
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response['json.return_value']
        
        quote = self.zen_quotes_api.get_quote()
        self.assertEqual(quote, "\"MockQuote\" - MockPerson")

    #Alternative Path
    @patch('requests.get')
    def test_get_quote_no_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = []
        quote = self.zen_quotes_api.get_quote()
        self.assertEqual(quote, "No quote found.")

    #Error Path, given network error
    @patch('requests.get')
    def test_get_quote_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        quote = self.zen_quotes_api.get_quote()
        self.assertTrue(quote.startswith("Error fetching quote: Network error"))

if __name__ == '__main__':
    unittest.main()
