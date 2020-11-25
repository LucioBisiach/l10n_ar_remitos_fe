# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inheritAccountMove(models.Model):
    _inherit = 'account.move'

    n_remito_pdv = fields.Char()
    n_remito = fields.Char()