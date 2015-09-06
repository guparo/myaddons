# -*- coding: utf-8 -*-
 
from openerp import models, fields, api
 
class condominium_unidad (models.Model):
    _name = 'condominium.unidad'
    name = fields.Char(string="Title", required=True)
    image = fields.binary("Imagen", help="Seleccionar imagen aqui")
    description = fields.Text()

