#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicinalProductAuthorization(domainresource.DomainResource):
    """ 
    T
    h
    e
    r
    e
    g
    u
    l
    a
    t
    o
    r
    y
    a
    u
    t
    h
    o
    r
    i
    z
    a
    t
    i
    o
    n
    o
    f
    a
    m
    e
    d
    i
    c
    i
    n
    a
    l
    p
    r
    o
    d
    u
    c
    t
    .
    """
    
    resource_type = "MedicinalProductAuthorization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ 
        T
        h
        e
        c
        o
        u
        n
        t
        r
        y
        i
        n
        w
        h
        i
        c
        h
        t
        h
        e
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        h
        a
        s
        b
        e
        e
        n
        g
        r
        a
        n
        t
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dataExclusivityPeriod = None
        """ 
        A
        p
        e
        r
        i
        o
        d
        o
        f
        t
        i
        m
        e
        a
        f
        t
        e
        r
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        b
        e
        f
        o
        r
        e
        g
        e
        n
        e
        r
        i
        c
        p
        r
        o
        d
        u
        c
        t
        a
        p
        p
        l
        i
        c
        a
        t
        i
        o
        s
        n
        c
        a
        n
        b
        e
        s
        u
        b
        m
        i
        t
        t
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.dateOfFirstAuthorization = None
        """ 
        T
        h
        e
        d
        a
        t
        e
        w
        h
        e
        n
        t
        h
        e
        f
        i
        r
        s
        t
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        w
        a
        s
        g
        r
        a
        n
        t
        e
        d
        b
        y
        a
        M
        e
        d
        i
        c
        i
        n
        e
        s
        R
        e
        g
        u
        l
        a
        t
        o
        r
        y
        A
        g
        e
        n
        c
        y
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.holder = None
        """ 
        M
        a
        r
        k
        e
        t
        i
        n
        g
        A
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        H
        o
        l
        d
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        f
        o
        r
        t
        h
        e
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        ,
        a
        s
        a
        s
        s
        i
        g
        n
        e
        d
        b
        y
        a
        r
        e
        g
        u
        l
        a
        t
        o
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.internationalBirthDate = None
        """ 
        D
        a
        t
        e
        o
        f
        f
        i
        r
        s
        t
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        f
        o
        r
        a
        c
        o
        m
        p
        a
        n
        y
        '
        s
        n
        e
        w
        m
        e
        d
        i
        c
        i
        n
        a
        l
        p
        r
        o
        d
        u
        c
        t
        i
        n
        a
        n
        y
        c
        o
        u
        n
        t
        r
        y
        i
        n
        t
        h
        e
        W
        o
        r
        l
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.jurisdiction = None
        """ 
        J
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        w
        i
        t
        h
        i
        n
        a
        c
        o
        u
        n
        t
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.jurisdictionalAuthorization = None
        """ 
        A
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        i
        n
        a
        r
        e
        a
        s
        w
        i
        t
        h
        i
        n
        a
        c
        o
        u
        n
        t
        r
        y
        .
        List of `MedicinalProductAuthorizationJurisdictionalAuthorization` items (represented as `dict` in JSON). """
        
        self.legalBasis = None
        """ 
        T
        h
        e
        l
        e
        g
        a
        l
        f
        r
        a
        m
        e
        w
        o
        r
        k
        a
        g
        a
        i
        n
        s
        t
        w
        h
        i
        c
        h
        t
        h
        i
        s
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        i
        s
        g
        r
        a
        n
        t
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ 
        T
        h
        e
        r
        e
        g
        u
        l
        a
        t
        o
        r
        y
        p
        r
        o
        c
        e
        d
        u
        r
        e
        f
        o
        r
        g
        r
        a
        n
        t
        i
        n
        g
        o
        r
        a
        m
        e
        n
        d
        i
        n
        g
        a
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        .
        Type `MedicinalProductAuthorizationProcedure` (represented as `dict` in JSON). """
        
        self.regulator = None
        """ 
        M
        e
        d
        i
        c
        i
        n
        e
        s
        R
        e
        g
        u
        l
        a
        t
        o
        r
        y
        A
        g
        e
        n
        c
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.restoreDate = None
        """ 
        T
        h
        e
        d
        a
        t
        e
        w
        h
        e
        n
        a
        s
        u
        s
        p
        e
        n
        d
        e
        d
        t
        h
        e
        m
        a
        r
        k
        e
        t
        i
        n
        g
        o
        r
        t
        h
        e
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        o
        f
        t
        h
        e
        p
        r
        o
        d
        u
        c
        t
        i
        s
        a
        n
        t
        i
        c
        i
        p
        a
        t
        e
        d
        t
        o
        b
        e
        r
        e
        s
        t
        o
        r
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ 
        T
        h
        e
        s
        t
        a
        t
        u
        s
        o
        f
        t
        h
        e
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.statusDate = None
        """ 
        T
        h
        e
        d
        a
        t
        e
        a
        t
        w
        h
        i
        c
        h
        t
        h
        e
        g
        i
        v
        e
        n
        s
        t
        a
        t
        u
        s
        h
        a
        s
        b
        e
        c
        o
        m
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None
        """ 
        T
        h
        e
        m
        e
        d
        i
        c
        i
        n
        a
        l
        p
        r
        o
        d
        u
        c
        t
        t
        h
        a
        t
        i
        s
        b
        e
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ 
        T
        h
        e
        b
        e
        g
        i
        n
        n
        i
        n
        g
        o
        f
        t
        h
        e
        t
        i
        m
        e
        p
        e
        r
        i
        o
        d
        i
        n
        w
        h
        i
        c
        h
        t
        h
        e
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        i
        s
        i
        n
        t
        h
        e
        s
        p
        e
        c
        i
        f
        i
        c
        s
        t
        a
        t
        u
        s
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        A
        c
        o
        m
        p
        l
        e
        t
        e
        d
        a
        t
        e
        c
        o
        n
        s
        i
        s
        t
        i
        n
        g
        o
        f
        d
        a
        y
        ,
        m
        o
        n
        t
        h
        a
        n
        d
        y
        e
        a
        r
        s
        h
        a
        l
        l
        b
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        u
        s
        i
        n
        g
        t
        h
        e
        I
        S
        O
        8
        6
        0
        1
        d
        a
        t
        e
        f
        o
        r
        m
        a
        t
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("dataExclusivityPeriod", "dataExclusivityPeriod", period.Period, False, None, False),
            ("dateOfFirstAuthorization", "dateOfFirstAuthorization", fhirdate.FHIRDate, False, None, False),
            ("holder", "holder", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("internationalBirthDate", "internationalBirthDate", fhirdate.FHIRDate, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdictionalAuthorization", "jurisdictionalAuthorization", MedicinalProductAuthorizationJurisdictionalAuthorization, True, None, False),
            ("legalBasis", "legalBasis", codeableconcept.CodeableConcept, False, None, False),
            ("procedure", "procedure", MedicinalProductAuthorizationProcedure, False, None, False),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False),
            ("restoreDate", "restoreDate", fhirdate.FHIRDate, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductAuthorizationJurisdictionalAuthorization(backboneelement.BackboneElement):
    """ 
    A
    u
    t
    h
    o
    r
    i
    z
    a
    t
    i
    o
    n
    i
    n
    a
    r
    e
    a
    s
    w
    i
    t
    h
    i
    n
    a
    c
    o
    u
    n
    t
    r
    y
    .
    """
    
    resource_type = "MedicinalProductAuthorizationJurisdictionalAuthorization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ 
        C
        o
        u
        n
        t
        r
        y
        o
        f
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        T
        h
        e
        a
        s
        s
        i
        g
        n
        e
        d
        n
        u
        m
        b
        e
        r
        f
        o
        r
        t
        h
        e
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ 
        J
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        w
        i
        t
        h
        i
        n
        a
        c
        o
        u
        n
        t
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.legalStatusOfSupply = None
        """ 
        T
        h
        e
        l
        e
        g
        a
        l
        s
        t
        a
        t
        u
        s
        o
        f
        s
        u
        p
        p
        l
        y
        i
        n
        a
        j
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        o
        r
        r
        e
        g
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ 
        T
        h
        e
        s
        t
        a
        r
        t
        a
        n
        d
        e
        x
        p
        e
        c
        t
        e
        d
        e
        n
        d
        d
        a
        t
        e
        o
        f
        t
        h
        e
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js


