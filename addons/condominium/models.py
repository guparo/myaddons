# -*- coding: utf-8 -*-
 
##from openerp import models, fields, api
 
##class condominium_unidad (models.Model):
 ##   _name = 'condominium.unidad'
 ##   name = fields.Char(string="Titulo", required=True)
 #   image = fields.binary(string="Imagen", help="Seleccionar imagen aqui")
##    date_act = fields.Date('Fecha')

 #   image = fields.binary('Imagen', help='Seleccionar imagen aqui')
##    description = fields.Text()



from openerp.osv import osv,fields
class condominium_unidad(osv.osv):
  _name = 'condominium.unidad'
  _description = 'Ficha'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'apellidosyn': fields.char('Apellidos y Nombre', size=400, required=True),
    'fecha': fields.date('Fecha', required=False),
    'email': fields.char('Correo electrónico', size=200, required=False),
    'telf': fields.integer('Telf Móvil',size=9, required=False),
    'telffijo': fields.integer('Telf Fijo',size=9, required=False),
    'direccion': fields.char('Dirección', size=400, required=False),
    'titulo': fields.text('Título', required=False),
    'becario': fields.text('Becario', required=False),
    'idiomas': fields.text('Idiomas', required=False),
  }
  
condominium_unidad