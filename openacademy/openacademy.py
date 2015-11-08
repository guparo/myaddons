#
# module openacademy
#


from openerp.osv import fields, osv
import time
#from openerp.datetime import datetime, timedelta
import datetime
from datetime import timedelta
from tools.translate import _

class Course(osv.Model):
    _name = 'openacademy.course'
    _description = 'Course'
    _columns = {
        'name': fields.char('Title', size=128, translate=True, required=True),
        'description': fields.text('Description', translate=True),
        'responsible_id': fields.many2one('res.users', string='Responsible'),
        'session_ids': fields.one2many('openacademy.session', 'course_id',
            string='Session'),
    }

 #   _defaults = {
  #      'responsible_id': lambda self, cr, uid, context: uid,
 #   }

    def _check_description(self, cr, uid, ids, context=None):
        for course in self.browse(cr, uid, ids, context):
            if course.name == course.description:
                return False
        return True

    _constraints = [(_check_description,
        'Course title and description must be different',
        ['name', 'description'])]

    _sql_constraints = [('unique_name', 'UNIQUE(name)',
        'Course titles must be distinct')]

    def copy(self, cr, uid, id, defaults, context=None):
        # avoid breaking sql constraint when duplicating record
        course = self.browse(cr, uid, id, context)
        defaults['name'] = _('%s (copy)') % course.name
        # do not copy sessions
        defaults['session_ids'] = []
        return super(Course, self).copy(cr, uid, id, defaults, context)

class Session(osv.Model):
    _name = 'openacademy.session'
    _description = 'Session'
    _order = 'start_date'

    def _get_taken_seats_pct(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for sess in self.browse(cr, uid, ids, context):
            res[sess.id] = sess.seats and \
                100.0 * len(sess.attendee_ids) / sess.seats
        return res

    def _get_end_date(self, cr, uid, ids, fname, arg, context=None):
        res = {}
        for sess in self.browse(cr, uid, ids, context):
            if sess.start_date:
                start = datetime.strptime(sess.start_date, '%Y-%m-%d')
                if sess.duration:
                    end = start + timedelta(sess.duration, seconds=-1)
                else:
                    end = start
                res[sess.id] = end.strftime('%Y-%m-%d')
        return res

    _columns = {
        'name': fields.char('Title', size=128, required=True),
        'start_date': fields.date('Start Date'),
        'duration': fields.float('Duration', help='Duration in days'),
        'seats': fields.integer('Number of Seats'),
        'instructor_id': fields.many2one('res.partner', string='Instructor',
            domain=['|',
                ('instructor', '=', True),
                ('category_id', 'child_of', 'Teacher'),
            ]),
        'course_id': fields.many2one('openacademy.course', string='Course',
            required=True),
        'attendee_ids': fields.one2many('openacademy.attendee', 'session_id',
            string='Attendees'),
        'taken_seats_pct': fields.function(_get_taken_seats_pct, type='float',
            string='Taken Seats', help='Percentage of taken seats'),
        'active': fields.boolean('Active'),
        'end_date': fields.function(_get_end_date, type='date'),
        'state': fields.selection(
            [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done')],
            string='State', required=True, readonly=True),
    }

    #_defaults = {
    #    'active': True,
     #   'state': 'draft',
    #    'start_date': lambda self, cr, uid, context: time.strftime('%Y-%m-%d'),
    #}

    def onchange_seats(self, cr, uid, ids, seats, attendee_ids, context=None):
        # interpret the elements of attendee_ids to count them;
        # elements are like: (0, 0, dict), (1, id, dict), (2, id), (4, id)
        count = 0
        for elem in attendee_ids:
            if elem[0] in (0, 1, 4): count = count + 1
        res = {'value': {'taken_seats_pct': seats and 100.0 * count / seats}}
        if seats < 0:
            res['warning'] = {
                'title': _('Warning'),
                'message': _('The number of seats should not be negative!'),
            }
        return res

    def action_confirm(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'confirmed'}, context)

    def action_done(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'done'}, context)

    def action_reset(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'draft'}, context)

class Attendee(osv.Model):
    _name = 'openacademy.attendee'
    _description = 'Attendee'
    _columns = {
        'partner_id': fields.many2one('res.partner', string='Partner',
            required=True),
        'session_id': fields.many2one('openacademy.session', string='Session',
            required=True, ondelete='cascade'),
    }
