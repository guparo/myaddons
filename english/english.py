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
from datetime import datetime
#import decimal_precision as dp
class english_tobeview(osv.osv):
  _name = 'english.tobeview'
  _description = 'To be images'
  _rac_name='name'
  _columns = {
    'name': fields.char('Base Form', size=200, required=True),
    'image1': fields.binary("There is a rabbit inside", required=False, help="Seleccionar imagen aqui"),
    'image2': fields.binary("There is nothing in the fridge", required=False, help="Seleccionar imagen aqui"),
    'image3': fields.binary("There is a problem..", required=False, help="Seleccionar imagen aqui"),
    'image4': fields.binary("There is a difference.", required=False, help="Seleccionar imagen aqui"),
    
    'image5': fields.binary("The party IS tonight.", required=False, help="Seleccionar imagen aqui"),
    'image6': fields.binary("The meeting is down the hall.", required=False, help="Seleccionar imagen aqui"),
    'image7': fields.binary("Come, it is over there", required=False, help="Seleccionar imagen aqui"),
    

    'image8': fields.binary("She is at school.", required=False, help="Seleccionar imagen aqui"),
    'image9': fields.binary("She is home.", required=False, help="Seleccionar imagen aqui"),
    'image10': fields.binary("The food is on the table.", required=False, help="Seleccionar imagen aqui"),
 
    'image11': fields.binary("She is Alexis and this is Bob.", required=False, help="Seleccionar imagen aqui"),
    'image12': fields.binary("He is a singer.", required=False, help="Seleccionar imagen aqui"),
    'image13': fields.binary("He is not a singer.", required=False, help="Seleccionar imagen aqui"), 

    'image14': fields.binary("She is beautiful..", required=False, help="Seleccionar imagen aqui"),
    'image15': fields.binary("It is stinky.", required=False, help="Seleccionar imagen aqui"),
    'image16': fields.binary("This is dangerous.", required=False, help="Seleccionar imagen aqui"),
  

  
  }  
  
english_tobeview()

class english_tobeaf(osv.osv):
  _name = 'english.tobeaf'
  _description = 'The present of BE'
  _rac_name='name'
  _columns = {
    'tobeaf' : fields.selection([
     ("1","I am"), 
     ("2","I'm"),
     ("3","You are"), 
     ("4","You're"),
     ("5","He is"),
     ("6","He's"), 
     ("7","She is"),
     ("8","She's"), 
     ("9","It is"),
     ("10","It's"),
     ("11","We are"),
     ("12","We're"),
     ("13","They are"),
     ("14","They're"),
     ("15","Gustavo is"),
     ("16","Gustavo's"),
     ],'Subject + Be', required = True),
    'complement': fields.char('Complement', size=200, required=False),
  }
english_tobeaf()


class english_tobene(osv.osv):
  _name = 'english.tobene'
  _description = 'The negative of BE'
  _rac_name='name'
  _columns = {
    'tobene' : fields.selection([
     ("1","I am not"), 
     ("2","I'm not"),
     ("3","You are not"), 
     ("4","You're not"),
     ("5","You aren't"), 
     ("6","He is not"),
     ("7","He's not"),
     ("8","He isn't"),
     ("9","She is not"),
     ("10","She's not"),
     ("11","She isn't"),
     ("12","It is not"),
     ("13","It's not"),
     ("14","It isn't"),
     ("15","We are not"),
     ("16","We're not"),
     ("17","We aren't"),
     ("18","They are not"),
     ("19","They're not"),
     ("20","They aren't"), 
     ],'Subject + Be/not ', required = True),
    'complement': fields.char('Complement', size=200, required=False),
  }
english_tobene()


class english_tobeyesno(osv.osv):
  _name = 'english.tobeyesno'
  _description = 'The Yes/No questions of BE'
  _rac_name='name'
  _columns = {
    'tobequestions' : fields.selection([
     ("1","Am I"), 
     ("2","Are you"),
     ("3","Is he"), 
     ("4","Is she"),
     ("5","Is it"), 
     ("6","Are we"),
     ("7","Are you"),
     ("8","Are they"),
 
     ],'QUESTIONS (Be+Subject) ', required = True),
    'complement': fields.char('Complement', size=200, required=False),

     'shortanswersyes' : fields.selection([
     ("1","Yes, you are."), 
     ("2","Yes, I am."),
     ("3","Yes, he is"), 
     ("4","Yes, she is."),
     ("5","Yes, it is"), 
     ("6","Yes, we are."),
     ("7","Yes, they are."),
     ],'Afirmative', required = False),  

     'shortanswersno' : fields.selection([
     ("1","No, you're not."),
     ("2","No, you aren't."),  
     ("3","No, I'm not."),
     ("4","No, he's not"), 
     ("5","No, he isn't"), 
     ("6","No, she's not."),
     ("7","No, she isn't."),
     ("8","No, it's not"), 
     ("9","No, it isn't"), 
     ("10","No, we're not."),
     ("11","No, we aren't."),
     ("12","No, they're not."),
     ("13","No, they aren't."),
     ],'Negative ', required = False),  

  }
