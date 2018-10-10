import unittest
import os
import json
from app import create_app, db

class BucketlistTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name='testing')
