# This file is part of the internetdomain_invoice_standalone module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class InternetdomainInvoiceStandaloneTestCase(ModuleTestCase):
    'Test Internetdomain Invoice Standalone module'
    module = 'internetdomain_invoice_standalone'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        InternetdomainInvoiceStandaloneTestCase))
    return suite