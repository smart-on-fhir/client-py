#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Construct server search parameters.
#  2014, SMART Health IT.

from . import fhirsearch


class FHIRSearchElement(object):
    """ This class enables pythonic creation of search URL strings.
    
    Search elements are designed to be chained together. The first parameter
    instance in the chain must define `resource_type`, all subsequent params
    must have their `subject` set to be useful. Upon calling `construct()` on
    the last item in a chain, all instances are constructed into a URL query:
    
    qry = Patient.where().address("Boston").gender('male').given_exact("Willis")
    
    Then qry.construct() will create the string:
    
    "Patient?address=Boston&gender=male&given:exact=Willis"
    """
    
    def __init__(self, subject):
        self._previous = None
        self._next = None
        
        self.subject = subject
        """ The name of the search parameter. """
        
        self.resource_type = None
        """ The first search parameter in a list must define a resource type to
        which the search is applied. """
        
        self.supported_profiles = None
        """ On which profiles the receiver's subject is supported; can be used
        for validation. """
        
        self.string = None
        """ The param's value is a string.
        http://www.hl7.org/implement/standards/fhir/search.html#string """
        
        self.token = None
        """ The param's value is a token. Can be modified with `token_as_text`.
        http://www.hl7.org/implement/standards/fhir/search.html#token """
        
        self.number = None
        """ The param describes a numerical value.
        http://www.hl7.org/implement/standards/fhir/search.html#number """
        
        self.date = None
        """ The param's value is a date string.
        http://www.hl7.org/implement/standards/fhir/search.html#date """
        
        self.quantity = None
        """ The param describes a numerical quantity.
        http://www.hl7.org/implement/standards/fhir/search.html#quantity """
        
        self.reference = None
        """ The param's value is a reference.
        http://www.hl7.org/implement/standards/fhir/search.html#reference """
        
        self.composite = None
        """ A composite search parameter.
        http://www.hl7.org/implement/standards/fhir/search.html#combining """
        
        # Modifiers: http://www.hl7.org/implement/standards/fhir/search.html#modifiers
        
        self.missing = None
        """ If `true` we're looking for a missing parameter. """
        
        self.string_exact = False
        """ Only needed for strings; if `true` the match must be exact. """
        
        self.token_as_text = False
        """ Only needed for tokens; if `true` the token should be queried like text. """
        
        self.reference_type = None
        """ Only needed for references: the type of the reference. """
    
    
    # MARK: Construction
    
    def as_param(self):
        """ Returns a FHIRSearchParam instance representing the receiver.
        """
        if self.subject:
            if self.missing is not None:
                return fhirsearch.FHIRSearchParam('{}:missing'.format(self.subject), 'true' if self.missing else 'false')
            
            if self.string and self.string_exact:
                return fhirsearch.FHIRSearchParam('{}:exact'.format(self.subject), self.param_value())
            
            if self.token and self.token_as_text:
                return fhirsearch.FHIRSearchParam('{}:text'.format(self.subject), self.param_value())
            
        return fhirsearch.FHIRSearchParam(self.subject, self.param_value())
    
    def param_value(self):
        """ The value of the parameter. """
        if self.string:
            return self.string
        if self.token:
            return self.token
        if self.number:
            return self.number
        if self.date:
            return self.date
        if self.quantity:
            return self.quantity
        if self.reference:
            return self.reference
        return ''
    
    
    # MARK: Execution
    
    def as_search(self):
        """ Create a `FHIRSearch` representation of the chain up to the
        receiver. This is internally used for the `construct` and `perform`
        calls, which are executed on the FHIRSearch instance created here.
        """
        params = []
        prev = self
        while prev.previous is not None:
            params.insert(0, prev.as_param())
            prev = prev.previous
        
        if not prev.resource_type:
            raise Exception("The first search parameter needs to have \"resource_type\" set")
        
        srch = fhirsearch.FHIRSearch(prev.resource_type)
        srch.params = params
        return srch
    
    def construct(self):
        """ Construct and return the search query string.
        
        Use the `last` method to get the last param of a chain if needed, then
        call this method to create the parameter string of the whole chain.
        """
        return self.as_search().construct()
    
    def perform(self, server):
        """ Construct the search URL, execute it against the given server and
        return a list of instances created from returned data.
        """
        return self.as_search().perform(server)
    
    
    # MARK: Chaning
    
    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, prev):
        if self._previous == prev:
            return
        if self._previous is not None and self == self._previous.next:
            self._previous.next = None
        self._previous = prev
        prev.next = self
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, nxt):
        if self._next == nxt:
            return
        if self._next is not None and self == self._next.previous:
            self._next.previous = None
        self._next = nxt
        nxt.previous = self
    
    def first(self):
        if self._previous is not None:
            return self._previous.first()
        return self
    
    def last(self):
        if self._next is not None:
            return self._next.last()
        return self
    
