# -*- coding: utf-8 -*-
# tente algo como
def list_activity(): 
    db.work_activity.id.writable = False
    db.work_activity.id.readable  = False
    grid = SQLFORM.grid(db.work_activity.created_by == auth.user, paginate=20, csv=False, fields = [db.work_activity.description, db.work_activity.person, db.work_activity.activity_date, db.work_activity.value_activity])
    return locals()
