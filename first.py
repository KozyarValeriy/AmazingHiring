import unittest

def mapping(values, param: bool):
    ''' Function by table '''
    assert isinstance(values, list) or values is None, \
            'List or None required, received ' + str(type(values))
    if param:
        return values
    # Next for all 'param' is False
    if not values:
        return ['any']
    for value in values:
        if value != 'no':
            return values

class TestMapping(unittest.TestCase):
    def test_result(self):
        self.assertEqual(mapping(['no'], True), ['no'])
        self.assertEqual(mapping(['no'], False), None)
        self.assertEqual(mapping(None, False), ['any'])
        self.assertEqual(mapping(['no', 'phone'], False), ['no', 'phone'])

if __name__ == '__main__':
    unittest.main()