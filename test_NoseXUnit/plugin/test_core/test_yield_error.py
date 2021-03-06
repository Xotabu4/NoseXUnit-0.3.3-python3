#-*- coding: utf-8 -*-
import os
import test_NoseXUnit

import nosexunit.tools as ntools
import nosexunit.excepts as nexcepts

class TestYieldError(test_NoseXUnit.PluginTestCase):
    
    def setUpCase(self):
        content = """
class TestYieldError(object):
    def test(self): yield self._test_body, yoo
    def _test_body(self): pass
"""
        test = test_NoseXUnit.Module('test_yield', content)
        test.save(self.source)
        self.suitepath = self.source
        self.setUpCore(self.core_target, self.source)

    def test(self):
        self.assertWasNotSuccessful()
        self.assertExists(os.path.join(self.core_target, 'TEST-nose.xml'))

if __name__=="__main__":
    test_NoseXUnit.main()

