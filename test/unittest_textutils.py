# -*- coding: utf-8 -*-
# copyright 2003-2010 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of logilab-common.
#
# logilab-common is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option) any
# later version.
#
# logilab-common is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with logilab-common.  If not, see <http://www.gnu.org/licenses/>.
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
        self.assertEquals(ulines(tu.normalize_text("""... Il est donc evident que tout le monde doit lire le compte-rendu de RSH et aller discuter avec les autres si c'est utile ou necessaire.
        """, rest=True)), """... Il est donc evident que tout le monde doit lire le compte-rendu de RSH et
aller discuter avec les autres si c'est utile ou necessaire.""")

    def test_normalize_rest_paragraph(self):
        self.assertEquals(ulines(tu.normalize_rest_paragraph("""**nico**: toto""")),
                          """**nico**: toto""")

    def test_normalize_rest_paragraph2(self):
        self.assertEquals(ulines(tu.normalize_rest_paragraph(""".. _tdm: http://www.editions-eni.fr/Livres/Python-Les-fondamentaux-du-langage---La-programmation-pour-les-scientifiques-Table-des-matieres/.20_adaa41fb-c125-4919-aece-049601e81c8e_0_0.pdf
.. _extrait: http://www.editions-eni.fr/Livres/Python-Les-fondamentaux-du-langage---La-programmation-pour-les-scientifiques-Extrait-du-livre/.20_d6eed0be-0d36-4384-be59-2dd09e081012_0_0.pdf""", indent='> ')),
                          """> .. _tdm:
> http://www.editions-eni.fr/Livres/Python-Les-fondamentaux-du-langage---La-programmation-pour-les-scientifiques-Table-des-matieres/.20_adaa41fb-c125-4919-aece-049601e81c8e_0_0.pdf
> .. _extrait:
> http://www.editions-eni.fr/Livres/Python-Les-fondamentaux-du-langage---La-programmation-pour-les-scientifiques-Extrait-du-livre/.20_d6eed0be-0d36-4384-be59-2dd09e081012_0_0.pdf""")

    def test_normalize_paragraph2(self):
        self.assertEquals(ulines(tu.normalize_paragraph(""".. _tdm: http://www.editions-eni.fr/Livres/Python-Les-fondamentaux-du-langage---La-programmation-pour-les-scientifiques-Table-des-matieres/.20_adaa41fb-c125-4919-aece-049601e81c8e_0_0.pdf
.. _extrait: http://www.editions-eni.fr/Livres/Python-Les-fondamentaux-du-langage---La-programmation-pour-les-scientifiques-Extrait-du-livre/.20_d6eed0be-0d36-4384-be59-2dd09e081012_0_0.pdf""", indent='> ')),
                          """> .. _tdm:
> http://www.editions-eni.fr/Livres/Python-Les-fondamentaux-du-langage---La-programmation-pour-les-scientifiques-Table-des-matieres/.20_adaa41fb-c125-4919-aece-049601e81c8e_0_0.pdf
> .. _extrait:
> http://www.editions-eni.fr/Livres/Python-Les-fondamentaux-du-langage---La-programmation-pour-les-scientifiques-Extrait-du-livre/.20_d6eed0be-0d36-4384-be59-2dd09e081012_0_0.pdf""")

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
        self.assertEquals(tu.splitstrip('a, b,c '), ['a', 'b', 'c'])

class UnitsTC(TestCase):

    def setUp(self):
        self.units = {
            'm':60,
            'kb':1024,
            'mb':1024*1024,
            }

    def test_empty_base(self):
        self.assertEquals(tu.apply_units('17', {}), 17)

    def test_empty_inter(self):
        def inter(value):
            return int(float(value)) * 2
        result = tu.apply_units('12.4', {}, inter=inter)
        self.assertEquals(result, 12 * 2)
        self.assertIsInstance(result, float)

    def test_empty_final(self):
        # int('12.4') raise value error
        self.assertRaises(ValueError, tu.apply_units,'12.4', {}, final=int)

    def test_empty_inter_final(self):
        result = tu.apply_units('12.4', {}, inter=float,final=int)
        self.assertEquals(result, 12)
        self.assertIsInstance(result, int)

    def test_blank_base(self):
        result = tu.apply_units(' 42  ', {}, final=int)
        self.assertEquals(result, 42)

    def test_blank_space(self):
        result = tu.apply_units(' 1 337 ', {}, final=int)
        self.assertEquals(result, 1337)

    def test_blank_coma(self):
        result = tu.apply_units(' 4,298.42 ', {})
        self.assertEquals(result, 4298.42)

    def test_blank_mixed(self):
        result = tu.apply_units('45, 317, 337', {},final=int)
        self.assertEquals(result, 45317337)

    def test_unit_singleunit_singleletter(self):
        result = tu.apply_units('15m', self.units)
        self.assertEquals(result, 15 * self.units['m'] )

    def test_unit_singleunit_multipleletter(self):
        result = tu.apply_units('47KB', self.units)
        self.assertEquals(result, 47 * self.units['kb'] )

    def test_unit_singleunit_caseinsensitive(self):
        result = tu.apply_units('47kb', self.units)
        self.assertEquals(result, 47 * self.units['kb'] )

    def test_unit_multipleunit(self):
        result = tu.apply_units('47KB 1.5MB', self.units)
        self.assertEquals(result, 47 * self.units['kb'] + 1.5 * self.units['mb'])

    def test_unit_with_blank(self):
        result = tu.apply_units('1 000 KB', self.units)
        self.assertEquals(result, 1000 * self.units['kb'])

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


class UnormalizeTC(TestCase):
    def test_unormalize(self):
        data = [(u'\u0153nologie', u'oenologie'),
                (u'\u0152nologie', u'OEnologie'),
                (u'l\xf8to', u'loto'),
                (u'été', u'ete'),
                (u'àèùéïîôêç', u'aeueiioec'),
                (u'ÀÈÙÉÏÎÔÊÇ', u'AEUEIIOEC'),
                (u'\xa0', u' '), # NO-BREAK SPACE managed by NFKD decomposition
               ]
        for input, output in data:
            yield self.assertEqual, tu.unormalize(input), output
        self.assertRaises(ValueError, tu.unormalize, u"non ascii char is \u0154",
                          ignorenonascii=False)


class ModuleDocTest(DocTest):
    """test doc test in this module"""
    module = tu
    # from logilab.common import textutils as module
del DocTest # necessary if we don't want it to be executed (we don't...)

if __name__ == '__main__':
    unittest_main()
