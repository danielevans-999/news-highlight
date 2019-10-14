

import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('CNN News','A thrilling new Python news',' "https://abcnews.go.com', 'general','en','us','oy')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


