#This file is part internetdomain_invoice_standalone module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.pool import Pool
from .internetdomain import *

def register():
    Pool.register(
        Renewal,
        module='internetdomain_invoice_standalone', type_='model')

