from odoo import fields, models

class StockMove(models.Model):
	_inherit = "stock.move"

	line_notes = fields.Char(string="Additional Notes")

class StockMoveLine(models.Model):
	_inherit = "stock.move.line"

	xtra_line_notes = fields.Char(string="Detail Notes")