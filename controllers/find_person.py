# -*- coding: utf-8 -*-

@auth.requires_login()
def list_people():
    db.person.id.writable = False
    db.person.id.readable  = False
    grid = SQLFORM.grid(db.person.created_by == auth.user, paginate=20, csv=False, fields = [db.person.name_person, db.person.whatzapp, db.person.date_of_birth,  db.person.profession, db.person.open_to_business])
    return locals()
