from odoo import fields, models

class AccountMove(models.Model):
	_inherit = "account.move"

	ref = fields.Char(string='Reference', copy=False, tracking=True, required=True)


class AccountMoveLine(models.Model):
	_inherit = "account.move.line"

	line_notes = fields.Char(string="Additional Notes")