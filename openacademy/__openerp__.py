#
# module openacademy
#
{
    'name': 'Open Academy',
    'version': '1.0',
    'author': 'Ing. OpenERP',
    'category': 'Extra Tools',
    'description': """
        The module Open Academy helps managing trainings:
         - training courses,
         - training sessions,
         - attendee subscription.
    """,
    'depends': ['base', 'report_webkit'],
    'data': [
        'security/openacademy.xml',
        'security/ir.model.access.csv',
        'openacademy_data.xml',
        'openacademy_view.xml',
        'partner_view.xml',
        'workflow/openacademy.xml',
        'wizard/openacademy_view.xml',
        'report/openacademy.xml',
    ],
}