class MedicinalProductAuthorizationProcedure(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    r
    e
    g
    u
    l
    a
    t
    o
    r
    y
    p
    r
    o
    c
    e
    d
    u
    r
    e
    f
    o
    r
    g
    r
    a
    n
    t
    i
    n
    g
    o
    r
    a
    m
    e
    n
    d
    i
    n
    g
    a
    m
    a
    r
    k
    e
    t
    i
    n
    g
    a
    u
    t
    h
    o
    r
    i
    z
    a
    t
    i
    o
    n
    .
    """
    
    resource_type = "MedicinalProductAuthorizationProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.application = None
        """ 
        A
        p
        p
        l
        c
        a
        t
        i
        o
        n
        s
        s
        u
        b
        m
        i
        t
        t
        e
        d
        t
        o
        o
        b
        t
        a
        i
        n
        a
        m
        a
        r
        k
        e
        t
        i
        n
        g
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        .
        List of `MedicinalProductAuthorizationProcedure` items (represented as `dict` in JSON). """
        
        self.dateDateTime = None
        """ 
        D
        a
        t
        e
        o
        f
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.datePeriod = None
        """ 
        D
        a
        t
        e
        o
        f
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        I
        d
        e
        n
        t
        i
        f
        i
        e
        r
        f
        o
        r
        t
        h
        i
        s
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorizationProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationProcedure, self).elementProperties()
        js.extend([
            ("application", "application", MedicinalProductAuthorizationProcedure, True, None, False),
            ("dateDateTime", "dateDateTime", fhirdate.FHIRDate, False, "date", False),
            ("datePeriod", "datePeriod", period.Period, False, "date", False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
