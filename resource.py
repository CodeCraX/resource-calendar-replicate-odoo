# It has to be in resource.calendar model
def dup_line(self):
        obj = self.env['resource.calendar.attendance']
        l = []
        
        for i in self.attendance_ids:
            l.append(i.id)

        try:
            j = max(l)
        except ValueError:
            raise exceptions.except_orm(_('Error'), _('Enter atleast one line of record'))

        for i in self.attendance_ids:
            if i.id==j:
                k = i
        if k:
            for i in k:
                last_name = i.name
                last_dayofweek = i.dayofweek
                last_hour_from = i.hour_from
                last_hour_to = i.hour_to
                
                s = unicode(int(last_dayofweek)+1)
                
                if s<unicode(7):
                    d = {
                    # 'name':last_name,
                    'dayofweek':s,
                    'hour_from':last_hour_from,
                    'hour_to':last_hour_to,
                    'calendar_id':self.id}
                    obj.create(d)

                if s==unicode(7):
                    s = unicode(0)
                    d = {
                    # 'name':last_name,
                    'dayofweek':s,
                    'hour_from':last_hour_from,
                    'hour_to':last_hour_to,
                    'calendar_id':self.id}
                    obj.create(d)
