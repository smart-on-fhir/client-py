#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MolecularSequence) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MolecularSequence(domainresource.DomainResource):
    """ 
    I
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
    a
    b
    i
    o
    l
    o
    g
    i
    c
    a
    l
    s
    e
    q
    u
    e
    n
    c
    e
    .
    
    
    R
    a
    w
    d
    a
    t
    a
    d
    e
    s
    c
    r
    i
    b
    i
    n
    g
    a
    b
    i
    o
    l
    o
    g
    i
    c
    a
    l
    s
    e
    q
    u
    e
    n
    c
    e
    .
    
    """
    
    resource_type = "MolecularSequence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coordinateSystem = None
        """ 
        B
        a
        s
        e
        n
        u
        m
        b
        e
        r
        o
        f
        c
        o
        o
        r
        d
        i
        n
        a
        t
        e
        s
        y
        s
        t
        e
        m
        (
        0
        f
        o
        r
        0
        -
        b
        a
        s
        e
        d
        n
        u
        m
        b
        e
        r
        i
        n
        g
        o
        r
        c
        o
        o
        r
        d
        i
        n
        a
        t
        e
        s
        ,
        i
        n
        c
        l
        u
        s
        i
        v
        e
        s
        t
        a
        r
        t
        ,
        e
        x
        c
        l
        u
        s
        i
        v
        e
        e
        n
        d
        ,
        1
        f
        o
        r
        1
        -
        b
        a
        s
        e
        d
        n
        u
        m
        b
        e
        r
        i
        n
        g
        ,
        i
        n
        c
        l
        u
        s
        i
        v
        e
        s
        t
        a
        r
        t
        ,
        i
        n
        c
        l
        u
        s
        i
        v
        e
        e
        n
        d
        )
        .
        Type `int`. """
        
        self.device = None
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
        f
        o
        r
        s
        e
        q
        u
        e
        n
        c
        i
        n
        g
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        U
        n
        i
        q
        u
        e
        I
        D
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
        i
        c
        u
        l
        a
        r
        s
        e
        q
        u
        e
        n
        c
        e
        .
        T
        h
        i
        s
        i
        s
        a
        F
        H
        I
        R
        -
        d
        e
        f
        i
        n
        e
        d
        i
        d
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.observedSeq = None
        """ 
        S
        e
        q
        u
        e
        n
        c
        e
        t
        h
        a
        t
        w
        a
        s
        o
        b
        s
        e
        r
        v
        e
        d
        .
        Type `str`. """
        
        self.patient = None
        """ 
        W
        h
        o
        a
        n
        d
        /
        o
        r
        w
        h
        a
        t
        t
        h
        i
        s
        i
        s
        a
        b
        o
        u
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        W
        h
        o
        s
        h
        o
        u
        l
        d
        b
        e
        r
        e
        s
        p
        o
        n
        s
        i
        b
        l
        e
        f
        o
        r
        t
        e
        s
        t
        r
        e
        s
        u
        l
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.pointer = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        n
        e
        x
        t
        a
        t
        o
        m
        i
        c
        s
        e
        q
        u
        e
        n
        c
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.quality = None
        """ 
        A
        n
        s
        e
        t
        o
        f
        v
        a
        l
        u
        e
        a
        s
        q
        u
        a
        l
        i
        t
        y
        o
        f
        s
        e
        q
        u
        e
        n
        c
        e
        .
        List of `MolecularSequenceQuality` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        T
        h
        e
        n
        u
        m
        b
        e
        r
        o
        f
        c
        o
        p
        i
        e
        s
        o
        f
        t
        h
        e
        s
        e
        q
        u
        e
        n
        c
        e
        o
        f
        i
        n
        t
        e
        r
        e
        s
        t
        .
        (
        R
        N
        A
        S
        e
        q
        )
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.readCoverage = None
        """ 
        A
        v
        e
        r
        a
        g
        e
        n
        u
        m
        b
        e
        r
        o
        f
        r
        e
        a
        d
        s
        r
        e
        p
        r
        e
        s
        e
        n
        t
        i
        n
        g
        a
        g
        i
        v
        e
        n
        n
        u
        c
        l
        e
        o
        t
        i
        d
        e
        i
        n
        t
        h
        e
        r
        e
        c
        o
        n
        s
        t
        r
        u
        c
        t
        e
        d
        s
        e
        q
        u
        e
        n
        c
        e
        .
        Type `int`. """
        
        self.referenceSeq = None
        """ 
        A
        s
        e
        q
        u
        e
        n
        c
        e
        u
        s
        e
        d
        a
        s
        r
        e
        f
        e
        r
        e
        n
        c
        e
        .
        Type `MolecularSequenceReferenceSeq` (represented as `dict` in JSON). """
        
        self.repository = None
        """ 
        E
        x
        t
        e
        r
        n
        a
        l
        r
        e
        p
        o
        s
        i
        t
        o
        r
        y
        w
        h
        i
        c
        h
        c
        o
        n
        t
        a
        i
        n
        s
        d
        e
        t
        a
        i
        l
        e
        d
        r
        e
        p
        o
        r
        t
        r
        e
        l
        a
        t
        e
        d
        w
        i
        t
        h
        o
        b
        s
        e
        r
        v
        e
        d
        S
        e
        q
        i
        n
        t
        h
        i
        s
        r
        e
        s
        o
        u
        r
        c
        e
        .
        List of `MolecularSequenceRepository` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        u
        s
        e
        d
        f
        o
        r
        s
        e
        q
        u
        e
        n
        c
        i
        n
        g
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.structureVariant = None
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
        v
        a
        r
        i
        a
        n
        t
        .
        List of `MolecularSequenceStructureVariant` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        a
        a
        |
        d
        n
        a
        |
        r
        n
        a
        .
        Type `str`. """
        
        self.variant = None
        """ 
        V
        a
        r
        i
        a
        n
        t
        i
        n
        s
        e
        q
        u
        e
        n
        c
        e
        .
        List of `MolecularSequenceVariant` items (represented as `dict` in JSON). """
        
        super(MolecularSequence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequence, self).elementProperties()
        js.extend([
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False),
            ("quality", "quality", MolecularSequenceQuality, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False),
            ("repository", "repository", MolecularSequenceRepository, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False),
            ("type", "type", str, False, None, False),
            ("variant", "variant", MolecularSequenceVariant, True, None, False),
        ])
        return js


