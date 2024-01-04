import unittest
import sys
import logging
from unittest.mock import patch

# Assuming the get_inputs function is in a module named main
from main import get_inputs

class TestGetInputs(unittest.TestCase):
    @patch('sys.argv', ["", "gh_token", "openai_api_key", "", "azure_endpoint"])
    @patch('logging.error')
    def test_get_inputs(self, mock_logging):
        inputs = get_inputs()
        self.assertEqual(inputs["gh_token"], "gh_token")
        self.assertEqual(inputs["openai_api_key"], "openai_api_key")
        self.assertIsNone(inputs["azure_api_key"])
        self.assertEqual(inputs["azure_endpoint"], "azure_endpoint")
        mock_logging.assert_not_called()

    @patch('sys.argv', ["", "", "", "", ""])
    @patch('logging.error')
    def test_get_inputs_no_keys(self, mock_logging):
        with self.assertRaises(SystemExit) as cm:
            get_inputs()
        self.assertEqual(cm.exception.code, 1)
        mock_logging.assert_called_once_with("Both openai_api_key and azure_api_key are empty. Exiting.")

    @patch('sys.argv', ["", "gh_token", "openai_api_key", "azure_api_key", "azure_endpoint"])
    @patch('logging.error')
    def test_get_inputs_both_keys(self, mock_logging):
        with self.assertRaises(SystemExit) as cm:
            get_inputs()
        self.assertEqual(cm.exception.code, 1)
        mock_logging.assert_called_once_with("Both openai_api_key and azure_api_key are set. Exiting.")

if __name__ == '__main__':
    unittest.main()