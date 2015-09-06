# -*- coding: utf-8 -*-
#importamos las librerias propias de openerp, con la cual vamos a hacer referencia a las clases maestras
from openerp.osv import osv,fields
from openerp import netsvc
from openerp.tools.translate import _
from datetime import datetime
 
#Definimos la clase demo
class demoo_demoo(osv.osv):
        _name = 'demoo.demoo' # nombre de la tabla que se creara en la base de datos cuando se instala el modulo
                # lo siguiente son las columnas de la tabla
        _columns = {
                'name': fields.char('Nombre', size=64),
                'edad': fields.integer('Edad',size=3,help="Edad actual"),
                'fecha_nac': fields.date('Fecha'),
            	'active': fields.boolean('Activo'),
 	         	'state' : fields.selecction([('draft','Borrador'),('çonfirmed', 'Confirmado'), ('cancel','Cancelado')], 'Estado', readonly=True),
                }
demoo_demoo()