from atf import *
from atf.ui import *


class TestSubTest(TestCaseUI):
    def test(self):
        self.browser.open('https://sbis.ru')
        self.browser.should_be(UrlExact('https://fix.sbis.ru'))