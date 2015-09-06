#
# module openacademy/wizard
#

from osv import osv, fields

class SubscriptionWizard(osv.TransientModel):
    _name = 'openacademy.wizard.subscription'
    _columns = {
        'session_ids': fields.many2many('openacademy.session',
            'openacademy_wizard_sessions', 'wizard_id', 'session_id',
            string='Sessions', required=True),
        'attendee_ids': fields.one2many('openacademy.wizard.attendee',
            'wizard_id', string='Attendees'),
    }

    def _get_current_sessions(self, cr, uid, context=None):
        if context and context.get('active_model') == 'openacademy.session':
            return context.get('active_ids', False)
        return False

    _defaults = {
        'session_ids': _get_current_sessions,
    }

    def subscribe(self, cr, uid, ids, context=None):
        session_model = self.pool.get('openacademy.session')
        wizard = self.browse(cr, uid, ids[0], context)
        session_ids = [session.id for session in wizard.session_ids]
        attendee_changes = [(0, 0, {'partner_id': attendee.partner_id.id})
                            for attendee in wizard.attendee_ids]
        session_model.write(cr, uid, session_ids,
            {'attendee_ids': attendee_changes}, context)
        return {}

class AttendeeWizard(osv.TransientModel):
    _name = 'openacademy.wizard.attendee'
    _columns = {
        'wizard_id': fields.many2one('openacademy.wizard.subscription'),
        'partner_id': fields.many2one('res.partner', string='Partner',
            required=True),
    }