from . import backboneelement

class MolecularSequenceQuality(backboneelement.BackboneElement):
    """ 
    A
    n
    s
    e
    t
    o
    f
    v
    a
    l
    u
    e
    a
    s
    q
    u
    a
    l
    i
    t
    y
    o
    f
    s
    e
    q
    u
    e
    n
    c
    e
    .
    
    
    A
    n
    e
    x
    p
    e
    r
    i
    m
    e
    n
    t
    a
    l
    f
    e
    a
    t
    u
    r
    e
    a
    t
    t
    r
    i
    b
    u
    t
    e
    t
    h
    a
    t
    d
    e
    f
    i
    n
    e
    s
    t
    h
    e
    q
    u
    a
    l
    i
    t
    y
    o
    f
    t
    h
    e
    f
    e
    a
    t
    u
    r
    e
    i
    n
    a
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
    w
    a
    y
    ,
    s
    u
    c
    h
    a
    s
    a
    p
    h
    r
    e
    d
    q
    u
    a
    l
    i
    t
    y
    s
    c
    o
    r
    e
    (
    [
    S
    O
    :
    0
    0
    0
    1
    6
    8
    6
    ]
    (
    h
    t
    t
    p
    :
    /
    /
    w
    w
    w
    .
    s
    e
    q
    u
    e
    n
    c
    e
    o
    n
    t
    o
    l
    o
    g
    y
    .
    o
    r
    g
    /
    b
    r
    o
    w
    s
    e
    r
    /
    c
    u
    r
    r
    e
    n
    t
    _
    s
    v
    n
    /
    t
    e
    r
    m
    /
    S
    O
    :
    0
    0
    0
    1
    6
    8
    6
    )
    )
    .
    
    """
    
    resource_type = "MolecularSequenceQuality"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ 
        E
        n
        d
        p
        o
        s
        i
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
        e
        q
        u
        e
        n
        c
        e
        .
        Type `int`. """
        
        self.fScore = None
        """ 
        F
        -
        s
        c
        o
        r
        e
        .
        Type `float`. """
        
        self.gtFP = None
        """ 
        F
        a
        l
        s
        e
        p
        o
        s
        i
        t
        i
        v
        e
        s
        w
        h
        e
        r
        e
        t
        h
        e
        n
        o
        n
        -
        R
        E
        F
        a
        l
        l
        e
        l
        e
        s
        i
        n
        t
        h
        e
        T
        r
        u
        t
        h
        a
        n
        d
        Q
        u
        e
        r
        y
        C
        a
        l
        l
        S
        e
        t
        s
        m
        a
        t
        c
        h
        .
        Type `float`. """
        
        self.method = None
        """ 
        M
        e
        t
        h
        o
        d
        t
        o
        g
        e
        t
        q
        u
        a
        l
        i
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.precision = None
        """ 
        P
        r
        e
        c
        i
        s
        i
        o
        n
        o
        f
        c
        o
        m
        p
        a
        r
        i
        s
        o
        n
        .
        Type `float`. """
        
        self.queryFP = None
        """ 
        F
        a
        l
        s
        e
        p
        o
        s
        i
        t
        i
        v
        e
        s
        .
        Type `float`. """
        
        self.queryTP = None
        """ 
        T
        r
        u
        e
        p
        o
        s
        i
        t
        i
        v
        e
        s
        f
        r
        o
        m
        t
        h
        e
        p
        e
        r
        s
        p
        e
        c
        t
        i
        v
        e
        o
        f
        t
        h
        e
        q
        u
        e
        r
        y
        d
        a
        t
        a
        .
        Type `float`. """
        
        self.recall = None
        """ 
        R
        e
        c
        a
        l
        l
        o
        f
        c
        o
        m
        p
        a
        r
        i
        s
        o
        n
        .
        Type `float`. """
        
        self.roc = None
        """ 
        R
        e
        c
        e
        i
        v
        e
        r
        O
        p
        e
        r
        a
        t
        o
        r
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
        (
        R
        O
        C
        )
        C
        u
        r
        v
        e
        .
        Type `MolecularSequenceQualityRoc` (represented as `dict` in JSON). """
        
        self.score = None
        """ 
        Q
        u
        a
        l
        i
        t
        y
        s
        c
        o
        r
        e
        f
        o
        r
        t
        h
        e
        c
        o
        m
        p
        a
        r
        i
        s
        o
        n
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.standardSequence = None
        """ 
        S
        t
        a
        n
        d
        a
        r
        d
        s
        e
        q
        u
        e
        n
        c
        e
        f
        o
        r
        c
        o
        m
        p
        a
        r
        i
        s
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.start = None
        """ 
        S
        t
        a
        r
        t
        p
        o
        s
        i
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
        e
        q
        u
        e
        n
        c
        e
        .
        Type `int`. """
        
        self.truthFN = None
        """ 
        F
        a
        l
        s
        e
        n
        e
        g
        a
        t
        i
        v
        e
        s
        .
        Type `float`. """
        
        self.truthTP = None
        """ 
        T
        r
        u
        e
        p
        o
        s
        i
        t
        i
        v
        e
        s
        f
        r
        o
        m
        t
        h
        e
        p
        e
        r
        s
        p
        e
        c
        t
        i
        v
        e
        o
        f
        t
        h
        e
        t
        r
        u
        t
        h
        d
        a
        t
        a
        .
        Type `float`. """
        
        self.type = None
        """ 
        i
        n
        d
        e
        l
        |
        s
        n
        p
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        super(MolecularSequenceQuality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("standardSequence", "standardSequence", codeableconcept.CodeableConcept, False, None, False),
            ("start", "start", int, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    """ 
    R
    e
    c
    e
    i
    v
    e
    r
    O
    p
    e
    r
    a
    t
    o
    r
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
    (
    R
    O
    C
    )
    C
    u
    r
    v
    e
    .
    
    
    R
    e
    c
    e
    i
    v
    e
    r
    O
    p
    e
    r
    a
    t
    o
    r
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
    (
    R
    O
    C
    )
    C
    u
    r
    v
    e
    t
    o
    g
    i
    v
    e
    s
    e
    n
    s
    i
    t
    i
    v
    i
    t
    y
    /
    s
    p
    e
    c
    i
    f
    i
    c
    i
    t
    y
    t
    r
    a
    d
    e
    o
    f
    f
    .
    
    """
    
    resource_type = "MolecularSequenceQualityRoc"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fMeasure = None
        """ 
        F
        S
        c
        o
        r
        e
        o
        f
        t
        h
        e
        G
        Q
        s
        c
        o
        r
        e
        .
        List of `float` items. """
        
        self.numFN = None
        """ 
        R
        o
        c
        s
        c
        o
        r
        e
        f
        a
        l
        s
        e
        n
        e
        g
        a
        t
        i
        v
        e
        n
        u
        m
        b
        e
        r
        s
        .
        List of `int` items. """
        
        self.numFP = None
        """ 
        R
        o
        c
        s
        c
        o
        r
        e
        f
        a
        l
        s
        e
        p
        o
        s
        i
        t
        i
        v
        e
        n
        u
        m
        b
        e
        r
        s
        .
        List of `int` items. """
        
        self.numTP = None
        """ 
        R
        o
        c
        s
        c
        o
        r
        e
        t
        r
        u
        e
        p
        o
        s
        i
        t
        i
        v
        e
        n
        u
        m
        b
        e
        r
        s
        .
        List of `int` items. """
        
        self.precision = None
        """ 
        P
        r
        e
        c
        i
        s
        i
        o
        n
        o
        f
        t
        h
        e
        G
        Q
        s
        c
        o
        r
        e
        .
        List of `float` items. """
        
        self.score = None
        """ 
        G
        e
        n
        o
        t
        y
        p
        e
        q
        u
        a
        l
        i
        t
        y
        s
        c
        o
        r
        e
        .
        List of `int` items. """
        
        self.sensitivity = None
        """ 
        S
        e
        n
        s
        i
        t
        i
        v
        i
        t
        y
        o
        f
        t
        h
        e
        G
        Q
        s
        c
        o
        r
        e
        .
        List of `float` items. """
        
        super(MolecularSequenceQualityRoc, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceQualityRoc, self).elementProperties()
        js.extend([
            ("fMeasure", "fMeasure", float, True, None, False),
            ("numFN", "numFN", int, True, None, False),
            ("numFP", "numFP", int, True, None, False),
            ("numTP", "numTP", int, True, None, False),
            ("precision", "precision", float, True, None, False),
            ("score", "score", int, True, None, False),
            ("sensitivity", "sensitivity", float, True, None, False),
        ])
        return js


class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """ 
    A
    s
    e
    q
    u
    e
    n
    c
    e
    u
    s
    e
    d
    a
    s
    r
    e
    f
    e
    r
    e
    n
    c
    e
    .
    
    
    A
    s
    e
    q
    u
    e
    n
    c
    e
    t
    h
    a
    t
    i
    s
    u
    s
    e
    d
    a
    s
    a
    r
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
    d
    e
    s
    c
    r
    i
    b
    e
    v
    a
    r
    i
    a
    n
    t
    s
    t
    h
    a
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
    i
    n
    a
    s
    e
    q
    u
    e
    n
    c
    e
    a
    n
    a
    l
    y
    z
    e
    d
    .
    
    """
    
    resource_type = "MolecularSequenceReferenceSeq"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chromosome = None
        """ 
        C
        h
        r
        o
        m
        o
        s
        o
        m
        e
        c
        o
        n
        t
        a
        i
        n
        i
        n
        g
        g
        e
        n
        e
        t
        i
        c
        f
        i
        n
        d
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genomeBuild = None
        """ 
        T
        h
        e
        G
        e
        n
        o
        m
        e
        B
        u
        i
        l
        d
        u
        s
        e
        d
        f
        o
        r
        r
        e
        f
        e
        r
        e
        n
        c
        e
        ,
        f
        o
        l
        l
        o
        w
        i
        n
        g
        G
        R
        C
        h
        b
        u
        i
        l
        d
        v
        e
        r
        s
        i
        o
        n
        s
        e
        .
        g
        .
        '
        G
        R
        C
        h
        3
        7
        '
        .
        Type `str`. """
        
        self.orientation = None
        """ 
        s
        e
        n
        s
        e
        |
        a
        n
        t
        i
        s
        e
        n
        s
        e
        .
        Type `str`. """
        
        self.referenceSeqId = None
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referenceSeqPointer = None
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
        M
        o
        l
        e
        c
        u
        l
        a
        r
        S
        e
        q
        u
        e
        n
        c
        e
        e
        n
        t
        i
        t
        y
        a
        s
        r
        e
        f
        e
        r
        e
        n
        c
        e
        s
        e
        q
        u
        e
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceSeqString = None
        """ 
        A
        s
        t
        r
        i
        n
        g
        t
        o
        r
        e
        p
        r
        e
        s
        e
        n
        t
        r
        e
        f
        e
        r
        e
        n
        c
        e
        s
        e
        q
        u
        e
        n
        c
        e
        .
        Type `str`. """
        
        self.strand = None
        """ 
        w
        a
        t
        s
        o
        n
        |
        c
        r
        i
        c
        k
        .
        Type `str`. """
        
        self.windowEnd = None
        """ 
        E
        n
        d
        p
        o
        s
        i
        t
        i
        o
        n
        o
        f
        t
        h
        e
        w
        i
        n
        d
        o
        w
        o
        n
        t
        h
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        s
        e
        q
        u
        e
        n
        c
        e
        .
        Type `int`. """
        
        self.windowStart = None
        """ 
        S
        t
        a
        r
        t
        p
        o
        s
        i
        t
        i
        o
        n
        o
        f
        t
        h
        e
        w
        i
        n
        d
        o
        w
        o
        n
        t
        h
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        s
        e
        q
        u
        e
        n
        c
        e
        .
        Type `int`. """
        
        super(MolecularSequenceReferenceSeq, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("orientation", "orientation", str, False, None, False),
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("strand", "strand", str, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, False),
            ("windowStart", "windowStart", int, False, None, False),
        ])
        return js


