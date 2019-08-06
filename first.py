import unittest

def mapping(values, param: bool):
    ''' Function by table '''
    assert isinstance(values, list) or values is None, \
            'List or None required, received ' + str(type(values))
    #if param or (values and len(values) > 1):
    if param:
        return values
    # Next for all 'param' is False
    if not values:
        return ['any']
    if 'no' not in values or len(values) > 1:
        return values

class TestMapping(unittest.TestCase):
    def test_result(self):
        self.assertEqual(mapping(['no'], True), ['no'])
        self.assertEqual(mapping(['no'], False), None)
        self.assertEqual(mapping(None, False), ['any'])
        self.assertEqual(mapping(['no', 'phone'], False), ['no', 'phone'])
        self.assertEqual(mapping(['phone'], False), ['phone'])


if __name__ == '__main__':
    unittest.main()
