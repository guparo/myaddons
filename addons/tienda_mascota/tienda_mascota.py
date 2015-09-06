# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv, fields

class tienda_mascota_verbs(osv.osv):
  _name = 'tienda_mascota.verbs'
  _description = 'Verb Forms'
  _rac_name='name'
  _columns = {
    'image': fields.binary("Image", help="Seleccionar imagen aqui"),
    'name': fields.char('Base Form', size=20, required=True),
    'pastform': fields.char('Past Form', size=20,required=False),
    'pastparticiple': fields.char('Past Participle', size=20, required=False),
    'spanish': fields.char('Espanol',size=50, required=False),
    'irregular': fields.boolean('Irregular'),
  }
  
tienda_mascota_verbs()

