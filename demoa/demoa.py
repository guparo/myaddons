# -*- coding: utf-8 -*-
#importamos las librerias propias de openerp, con la cual vamos a hacer referencia a las clases maestras
from openerp.osv import osv,fields, orm
from datetime import datetime
from openerp.tools.translate import _

#Definimos la clase demo
class demoa_demoa(osv.osv):

    def draft(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'draft'}, context=None)
        return True

    def confirm(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'confirmed'}, context=None)
        return True            

    def cancel(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'cancel'}, context=None)
        return True       
    _name = 'demoa.demoa' # nombre de la tabla que se creara en la base de datos cuando se instala el modulo
                # lo siguiente son las columnas de la tabla
    _columns = {
        'name': fields.char('Nombre', size=64),
        'last': fields.char('Apellidos', size=64),
        'edad': fields.integer('Edad',size=3,help="Edad actual"),
        'fecha_nac': fields.date('Fecha'),
        'active': fields.boolean('Activo'),
        'state': fields.selection(
            [
            ('draft','Borrador'),('confirmed', 'Confirmado'),('cancel','Cancelado'),], 'Estado', readonly=True),
        'escuela_id':  fields.many2one('res.partner', 'Escuela', required=True),  
        'horario_ids': fields.one2many('demoa.lines', 'student_id', 'Horario de Clases'), 

    }
    _defaults = {
 #              'fecha_nac': lambda *a: time.strftime('%Y-%m-%d'),
        'state': 'draft',
        'active': True,
     }


demoa_demoa()

class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'school': fields.boolean('Escuela'),
    }
    _default = {

    } 
res_partner()

class demoa_lines(osv.osv):
    _name = 'demoa.lines'
    _description ='Materias'
    _columns = {
        'student_id':fields.many2one('demoa.student', 'ID Referencia'),
        'name':fields.char('Nombre de la Materia', size=64, required=True),
        'horario':fields.text('Horario', required=True),
    }
demoa_lines()



