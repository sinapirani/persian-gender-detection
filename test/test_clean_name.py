import unittest
from persian_gender_detection.persian_gender_detection import clean_name


class TestCleanName(unittest.TestCase):
    def test_farsi_word(self):
        self.assertEqual(clean_name('   علی '), 'علی')
        self.assertEqual(clean_name('هــــادی'), 'هادی')
        self.assertEqual(clean_name('محمد   رضا'), 'محمدرضا')
        self.assertEqual(clean_name('احسا   ن'), 'احسان')
        self.assertEqual(clean_name('كامران'), 'کامران')
        self.assertEqual(clean_name('  پیمـــان  '), 'پیمان')
        self.assertEqual(clean_name('  مهـدی  '), 'مهدی')
        self.assertEqual(clean_name('حســ😎ــن'), 'حسن')
        self.assertEqual(clean_name('۱۲۳۹۹۳محمدعلی123'), 'محمدعلی')
        self.assertEqual(clean_name('<<محمد>>'), 'محمد')

    def test_english_word(self):
        self.assertEqual(clean_name('Ali'), 'ali')
        self.assertEqual(clean_name('    J  ohn '), 'john')
        self.assertEqual(clean_name('Pey😎man'), 'peyman')
        self.assertEqual(clean_name('12345Pey44man555'), 'peyman')
        self.assertEqual(clean_name('<<pey44man>>'), 'peyman')
        self.assertEqual(clean_name('<<pey44man>'), 'peyman')
        self.assertEqual(clean_name('<<pey44man>'), 'peyman')
        self.assertEqual(clean_name('<<me44h785di>'), 'mehdi')



if __name__=='__main__':
  unittest.main()
