#!/usr/bin/env python3
'''Task 4's module.
'''
from typing import Dict
import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from requests import HTTPError
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''Tests GithubOrgClient.
    '''
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, test_org: str, mock_get_json: Mock):
        '''Tests GithubOrgClient.org.
        '''
        test_url = f'https://api.github.com/orgs/{test_org}'
        test_payload = {'payload': True}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(test_org)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(test_url)

    def test_public_repos_url(self):
        '''Tests GithubOrgClient._public_repos_url.
        '''
        test_org = 'google'
        test_url = f'https://api.github.com/orgs/{test_org}/repos'
        client = GithubOrgClient(test_org)
        self.assertEqual(client._public_repos_url, test_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock):
        '''Tests GithubOrgClient.public_repos.
        '''
        test_org = 'google'
        test_payload = {'payload': True}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(test_org)
        self.assertEqual(client.public_repos(), test_payload)
        mock_get_json.assert_called_once_with(client._public_repos_url)

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos_with_property(self, test_org: str, mock_get_json: Mock, mock_public_repos_url: Mock):
        '''Tests GithubOrgClient.public_repos.
        '''
        test_payload = {'payload': True}
        mock_get_json.return_value = test_payload
        mock_public_repos_url.return_value = 'https://api.github.com/orgs/google/repos'
        client = GithubOrgClient(test_org)
        self.assertEqual(client.public_repos(), test_payload)
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/google/repos')

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_has_license(self, test_org: str, mock_get_json: Mock):
        '''Tests GithubOrgClient.has_license.
        '''
        test_payload = [{'license': {'key': 'key'}}]
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(test_org)
        self.assertTrue(client.has_license('key'))
        mock_get_json.assert_called_once_with(client._public_repos_url)


@parameterized_class([
    {'payload': TEST_PAYLOAD, 'license_key': 'mit', 'expected': True},
    {'payload': TEST_PAYLOAD, 'license_key': 'bsd-3-clause', 'expected': False},
    {'payload': [], 'license_key': 'mit', 'expected': False},
])

class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Tests GithubOrgClient.
    '''
    @classmethod
    def setUpClass(cls):
        '''Sets up the class.
        '''
        cls.get_patcher = patch('client.get_json', return_value=cls.payload)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''Tears down the class.
        '''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''Tests GithubOrgClient.public_repos.
        '''
        test_org = 'google'
        client = GithubOrgClient(test_org)
        self.assertEqual(client.public_repos(), self.payload)

    def test_has_license(self):
        '''Tests GithubOrgClient.has_license.
        '''
        test_org = 'google'
        client = GithubOrgClient(test_org)
        self.assertEqual(client.has_license(self.license_key), self.expected)

    def test_public_repos_with_license(self):
        '''Tests GithubOrgClient.public_repos_with_license.
        '''
        test_org = 'google'
        client = GithubOrgClient(test_org)
        self.assertEqual(client.public_repos_with_license(self.license_key), self.payload)
