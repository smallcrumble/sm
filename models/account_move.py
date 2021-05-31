from odoo import fields, models

class AccountMove(models.Model):
	_inherit = "account.move"

	#ga jadi
	#ref = fields.Char(string='Reference', copy=False, tracking=True, required=True)