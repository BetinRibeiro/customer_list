# -*- coding: utf-8 -*-
db.define_table("person",
                         Field("name_person", label=T('Name Person'),notnull=True),
                         Field('whatzapp', 'string',label=T("whatzapp") ,notnull=True),
                         Field('facebook', 'string',label=T("facebook")),
                         Field('instagram', 'string',label=T("instagram")),
                         Field('genre', 'string',label=T("genre") ,default=T('feminine'), notnull=True),
                         Field('address', 'string', label=T("address")),
                         Field('date_of_birth', 'date', label=T("date_of_birth"),default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                         Field('marital_status', 'string',label=T("marital_status") ,default=T('married')),
                         Field('credit_card', 'boolean',label=T("credit_card") , notnull=True),
                         Field('profession', 'string',label=T("profession") ),
                         Field('average_wage', 'double',label=T("average_wage") , notnull=True, default=1000),
                         Field('buying_motivator', 'text',label=T("buying_motivator")),
                         Field('aches', 'text',label=T("aches") , default=T("aches")),
                         Field('open_to_business', 'boolean',label=T("open_to_business") , default=True),
                         Field('amount_of_activities', 'integer',label=T("amount_of_activities") ,writable=False, readable=False, default=0, notnull=True),
                        Field('note', 'text',label=T("note")),

                        auth.signature,
                        format='%(name_person)s')

db.person.marital_status.requires = IS_IN_SET([T('not married'), T('dating'), T('married')])

db.person.genre.requires = IS_IN_SET([T('male'), T('feminine')])


db.define_table("work_activity",
                         Field("description", 'string',label=T('Description'),notnull=True),
                         Field("person", 'reference person', label=T('Person'),notnull=True),
                         Field('activity_date', 'date', label=T("Activity Date"),default=request.now, requires = IS_DATE(format=('%d-%m-%Y'))),
                         Field("value_activity", 'double',label=T("Value"), default=0.00 , notnull=True),
                         Field("reschedule", 'boolean',label=T("Reschedule") , notnull=True),
                         Field("note", 'text', label=T('Note'),notnull=True),
                         auth.signature)

db.work_activity.description.requires = IS_IN_SET([T('Contacted'), T('Has Invited'),T('Product Presentation'), T('Business Presentation'),T('Process Monitoring'), T('Sale'), T('Promote Event'), T('Responsible Sponsorship')])
