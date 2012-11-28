from url import URL
import unittest

class TestValidatorAndCanonicalizer(unittest.TestCase):

    def test_validURLs(self):
        self.assertTrue(URL("http://example.com/").isValid())
        self.assertTrue(URL("http://example.com/?q=%C3%871").isValid())
        self.assertTrue(URL("http://example.com/?q=%E2%85%A0").isValid())
        self.assertTrue(URL("http://example.com/?q=%5C").isValid())
        self.assertTrue(URL("http://example.com/~jane").isValid())
        self.assertTrue(URL("http://example.com/a/b").isValid())
        self.assertTrue(URL("http://example.com:8080/").isValid())
        self.assertTrue(URL("http://user:password@example.com/").isValid())
        self.assertTrue(URL("ftp://ftp.is.co.za/rfc/rfc1808.txt").isValid())
        self.assertTrue(URL("http://www.ietf.org/rfc/rfc2396.txt").isValid())
        self.assertTrue(URL("ldap://[2001:db8::7]/c=GB?objectClass?one").isValid())
        self.assertTrue(URL("mailto:John.Doe@example.com").isValid())
        self.assertTrue(URL("news:comp.infosystems.www.servers.unix").isValid())
        self.assertTrue(URL("tel:+1-816-555-1212").isValid())
        self.assertTrue(URL("telnet://192.0.2.16:80/").isValid())
        self.assertTrue(URL("urn:oasis:names:specification:docbook:dtd:xml:4.1.2").isValid())
        self.assertTrue(URL("http://127.0.0.1/").isValid())
        self.assertTrue(URL("http://www.w3.org/2000/01/rdf-schema#").isValid())
    
    def test_invalidURLs(self):
        self.assertFalse(URL("http://:@example.com/").isValid())
        self.assertFalse(URL("http://@example.com/").isValid())
        self.assertFalse(URL("http://example.com").isValid())
        self.assertFalse(URL("HTTP://example.com/").isValid())
        self.assertFalse(URL("http://EXAMPLE.COM/").isValid())
        self.assertFalse(URL("http://example.com/%7Ejane").isValid())
        self.assertFalse(URL("http://example.com/?q=%C7").isValid())
        self.assertFalse(URL("http://example.com/?q=%5c").isValid())
        self.assertFalse(URL("http://example.com/?q=C%CC%A7").isValid())
        self.assertFalse(URL("http://example.com/a/../a/b").isValid())
        self.assertFalse(URL("http://example.com/a/./b").isValid())
        self.assertFalse(URL("http://example.com:80/").isValid())
        self.assertFalse(URL("http://127.0.0.1:80/").isValid())
        self.assertFalse(URL("http://example.com:081/").isValid())

    def test_canonicalFormForValidURLs(self):
        alreadyCanonicalForm = ["http://example.com/", 
                               "http://example.com/?q=%C3%871",
                               "http://example.com/?q=%E2%85%A0",
                               "http://example.com/?q=%5C",
                               "http://example.com/~jane",
                               "http://example.com/a/b",
                               "http://example.com:8080/",
                               "http://user:password@example.com/",
                               "ftp://ftp.is.co.za/rfc/rfc1808.txt",
                               "http://www.ietf.org/rfc/rfc2396.txt"]
        self.assertEqual(URL(alreadyCanonicalForm[0]).normalized, alreadyCanonicalForm[0])
        self.assertEqual(URL(alreadyCanonicalForm[1]).normalized, alreadyCanonicalForm[1])
        self.assertEqual(URL(alreadyCanonicalForm[2]).normalized, alreadyCanonicalForm[2])
        self.assertEqual(URL(alreadyCanonicalForm[3]).normalized, alreadyCanonicalForm[3])
        self.assertEqual(URL(alreadyCanonicalForm[4]).normalized, alreadyCanonicalForm[4])
        self.assertEqual(URL(alreadyCanonicalForm[5]).normalized, alreadyCanonicalForm[5])
        self.assertEqual(URL(alreadyCanonicalForm[6]).normalized, alreadyCanonicalForm[6])
        self.assertEqual(URL(alreadyCanonicalForm[7]).normalized, alreadyCanonicalForm[7])
        self.assertEqual(URL(alreadyCanonicalForm[8]).normalized, alreadyCanonicalForm[8])
        self.assertEqual(URL(alreadyCanonicalForm[9]).normalized, alreadyCanonicalForm[9])

    def test_canonicalForForInvalidURLs(self):
        invalidURLs = ["http://:@example.com/",
                       "http://@example.com/",
                       "http://example.com",
                       "HTTP://example.com/",
                       "http://EXAMPLE.COM/",
                       "http://example.com/%7Ejane",
                       "http://example.com/?q=%C7",
                       "http://example.com/?q=%5c",
                       "http://example.com/?q=C%CC%A7",
                       "http://example.com/a/../a/b",
                       "http://example.com/a/./b",
                       "http://example.com:80/",
                       "http://127.0.0.1:80/",
                       "http://example.com:081/"]
        canonicalizedURLs = ["http://example.com/",
                            "http://example.com/",
                            "http://example.com/",
                            "http://example.com/",
                            "http://example.com/",
                            "http://example.com/~jane",
                            "http://example.com/?q=%EF%BF%BD",
                            "http://example.com/?q=%5C",
                            "http://example.com/?q=%C3%87",
                            "http://example.com/a/b",
                            "http://example.com/a/b",
                            "http://example.com/",
                            "http://127.0.0.1/",
                            "http://example.com:81/"]
        self.assertEqual(URL(invalidURLs[0]).normalized, canonicalizedURLs[0])
        self.assertEqual(URL(invalidURLs[1]).normalized, canonicalizedURLs[1])
        self.assertEqual(URL(invalidURLs[2]).normalized, canonicalizedURLs[2])
        self.assertEqual(URL(invalidURLs[3]).normalized, canonicalizedURLs[3])
        self.assertEqual(URL(invalidURLs[4]).normalized, canonicalizedURLs[4])
        self.assertEqual(URL(invalidURLs[5]).normalized, canonicalizedURLs[5])
        self.assertEqual(URL(invalidURLs[6]).normalized, canonicalizedURLs[6])
        self.assertEqual(URL(invalidURLs[7]).normalized, canonicalizedURLs[7])
        self.assertEqual(URL(invalidURLs[8]).normalized, canonicalizedURLs[8])
        self.assertEqual(URL(invalidURLs[9]).normalized, canonicalizedURLs[9])
        self.assertEqual(URL(invalidURLs[10]).normalized, canonicalizedURLs[10])
        self.assertEqual(URL(invalidURLs[11]).normalized, canonicalizedURLs[11])
        self.assertEqual(URL(invalidURLs[12]).normalized, canonicalizedURLs[12])
        self.assertEqual(URL(invalidURLs[13]).normalized, canonicalizedURLs[13])

    def test_comparators(self):
        urls = ["http://:@example.com/",
                       "http://@example.com/",
                       "http://example.com",
                       "HTTP://example.com/",
                       "http://EXAMPLE.COM/",
                       "http://example.com/%7Ejane",
                       "http://example.com/?q=%C7",
                       "http://example.com/?q=%5c",
                       "http://example.com/?q=C%CC%A7",
                       "http://example.com/a/../a/b",
                       "http://example.com/a/./b",
                       "http://example.com:80/",
                       "http://127.0.0.1:80/",
                       "http://example.com:081/"]

        self.assertEqual(URL(urls[0]).normalized, URL(urls[1]).normalized)
        self.assertEqual(URL(urls[1]).normalized, URL(urls[2]).normalized)
        self.assertEqual(URL(urls[2]).normalized, URL(urls[3]).normalized)
        self.assertEqual(URL(urls[3]).normalized, URL(urls[0]).normalized)

        self.assertGreater(URL(urls[13]).normalized, URL(urls[2]).normalized)
        self.assertGreater(URL(urls[9]).normalized, URL(urls[7]).normalized)
        self.assertGreater(URL(urls[5]).normalized, URL(urls[8]).normalized)
        self.assertGreater(URL(urls[13]).normalized, URL(urls[0]).normalized)

        self.assertLess(URL(urls[12]).normalized, URL(urls[1]).normalized)
        self.assertLess(URL(urls[7]).normalized, URL(urls[9]).normalized)
        self.assertLess(URL(urls[7]).normalized, URL(urls[6]).normalized)
        self.assertLess(URL(urls[8]).normalized, URL(urls[5]).normalized)

if __name__ == '__main__':
    unittest.main()
