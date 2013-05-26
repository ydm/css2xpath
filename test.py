#!/usr/bin/env python3

import io
import unittest
import css2xpath


class Css2XpathTest(unittest.TestCase):

    def runfunc(self, func, expwrite, expreturn, *args):
        f = io.StringIO()
        actreturn = func(*(args + (f.write,)))
        actwrited = f.getvalue()
        msg = lambda e, a: 'Tested: {}{},\n : Expected={}, Actual={}'.format(
            func.__name__, args, e, a)
        self.assertEqual(expwrite, actwrited, msg(expwrite, actwrited))
        self.assertEqual(expreturn, actreturn, msg(expreturn, actreturn))

    def batch(self, func, expwrite, expreturn, args):
        for w, r, a in zip(expwrite, expreturn, args):
            self.runfunc(func, w, r, a)

    def test_node_star(self):
        i = ['#egg', '.egg', '.spam:nth-child(1)',]
        w = ['*', '*', '*']
        r = i.copy()
        self.batch(css2xpath.tok2nodetest, w, r, i)

    def test_node_el(self):
        i = ['h1#egg', 'h2.egg', 'h3.spam:nth-child(1)',]
        w = ['h1', 'h2', 'h3']
        r = ['#egg', '.egg', '.spam:nth-child(1)']
        self.batch(css2xpath.tok2nodetest, w, r, i)

    def test_predicate(self):
        i = ['.eggs', '#egg', '.eggs:nth-child(1)', ':nth-child(1)']
        w = ["[contains(@class, 'eggs')]", "[@id='egg']",
             "[contains(@class, 'eggs')]", '[1]']
        r = ['', '', ':nth-child(1)', '']
        self.batch(css2xpath.tok2predicate, w, r, i)

    def test_transform(self):
        inp = '.spam > p.and-eggs:nth-child(3) a.something.otherthing'
        exp = "//*[contains(@class, 'spam')]"\
              "/p[contains(@class, 'and-eggs')][3]"\
              "//a[contains(@class, 'something')]"\
              "[contains(@class, 'otherthing')]"
        self.assertEqual(exp, css2xpath.transform(inp))


if __name__ == '__main__':
    unittest.main()
