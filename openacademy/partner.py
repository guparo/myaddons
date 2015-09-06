#
# module openacademy
#

from osv import osv, fields

class Partner(osv.Model):
    _inherit = 'res.partner'
    _columns = {
        'instructor': fields.boolean('Instructor',
            help='Check this if the partner can instruct an Open Academy session.'),
    }
