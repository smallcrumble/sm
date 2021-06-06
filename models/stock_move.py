from odoo import fields, models
import logging

_logger = logging.getLogger(__name__)

class StockMove(models.Model):
	_inherit = "stock.move"

	line_notes = fields.Char(string="Detail Notes")

	def _action_done(self, cancel_backorder=False):
		res = super(StockMove,self)._action_done(cancel_backorder)
		_logger.info('po line id : %s', str(res['purchase_line_id'].id))
		_logger.info('line notes s.move : %s', str(res['line_notes']))
		
		if res['purchase_line_id']:
			res['purchase_line_id'].line_notes = res['line_notes']
		
		return res

	

class StockMoveLine(models.Model):
	_inherit = "stock.move.line"

	xtra_line_notes = fields.Char(string="Line Notes")