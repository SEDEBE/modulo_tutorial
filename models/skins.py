from odoo import models, fields
class Skin(models.Model):
    _name = 'Skins.CS'
    _description = 'Skins de Counter Strike 2'
    
    name = fields.Char(string='Nombre', required=True)
    image = fields.Binary(string='Image')
    price = fields.Float(string='Image')