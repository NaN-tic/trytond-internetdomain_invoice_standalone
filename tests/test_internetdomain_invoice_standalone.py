#!/usr/bin/env python
# This file is part internetdomain_invoice_standalone module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class InternentdomainInvoiceStandaloneTestCase(unittest.TestCase):
    'Test Internetdomain Invoice Standalone module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('internetdomain_invoice_standalone')

    def test0005views(self):
        'Test views'
        test_view('internetdomain_invoice_standalone')

    def test0006depends(self):
        'Test depends'
        test_depends()

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        InternentdomainInvoiceStandaloneTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
