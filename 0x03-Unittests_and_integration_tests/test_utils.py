#!/usr/bin/env python3
'''Task 0's module.
'''
import unittest
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''Tests access_nested_map.
    '''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple, expected: Union[int, str]):
        '''Tests access_nested_map.
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({'a': 1}, ('b',)),
        ({'a': {'b': 2}}, ('a', 'c')),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple):
        '''Tests access_nested_map.
        '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
    

class TestGetJson(unittest.TestCase):
    '''Tests get_json.
    '''
    @parameterized.expand([
        ('http://example.com', {'payload': 5}),
        ('http://holberton.io', {'payload': True}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get: Mock):
        '''Tests get_json.
        '''
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''Tests memoize.
    '''
    def test_memoize(self):
        '''Tests memoize.
        '''
        class TestClass:
            '''A TestClass.
            '''
            def a_method(self):
                '''A method.
                '''
                return 42

            @memoize
            def a_property(self):
                '''A property.
                '''
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock_method.assert_called_once()
            self.assertEqual(test_class.a_property, 42)
