#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceSpecification) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class SubstanceSpecification(domainresource.DomainResource):
    """ 
    T
    h
    e
    d
    e
    t
    a
    i
    l
    e
    d
    d
    e
    s
    c
    r
    i
    p
    t
    i
    o
    n
    o
    f
    a
    s
    u
    b
    s
    t
    a
    n
    c
    e
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
    a
    t
    a
    l
    e
    v
    e
    l
    b
    e
    y
    o
    n
    d
    w
    h
    a
    t
    i
    s
    u
    s
    e
    d
    f
    o
    r
    p
    r
    e
    s
    c
    r
    i
    b
    i
    n
    g
    .
    """
    
    resource_type = "SubstanceSpecification"
    
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
        s
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
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        List of `SubstanceSpecificationstr` items (represented as `dict` in JSON). """
        
        self.comment = None
        """ 
        T
        e
        x
        t
        u
        a
        l
        c
        o
        m
        m
        e
        n
        t
        a
        b
        o
        u
        t
        t
        h
        i
        s
        r
        e
        c
        o
        r
        d
        o
        f
        a
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.description = None
        """ 
        T
        e
        x
        t
        u
        a
        l
        d
        e
        s
        c
        r
        i
        p
        t
        i
        o
        n
        o
        f
        t
        h
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.domain = None
        """ 
        I
        f
        t
        h
        e
        s
        u
        b
        s
        t
        a
        n
        c
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
        o
        n
        l
        y
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        b
        y
        w
        h
        i
        c
        h
        t
        h
        i
        s
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        s
        k
        n
        o
        w
        n
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.moiety = None
        """ 
        M
        o
        i
        e
        t
        y
        ,
        f
        o
        r
        s
        t
        r
        u
        c
        t
        u
        r
        a
        l
        m
        o
        d
        i
        f
        i
        c
        a
        t
        i
        o
        n
        s
        .
        List of `SubstanceSpecificationMoiety` items (represented as `dict` in JSON). """
        
        self.molecularWeight = None
        """ 
        T
        h
        e
        m
        o
        l
        e
        c
        u
        l
        a
        r
        w
        e
        i
        g
        h
        t
        o
        r
        w
        e
        i
        g
        h
        t
        r
        a
        n
        g
        e
        (
        f
        o
        r
        p
        r
        o
        t
        e
        i
        n
        s
        ,
        p
        o
        l
        y
        m
        e
        r
        s
        o
        r
        n
        u
        c
        l
        e
        i
        c
        a
        c
        i
        d
        s
        )
        .
        List of `SubstanceSpecificationStructureIsotopeMolecularWeight` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        N
        a
        m
        e
        s
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
        t
        o
        t
        h
        i
        s
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        
        self.nucleicAcid = None
        """ 
        D
        a
        t
        a
        i
        t
        e
        m
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
        o
        n
        u
        c
        l
        e
        i
        c
        a
        c
        i
        d
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.polymer = None
        """ 
        D
        a
        t
        a
        i
        t
        e
        m
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
        o
        p
        o
        l
        y
        m
        e
        r
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.property = None
        """ 
        G
        e
        n
        e
        r
        a
        l
        s
        p
        e
        c
        i
        f
        i
        c
        a
        t
        i
        o
        n
        s
        f
        o
        r
        t
        h
        i
        s
        s
        u
        b
        s
        t
        a
        n
        c
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
        h
        o
        w
        i
        t
        i
        s
        r
        e
        l
        a
        t
        e
        d
        t
        o
        o
        t
        h
        e
        r
        s
        u
        b
        s
        t
        a
        n
        c
        e
        s
        .
        List of `SubstanceSpecificationProperty` items (represented as `dict` in JSON). """
        
        self.protein = None
        """ 
        D
        a
        t
        a
        i
        t
        e
        m
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
        o
        p
        r
        o
        t
        e
        i
        n
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceInformation = None
        """ 
        G
        e
        n
        e
        r
        a
        l
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
        d
        e
        t
        a
        i
        l
        i
        n
        g
        t
        h
        i
        s
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        A
        l
        i
        n
        k
        b
        e
        t
        w
        e
        e
        n
        t
        h
        i
        s
        s
        u
        b
        s
        t
        a
        n
        c
        e
        a
        n
        d
        a
        n
        o
        t
        h
        e
        r
        ,
        w
        i
        t
        h
        d
        e
        t
        a
        i
        l
        s
        o
        f
        t
        h
        e
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        .
        List of `SubstanceSpecificationRelationship` items (represented as `dict` in JSON). """
        
        self.source = None
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
        l
        i
        t
        e
        r
        a
        t
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sourceMaterial = None
        """ 
        M
        a
        t
        e
        r
        i
        a
        l
        o
        r
        t
        a
        x
        o
        n
        o
        m
        i
        c
        /
        a
        n
        a
        t
        o
        m
        i
        c
        a
        l
        s
        o
        u
        r
        c
        e
        f
        o
        r
        t
        h
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        S
        t
        a
        t
        u
        s
        o
        f
        s
        u
        b
        s
        t
        a
        n
        c
        e
        w
        i
        t
        h
        i
        n
        t
        h
        e
        c
        a
        t
        a
        l
        o
        g
        u
        e
        e
        .
        g
        .
        a
        p
        p
        r
        o
        v
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.structure = None
        """ 
        S
        t
        r
        u
        c
        t
        u
        r
        a
        l
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
        .
        Type `SubstanceSpecificationStructure` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        H
        i
        g
        h
        l
        e
        v
        e
        l
        c
        a
        t
        e
        g
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
        e
        .
        g
        .
        p
        o
        l
        y
        m
        e
        r
        o
        r
        n
        u
        c
        l
        e
        i
        c
        a
        c
        i
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecification, self).elementProperties()
        js.extend([
            ("code", "code", SubstanceSpecificationstr, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("moiety", "moiety", SubstanceSpecificationMoiety, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, True, None, False),
            ("name", "name", SubstanceSpecificationName, True, None, False),
            ("nucleicAcid", "nucleicAcid", fhirreference.FHIRReference, False, None, False),
            ("polymer", "polymer", fhirreference.FHIRReference, False, None, False),
            ("property", "property", SubstanceSpecificationProperty, True, None, False),
            ("protein", "protein", fhirreference.FHIRReference, False, None, False),
            ("referenceInformation", "referenceInformation", fhirreference.FHIRReference, False, None, False),
            ("relationship", "relationship", SubstanceSpecificationRelationship, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("sourceMaterial", "sourceMaterial", fhirreference.FHIRReference, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("structure", "structure", SubstanceSpecificationStructure, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class SubstanceSpecificationMoiety(backboneelement.BackboneElement):
    """ 
    M
    o
    i
    e
    t
    y
    ,
    f
    o
    r
    s
    t
    r
    u
    c
    t
    u
    r
    a
    l
    m
    o
    d
    i
    f
    i
    c
    a
    t
    i
    o
    n
    s
    .
    """
    
    resource_type = "SubstanceSpecificationMoiety"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ 
        Q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
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
        i
        s
        m
        o
        i
        e
        t
        y
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.amountString = None
        """ 
        Q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
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
        i
        s
        m
        o
        i
        e
        t
        y
        .
        Type `str`. """
        
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
        b
        y
        w
        h
        i
        c
        h
        t
        h
        i
        s
        m
        o
        i
        e
        t
        y
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        s
        k
        n
        o
        w
        n
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.molecularFormula = None
        """ 
        M
        o
        l
        e
        c
        u
        l
        a
        r
        f
        o
        r
        m
        u
        l
        a
        .
        Type `str`. """
        
        self.name = None
        """ 
        T
        e
        x
        t
        u
        a
        l
        n
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        m
        o
        i
        e
        t
        y
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.opticalActivity = None
        """ 
        O
        p
        t
        i
        c
        a
        l
        a
        c
        t
        i
        v
        i
        t
        y
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        R
        o
        l
        e
        t
        h
        a
        t
        t
        h
        e
        m
        o
        i
        e
        t
        y
        i
        s
        p
        l
        a
        y
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stereochemistry = None
        """ 
        S
        t
        e
        r
        e
        o
        c
        h
        e
        m
        i
        s
        t
        r
        y
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationMoiety, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationMoiety, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationName(backboneelement.BackboneElement):
    """ 
    N
    a
    m
    e
    s
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
    t
    o
    t
    h
    i
    s
    s
    u
    b
    s
    t
    a
    n
    c
    e
    .
    """
    
    resource_type = "SubstanceSpecificationName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.domain = None
        """ 
        T
        h
        e
        u
        s
        e
        c
        o
        n
        t
        e
        x
        t
        o
        f
        t
        h
        i
        s
        n
        a
        m
        e
        f
        o
        r
        e
        x
        a
        m
        p
        l
        e
        i
        f
        t
        h
        e
        r
        e
        i
        s
        a
        d
        i
        f
        f
        e
        r
        e
        n
        t
        n
        a
        m
        e
        a
        d
        r
        u
        g
        a
        c
        t
        i
        v
        e
        i
        n
        g
        r
        e
        d
        i
        e
        n
        t
        a
        s
        o
        p
        p
        o
        s
        e
        d
        t
        o
        a
        f
        o
        o
        d
        c
        o
        l
        o
        u
        r
        a
        d
        d
        i
        t
        i
        v
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ 
        T
        h
        e
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        T
        h
        e
        a
        c
        t
        u
        a
        l
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.official = None
        """ 
        D
        e
        t
        a
        i
        l
        s
        o
        f
        t
        h
        e
        o
        f
        f
        i
        c
        i
        a
        l
        n
        a
        t
        u
        r
        e
        o
        f
        t
        h
        i
        s
        n
        a
        m
        e
        .
        List of `SubstanceSpecificationNameOfficial` items (represented as `dict` in JSON). """
        
        self.preferred = None
        """ 
        I
        f
        t
        h
        i
        s
        i
        s
        t
        h
        e
        p
        r
        e
        f
        e
        r
        r
        e
        d
        n
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `bool`. """
        
        self.source = None
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
        l
        i
        t
        e
        r
        a
        t
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        n
        a
        m
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.synonym = None
        """ 
        A
        s
        y
        n
        o
        n
        y
        m
        o
        f
        t
        h
        i
        s
        n
        a
        m
        e
        .
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        
        self.translation = None
        """ 
        A
        t
        r
        a
        n
        s
        l
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
        i
        s
        n
        a
        m
        e
        .
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        N
        a
        m
        e
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationName, self).elementProperties()
        js.extend([
            ("domain", "domain", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("language", "language", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("official", "official", SubstanceSpecificationNameOfficial, True, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("synonym", "synonym", SubstanceSpecificationName, True, None, False),
            ("translation", "translation", SubstanceSpecificationName, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationNameOfficial(backboneelement.BackboneElement):
    """ 
    D
    e
    t
    a
    i
    l
    s
    o
    f
    t
    h
    e
    o
    f
    f
    i
    c
    i
    a
    l
    n
    a
    t
    u
    r
    e
    o
    f
    t
    h
    i
    s
    n
    a
    m
    e
    .
    """
    
    resource_type = "SubstanceSpecificationNameOfficial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ 
        W
        h
        i
        c
        h
        a
        u
        t
        h
        o
        r
        i
        t
        y
        u
        s
        e
        s
        t
        h
        i
        s
        o
        f
        f
        i
        c
        i
        a
        l
        n
        a
        m
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        D
        a
        t
        e
        o
        f
        o
        f
        f
        i
        c
        i
        a
        l
        n
        a
        m
        e
        c
        h
        a
        n
        g
        e
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
        o
        f
        f
        i
        c
        i
        a
        l
        n
        a
        m
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationNameOfficial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationNameOfficial, self).elementProperties()
        js.extend([
            ("authority", "authority", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationProperty(backboneelement.BackboneElement):
    """ 
    G
    e
    n
    e
    r
    a
    l
    s
    p
    e
    c
    i
    f
    i
    c
    a
    t
    i
    o
    n
    s
    f
    o
    r
    t
    h
    i
    s
    s
    u
    b
    s
    t
    a
    n
    c
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
    h
    o
    w
    i
    t
    i
    s
    r
    e
    l
    a
    t
    e
    d
    t
    o
    o
    t
    h
    e
    r
    s
    u
    b
    s
    t
    a
    n
    c
    e
    s
    .
    """
    
    resource_type = "SubstanceSpecificationProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ 
        Q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
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
        i
        s
        p
        r
        o
        p
        e
        r
        t
        y
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.amountString = None
        """ 
        Q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
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
        i
        s
        p
        r
        o
        p
        e
        r
        t
        y
        .
        Type `str`. """
        
        self.category = None
        """ 
        A
        c
        a
        t
        e
        g
        o
        r
        y
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
        p
        e
        r
        t
        y
        ,
        e
        .
        g
        .
        P
        h
        y
        s
        i
        c
        a
        l
        ,
        C
        h
        e
        m
        i
        c
        a
        l
        ,
        E
        n
        z
        y
        m
        a
        t
        i
        c
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        P
        r
        o
        p
        e
        r
        t
        y
        t
        y
        p
        e
        e
        .
        g
        .
        v
        i
        s
        c
        o
        s
        i
        t
        y
        ,
        p
        H
        ,
        i
        s
        o
        e
        l
        e
        c
        t
        r
        i
        c
        p
        o
        i
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definingSubstanceCodeableConcept = None
        """ 
        A
        s
        u
        b
        s
        t
        a
        n
        c
        e
        u
        p
        o
        n
        w
        h
        i
        c
        h
        a
        d
        e
        f
        i
        n
        i
        n
        g
        p
        r
        o
        p
        e
        r
        t
        y
        d
        e
        p
        e
        n
        d
        s
        (
        e
        .
        g
        .
        f
        o
        r
        s
        o
        l
        u
        b
        i
        l
        i
        t
        y
        :
        i
        n
        w
        a
        t
        e
        r
        ,
        i
        n
        a
        l
        c
        o
        h
        o
        l
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definingSubstanceReference = None
        """ 
        A
        s
        u
        b
        s
        t
        a
        n
        c
        e
        u
        p
        o
        n
        w
        h
        i
        c
        h
        a
        d
        e
        f
        i
        n
        i
        n
        g
        p
        r
        o
        p
        e
        r
        t
        y
        d
        e
        p
        e
        n
        d
        s
        (
        e
        .
        g
        .
        f
        o
        r
        s
        o
        l
        u
        b
        i
        l
        i
        t
        y
        :
        i
        n
        w
        a
        t
        e
        r
        ,
        i
        n
        a
        l
        c
        o
        h
        o
        l
        )
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.parameters = None
        """ 
        P
        a
        r
        a
        m
        e
        t
        e
        r
        s
        t
        h
        a
        t
        w
        e
        r
        e
        u
        s
        e
        d
        i
        n
        t
        h
        e
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
        o
        f
        a
        p
        r
        o
        p
        e
        r
        t
        y
        (
        e
        .
        g
        .
        f
        o
        r
        v
        i
        s
        c
        o
        s
        i
        t
        y
        :
        m
        e
        a
        s
        u
        r
        e
        d
        a
        t
        2
        0
        C
        w
        i
        t
        h
        a
        p
        H
        o
        f
        7
        .
        1
        )
        .
        Type `str`. """
        
        super(SubstanceSpecificationProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationProperty, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("definingSubstanceCodeableConcept", "definingSubstanceCodeableConcept", codeableconcept.CodeableConcept, False, "definingSubstance", False),
            ("definingSubstanceReference", "definingSubstanceReference", fhirreference.FHIRReference, False, "definingSubstance", False),
            ("parameters", "parameters", str, False, None, False),
        ])
        return js


class SubstanceSpecificationRelationship(backboneelement.BackboneElement):
    """ 
    A
    l
    i
    n
    k
    b
    e
    t
    w
    e
    e
    n
    t
    h
    i
    s
    s
    u
    b
    s
    t
    a
    n
    c
    e
    a
    n
    d
    a
    n
    o
    t
    h
    e
    r
    ,
    w
    i
    t
    h
    d
    e
    t
    a
    i
    l
    s
    o
    f
    t
    h
    e
    r
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    .
    """
    
    resource_type = "SubstanceSpecificationRelationship"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ 
        A
        n
        u
        m
        e
        r
        i
        c
        f
        a
        c
        t
        o
        r
        f
        o
        r
        t
        h
        e
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        ,
        f
        o
        r
        i
        n
        s
        t
        a
        n
        c
        e
        t
        o
        e
        x
        p
        r
        e
        s
        s
        t
        h
        a
        t
        t
        h
        e
        s
        a
        l
        t
        o
        f
        a
        s
        u
        b
        s
        t
        a
        n
        c
        e
        h
        a
        s
        s
        o
        m
        e
        p
        e
        r
        c
        e
        n
        t
        a
        g
        e
        o
        f
        t
        h
        e
        a
        c
        t
        i
        v
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        n
        r
        e
        l
        a
        t
        i
        o
        n
        t
        o
        s
        o
        m
        e
        o
        t
        h
        e
        r
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.amountRange = None
        """ 
        A
        n
        u
        m
        e
        r
        i
        c
        f
        a
        c
        t
        o
        r
        f
        o
        r
        t
        h
        e
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        ,
        f
        o
        r
        i
        n
        s
        t
        a
        n
        c
        e
        t
        o
        e
        x
        p
        r
        e
        s
        s
        t
        h
        a
        t
        t
        h
        e
        s
        a
        l
        t
        o
        f
        a
        s
        u
        b
        s
        t
        a
        n
        c
        e
        h
        a
        s
        s
        o
        m
        e
        p
        e
        r
        c
        e
        n
        t
        a
        g
        e
        o
        f
        t
        h
        e
        a
        c
        t
        i
        v
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        n
        r
        e
        l
        a
        t
        i
        o
        n
        t
        o
        s
        o
        m
        e
        o
        t
        h
        e
        r
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.amountRatio = None
        """ 
        A
        n
        u
        m
        e
        r
        i
        c
        f
        a
        c
        t
        o
        r
        f
        o
        r
        t
        h
        e
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        ,
        f
        o
        r
        i
        n
        s
        t
        a
        n
        c
        e
        t
        o
        e
        x
        p
        r
        e
        s
        s
        t
        h
        a
        t
        t
        h
        e
        s
        a
        l
        t
        o
        f
        a
        s
        u
        b
        s
        t
        a
        n
        c
        e
        h
        a
        s
        s
        o
        m
        e
        p
        e
        r
        c
        e
        n
        t
        a
        g
        e
        o
        f
        t
        h
        e
        a
        c
        t
        i
        v
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        n
        r
        e
        l
        a
        t
        i
        o
        n
        t
        o
        s
        o
        m
        e
        o
        t
        h
        e
        r
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.amountRatioLowLimit = None
        """ 
        F
        o
        r
        u
        s
        e
        w
        h
        e
        n
        t
        h
        e
        n
        u
        m
        e
        r
        i
        c
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.amountString = None
        """ 
        A
        n
        u
        m
        e
        r
        i
        c
        f
        a
        c
        t
        o
        r
        f
        o
        r
        t
        h
        e
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        ,
        f
        o
        r
        i
        n
        s
        t
        a
        n
        c
        e
        t
        o
        e
        x
        p
        r
        e
        s
        s
        t
        h
        a
        t
        t
        h
        e
        s
        a
        l
        t
        o
        f
        a
        s
        u
        b
        s
        t
        a
        n
        c
        e
        h
        a
        s
        s
        o
        m
        e
        p
        e
        r
        c
        e
        n
        t
        a
        g
        e
        o
        f
        t
        h
        e
        a
        c
        t
        i
        v
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        n
        r
        e
        l
        a
        t
        i
        o
        n
        t
        o
        s
        o
        m
        e
        o
        t
        h
        e
        r
        .
        Type `str`. """
        
        self.amountType = None
        """ 
        A
        n
        o
        p
        e
        r
        a
        t
        o
        r
        f
        o
        r
        t
        h
        e
        a
        m
        o
        u
        n
        t
        ,
        f
        o
        r
        e
        x
        a
        m
        p
        l
        e
        "
        a
        v
        e
        r
        a
        g
        e
        "
        ,
        "
        a
        p
        p
        r
        o
        x
        i
        m
        a
        t
        e
        l
        y
        "
        ,
        "
        l
        e
        s
        s
        t
        h
        a
        n
        "
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.isDefining = None
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
        w
        h
        e
        r
        e
        a
        n
        e
        n
        z
        y
        m
        e
        s
        t
        r
        o
        n
        g
        l
        y
        b
        o
        n
        d
        s
        w
        i
        t
        h
        a
        p
        a
        r
        t
        i
        c
        u
        l
        a
        r
        s
        u
        b
        s
        t
        a
        n
        c
        e
        ,
        t
        h
        i
        s
        i
        s
        a
        d
        e
        f
        i
        n
        i
        n
        g
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        f
        o
        r
        t
        h
        a
        t
        e
        n
        z
        y
        m
        e
        ,
        o
        u
        t
        o
        f
        s
        e
        v
        e
        r
        a
        l
        p
        o
        s
        s
        i
        b
        l
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        s
        .
        Type `bool`. """
        
        self.relationship = None
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
        "
        s
        a
        l
        t
        t
        o
        p
        a
        r
        e
        n
        t
        "
        ,
        "
        a
        c
        t
        i
        v
        e
        m
        o
        i
        e
        t
        y
        "
        ,
        "
        s
        t
        a
        r
        t
        i
        n
        g
        m
        a
        t
        e
        r
        i
        a
        l
        "
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
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
        l
        i
        t
        e
        r
        a
        t
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.substanceCodeableConcept = None
        """ 
        A
        p
        o
        i
        n
        t
        e
        r
        t
        o
        a
        n
        o
        t
        h
        e
        r
        s
        u
        b
        s
        t
        a
        n
        c
        e
        ,
        a
        s
        a
        r
        e
        s
        o
        u
        r
        c
        e
        o
        r
        j
        u
        s
        t
        a
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
        a
        l
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.substanceReference = None
        """ 
        A
        p
        o
        i
        n
        t
        e
        r
        t
        o
        a
        n
        o
        t
        h
        e
        r
        s
        u
        b
        s
        t
        a
        n
        c
        e
        ,
        a
        s
        a
        r
        e
        s
        o
        u
        r
        c
        e
        o
        r
        j
        u
        s
        t
        a
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
        a
        l
        c
        o
        d
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationRelationship, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationRelationship, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("amountRatio", "amountRatio", ratio.Ratio, False, "amount", False),
            ("amountRatioLowLimit", "amountRatioLowLimit", ratio.Ratio, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", False),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", False),
        ])
        return js


class SubstanceSpecificationStructure(backboneelement.BackboneElement):
    """ 
    S
    t
    r
    u
    c
    t
    u
    r
    a
    l
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
    .
    """
    
    resource_type = "SubstanceSpecificationStructure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.isotope = None
        """ 
        A
        p
        p
        l
        i
        c
        a
        b
        l
        e
        f
        o
        r
        s
        i
        n
        g
        l
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        s
        t
        h
        a
        t
        c
        o
        n
        t
        a
        i
        n
        a
        r
        a
        d
        i
        o
        n
        u
        c
        l
        i
        d
        e
        o
        r
        a
        n
        o
        n
        -
        n
        a
        t
        u
        r
        a
        l
        i
        s
        o
        t
        o
        p
        i
        c
        r
        a
        t
        i
        o
        .
        List of `SubstanceSpecificationStructureIsotope` items (represented as `dict` in JSON). """
        
        self.molecularFormula = None
        """ 
        M
        o
        l
        e
        c
        u
        l
        a
        r
        f
        o
        r
        m
        u
        l
        a
        .
        Type `str`. """
        
        self.molecularFormulaByMoiety = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        d
        p
        e
        r
        m
        o
        i
        e
        t
        y
        a
        c
        c
        o
        r
        d
        i
        n
        g
        t
        o
        t
        h
        e
        H
        i
        l
        l
        s
        y
        s
        t
        e
        m
        ,
        i
        .
        e
        .
        f
        i
        r
        s
        t
        C
        ,
        t
        h
        e
        n
        H
        ,
        t
        h
        e
        n
        a
        l
        p
        h
        a
        b
        e
        t
        i
        c
        a
        l
        ,
        e
        a
        c
        h
        m
        o
        i
        e
        t
        y
        s
        e
        p
        a
        r
        a
        t
        e
        d
        b
        y
        a
        d
        o
        t
        .
        Type `str`. """
        
        self.molecularWeight = None
        """ 
        T
        h
        e
        m
        o
        l
        e
        c
        u
        l
        a
        r
        w
        e
        i
        g
        h
        t
        o
        r
        w
        e
        i
        g
        h
        t
        r
        a
        n
        g
        e
        (
        f
        o
        r
        p
        r
        o
        t
        e
        i
        n
        s
        ,
        p
        o
        l
        y
        m
        e
        r
        s
        o
        r
        n
        u
        c
        l
        e
        i
        c
        a
        c
        i
        d
        s
        )
        .
        Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON). """
        
        self.opticalActivity = None
        """ 
        O
        p
        t
        i
        c
        a
        l
        a
        c
        t
        i
        v
        i
        t
        y
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.representation = None
        """ 
        M
        o
        l
        e
        c
        u
        l
        a
        r
        s
        t
        r
        u
        c
        t
        u
        r
        a
        l
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
        .
        List of `SubstanceSpecificationStructureRepresentation` items (represented as `dict` in JSON). """
        
        self.source = None
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
        l
        i
        t
        e
        r
        a
        t
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.stereochemistry = None
        """ 
        S
        t
        e
        r
        e
        o
        c
        h
        e
        m
        i
        s
        t
        r
        y
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructure, self).elementProperties()
        js.extend([
            ("isotope", "isotope", SubstanceSpecificationStructureIsotope, True, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("representation", "representation", SubstanceSpecificationStructureRepresentation, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationStructureIsotope(backboneelement.BackboneElement):
    """ 
    A
    p
    p
    l
    i
    c
    a
    b
    l
    e
    f
    o
    r
    s
    i
    n
    g
    l
    e
    s
    u
    b
    s
    t
    a
    n
    c
    e
    s
    t
    h
    a
    t
    c
    o
    n
    t
    a
    i
    n
    a
    r
    a
    d
    i
    o
    n
    u
    c
    l
    i
    d
    e
    o
    r
    a
    n
    o
    n
    -
    n
    a
    t
    u
    r
    a
    l
    i
    s
    o
    t
    o
    p
    i
    c
    r
    a
    t
    i
    o
    .
    """
    
    resource_type = "SubstanceSpecificationStructureIsotope"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.halfLife = None
        """ 
        H
        a
        l
        f
        l
        i
        f
        e
        -
        f
        o
        r
        a
        n
        o
        n
        -
        n
        a
        t
        u
        r
        a
        l
        n
        u
        c
        l
        i
        d
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        S
        u
        b
        s
        t
        a
        n
        c
        e
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
        e
        a
        c
        h
        n
        o
        n
        -
        n
        a
        t
        u
        r
        a
        l
        o
        r
        r
        a
        d
        i
        o
        i
        s
        o
        t
        o
        p
        e
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.molecularWeight = None
        """ 
        T
        h
        e
        m
        o
        l
        e
        c
        u
        l
        a
        r
        w
        e
        i
        g
        h
        t
        o
        r
        w
        e
        i
        g
        h
        t
        r
        a
        n
        g
        e
        (
        f
        o
        r
        p
        r
        o
        t
        e
        i
        n
        s
        ,
        p
        o
        l
        y
        m
        e
        r
        s
        o
        r
        n
        u
        c
        l
        e
        i
        c
        a
        c
        i
        d
        s
        )
        .
        Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        S
        u
        b
        s
        t
        a
        n
        c
        e
        n
        a
        m
        e
        f
        o
        r
        e
        a
        c
        h
        n
        o
        n
        -
        n
        a
        t
        u
        r
        a
        l
        o
        r
        r
        a
        d
        i
        o
        i
        s
        o
        t
        o
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.substitution = None
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
        i
        s
        o
        t
        o
        p
        i
        c
        s
        u
        b
        s
        t
        i
        t
        u
        t
        i
        o
        n
        p
        r
        e
        s
        e
        n
        t
        i
        n
        a
        s
        i
        n
        g
        l
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureIsotope, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotope, self).elementProperties()
        js.extend([
            ("halfLife", "halfLife", quantity.Quantity, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("name", "name", codeableconcept.CodeableConcept, False, None, False),
            ("substitution", "substitution", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationStructureIsotopeMolecularWeight(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    m
    o
    l
    e
    c
    u
    l
    a
    r
    w
    e
    i
    g
    h
    t
    o
    r
    w
    e
    i
    g
    h
    t
    r
    a
    n
    g
    e
    (
    f
    o
    r
    p
    r
    o
    t
    e
    i
    n
    s
    ,
    p
    o
    l
    y
    m
    e
    r
    s
    o
    r
    n
    u
    c
    l
    e
    i
    c
    a
    c
    i
    d
    s
    )
    .
    """
    
    resource_type = "SubstanceSpecificationStructureIsotopeMolecularWeight"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        U
        s
        e
        d
        t
        o
        c
        a
        p
        t
        u
        r
        e
        q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
        v
        a
        l
        u
        e
        s
        f
        o
        r
        a
        v
        a
        r
        i
        e
        t
        y
        o
        f
        e
        l
        e
        m
        e
        n
        t
        s
        .
        I
        f
        o
        n
        l
        y
        l
        i
        m
        i
        t
        s
        a
        r
        e
        g
        i
        v
        e
        n
        ,
        t
        h
        e
        a
        r
        i
        t
        h
        m
        e
        t
        i
        c
        m
        e
        a
        n
        w
        o
        u
        l
        d
        b
        e
        t
        h
        e
        a
        v
        e
        r
        a
        g
        e
        .
        I
        f
        o
        n
        l
        y
        a
        s
        i
        n
        g
        l
        e
        d
        e
        f
        i
        n
        i
        t
        e
        v
        a
        l
        u
        e
        f
        o
        r
        a
        g
        i
        v
        e
        n
        e
        l
        e
        m
        e
        n
        t
        i
        s
        g
        i
        v
        e
        n
        ,
        i
        t
        w
        o
        u
        l
        d
        b
        e
        c
        a
        p
        t
        u
        r
        e
        d
        i
        n
        t
        h
        i
        s
        f
        i
        e
        l
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.method = None
        """ 
        T
        h
        e
        m
        e
        t
        h
        o
        d
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
        m
        o
        l
        e
        c
        u
        l
        a
        r
        w
        e
        i
        g
        h
        t
        w
        a
        s
        d
        e
        t
        e
        r
        m
        i
        n
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        m
        o
        l
        e
        c
        u
        l
        a
        r
        w
        e
        i
        g
        h
        t
        s
        u
        c
        h
        a
        s
        e
        x
        a
        c
        t
        ,
        a
        v
        e
        r
        a
        g
        e
        (
        a
        l
        s
        o
        k
        n
        o
        w
        n
        a
        s
        .
        n
        u
        m
        b
        e
        r
        a
        v
        e
        r
        a
        g
        e
        )
        ,
        w
        e
        i
        g
        h
        t
        a
        v
        e
        r
        a
        g
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationStructureRepresentation(backboneelement.BackboneElement):
    """ 
    M
    o
    l
    e
    c
    u
    l
    a
    r
    s
    t
    r
    u
    c
    t
    u
    r
    a
    l
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
    .
    """
    
    resource_type = "SubstanceSpecificationStructureRepresentation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attachment = None
        """ 
        A
        n
        a
        t
        t
        a
        c
        h
        e
        d
        f
        i
        l
        e
        w
        i
        t
        h
        t
        h
        e
        s
        t
        r
        u
        c
        t
        u
        r
        a
        l
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
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.representation = None
        """ 
        T
        h
        e
        s
        t
        r
        u
        c
        t
        u
        r
        a
        l
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
        a
        s
        t
        e
        x
        t
        s
        t
        r
        i
        n
        g
        i
        n
        a
        f
        o
        r
        m
        a
        t
        e
        .
        g
        .
        I
        n
        C
        h
        I
        ,
        S
        M
        I
        L
        E
        S
        ,
        M
        O
        L
        F
        I
        L
        E
        ,
        C
        D
        X
        .
        Type `str`. """
        
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
        t
        r
        u
        c
        t
        u
        r
        e
        (
        e
        .
        g
        .
        F
        u
        l
        l
        ,
        P
        a
        r
        t
        i
        a
        l
        ,
        R
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
        v
        e
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureRepresentation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSpecificationstr(backboneelement.BackboneElement):
    """ 
    C
    o
    d
    e
    s
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
    s
    u
    b
    s
    t
    a
    n
    c
    e
    .
    """
    
    resource_type = "SubstanceSpecificationstr"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        T
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
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comment = None
        """ 
        A
        n
        y
        c
        o
        m
        m
        e
        n
        t
        c
        a
        n
        b
        e
        p
        r
        o
        v
        i
        d
        e
        d
        i
        n
        t
        h
        i
        s
        f
        i
        e
        l
        d
        ,
        i
        f
        n
        e
        c
        e
        s
        s
        a
        r
        y
        .
        Type `str`. """
        
        self.source = None
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
        l
        i
        t
        e
        r
        a
        t
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        S
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
        c
        o
        d
        e
        a
        s
        s
        i
        g
        n
        m
        e
        n
        t
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
        c
        o
        d
        e
        s
        t
        a
        t
        u
        s
        i
        s
        c
        h
        a
        n
        g
        e
        d
        a
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        m
        a
        i
        n
        t
        e
        n
        a
        n
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(SubstanceSpecificationstr, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationstr, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
