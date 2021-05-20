from odoo import fields, models

class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	picking_type_id = fields.Many2one('stock.picking.type', 'Deliver To', states=Purchase.READONLY_STATES, required=True, default=_default_picking_type, domain="['|', ('warehouse_id', '=', False), ('warehouse_id.company_id', '=', company_id)]",
		help="This will determine operation type of incoming shipment")