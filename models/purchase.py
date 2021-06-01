from odoo import api, fields, models

from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	@api.model
	def _default_picking_type(self):
		return self._get_picking_type(self.env.context.get('company_id') or self.env.company.id)

	picking_type_id = fields.Many2one('stock.picking.type', 'Deliver To', states=Purchase.READONLY_STATES, required=True, default=_default_picking_type, domain="['|', ('warehouse_id', '=', False), ('warehouse_id.company_id', '=', company_id)]",
		help="This will determine operation type of incoming shipment")


class PurchaseOrderLine(models.Model):
	_inherit = 'purchase.order.line'

	line_notes = fields.Char(string="Additional Notes")

	def _prepare_account_move_line(self, move=False):
		res = super(PurchaseOrderLine, self)._prepare_account_move_line(move)
		res['line_notes']=self.line_notes
		return res