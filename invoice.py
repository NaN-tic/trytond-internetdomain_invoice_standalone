#This file is part of internetdomain_invoice_standalone module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['InvoiceLine']
__metaclass__ = PoolMeta


class InvoiceLine:
    __name__ = 'account.invoice.line'
    renewal = fields.Many2One('internetdomain.renewal', 'Renewal')
