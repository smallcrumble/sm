from odoo import fields, models

class StockMove(models.Model):
	_inherit = "stock.move"

	line_notes = fields.Char(string="Additional Desc")