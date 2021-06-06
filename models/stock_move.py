from odoo import fields, models

class StockMove(models.Model):
	_inherit = "stock.move"

	line_notes = fields.Char(string="Detail Notes")

	def _action_done(self, cancel_backorder=False):
		res = super(StockMove,self)._action_done(cancel_backorder)
		print('po line id : '+ str(res['purchase_line_id'].id))
		print('line notes s.move : '+ str(res['line_notes']))
		#res['purchase_line_id'].line_notes = res['line_notes']
		
		return res

	

class StockMoveLine(models.Model):
	_inherit = "stock.move.line"

	xtra_line_notes = fields.Char(string="Line Notes")