from odoo import api, fields, models


class HzReporter(models.Model):
    _name = 'hz.reporter'
    _description = 'HzReporter'

    name = fields.Char()
    description = fields.Text()
