# This file is part internetdomain_invoice_standalone module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Renewal']


class Renewal:
    __metaclass__ = PoolMeta
    __name__ = 'internetdomain.renewal'
    account_invoice_lines = fields.Function(fields.One2Many('account.invoice.line', None,
        'Invoice Lines'), 'get_account_invoice_lines')

    def get_account_invoice_lines(self, name):
        InvoiceLine = Pool().get('account.invoice.line')
        lines = InvoiceLine.search([
                ('origin', 'like', 'internetdomain.renewal,%s' % self.id),
                ])
        return [l.id for l in lines]

    def _get_invoice_line_description(self):
        '''
        Return the renewal description
        :param renewal: the BrowseRecord of the renewal
        :return: str
        '''
        description = (self.domain.name +
            ' (' + str(self.date_renewal) +
            ' / ' + str(self.date_expire) + ')')
        return description

    def get_invoice_lines_to_create(self):
        InvoiceLine = Pool().get('account.invoice.line')

        if not self.domain.products:
            return []

        to_create = []
        for product in self.domain.products:
            invoice_line = InvoiceLine.get_invoice_line_product(
                party=self.domain.party,
                product=product,
                qty=1)
            invoice_line.invoice_type = 'out_invoice'
            invoice_line.description = '%s - %s' % (
                invoice_line.description,
                self._get_invoice_line_description(),
                )
            invoice_line.origin = self
            to_create.append(invoice_line)
        return to_create

    @classmethod
    def create(cls, values):
        renewals = super(Renewal, cls).create(values)
        with Transaction().set_context({
                'invoice_type': 'out_invoice',
                'standalone': True,
                }):
            for renewal in renewals:
                for line in renewal.get_invoice_lines_to_create():
                    line.origin = renewal
                    line.save()
        return renewals
