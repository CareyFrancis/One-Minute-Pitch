import unittest
from app.models import Pitch

class NewsTest(unittest.TestCase):
        '''
        Test class to test the behavior of the news source class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_pitch = Pitch(1, 1,'my pitch', 'motivational','business', 'technology', 0, 0)

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_pitch, Pitch))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_pitch.id, 1)
            self.assertEquals(self.new_pitch.owner_id, 1)
            self.assertEquals(self.new_pitch.description, 'my pitch')
            self.assertEquals(self.new_pitch.title, 'motivational')
            self.assertEquals(self.new_pitch.category, 'business')
            self.assertEquals(self.new_pitch.comments, 'technology')
            self.assertEquals(self.new_pitch.upvotes, 0)
            self.assertEquals(self.new_pitch.downvotes, 0)




if __name__ == '__main__':
    unittest.main()