class MolecularSequenceRepository(backboneelement.BackboneElement):
    """ 
    E
    x
    t
    e
    r
    n
    a
    l
    r
    e
    p
    o
    s
    i
    t
    o
    r
    y
    w
    h
    i
    c
    h
    c
    o
    n
    t
    a
    i
    n
    s
    d
    e
    t
    a
    i
    l
    e
    d
    r
    e
    p
    o
    r
    t
    r
    e
    l
    a
    t
    e
    d
    w
    i
    t
    h
    o
    b
    s
    e
    r
    v
    e
    d
    S
    e
    q
    i
    n
    t
    h
    i
    s
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    
    C
    o
    n
    f
    i
    g
    u
    r
    a
    t
    i
    o
    n
    s
    o
    f
    t
    h
    e
    e
    x
    t
    e
    r
    n
    a
    l
    r
    e
    p
    o
    s
    i
    t
    o
    r
    y
    .
    T
    h
    e
    r
    e
    p
    o
    s
    i
    t
    o
    r
    y
    s
    h
    a
    l
    l
    s
    t
    o
    r
    e
    t
    a
    r
    g
    e
    t
    '
    s
    o
    b
    s
    e
    r
    v
    e
    d
    S
    e
    q
    o
    r
    r
    e
    c
    o
    r
    d
    s
    r
    e
    l
    a
    t
    e
    d
    w
    i
    t
    h
    t
    a
    r
    g
    e
    t
    '
    s
    o
    b
    s
    e
    r
    v
    e
    d
    S
    e
    q
    .
    
    """
    
    resource_type = "MolecularSequenceRepository"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.datasetId = None
        """ 
        I
        d
        o
        f
        t
        h
        e
        d
        a
        t
        a
        s
        e
        t
        t
        h
        a
        t
        u
        s
        e
        d
        t
        o
        c
        a
        l
        l
        f
        o
        r
        d
        a
        t
        a
        s
        e
        t
        i
        n
        r
        e
        p
        o
        s
        i
        t
        o
        r
        y
        .
        Type `str`. """
        
        self.name = None
        """ 
        R
        e
        p
        o
        s
        i
        t
        o
        r
        y
        '
        s
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.readsetId = None
        """ 
        I
        d
        o
        f
        t
        h
        e
        r
        e
        a
        d
        .
        Type `str`. """
        
        self.type = None
        """ 
        d
        i
        r
        e
        c
        t
        l
        i
        n
        k
        |
        o
        p
        e
        n
        a
        p
        i
        |
        l
        o
        g
        i
        n
        |
        o
        a
        u
        t
        h
        |
        o
        t
        h
        e
        r
        .
        Type `str`. """
        
        self.url = None
        """ 
        U
        R
        I
        o
        f
        t
        h
        e
        r
        e
        p
        o
        s
        i
        t
        o
        r
        y
        .
        Type `str`. """
        
        self.variantsetId = None
        """ 
        I
        d
        o
        f
        t
        h
        e
        v
        a
        r
        i
        a
        n
        t
        s
        e
        t
        t
        h
        a
        t
        u
        s
        e
        d
        t
        o
        c
        a
        l
        l
        f
        o
        r
        v
        a
        r
        i
        a
        n
        t
        s
        e
        t
        i
        n
        r
        e
        p
        o
        s
        i
        t
        o
        r
        y
        .
        Type `str`. """
        
        super(MolecularSequenceRepository, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceRepository, self).elementProperties()
        js.extend([
            ("datasetId", "datasetId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("readsetId", "readsetId", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("variantsetId", "variantsetId", str, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
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
    v
    a
    r
    i
    a
    n
    t
    .
    
    
    I
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
    c
    h
    r
    o
    m
    o
    s
    o
    m
    e
    s
    t
    r
    u
    c
    t
    u
    r
    e
    v
    a
    r
    i
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "MolecularSequenceStructureVariant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exact = None
        """ 
        D
        o
        e
        s
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
        v
        a
        r
        i
        a
        n
        t
        h
        a
        v
        e
        b
        a
        s
        e
        p
        a
        i
        r
        r
        e
        s
        o
        l
        u
        t
        i
        o
        n
        b
        r
        e
        a
        k
        p
        o
        i
        n
        t
        s
        ?
        .
        Type `bool`. """
        
        self.inner = None
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
        v
        a
        r
        i
        a
        n
        t
        i
        n
        n
        e
        r
        .
        Type `MolecularSequenceStructureVariantInner` (represented as `dict` in JSON). """
        
        self.length = None
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
        v
        a
        r
        i
        a
        n
        t
        l
        e
        n
        g
        t
        h
        .
        Type `int`. """
        
        self.outer = None
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
        v
        a
        r
        i
        a
        n
        t
        o
        u
        t
        e
        r
        .
        Type `MolecularSequenceStructureVariantOuter` (represented as `dict` in JSON). """
        
        self.variantType = None
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
        v
        a
        r
        i
        a
        n
        t
        c
        h
        a
        n
        g
        e
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MolecularSequenceStructureVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend([
            ("exact", "exact", bool, False, None, False),
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False),
            ("length", "length", int, False, None, False),
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False),
            ("variantType", "variantType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
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
    v
    a
    r
    i
    a
    n
    t
    i
    n
    n
    e
    r
    .
    """
    
    resource_type = "MolecularSequenceStructureVariantInner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
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
        v
        a
        r
        i
        a
        n
        t
        i
        n
        n
        e
        r
        e
        n
        d
        .
        Type `int`. """
        
        self.start = None
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
        v
        a
        r
        i
        a
        n
        t
        i
        n
        n
        e
        r
        s
        t
        a
        r
        t
        .
        Type `int`. """
        
        super(MolecularSequenceStructureVariantInner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
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
    v
    a
    r
    i
    a
    n
    t
    o
    u
    t
    e
    r
    .
    """
    
    resource_type = "MolecularSequenceStructureVariantOuter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
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
        v
        a
        r
        i
        a
        n
        t
        o
        u
        t
        e
        r
        e
        n
        d
        .
        Type `int`. """
        
        self.start = None
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
        v
        a
        r
        i
        a
        n
        t
        o
        u
        t
        e
        r
        s
        t
        a
        r
        t
        .
        Type `int`. """
        
        super(MolecularSequenceStructureVariantOuter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class MolecularSequenceVariant(backboneelement.BackboneElement):
    """ 
    V
    a
    r
    i
    a
    n
    t
    i
    n
    s
    e
    q
    u
    e
    n
    c
    e
    .
    
    
    T
    h
    e
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
    v
    a
    r
    i
    a
    n
    t
    h
    e
    r
    e
    o
    r
    i
    g
    i
    n
    a
    t
    e
    s
    f
    r
    o
    m
    S
    e
    q
    u
    e
    n
    c
    e
    o
    n
    t
    o
    l
    o
    g
    y
    (
    [
    v
    a
    r
    i
    a
    n
    t
    _
    o
    f
    ]
    (
    h
    t
    t
    p
    :
    /
    /
    w
    w
    w
    .
    s
    e
    q
    u
    e
    n
    c
    e
    o
    n
    t
    o
    l
    o
    g
    y
    .
    o
    r
    g
    /
    b
    r
    o
    w
    s
    e
    r
    /
    c
    u
    r
    r
    e
    n
    t
    _
    s
    v
    n
    /
    t
    e
    r
    m
    /
    v
    a
    r
    i
    a
    n
    t
    _
    o
    f
    )
    )
    .
    T
    h
    i
    s
    e
    l
    e
    m
    e
    n
    t
    c
    a
    n
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
    m
    i
    n
    o
    a
    c
    i
    d
    o
    r
    n
    u
    c
    l
    e
    i
    c
    s
    e
    q
    u
    e
    n
    c
    e
    c
    h
    a
    n
    g
    e
    (
    i
    n
    c
    l
    u
    d
    i
    n
    g
    i
    n
    s
    e
    r
    t
    i
    o
    n
    ,
    d
    e
    l
    e
    t
    i
    o
    n
    ,
    S
    N
    P
    ,
    e
    t
    c
    .
    )
    I
    t
    c
    a
    n
    r
    e
    p
    r
    e
    s
    e
    n
    t
    s
    o
    m
    e
    c
    o
    m
    p
    l
    e
    x
    m
    u
    t
    a
    t
    i
    o
    n
    o
    r
    s
    e
    g
    m
    e
    n
    t
    v
    a
    r
    i
    a
    t
    i
    o
    n
    w
    i
    t
    h
    t
    h
    e
    a
    s
    s
    i
    s
    t
    o
    f
    C
    I
    G
    A
    R
    s
    t
    r
    i
    n
    g
    .
    
    """
    
    resource_type = "MolecularSequenceVariant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cigar = None
        """ 
        E
        x
        t
        e
        n
        d
        e
        d
        C
        I
        G
        A
        R
        s
        t
        r
        i
        n
        g
        f
        o
        r
        a
        l
        i
        g
        n
        i
        n
        g
        t
        h
        e
        s
        e
        q
        u
        e
        n
        c
        e
        w
        i
        t
        h
        r
        e
        f
        e
        r
        e
        n
        c
        e
        b
        a
        s
        e
        s
        .
        Type `str`. """
        
        self.end = None
        """ 
        E
        n
        d
        p
        o
        s
        i
        t
        i
        o
        n
        o
        f
        t
        h
        e
        v
        a
        r
        i
        a
        n
        t
        o
        n
        t
        h
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        s
        e
        q
        u
        e
        n
        c
        e
        .
        Type `int`. """
        
        self.observedAllele = None
        """ 
        A
        l
        l
        e
        l
        e
        t
        h
        a
        t
        w
        a
        s
        o
        b
        s
        e
        r
        v
        e
        d
        .
        Type `str`. """
        
        self.referenceAllele = None
        """ 
        A
        l
        l
        e
        l
        e
        i
        n
        t
        h
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        s
        e
        q
        u
        e
        n
        c
        e
        .
        Type `str`. """
        
        self.start = None
        """ 
        S
        t
        a
        r
        t
        p
        o
        s
        i
        t
        i
        o
        n
        o
        f
        t
        h
        e
        v
        a
        r
        i
        a
        n
        t
        o
        n
        t
        h
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        s
        e
        q
        u
        e
        n
        c
        e
        .
        Type `int`. """
        
        self.variantPointer = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        o
        b
        s
        e
        r
        v
        e
        d
        v
        a
        r
        i
        a
        n
        t
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MolecularSequenceVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend([
            ("cigar", "cigar", str, False, None, False),
            ("end", "end", int, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("start", "start", int, False, None, False),
            ("variantPointer", "variantPointer", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
