from odoo import models, fields
class Skin(models.Model):
    _name = 'cs.skins'
    _description = 'Skins de Counter Strike 2'
    
    name = fields.Char(string='Nombre', required=True)
    image = fields.Binary(string='Image', attachment=True, store=True)
    price = fields.Float(string='Price')