from odoo import fields, models

class StockMoveLine(models.Model):
	_inherit = "stock.move.line"

	line_notes = fields.Char(string="Additional Desc")