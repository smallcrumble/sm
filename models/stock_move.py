from odoo import fields, models

class StockMove(models.Model):
	_inherit = "stock.move"

	line_notes = fields.Char(string="Additional Desc")

class StockMoveLine(models.Model):
	_inherit = "stock.move.line"

	#line_notes = fields.Char(related="move_id.line_notes", string="Additional Desc")