english_tobeyesno()

class english_verbs(osv.osv):
  _name = 'english.verbs'
  _description = 'Verb Forms'
  _rac_name='name'
  _columns = {
    'image': fields.binary("Image", help="Seleccionar imagen aqui"),
    'name': fields.char('Base Form', size=20, required=True),
    'pastform': fields.char('Past Form', size=20,required=False),
    'pastparticiple': fields.char('Past Participle', size=20, required=False),
    'spanish': fields.char('Espanol',size=50, required=False),
    'progressive': fields.char('Progressive',size=50, required=False),
    'irregular': fields.boolean('Irregular'),
  }
  
english_verbs()










class english_simppresentaf(osv.osv):
  _name = 'english.simppresentaf'
  _description = 'Simple Present Afirmative'
  _rac_name='name'
  _columns = {
    'subject_id': fields.many2one('english.subject','Subject', help='Ingrese el Sujeto'),
    'verb_id': fields.many2one('english.verbs','Verb (-s/es)'),
   # 'ver_id': fields.many2one('english.subject','Subject'),
    'name': fields.char('Complement', size=100, required=True),

    'state' : fields.selection([('draft','Borrador'),('confirmed', 'Confirmado'), ('cancel','Cancelado')], 'Estado', readonly=True),
    
    }
  _defaults = {
 
    'state': 'draft',

          } 

  def draft(self, cr, uid, ids, context=None):
      self.write(cr, uid, ids,{'state':'draft'}, context=None) 
      return True 

  def confirm(self, cr, uid, ids, context=None):
      self.write(cr, uid, ids,{'state':'confirmed'}, context=None) 
      return True 
  def cancel(self, cr, uid, ids, context=None):
      self.write(cr, uid, ids,{'state':'cancel'}, context=None) 
      return True         
english_simppresentaf()

class english_simppresentne(osv.osv):
  _name = 'english.simppresentne'
  _description = 'Simple Present Negative'
  _rac_name='name'
  _columns = {
    'subject_id': fields.many2one('english.subject','Subject', help='Ingrese el Sujeto', required = True),
  
    'dodoesnot' : fields.selection([ ("1","do not"), ("2","don't"),("3","does not"), ("4","doesn't"),],'(do/does) not', required = True),
    'verb_id': fields.many2one('english.verbs','Verb', help='Ingrese el verbo'),
   # 'ver_id': fields.many2one('english.subject','Subject'),
    'name': fields.char('Complement', size=100, required=True),
  } 
english_simppresentne()

class english_yesnoquestions(osv.osv):
  _name = 'english.yesnoquestions'
  _description = 'Simple Present Yes/No questions and Short Answer'
  _rac_name='name'
  _columns = {
    'dodoesnot' : fields.selection([ ("1","Do"), ("2","Does"),],'(do/does)', required = True),
    'subject_id': fields.many2one('english.subject','Subject', help='Ingrese el Sujeto', required = True),
    'verb_id': fields.many2one('english.verbs','Verb (base form)', help='base form'),
   # 'ver_id': fields.many2one('english.subject','Subject'),
    'complement': fields.char('Complement', size=200, required=False),
    'shortanswerafne': fields.selection([ ("1","Yes,"), ("2","No,"),],'( SHORT ANSWER )', required = False),
    'shortanswersubject': fields.many2one('english.subject','Subject', help='Ingrese el Sujeto', required = True),   
    'shortanswerafne2': fields.selection([ ("1","do,"), ("2","does,"),("3","don't,"), ("4","doesn't,"),],"Affirmative/Negative", required = False),
  } 
english_yesnoquestions()

class english_whquestions(osv.osv):
  _name = 'english.whquestions'
  _description = 'Simple Present WH questions and Short Answer'
  _rac_name='name'
  _columns = {
    'whword' : fields.selection([
     ("1","When"), 
     ("2","Where"),
     ("3","What"), 
     ("4","Why"),
     ("5","Who(m)"), 
     ("6","How"),


     ],'Wh-Word', required = True),
    'dodoesnot' : fields.selection([ ("1","Do"), ("2","Does"),],'do/does', required = False),
    'subject_id': fields.many2one('english.subject','Subject', help='Ingrese el Sujeto', required = True),
    'verb_id': fields.many2one('english.verbs','Verb (base form)', help='base form'),
   # 'ver_id': fields.many2one('english.subject','Subject'),
    'complement': fields.char('Complement', size=200, required=False),
    'shortanswers': fields.char('Short Answers' , size=200,  required=False),
    'longanswers': fields.char('Long Answers' , size=200,  required=False),

  } 
