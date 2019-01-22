#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProduct) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicinalProduct(domainresource.DomainResource):
    """ 
    D
    e
    t
    a
    i
    l
    e
    d
    d
    e
    f
    i
    n
    i
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
    ,
    t
    y
    p
    i
    c
    a
    l
    l
    y
    f
    o
    r
    u
    s
    e
    s
    o
    t
    h
    e
    r
    t
    h
    a
    n
    d
    i
    r
    e
    c
    t
    p
    a
    t
    i
    e
    n
    t
    c
    a
    r
    e
    (
    e
    .
    g
    .
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
    u
    s
    e
    )
    .
    """
    
    resource_type = "MedicinalProduct"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalMonitoringIndicator = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        h
        e
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
        i
        s
        s
        u
        b
        j
        e
        c
        t
        t
        o
        a
        d
        d
        i
        t
        i
        o
        n
        a
        l
        m
        o
        n
        i
        t
        o
        r
        i
        n
        g
        f
        o
        r
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
        r
        e
        a
        s
        o
        n
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.attachedDocument = None
        """ 
        S
        u
        p
        p
        o
        r
        t
        i
        n
        g
        d
        o
        c
        u
        m
        e
        n
        t
        a
        t
        i
        o
        n
        ,
        t
        y
        p
        i
        c
        a
        l
        l
        y
        f
        o
        r
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
        s
        u
        b
        m
        i
        s
        s
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.clinicalTrial = None
        """ 
        C
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
        s
        o
        r
        s
        t
        u
        d
        i
        e
        s
        t
        h
        a
        t
        t
        h
        i
        s
        p
        r
        o
        d
        u
        c
        t
        i
        s
        i
        n
        v
        o
        l
        v
        e
        d
        i
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.combinedPharmaceuticalDoseForm = None
        """ 
        T
        h
        e
        d
        o
        s
        e
        f
        o
        r
        m
        f
        o
        r
        a
        s
        i
        n
        g
        l
        e
        p
        a
        r
        t
        p
        r
        o
        d
        u
        c
        t
        ,
        o
        r
        c
        o
        m
        b
        i
        n
        e
        d
        f
        o
        r
        m
        o
        f
        a
        m
        u
        l
        t
        i
        p
        l
        e
        p
        a
        r
        t
        p
        r
        o
        d
        u
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ 
        A
        p
        r
        o
        d
        u
        c
        t
        s
        p
        e
        c
        i
        f
        i
        c
        c
        o
        n
        t
        a
        c
        t
        ,
        p
        e
        r
        s
        o
        n
        (
        i
        n
        a
        r
        o
        l
        e
        )
        ,
        o
        r
        a
        n
        o
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.crossReference = None
        """ 
        R
        e
        f
        e
        r
        e
        n
        c
        e
        t
        o
        a
        n
        o
        t
        h
        e
        r
        p
        r
        o
        d
        u
        c
        t
        ,
        e
        .
        g
        .
        f
        o
        r
        l
        i
        n
        k
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
        s
        e
        d
        t
        o
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
        
        self.domain = None
        """ 
        I
        f
        t
        h
        i
        s
        m
        e
        d
        i
        c
        i
        n
        e
        a
        p
        p
        l
        i
        e
        s
        t
        o
        h
        u
        m
        a
        n
        o
        r
        v
        e
        t
        e
        r
        i
        n
        a
        r
        y
        u
        s
        e
        s
        .
        Type `Coding` (represented as `dict` in JSON). """
        
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
        i
        s
        p
        r
        o
        d
        u
        c
        t
        .
        C
        o
        u
        l
        d
        b
        e
        a
        n
        M
        P
        I
        D
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
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
        o
        f
        t
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
        a
        s
        c
        l
        a
        s
        s
        i
        f
        i
        e
        d
        b
        y
        t
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manufacturingBusinessOperation = None
        """ 
        A
        n
        o
        p
        e
        r
        a
        t
        i
        o
        n
        a
        p
        p
        l
        i
        e
        d
        t
        o
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
        ,
        f
        o
        r
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        i
        n
        g
        o
        r
        a
        d
        m
        i
        n
        s
        i
        t
        r
        a
        t
        i
        v
        e
        p
        u
        r
        p
        o
        s
        e
        .
        List of `MedicinalProductManufacturingBusinessOperation` items (represented as `dict` in JSON). """
        
        self.marketingStatus = None
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
        ,
        i
        n
        c
        o
        n
        t
        r
        a
        s
        t
        t
        o
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
        o
        n
        .
        List of `MarketingStatus` items (represented as `dict` in JSON). """
        
        self.masterFile = None
        """ 
        A
        m
        a
        s
        t
        e
        r
        f
        i
        l
        e
        f
        o
        r
        t
        o
        t
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
        (
        e
        .
        g
        .
        P
        h
        a
        r
        m
        a
        c
        o
        v
        i
        g
        i
        l
        a
        n
        c
        e
        S
        y
        s
        t
        e
        m
        M
        a
        s
        t
        e
        r
        F
        i
        l
        e
        )
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        T
        h
        e
        p
        r
        o
        d
        u
        c
        t
        '
        s
        n
        a
        m
        e
        ,
        i
        n
        c
        l
        u
        d
        i
        n
        g
        f
        u
        l
        l
        n
        a
        m
        e
        a
        n
        d
        p
        o
        s
        s
        i
        b
        l
        y
        c
        o
        d
        e
        d
        p
        a
        r
        t
        s
        .
        List of `MedicinalProductName` items (represented as `dict` in JSON). """
        
        self.packagedMedicinalProduct = None
        """ 
        P
        a
        c
        k
        a
        g
        e
        r
        e
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        f
        o
        r
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.paediatricUseIndicator = None
        """ 
        I
        f
        a
        u
        t
        h
        o
        r
        i
        s
        e
        d
        f
        o
        r
        u
        s
        e
        i
        n
        c
        h
        i
        l
        d
        r
        e
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.pharmaceuticalProduct = None
        """ 
        P
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
        a
        s
        p
        e
        c
        t
        s
        o
        f
        p
        r
        o
        d
        u
        c
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.productClassification = None
        """ 
        A
        l
        l
        o
        w
        s
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
        t
        o
        b
        e
        c
        l
        a
        s
        s
        i
        f
        i
        e
        d
        b
        y
        v
        a
        r
        i
        o
        u
        s
        s
        y
        s
        t
        e
        m
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialDesignation = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
        i
        f
        t
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
        h
        a
        s
        a
        n
        o
        r
        p
        h
        a
        n
        d
        e
        s
        i
        g
        n
        a
        t
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
        r
        e
        a
        t
        m
        e
        n
        t
        o
        f
        a
        r
        a
        r
        e
        d
        i
        s
        e
        a
        s
        e
        .
        List of `MedicinalProductSpecialDesignation` items (represented as `dict` in JSON). """
        
        self.specialMeasures = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        h
        e
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
        i
        s
        s
        u
        b
        j
        e
        c
        t
        t
        o
        s
        p
        e
        c
        i
        a
        l
        m
        e
        a
        s
        u
        r
        e
        s
        f
        o
        r
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
        r
        e
        a
        s
        o
        n
        s
        .
        List of `str` items. """
        
        self.type = None
        """ 
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
        t
        y
        p
        e
        ,
        e
        .
        g
        .
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
        o
        r
        A
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProduct, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProduct, self).elementProperties()
        js.extend([
            ("additionalMonitoringIndicator", "additionalMonitoringIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("attachedDocument", "attachedDocument", fhirreference.FHIRReference, True, None, False),
            ("clinicalTrial", "clinicalTrial", fhirreference.FHIRReference, True, None, False),
            ("combinedPharmaceuticalDoseForm", "combinedPharmaceuticalDoseForm", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", fhirreference.FHIRReference, True, None, False),
            ("crossReference", "crossReference", identifier.Identifier, True, None, False),
            ("domain", "domain", coding.Coding, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("manufacturingBusinessOperation", "manufacturingBusinessOperation", MedicinalProductManufacturingBusinessOperation, True, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("masterFile", "masterFile", fhirreference.FHIRReference, True, None, False),
            ("name", "name", MedicinalProductName, True, None, True),
            ("packagedMedicinalProduct", "packagedMedicinalProduct", fhirreference.FHIRReference, True, None, False),
            ("paediatricUseIndicator", "paediatricUseIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("pharmaceuticalProduct", "pharmaceuticalProduct", fhirreference.FHIRReference, True, None, False),
            ("productClassification", "productClassification", codeableconcept.CodeableConcept, True, None, False),
            ("specialDesignation", "specialDesignation", MedicinalProductSpecialDesignation, True, None, False),
            ("specialMeasures", "specialMeasures", str, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductManufacturingBusinessOperation(backboneelement.BackboneElement):
    """ 
    A
    n
    o
    p
    e
    r
    a
    t
    i
    o
    n
    a
    p
    p
    l
    i
    e
    d
    t
    o
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
    ,
    f
    o
    r
    m
    a
    n
    u
    f
    a
    c
    t
    u
    r
    i
    n
    g
    o
    r
    a
    d
    m
    i
    n
    s
    i
    t
    r
    a
    t
    i
    v
    e
    p
    u
    r
    p
    o
    s
    e
    .
    """
    
    resource_type = "MedicinalProductManufacturingBusinessOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorisationReferenceNumber = None
        """ 
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
        r
        e
        f
        e
        r
        e
        n
        c
        e
        n
        u
        m
        b
        e
        r
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.confidentialityIndicator = None
        """ 
        T
        o
        i
        n
        d
        i
        c
        a
        t
        e
        i
        f
        t
        h
        i
        s
        p
        r
        o
        c
        e
        s
        i
        s
        c
        o
        m
        m
        e
        r
        c
        i
        a
        l
        l
        y
        c
        o
        n
        f
        i
        d
        e
        n
        t
        i
        a
        l
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.effectiveDate = None
        """ 
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
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.manufacturer = None
        """ 
        T
        h
        e
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        r
        o
        r
        e
        s
        t
        a
        b
        l
        i
        s
        h
        m
        e
        n
        t
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        t
        h
        e
        p
        r
        o
        c
        e
        s
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.operationType = None
        """ 
        T
        h
        e
        t
        y
        p
        e
        o
        f
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        i
        n
        g
        o
        p
        e
        r
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.regulator = None
        """ 
        A
        r
        e
        g
        u
        l
        a
        t
        o
        r
        w
        h
        i
        c
        h
        o
        v
        e
        r
        s
        e
        e
        s
        t
        h
        e
        o
        p
        e
        r
        a
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MedicinalProductManufacturingBusinessOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductManufacturingBusinessOperation, self).elementProperties()
        js.extend([
            ("authorisationReferenceNumber", "authorisationReferenceNumber", identifier.Identifier, False, None, False),
            ("confidentialityIndicator", "confidentialityIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("effectiveDate", "effectiveDate", fhirdate.FHIRDate, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("operationType", "operationType", codeableconcept.CodeableConcept, False, None, False),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class MedicinalProductName(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    p
    r
    o
    d
    u
    c
    t
    '
    s
    n
    a
    m
    e
    ,
    i
    n
    c
    l
    u
    d
    i
    n
    g
    f
    u
    l
    l
    n
    a
    m
    e
    a
    n
    d
    p
    o
    s
    s
    i
    b
    l
    y
    c
    o
    d
    e
    d
    p
    a
    r
    t
    s
    .
    """
    
    resource_type = "MedicinalProductName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.countryLanguage = None
        """ 
        C
        o
        u
        n
        t
        r
        y
        w
        h
        e
        r
        e
        t
        h
        e
        n
        a
        m
        e
        a
        p
        p
        l
        i
        e
        s
        .
        List of `MedicinalProductNameCountryLanguage` items (represented as `dict` in JSON). """
        
        self.namePart = None
        """ 
        C
        o
        d
        i
        n
        g
        w
        o
        r
        d
        s
        o
        r
        p
        h
        r
        a
        s
        e
        s
        o
        f
        t
        h
        e
        n
        a
        m
        e
        .
        List of `MedicinalProductNameNamePart` items (represented as `dict` in JSON). """
        
        self.productName = None
        """ 
        T
        h
        e
        f
        u
        l
        l
        p
        r
        o
        d
        u
        c
        t
        n
        a
        m
        e
        .
        Type `str`. """
        
        super(MedicinalProductName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductName, self).elementProperties()
        js.extend([
            ("countryLanguage", "countryLanguage", MedicinalProductNameCountryLanguage, True, None, False),
            ("namePart", "namePart", MedicinalProductNameNamePart, True, None, False),
            ("productName", "productName", str, False, None, True),
        ])
        return js


class MedicinalProductNameCountryLanguage(backboneelement.BackboneElement):
    """ 
    C
    o
    u
    n
    t
    r
    y
    w
    h
    e
    r
    e
    t
    h
    e
    n
    a
    m
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
    
    resource_type = "MedicinalProductNameCountryLanguage"
    
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
        c
        o
        d
        e
        f
        o
        r
        w
        h
        e
        r
        e
        t
        h
        i
        s
        n
        a
        m
        e
        a
        p
        p
        l
        i
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        c
        o
        d
        e
        f
        o
        r
        w
        h
        e
        r
        e
        t
        h
        i
        s
        n
        a
        m
        e
        a
        p
        p
        l
        i
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.language = None
        """ 
        L
        a
        n
        g
        u
        a
        g
        e
        c
        o
        d
        e
        f
        o
        r
        t
        h
        i
        s
        n
        a
        m
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductNameCountryLanguage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductNameCountryLanguage, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicinalProductNameNamePart(backboneelement.BackboneElement):
    """ 
    C
    o
    d
    i
    n
    g
    w
    o
    r
    d
    s
    o
    r
    p
    h
    r
    a
    s
    e
    s
    o
    f
    t
    h
    e
    n
    a
    m
    e
    .
    """
    
    resource_type = "MedicinalProductNameNamePart"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.part = None
        """ 
        A
        f
        r
        a
        g
        m
        e
        n
        t
        o
        f
        a
        p
        r
        o
        d
        u
        c
        t
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        I
        d
        e
        n
        i
        f
        y
        i
        n
        g
        t
        y
        p
        e
        f
        o
        r
        t
        h
        i
        s
        p
        a
        r
        t
        o
        f
        t
        h
        e
        n
        a
        m
        e
        (
        e
        .
        g
        .
        s
        t
        r
        e
        n
        g
        t
        h
        p
        a
        r
        t
        )
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        super(MedicinalProductNameNamePart, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductNameNamePart, self).elementProperties()
        js.extend([
            ("part", "part", str, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class MedicinalProductSpecialDesignation(backboneelement.BackboneElement):
    """ 
    I
    n
    d
    i
    c
    a
    t
    e
    s
    i
    f
    t
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
    h
    a
    s
    a
    n
    o
    r
    p
    h
    a
    n
    d
    e
    s
    i
    g
    n
    a
    t
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
    r
    e
    a
    t
    m
    e
    n
    t
    o
    f
    a
    r
    a
    r
    e
    d
    i
    s
    e
    a
    s
    e
    .
    """
    
    resource_type = "MedicinalProductSpecialDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ 
        D
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
        d
        e
        s
        i
        g
        n
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
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        e
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        ,
        o
        r
        p
        r
        o
        c
        e
        d
        u
        r
        e
        n
        u
        m
        b
        e
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indicationCodeableConcept = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
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
        m
        e
        d
        i
        c
        i
        n
        a
        l
        u
        s
        e
        a
        p
        p
        l
        i
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.indicationReference = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
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
        m
        e
        d
        i
        c
        i
        n
        a
        l
        u
        s
        e
        a
        p
        p
        l
        i
        e
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.intendedUse = None
        """ 
        T
        h
        e
        i
        n
        t
        e
        n
        d
        e
        d
        u
        s
        e
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
        ,
        e
        .
        g
        .
        p
        r
        e
        v
        e
        n
        t
        i
        o
        n
        ,
        t
        r
        e
        a
        t
        m
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.species = None
        """ 
        A
        n
        i
        m
        a
        l
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
        a
        p
        p
        l
        i
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        F
        o
        r
        e
        x
        a
        m
        p
        l
        e
        g
        r
        a
        n
        t
        e
        d
        ,
        p
        e
        n
        d
        i
        n
        g
        ,
        e
        x
        p
        i
        r
        e
        d
        o
        r
        w
        i
        t
        h
        d
        r
        a
        w
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        h
        e
        t
        y
        p
        e
        o
        f
        s
        p
        e
        c
        i
        a
        l
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        ,
        e
        .
        g
        .
        o
        r
        p
        h
        a
        n
        d
        r
        u
        g
        ,
        m
        i
        n
        o
        r
        u
        s
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductSpecialDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductSpecialDesignation, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", codeableconcept.CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", fhirreference.FHIRReference, False, "indication", False),
            ("intendedUse", "intendedUse", codeableconcept.CodeableConcept, False, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
    from . import marketingstatus
except ImportError:
    marketingstatus = sys.modules[__package__ + '.marketingstatus']
