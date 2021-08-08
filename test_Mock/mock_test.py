from unittest import mock
import unittest
import requests
from requests import status_codes
from .my_test import call_twitter,get_ip

class TestApi(unittest.TestCase):

    @mock.patch('test_Mock.my_test.get_data',return_value ='data_test')
    def test_api(self,twit):
        self.assertEqual(call_twitter(),'data_test')
    
    @mock.patch('test_Mock.my_test.requests.get')
    def test_get_api(self,mock_get):
        mock_get.return_value = mock.Mock(name='mock test',**{"status_code":200,"json.return_value":{"origin":"0.0.0.0"}})

        result = get_ip()

        self.assertEqual(result,"0.0.0.0")

        mock_get.assert_called_once_with("http://httpbin.org/ip")
        

       


        
        

        



