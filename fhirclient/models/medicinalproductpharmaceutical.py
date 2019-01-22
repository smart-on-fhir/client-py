#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicinalProductPharmaceutical(domainresource.DomainResource):
    """ 
    A
    p
    h
    a
    r
    m
    a
    c
    e
    u
    t
    i
    c
    a
    l
    p
    r
    o
    d
    u
    c
    t
    d
    e
    s
    c
    r
    i
    b
    e
    d
    i
    n
    t
    e
    r
    m
    s
    o
    f
    i
    t
    s
    c
    o
    m
    p
    o
    s
    i
    t
    i
    o
    n
    a
    n
    d
    d
    o
    s
    e
    f
    o
    r
    m
    .
    """
    
    resource_type = "MedicinalProductPharmaceutical"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.administrableDoseForm = None
        """ 
        T
        h
        e
        a
        d
        m
        i
        n
        i
        s
        t
        r
        a
        b
        l
        e
        d
        o
        s
        e
        f
        o
        r
        m
        ,
        a
        f
        t
        e
        r
        n
        e
        c
        e
        s
        s
        a
        r
        y
        r
        e
        c
        o
        n
        s
        t
        i
        t
        u
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.characteristics = None
        """ 
        C
        h
        a
        r
        a
        c
        t
        e
        r
        i
        s
        t
        i
        c
        s
        e
        .
        g
        .
        a
        p
        r
        o
        d
        u
        c
        t
        s
        o
        n
        s
        e
        t
        o
        f
        a
        c
        t
        i
        o
        n
        .
        List of `MedicinalProductPharmaceuticalCharacteristics` items (represented as `dict` in JSON). """
        
        self.device = None
        """ 
        A
        c
        c
        o
        m
        p
        a
        n
        y
        i
        n
        g
        d
        e
        v
        i
        c
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        A
        n
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
        p
        h
        a
        r
        m
        a
        c
        e
        u
        t
        i
        c
        a
        l
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
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ 
        I
        n
        g
        r
        e
        d
        i
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.routeOfAdministration = None
        """ 
        T
        h
        e
        p
        a
        t
        h
        b
        y
        w
        h
        i
        c
        h
        t
        h
        e
        p
        h
        a
        r
        m
        a
        c
        e
        u
        t
        i
        c
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
        s
        t
        a
        k
        e
        n
        i
        n
        t
        o
        o
        r
        m
        a
        k
        e
        s
        c
        o
        n
        t
        a
        c
        t
        w
        i
        t
        h
        t
        h
        e
        b
        o
        d
        y
        .
        List of `MedicinalProductPharmaceuticalRouteOfAdministration` items (represented as `dict` in JSON). """
        
        self.unitOfPresentation = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceutical, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceutical, self).elementProperties()
        js.extend([
            ("administrableDoseForm", "administrableDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("characteristics", "characteristics", MedicinalProductPharmaceuticalCharacteristics, True, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False),
            ("routeOfAdministration", "routeOfAdministration", MedicinalProductPharmaceuticalRouteOfAdministration, True, None, True),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductPharmaceuticalCharacteristics(backboneelement.BackboneElement):
    """ 
    C
    h
    a
    r
    a
    c
    t
    e
    r
    i
    s
    t
    i
    c
    s
    e
    .
    g
    .
    a
    p
    r
    o
    d
    u
    c
    t
    s
    o
    n
    s
    e
    t
    o
    f
    a
    c
    t
    i
    o
    n
    .
    """
    
    resource_type = "MedicinalProductPharmaceuticalCharacteristics"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        A
        c
        o
        d
        e
        d
        c
        h
        a
        r
        a
        c
        t
        e
        r
        i
        s
        t
        i
        c
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        c
        h
        a
        r
        a
        c
        t
        e
        r
        i
        s
        t
        i
        c
        e
        .
        g
        .
        a
        s
        s
        i
        g
        n
        e
        d
        o
        r
        p
        e
        n
        d
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalCharacteristics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalCharacteristics, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministration(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    p
    a
    t
    h
    b
    y
    w
    h
    i
    c
    h
    t
    h
    e
    p
    h
    a
    r
    m
    a
    c
    e
    u
    t
    i
    c
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
    s
    t
    a
    k
    e
    n
    i
    n
    t
    o
    o
    r
    m
    a
    k
    e
    s
    c
    o
    n
    t
    a
    c
    t
    w
    i
    t
    h
    t
    h
    e
    b
    o
    d
    y
    .
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        C
        o
        d
        e
        d
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        f
        o
        r
        t
        h
        e
        r
        o
        u
        t
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.firstDose = None
        """ 
        T
        h
        e
        f
        i
        r
        s
        t
        d
        o
        s
        e
        (
        d
        o
        s
        e
        q
        u
        a
        n
        t
        i
        t
        y
        )
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        i
        n
        h
        u
        m
        a
        n
        s
        c
        a
        n
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
        ,
        f
        o
        r
        a
        p
        r
        o
        d
        u
        c
        t
        u
        n
        d
        e
        r
        i
        n
        v
        e
        s
        t
        i
        g
        a
        t
        i
        o
        n
        ,
        u
        s
        i
        n
        g
        a
        n
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        a
        n
        d
        i
        t
        s
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerDay = None
        """ 
        T
        h
        e
        m
        a
        x
        i
        m
        u
        m
        d
        o
        s
        e
        p
        e
        r
        d
        a
        y
        (
        m
        a
        x
        i
        m
        u
        m
        d
        o
        s
        e
        q
        u
        a
        n
        t
        i
        t
        y
        t
        o
        b
        e
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        i
        n
        a
        n
        y
        o
        n
        e
        2
        4
        -
        h
        p
        e
        r
        i
        o
        d
        )
        t
        h
        a
        t
        c
        a
        n
        b
        e
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        a
        s
        p
        e
        r
        t
        h
        e
        p
        r
        o
        t
        o
        c
        o
        l
        r
        e
        f
        e
        r
        e
        n
        c
        e
        d
        i
        n
        t
        h
        e
        c
        l
        i
        n
        i
        c
        a
        l
        t
        r
        i
        a
        l
        a
        u
        t
        h
        o
        r
        i
        s
        a
        t
        i
        o
        n
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerTreatmentPeriod = None
        """ 
        T
        h
        e
        m
        a
        x
        i
        m
        u
        m
        d
        o
        s
        e
        p
        e
        r
        t
        r
        e
        a
        t
        m
        e
        n
        t
        p
        e
        r
        i
        o
        d
        t
        h
        a
        t
        c
        a
        n
        b
        e
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        a
        s
        p
        e
        r
        t
        h
        e
        p
        r
        o
        t
        o
        c
        o
        l
        r
        e
        f
        e
        r
        e
        n
        c
        e
        d
        i
        n
        t
        h
        e
        c
        l
        i
        n
        i
        c
        a
        l
        t
        r
        i
        a
        l
        a
        u
        t
        h
        o
        r
        i
        s
        a
        t
        i
        o
        n
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.maxSingleDose = None
        """ 
        T
        h
        e
        m
        a
        x
        i
        m
        u
        m
        s
        i
        n
        g
        l
        e
        d
        o
        s
        e
        t
        h
        a
        t
        c
        a
        n
        b
        e
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        a
        s
        p
        e
        r
        t
        h
        e
        p
        r
        o
        t
        o
        c
        o
        l
        o
        f
        a
        c
        l
        i
        n
        i
        c
        a
        l
        t
        r
        i
        a
        l
        c
        a
        n
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
        a
        n
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        a
        n
        d
        i
        t
        s
        u
        n
        i
        t
        o
        f
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxTreatmentPeriod = None
        """ 
        T
        h
        e
        m
        a
        x
        i
        m
        u
        m
        t
        r
        e
        a
        t
        m
        e
        n
        t
        p
        e
        r
        i
        o
        d
        d
        u
        r
        i
        n
        g
        w
        h
        i
        c
        h
        a
        n
        I
        n
        v
        e
        s
        t
        i
        g
        a
        t
        i
        o
        n
        a
        l
        M
        e
        d
        i
        c
        i
        n
        a
        l
        P
        r
        o
        d
        u
        c
        t
        c
        a
        n
        b
        e
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        a
        s
        p
        e
        r
        t
        h
        e
        p
        r
        o
        t
        o
        c
        o
        l
        r
        e
        f
        e
        r
        e
        n
        c
        e
        d
        i
        n
        t
        h
        e
        c
        l
        i
        n
        i
        c
        a
        l
        t
        r
        i
        a
        l
        a
        u
        t
        h
        o
        r
        i
        s
        a
        t
        i
        o
        n
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.targetSpecies = None
        """ 
        A
        s
        p
        e
        c
        i
        e
        s
        f
        o
        r
        w
        h
        i
        c
        h
        t
        h
        i
        s
        r
        o
        u
        t
        e
        a
        p
        p
        l
        i
        e
        s
        .
        List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("firstDose", "firstDose", quantity.Quantity, False, None, False),
            ("maxDosePerDay", "maxDosePerDay", quantity.Quantity, False, None, False),
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", ratio.Ratio, False, None, False),
            ("maxSingleDose", "maxSingleDose", quantity.Quantity, False, None, False),
            ("maxTreatmentPeriod", "maxTreatmentPeriod", duration.Duration, False, None, False),
            ("targetSpecies", "targetSpecies", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, True, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(backboneelement.BackboneElement):
    """ 
    A
    s
    p
    e
    c
    i
    e
    s
    f
    o
    r
    w
    h
    i
    c
    h
    t
    h
    i
    s
    r
    o
    u
    t
    e
    a
    p
    p
    l
    i
    e
    s
    .
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        C
        o
        d
        e
        d
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        f
        o
        r
        t
        h
        e
        s
        p
        e
        c
        i
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.withdrawalPeriod = None
        """ 
        A
        s
        p
        e
        c
        i
        e
        s
        s
        p
        e
        c
        i
        f
        i
        c
        t
        i
        m
        e
        d
        u
        r
        i
        n
        g
        w
        h
        i
        c
        h
        c
        o
        n
        s
        u
        m
        p
        t
        i
        o
        n
        o
        f
        a
        n
        i
        m
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
        s
        n
        o
        t
        a
        p
        p
        r
        o
        p
        r
        i
        a
        t
        e
        .
        List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("withdrawalPeriod", "withdrawalPeriod", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(backboneelement.BackboneElement):
    """ 
    A
    s
    p
    e
    c
    i
    e
    s
    s
    p
    e
    c
    i
    f
    i
    c
    t
    i
    m
    e
    d
    u
    r
    i
    n
    g
    w
    h
    i
    c
    h
    c
    o
    n
    s
    u
    m
    p
    t
    i
    o
    n
    o
    f
    a
    n
    i
    m
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
    s
    n
    o
    t
    a
    p
    p
    r
    o
    p
    r
    i
    a
    t
    e
    .
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.supportingInformation = None
        """ 
        E
        x
        t
        r
        a
        i
        n
        f
        o
        r
        m
        a
        t
        i
        o
        n
        a
        b
        o
        u
        t
        t
        h
        e
        w
        i
        t
        h
        d
        r
        a
        w
        a
        l
        p
        e
        r
        i
        o
        d
        .
        Type `str`. """
        
        self.tissue = None
        """ 
        C
        o
        d
        e
        d
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        f
        o
        r
        t
        h
        e
        t
        y
        p
        e
        o
        f
        t
        i
        s
        s
        u
        e
        f
        o
        r
        w
        h
        i
        c
        h
        t
        h
        e
        w
        i
        t
        h
        d
        r
        a
        w
        a
        l
        p
        e
        r
        i
        o
        d
        a
        p
        p
        l
        u
        e
        s
        ,
        e
        .
        g
        .
        m
        e
        a
        t
        ,
        m
        i
        l
        k
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        A
        v
        a
        l
        u
        e
        f
        o
        r
        t
        h
        e
        t
        i
        m
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("supportingInformation", "supportingInformation", str, False, None, False),
            ("tissue", "tissue", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
