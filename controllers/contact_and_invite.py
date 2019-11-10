# -*- coding: utf-8 -*-
# tente algo como
def list_contact(): 
    db.contact_and_invite.id.writable = False
    db.contact_and_invite.id.readable  = False
    grid = SQLFORM.smartgrid(db.contact_and_invite, paginate=20, csv=False)
    return locals()
