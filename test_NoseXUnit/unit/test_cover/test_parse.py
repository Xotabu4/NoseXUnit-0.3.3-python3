#-*- coding: utf-8 -*-
import test_NoseXUnit

import nosexunit.cover as cover

class TestParse(test_NoseXUnit.TestCase):
    
    def test_1(self):
        content = """Name    Stmts   Exec  Cover   Missing
-------------------------------------
foo         4      3    75%   5
"""
        sources = cover.parse(content)
        self.assertEqual(1, len(sources))
        source = sources[0]
        self.assertEqual('foo', source.full())
        self.assertEqual(4, source.all())
        self.assertEqual(3, source.exe())
        self.assertEqual(75.0, source.percent())
        self.assertEqual(75.0, sources.percent())

    def test_2(self):
        content = """Name    Stmts   Exec  Cover   Missing
-------------------------------------
foo_1       4      3    75%   5
foo_2       2      1    50%   3
-------------------------------------
TOTAL       6      4    66%   
"""
        sources = cover.parse(content)
        self.assertEqual(2, len(sources))
        self.assertEqual('66.667', '%.3f' % sources.percent())
        
if __name__=="__main__":
    test_NoseXUnit.main()
