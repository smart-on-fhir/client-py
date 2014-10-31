#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Facilitate working with dates.
#  2014, SMART Platforms.

import sys
import isodate
import datetime


class FHIRDate(object):
    """ Facilitate working with dates.
    
    - `date`: datetime object representing the receiver's date-time
    """
    
    def __init__(self, jsonval=None):
        self.date = None
        if jsonval is not None:
            if 'T' in jsonval:
                self.date = isodate.parse_datetime(jsonval)
            else:
                self.date = isodate.parse_date(jsonval)
    
    @property
    def isostring(self):
        if self.date is None:
            return None
        if isinstance(self.date, datetime.datetime):
            return isodate.datetime_isoformat(self.date)
        return isodate.date_isoformat(self.date)
    
    @classmethod
    def with_json(cls, jsonobj):
        """ Initialize a date from an ISO date string.
        """
        isstr = isinstance(jsonobj, str)
        if not isstr and sys.version_info[0] < 3:       # Python 2.x has 'str' and 'unicode'
            isstr = isinstance(jsonobj, basestring)
        if isstr:
            return cls(jsonobj)
        
        arr = []
        for jsonval in jsonobj:
            arr.append(cls(jsonval))
        return arr
    
