from datetime import datetime, date, timedelta
from openerp.osv import osv, fields
from openerp.report import report_sxw

class accounting_report_pdf(osv.AbstractModel):
    _name = 'report.full_accounting_report.full_accounting_report_pdf'

    def _get_periods(self, docs):
    	array_period = []
    	for object in docs:
    		array_period.append(object.period_id.name)
    		# to delete duplication
    	periods=list(set(array_period))
    	return periods

    	

  
            'get_start_date':self._get_start_date,
            'get_end_date':self._get_end_date,
            'get_target_move': self._get_target_move,
        })
        self.context = context

    def set_context(self, objects, data, ids, report_type=None):
        new_ids = ids
        if (data['model'] == 'ir.ui.menu'):
            new_ids = 'chart_account_id' in data['form'] and [data['form']['chart_account_id']] or []
            objects = self.pool.get('account.account').browse(self.cr, self.uid, new_ids)
        return super(account_balance, self).set_context(objects, data, new_ids, report_type=report_type)

    def _get_account(self, data):
        if data['model']=='account.account':
            return self.pool.get('account.account').browse(self.cr, self.uid, data['form']['id']).company_id.name
        return super(account_balance ,self)._get_account(data)