#This file is part internetdomain_invoice_standalone module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Renewal']
__metaclass__ = PoolMeta


class Renewal:
    'Renewal'
    __name__ = 'internetdomain.renewal'
    account_invoice_lines = fields.One2Many('account.invoice.line','renewal',
        'Invoice Lines')

    @classmethod
    def __setup__(cls):
        super(Renewal, cls).__setup__()
        cls._error_messages.update({
            'missing_account_revenue': 'Product not available Account Revenue!',
            })

    def _get_invoice_description(self):
        '''
        Return description renewal
        :param renewal: the BrowseRecord of the renewal
        :return: str
        '''
        description = self.domain.name + '' \
            '(' + str(self.date_renewal) + ' a ' \
            '' + str(self.date_expire) + ')'
        return description

    def get_invoice_lines_to_create(self):
        InvoiceLine = Pool().get('account.invoice.line')
        #Only create lines if they don't exists
        if (len(self.domain.products) <= len(self.account_invoice_lines)):
            return []
        to_create = []
        for product in self.domain.products:
            vals = InvoiceLine.get_invoice_line_product(
                party=self.domain.party,
                product=product,
                qty=1)
            vals['description'] += ' %s' % self._get_invoice_description()
            vals['renewal'] = self.id
            to_create.append(vals)
        return to_create

    @classmethod
    def create(cls, values):
        InvoiceLine = Pool().get('account.invoice.line')
        renewals = super(Renewal, cls).create(values)
        to_create = []
        for renewal in renewals:
            to_create.extend(renewal.get_invoice_lines_to_create())
        if(len(to_create) > 0):
            with Transaction().set_user(0, set_context=True):
                InvoiceLine.create(to_create)
        return renewals
