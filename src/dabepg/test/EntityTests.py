import unittest

from dabepg import ContentId, Crid

class ContentIdTests(unittest.TestCase):

    def test_parse_contentid_1(self):
        id = ContentId.fromstring('e1.ce15.c221.0.1')
        assert id.ecc == 0xe1
        assert id.eid == 0xce15
        assert id.sid == 0xc221
        assert id.scids == 0x0
        
    def test_parse_contentid_2(self):
        id = ContentId.fromstring('e1.c586')
        assert id.ecc == 0xe1
        assert id.eid == 0xc586   

class CridTests(unittest.TestCase):
    
    def test_parse_crid_1(self):
        crid = Crid.fromstring("crid://example.com/data;id=1")
        assert crid.authority == 'example.com'
        assert crid.data == 'data;id=1'

if __name__ == "__main__":
    unittest.main()