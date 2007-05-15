"""
unit tests for module textutils
squeleton generated by /home/syt/cvs_work/logilab/pyreverse/py2tests.py on Sep 08 at 09:1:31

"""
import re
from os import linesep

from logilab.common import textutils as tu # .textutils import *
from logilab.common.testlib import TestCase, DocTest, unittest_main


if linesep != '\n':
    import re
    LINE_RGX = re.compile(linesep)
    def ulines(string):
        return LINE_RGX.sub('\n', string)
else:
    def ulines(string):
        return string

class NormalizeTextTC(TestCase):

    def test_known_values(self):
        self.assertEquals(ulines(tu.normalize_text('''some really malformated
        text.
With some times some veeeeeeeeeeeeeeerrrrryyyyyyyyyyyyyyyyyyy loooooooooooooooooooooong linnnnnnnnnnnes

and empty lines!
        ''')),
                         '''some really malformated text. With some times some
veeeeeeeeeeeeeeerrrrryyyyyyyyyyyyyyyyyyy loooooooooooooooooooooong
linnnnnnnnnnnes

and empty lines!''')
        self.assertTextEquals(ulines(tu.normalize_text('''\
some ReST formated text
=======================
With some times some veeeeeeeeeeeeeeerrrrryyyyyyyyyyyyyyyyyyy loooooooooooooooooooooong linnnnnnnnnnnes
and normal lines!

another paragraph
        ''', rest=True)),
                         '''\
some ReST formated text
=======================
With some times some veeeeeeeeeeeeeeerrrrryyyyyyyyyyyyyyyyyyy
loooooooooooooooooooooong linnnnnnnnnnnes
and normal lines!

another paragraph''')

    def test_nonregr_unsplitable_word(self):
        self.assertEquals(ulines(tu.normalize_text('''petit complement :

http://www.plonefr.net/blog/archive/2005/10/30/tester-la-future-infrastructure-i18n
''', 80)),
                         '''petit complement :

http://www.plonefr.net/blog/archive/2005/10/30/tester-la-future-infrastructure-i18n''')


    def test_nonregr_rest_normalize(self):
        self.assertEquals(ulines(tu.normalize_text("""... xx xxx xxxx xxxxxxx xxx xxxx xx xxxxx xxxx xxxx xx xxxxxx-xxxxx xx xxx xx xxxxx xxxxxxxx xxxx xxx xxxxxx xx x'xxx xxxxx xx xxxxxxxxxx.


**xxxx**: xx xxxx xx xxxxx, xxx xxxxxx x'xxxxxx, xx xxxx xx yy xxxxx xx xxxxx x'xxx xx xxx xx xxxx xxxx y xxx xxxxx.

**xxx**: xxx xxxxx x  xxxx, xx xxx xx xxxxx xxxx-xxxx xx xxxxxxxx xxxxx xxyxyy.

**xxxxxx**: x'x xx xxxxxx x  xxxxx

**xxx**: xxxxyy xx xxxxx

**xxxxx**: xxxxxxxx xxxxyy xxx xxxxx xx xxxx xx yy xxxxxxxx xx xxxx xxxxxx xx xxxxx xxxxxx y xxxxxxx

**xxxx**: xxxxxxx xxx xxxxxxx, xxxxx xxx xxxxxxx xxxxxxxxxxxxxx, xxxxxxx xxx xxxxx xx xxxxxx xx xxxx xxx xxx xxxxxxxx x  xxxxx xx xxxxxxxx xxxxxx.


**xxxxx**: xxxxyy xxxxx xx xxxxxxxx xx x'x xxxxxx x'xxxxxx

**xxxxx**: xxxxxxxx xxxxyy xxxxxxx xxxxxxx xxxxx'x  xxxxx xxxxxxxx.

**xxxx**: xx xxxxxxxx (xxxx xxxxyy xxxx xxxxxxxx xx xx xxxxxx xx x'xxxx xx xxxx xxx xxxxxx x'xxxxx xxx) xx xxxx xx xxxxx x'xx xxxxxxx xx xxxx xxxxxx x  xxxxxx xx xx xx'xx x xxxx  (xxxxxxxxx xxx xxxxxxx, xxxxxxxx xx xxxxx xxxx xx xx xxxxx xxxxx xx xxxxxxxx, xxx.).

**xxx**: xxxxx, xxxxxxxxxxx, xxxxxxx xx xxxx, xxxxxxxx

**xxx**: xx xxxx xxxx xxx x  xxxxxxx xx xxxxx xxxx xxxxxxxxxxx xxxxxx xxxx xx xxxx xx xxx xx xxxxx xxx xxx xxxxx
        """, rest=True)), """... xx xxx xxxx xxxxxxx xxx xxxx xx xxxxx xxxx xxxx xx xxxxxx-xxxxx xx xxx xx
xxxxx xxxxxxxx xxxx xxx xxxxxx xx x'xxx xxxxx xx xxxxxxxxxx.

**xxxx**: xx xxxx xx xxxxx, xxx xxxxxx x'xxxxxx, xx xxxx xx yy xxxxx xx xxxxx
x'xxx xx xxx xx xxxx xxxx y xxx xxxxx.

**xxx**: xxx xxxxx x xxxx, xx xxx xx xxxxx xxxx-xxxx xx xxxxxxxx xxxxx xxyxyy.

**xxxxxx**: x'x xx xxxxxx x xxxxx

**xxx**: xxxxyy xx xxxxx

**xxxxx**: xxxxxxxx xxxxyy xxx xxxxx xx xxxx xx yy xxxxxxxx xx xxxx xxxxxx xx
xxxxx xxxxxx y xxxxxxx

**xxxx**: xxxxxxx xxx xxxxxxx, xxxxx xxx xxxxxxx xxxxxxxxxxxxxx, xxxxxxx xxx
xxxxx xx xxxxxx xx xxxx xxx xxx xxxxxxxx x xxxxx xx xxxxxxxx xxxxxx.

**xxxxx**: xxxxyy xxxxx xx xxxxxxxx xx x'x xxxxxx x'xxxxxx

**xxxxx**: xxxxxxxx xxxxyy xxxxxxx xxxxxxx xxxxx'x xxxxx xxxxxxxx.

**xxxx**: xx xxxxxxxx (xxxx xxxxyy xxxx xxxxxxxx xx xx xxxxxx xx x'xxxx xx xxxx
xxx xxxxxx x'xxxxx xxx) xx xxxx xx xxxxx x'xx xxxxxxx xx xxxx xxxxxx x xxxxxx xx
xx xx'xx x xxxx (xxxxxxxxx xxx xxxxxxx, xxxxxxxx xx xxxxx xxxx xx xx xxxxx xxxxx
xx xxxxxxxx, xxx.).

**xxx**: xxxxx, xxxxxxxxxxx, xxxxxxx xx xxxx, xxxxxxxx

**xxx**: xx xxxx xxxx xxx x xxxxxxx xx xxxxx xxxx xxxxxxxxxxx xxxxxx xxxx xx
xxxx xx xxx xx xxxxx xxx xxx xxxxx""")

    def test_normalize_rest_paragraph(self):
        self.assertEquals(ulines(tu.normalize_rest_paragraph("""**xxxx**: xx xxxxxxxx (xxxx xxxxyy xxxx xxxxxxxx xx xx xxxxxx xx x'xxxx xx xxxx
xxx xxxxxx x'xxxxx xxx) xx xxxx xx xxxxx x'xx xxxxxxx xx xxxx xxxxxx x xxxxxx xx xx xx'xx x xxxx (xxxxxxxxx xxx xxxxxxx, xxxxxxxx xx xxxxx xxxx xx xx xxxxx xxxxx xx xxxxxxxx, xxx.).""")),
                          """**xxxx**: xx xxxxxxxx (xxxx xxxxyy xxxx xxxxxxxx xx xx xxxxxx xx x'xxxx xx xxxx
xxx xxxxxx x'xxxxx xxx) xx xxxx xx xxxxx x'xx xxxxxxx xx xxxx xxxxxx x xxxxxx xx
xx xx'xx x xxxx (xxxxxxxxx xxx xxxxxxx, xxxxxxxx xx xxxxx xxxx xx xx xxxxx xxxxx
xx xxxxxxxx, xxx.).""")

    def test_normalize_rest_paragraph(self):
        self.assertEquals(ulines(tu.normalize_rest_paragraph("""**xxx**: xx xxxx xxxx xxx x xxxxxxx xx xxxxx xxxx xxxxxxxxxxx xxxxxx xxxx xx xxxx xx xxx xx xxxxx xxx xxx xxxxx""")),
                              """**xxx**: xx xxxx xxxx xxx x xxxxxxx xx xxxxx xxxx xxxxxxxxxxx xxxxxx xxxx xx\nxxxx xx xxx xx xxxxx xxx xxx xxxxx""")

        
