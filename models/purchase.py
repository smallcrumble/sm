from odoo import fields, models

from odoo.addons.purchase.models.purchase import PurchaseOrder as Purchase

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	@api.model
	def _default_picking_type(self):
		return self._get_picking_type(self.env.context.get('company_id') or self.env.company.id)
		
	picking_type_id = fields.Many2one('stock.picking.type', 'Deliver To', states=Purchase.READONLY_STATES, required=True, default=_default_picking_type, domain="['|', ('warehouse_id', '=', False), ('warehouse_id.company_id', '=', company_id)]",
		help="This will determine operation type of incoming shipment")