english_whquestions()



class english_adverbs(osv.osv):
  _name = 'english.adverbs'
  _description = 'Adverbs'
  _rac_name='name'
  _columns = {
    'name': fields.char('Adverb', size=100, required=True),
    'frequency': fields.char('Frequency', size=20,required=False),
    'spanish': fields.char('Espanol', size=240, required=False),
 
  }
  
english_adverbs()


class english_subject(osv.osv):
  _name = 'english.subject'
  _description = 'Subject'
  _rac_name='name'
  _columns = {
    'name': fields.char('Subject', size=20, required=True),
    'be' : fields.selection([
     ("1","am"), 
     ("2","are"),
     ("3","is"), 
     ],'be', required = True),
    'spanish': fields.char('Espanol', size=240, required=False),

 
  }
  
english_subject()



class english_tablas(osv.osv):
  _name = 'english.tablas'
  _description = 'Tablas'
  _rac_name='name'
  _columns = {
    'name': fields.char('Name', size=20, required=True),
    'image': fields.binary("Image", help="Seleccionar imagen aqui"),
  }
  
english_tablas()


class english_ficha(osv.osv):

  _name = 'english.ficha'
  _description = 'Ficha'
  _rac_name='name'
  _columns = {
    'image': fields.binary("Imagen", help="Seleccionar imagen aqui"),
    'name': fields.char('Apellidos y Nombre', size=400, required=True),
    'fecha': fields.date('Fecha', required=False),
    'email': fields.char('Correo electrónico', size=200, required=False),
    'telf': fields.integer('Telf Móvil',size=9, required=False),
    'telffijo': fields.integer('Telf Fijo',size=9, required=False),
    'direccion': fields.char('Dirección', size=400, required=False),
    'empresa_id': fields.many2one('english.empresas','Empresa TFM'),
    'titulo': fields.text('Título', required=False),
    'becario': fields.text('Becario', required=False),
    'idiomas': fields.text('Idiomas', required=False),
    'fecha_nacimiento' :fields.date('Fecha-nac', required=False),
    'edad': fields.integer('Edad',  required=False),
  }
  def on_change_fecha_nac(self, cr, uid, ids, fecha_nacimiento, context=None):
    res = {}
    if fecha_nacimiento:
        edad = (datetime.now().date() - datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()).days / 365
        if edad < 0:
            edad = 0
        res = {'edad': edad}
    return {'value': res}
english_ficha()







class english_calificaciones(osv.osv):

  def _get_total(self, cr, uid, ids, field_name, arg, context=None):
    result = {}
    for rec in self.browse(cr,uid,ids,context=context):
      result[rec.id]= rec.nota1 + rec.nota2
    return result
  def calcula_promedio(self, cr, uid, ids, field_name, arg, context=None):
    result = {}
    for rec in self.browse(cr,uid,ids,context=context):
      result[rec.id]= (rec.nota1 + rec.nota2) / 2
    return result

  _name = 'english.calificaciones'
  _description = 'Calificaciones'
  _columns = {
    'name_id': fields.many2one('english.asignaturas','name--id',help="obligado por one2many, no necesario aparezca en vista"),
    'nombre':  fields.char('Apellido y Nombres', size=30, required=False),
 
    'nota1': fields.float('Primer Examen ',  digits = (6,2),required=False),
    'nota2': fields.float('Segundo Examen',  digits = (6,2),required=False),
 #   'promedio': fields.float('Promedio', required=False),

    'promedio': fields.function(calcula_promedio, method=True, type='float', string='Promedio', store=True),
#    'total': fields.float('Total', required=False), 
    'total': fields.function(_get_total, method=True, type='float', string='Total', store=True),     


  }
 
  def onchange_notas(self, cr, uid, ids, nota1,nota2, context=None):
      if not context:
        context={}
      value = {}
      domain = {}
      count = 0
      if nota1 != 0:
          count += 1
      if nota2 != 0:
          count += 1  
      if count > 0:
          value['promedio'] = (nota1 + nota2) / count
      else:
          value['promedio'] = 100
      value['total'] = nota1 + nota2
      return{'value':value, 'domain':domain}
 

english_calificaciones()

class english_asignaturas(osv.osv):
  _name = 'english.asignaturas'
  _description = 'Asignaturas'
  _columns = {
    'nombre': fields.char('nombre de la asignatura', size=400, required=True),
    'profesor': fields.char('Profesor', required=False),
    'creditos': fields.char('Créditos', size=200, required=False),
    'notas_ids': fields.one2many('english.calificaciones','name_id','Alumnos'),
 
  }
  
english_asignaturas()
