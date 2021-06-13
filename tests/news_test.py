import unittest
from models import sources, articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('abc-news','ABC News','Your trusted source for breaking news, analysis, headlines, and videos at ABCNews.com.','"https://abcnews.go.com','general','en'))

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

class HeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("bbc-news","BBC News","BBC Sport","Eriksen 'awake' after collapsing","Denmark midfielder Christian Eriksen is \"awake\","http://www.bbc.co.uk/sport/footb",""https://ichef.bbci.co.uk/live-experience/cps/624/cpsprodpb/DE8A/production/_118907965_gettyimages-1233415322.jpg","2021-06-12T18:52:26.4082822Z","Denmark midfielder Christian Eriksen is \"awake\" )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

if __name__ == '__main__':
    unittest.main()