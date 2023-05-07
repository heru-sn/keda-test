from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MasterMaterial(models.Model):
    _name = 'master.material'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Master Material'
    _order = 'name'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    type_material = fields.Selection([
        ('fabric','Fabric'),
        ('jeans','Jeans'),
        ('cotton','Cotton')], string='Material Type')
    buy_price = fields.Float(string='Buy Price')
    partner_id = fields.Many2one('res.partner', string='Related Supplier')

    def create(self, vals):
        res = super(MasterMaterial, self).create(vals)
        if 'buy_price' in vals:
            if vals['buy_price'] < 100:
                raise ValidationError(
                _("You should set buy price bigger than 100 (one hundreed)."))
                
        return res
    
    def write(self, vals):
        res = super(MasterMaterial, self).write(vals)
        if 'buy_price' in vals:
            if vals['buy_price'] < 100:
                raise ValidationError(
                _("You should set buy price bigger than 100 (one hundreed)."))
        
        return res

    

    