import unittest
import os

from app import app

from mockupdb import MockupDB, go, Command
from pymongo import MongoClient
#from json import dumps

class GetDataSourceTestCase(unittest.TestCase):

    def test_getDataSource(self):
        # arrange

        future = go(self.app.get, f'/Login-Page/{username}')
        request = self.server.receives(
            Command({'find': 'dataSources', 'filter': {'username': username}, 'limit': 1, 'singleBatch': True}, flags=4, namespace='app'))
        request.ok(cursor={'firstBatch': [
            { "username" : "Subodh", "password" : "sakshi" [ "http://http://0.0.0.0:5000/" ] }]})

        # act
        http_response = future()
        # assert
self.assertIn('http://google.com/rest/api',http_response.get_data(as_text=True))