class NormalizeParagraphTC(TestCase):

    def test_known_values(self):
        self.assertEquals(ulines(tu.normalize_text("""This package contains test files shared by the logilab-common package. It isn't
necessary to install this package unless you want to execute or look at
the tests.""", indent=' ', line_len=70)),
                         """\
 This package contains test files shared by the logilab-common
 package. It isn't necessary to install this package unless you want
 to execute or look at the tests.""")

        
class GetCsvTC(TestCase):

    def test_known(self):
        self.assertEquals(tu.get_csv('a, b,c '), ['a', 'b', 'c'])

    
RGX = re.compile('abcd')
class PrettyMatchTC(TestCase):

    def test_known(self):
        string = 'hiuherabcdef'
        self.assertEquals(ulines(tu.pretty_match(RGX.search(string), string)),
                         'hiuherabcdef\n      ^^^^')
    def test_known_values_1(self):
        rgx = re.compile('(to*)')
        string = 'toto'
        match = rgx.search(string)
        self.assertEquals(ulines(tu.pretty_match(match, string)), '''toto
^^''')
        
    def test_known_values_2(self):
        rgx = re.compile('(to*)')
        string = ''' ... ... to to
 ... ... '''
        match = rgx.search(string)
        self.assertEquals(ulines(tu.pretty_match(match, string)), ''' ... ... to to
         ^^
 ... ...''')
        
        

class UnquoteTC(TestCase):
    def test(self):
        self.assertEquals(tu.unquote('"toto"'), 'toto')
        self.assertEquals(tu.unquote("'l'inenarrable toto'"), "l'inenarrable toto")
        self.assertEquals(tu.unquote("no quote"), "no quote")

        
class ColorizeAnsiTC(TestCase):
    def test_known(self):
        self.assertEquals(tu.colorize_ansi('hello', 'blue', 'strike'), '\x1b[9;34mhello\x1b[0m')
        self.assertEquals(tu.colorize_ansi('hello', style='strike, inverse'), '\x1b[9;7mhello\x1b[0m')
        self.assertEquals(tu.colorize_ansi('hello', None, None), 'hello')
        self.assertEquals(tu.colorize_ansi('hello', '', ''), 'hello')
    def test_raise(self):
        self.assertRaises(KeyError, tu.colorize_ansi, 'hello', 'bleu', None)
        self.assertRaises(KeyError, tu.colorize_ansi, 'hello', None, 'italique')


class ModuleDocTest(DocTest):
    """test doc test in this module"""
    module = tu
    # from logilab.common import textutils as module
del DocTest # necessary if we don't want it to be executed (we don't...)
        
if __name__ == '__main__':
    unittest_main()
