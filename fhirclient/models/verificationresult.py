#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/VerificationResult) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class VerificationResult(domainresource.DomainResource):
    """ 
    D
    e
    s
    c
    r
    i
    b
    e
    s
    v
    a
    l
    i
    d
    a
    t
    i
    o
    n
    r
    e
    q
    u
    i
    r
    e
    m
    e
    n
    t
    s
    ,
    s
    o
    u
    r
    c
    e
    (
    s
    )
    ,
    s
    t
    a
    t
    u
    s
    a
    n
    d
    d
    a
    t
    e
    s
    f
    o
    r
    o
    n
    e
    o
    r
    m
    o
    r
    e
    e
    l
    e
    m
    e
    n
    t
    s
    .
    """
    
    resource_type = "VerificationResult"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attestation = None
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
        t
        h
        e
        e
        n
        t
        i
        t
        y
        a
        t
        t
        e
        s
        t
        i
        n
        g
        t
        o
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
        Type `VerificationResultAttestation` (represented as `dict` in JSON). """
        
        self.failureAction = None
        """ 
        f
        a
        t
        a
        l
        |
        w
        a
        r
        n
        |
        r
        e
        c
        -
        o
        n
        l
        y
        |
        n
        o
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.frequency = None
        """ 
        F
        r
        e
        q
        u
        e
        n
        c
        y
        o
        f
        r
        e
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.lastPerformed = None
        """ 
        T
        h
        e
        d
        a
        t
        e
        /
        t
        i
        m
        e
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        w
        a
        s
        l
        a
        s
        t
        c
        o
        m
        p
        l
        e
        t
        e
        d
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
        f
        a
        i
        l
        e
        d
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.need = None
        """ 
        n
        o
        n
        e
        |
        i
        n
        i
        t
        i
        a
        l
        |
        p
        e
        r
        i
        o
        d
        i
        c
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.nextScheduled = None
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
        a
        r
        g
        e
        t
        i
        s
        n
        e
        x
        t
        v
        a
        l
        i
        d
        a
        t
        e
        d
        ,
        i
        f
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
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.primarySource = None
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
        t
        h
        e
        p
        r
        i
        m
        a
        r
        y
        s
        o
        u
        r
        c
        e
        (
        s
        )
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
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        .
        List of `VerificationResultPrimarySource` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        t
        t
        e
        s
        t
        e
        d
        |
        v
        a
        l
        i
        d
        a
        t
        e
        d
        |
        i
        n
        -
        p
        r
        o
        c
        e
        s
        s
        |
        r
        e
        q
        -
        r
        e
        v
        a
        l
        i
        d
        |
        v
        a
        l
        -
        f
        a
        i
        l
        |
        r
        e
        v
        a
        l
        -
        f
        a
        i
        l
        .
        Type `str`. """
        
        self.statusDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        s
        t
        a
        t
        u
        s
        w
        a
        s
        u
        p
        d
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.target = None
        """ 
        A
        r
        e
        s
        o
        u
        r
        c
        e
        t
        h
        a
        t
        w
        a
        s
        v
        a
        l
        i
        d
        a
        t
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.targetLocation = None
        """ 
        T
        h
        e
        f
        h
        i
        r
        p
        a
        t
        h
        l
        o
        c
        a
        t
        i
        o
        n
        (
        s
        )
        w
        i
        t
        h
        i
        n
        t
        h
        e
        r
        e
        s
        o
        u
        r
        c
        e
        t
        h
        a
        t
        w
        a
        s
        v
        a
        l
        i
        d
        a
        t
        e
        d
        .
        List of `str` items. """
        
        self.validationProcess = None
        """ 
        T
        h
        e
        p
        r
        i
        m
        a
        r
        y
        p
        r
        o
        c
        e
        s
        s
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
        t
        a
        r
        g
        e
        t
        i
        s
        v
        a
        l
        i
        d
        a
        t
        e
        d
        (
        e
        d
        i
        t
        c
        h
        e
        c
        k
        ;
        v
        a
        l
        u
        e
        s
        e
        t
        ;
        p
        r
        i
        m
        a
        r
        y
        s
        o
        u
        r
        c
        e
        ;
        m
        u
        l
        t
        i
        p
        l
        e
        s
        o
        u
        r
        c
        e
        s
        ;
        s
        t
        a
        n
        d
        a
        l
        o
        n
        e
        ;
        i
        n
        c
        o
        n
        t
        e
        x
        t
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.validationType = None
        """ 
        n
        o
        t
        h
        i
        n
        g
        |
        p
        r
        i
        m
        a
        r
        y
        |
        m
        u
        l
        t
        i
        p
        l
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.validator = None
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
        t
        h
        e
        e
        n
        t
        i
        t
        y
        v
        a
        l
        i
        d
        a
        t
        i
        n
        g
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
        List of `VerificationResultValidator` items (represented as `dict` in JSON). """
        
        super(VerificationResult, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VerificationResult, self).elementProperties()
        js.extend([
            ("attestation", "attestation", VerificationResultAttestation, False, None, False),
            ("failureAction", "failureAction", codeableconcept.CodeableConcept, False, None, False),
            ("frequency", "frequency", timing.Timing, False, None, False),
            ("lastPerformed", "lastPerformed", fhirdate.FHIRDate, False, None, False),
            ("need", "need", codeableconcept.CodeableConcept, False, None, False),
            ("nextScheduled", "nextScheduled", fhirdate.FHIRDate, False, None, False),
            ("primarySource", "primarySource", VerificationResultPrimarySource, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("target", "target", fhirreference.FHIRReference, True, None, False),
            ("targetLocation", "targetLocation", str, True, None, False),
            ("validationProcess", "validationProcess", codeableconcept.CodeableConcept, True, None, False),
            ("validationType", "validationType", codeableconcept.CodeableConcept, False, None, False),
            ("validator", "validator", VerificationResultValidator, True, None, False),
        ])
        return js


from . import backboneelement

class VerificationResultAttestation(backboneelement.BackboneElement):
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
    t
    h
    e
    e
    n
    t
    i
    t
    y
    a
    t
    t
    e
    s
    t
    i
    n
    g
    t
    o
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
    
    resource_type = "VerificationResultAttestation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.communicationMethod = None
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
        a
        t
        t
        e
        s
        t
        e
        d
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
        w
        a
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
        /
        r
        e
        t
        r
        i
        e
        v
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        T
        h
        e
        d
        a
        t
        e
        t
        h
        e
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
        w
        a
        s
        a
        t
        t
        e
        s
        t
        e
        d
        t
        o
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onBehalfOf = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        w
        h
        o
        i
        s
        a
        s
        s
        e
        r
        t
        i
        n
        g
        o
        n
        b
        e
        h
        a
        l
        f
        o
        f
        a
        n
        o
        t
        h
        e
        r
        (
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
        o
        r
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        )
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.proxyIdentityCertificate = None
        """ 
        A
        d
        i
        g
        i
        t
        a
        l
        i
        d
        e
        n
        t
        i
        t
        y
        c
        e
        r
        t
        i
        f
        i
        c
        a
        t
        e
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
        x
        y
        e
        n
        t
        i
        t
        y
        s
        u
        b
        m
        i
        t
        t
        i
        n
        g
        a
        t
        t
        e
        s
        t
        e
        d
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
        o
        n
        b
        e
        h
        a
        l
        f
        o
        f
        t
        h
        e
        a
        t
        t
        e
        s
        t
        a
        t
        i
        o
        n
        s
        o
        u
        r
        c
        e
        .
        Type `str`. """
        
        self.proxySignature = None
        """ 
        P
        r
        o
        x
        y
        s
        i
        g
        n
        a
        t
        u
        r
        e
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.sourceIdentityCertificate = None
        """ 
        A
        d
        i
        g
        i
        t
        a
        l
        i
        d
        e
        n
        t
        i
        t
        y
        c
        e
        r
        t
        i
        f
        i
        c
        a
        t
        e
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
        a
        t
        t
        e
        s
        t
        a
        t
        i
        o
        n
        s
        o
        u
        r
        c
        e
        .
        Type `str`. """
        
        self.sourceSignature = None
        """ 
        A
        t
        t
        e
        s
        t
        e
        r
        s
        i
        g
        n
        a
        t
        u
        r
        e
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.who = None
        """ 
        T
        h
        e
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        o
        r
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
        a
        t
        t
        e
        s
        t
        i
        n
        g
        t
        o
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
        
        super(VerificationResultAttestation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VerificationResultAttestation, self).elementProperties()
        js.extend([
            ("communicationMethod", "communicationMethod", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("proxyIdentityCertificate", "proxyIdentityCertificate", str, False, None, False),
            ("proxySignature", "proxySignature", signature.Signature, False, None, False),
            ("sourceIdentityCertificate", "sourceIdentityCertificate", str, False, None, False),
            ("sourceSignature", "sourceSignature", signature.Signature, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class VerificationResultPrimarySource(backboneelement.BackboneElement):
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
    t
    h
    e
    p
    r
    i
    m
    a
    r
    y
    s
    o
    u
    r
    c
    e
    (
    s
    )
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
    v
    a
    l
    i
    d
    a
    t
    i
    o
    n
    .
    """
    
    resource_type = "VerificationResultPrimarySource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.canPushUpdates = None
        """ 
        y
        e
        s
        |
        n
        o
        |
        u
        n
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
        
        self.communicationMethod = None
        """ 
        M
        e
        t
        h
        o
        d
        f
        o
        r
        e
        x
        c
        h
        a
        n
        g
        i
        n
        g
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
        w
        i
        t
        h
        t
        h
        e
        p
        r
        i
        m
        a
        r
        y
        s
        o
        u
        r
        c
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.pushTypeAvailable = None
        """ 
        s
        p
        e
        c
        i
        f
        i
        c
        |
        a
        n
        y
        |
        s
        o
        u
        r
        c
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        i
        m
        a
        r
        y
        s
        o
        u
        r
        c
        e
        (
        L
        i
        c
        e
        n
        s
        e
        B
        o
        a
        r
        d
        ;
        P
        r
        i
        m
        a
        r
        y
        E
        d
        u
        c
        a
        t
        i
        o
        n
        ;
        C
        o
        n
        t
        i
        n
        u
        i
        n
        g
        E
        d
        u
        c
        a
        t
        i
        o
        n
        ;
        P
        o
        s
        t
        a
        l
        S
        e
        r
        v
        i
        c
        e
        ;
        R
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
        o
        w
        n
        e
        r
        ;
        R
        e
        g
        i
        s
        t
        r
        a
        t
        i
        o
        n
        A
        u
        t
        h
        o
        r
        i
        t
        y
        ;
        l
        e
        g
        a
        l
        s
        o
        u
        r
        c
        e
        ;
        i
        s
        s
        u
        i
        n
        g
        s
        o
        u
        r
        c
        e
        ;
        a
        u
        t
        h
        o
        r
        i
        t
        a
        t
        i
        v
        e
        s
        o
        u
        r
        c
        e
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.validationDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        t
        a
        r
        g
        e
        t
        w
        a
        s
        v
        a
        l
        i
        d
        a
        t
        e
        d
        a
        g
        a
        i
        n
        s
        t
        t
        h
        e
        p
        r
        i
        m
        a
        r
        y
        s
        o
        u
        r
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.validationStatus = None
        """ 
        s
        u
        c
        c
        e
        s
        s
        f
        u
        l
        |
        f
        a
        i
        l
        e
        d
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.who = None
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
        t
        h
        e
        p
        r
        i
        m
        a
        r
        y
        s
        o
        u
        r
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(VerificationResultPrimarySource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VerificationResultPrimarySource, self).elementProperties()
        js.extend([
            ("canPushUpdates", "canPushUpdates", codeableconcept.CodeableConcept, False, None, False),
            ("communicationMethod", "communicationMethod", codeableconcept.CodeableConcept, True, None, False),
            ("pushTypeAvailable", "pushTypeAvailable", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("validationDate", "validationDate", fhirdate.FHIRDate, False, None, False),
            ("validationStatus", "validationStatus", codeableconcept.CodeableConcept, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class VerificationResultValidator(backboneelement.BackboneElement):
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
    t
    h
    e
    e
    n
    t
    i
    t
    y
    v
    a
    l
    i
    d
    a
    t
    i
    n
    g
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
    
    resource_type = "VerificationResultValidator"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attestationSignature = None
        """ 
        V
        a
        l
        i
        d
        a
        t
        o
        r
        s
        i
        g
        n
        a
        t
        u
        r
        e
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.identityCertificate = None
        """ 
        A
        d
        i
        g
        i
        t
        a
        l
        i
        d
        e
        n
        t
        i
        t
        y
        c
        e
        r
        t
        i
        f
        i
        c
        a
        t
        e
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
        v
        a
        l
        i
        d
        a
        t
        o
        r
        .
        Type `str`. """
        
        self.organization = None
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
        t
        h
        e
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
        v
        a
        l
        i
        d
        a
        t
        i
        n
        g
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
        
        super(VerificationResultValidator, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VerificationResultValidator, self).elementProperties()
        js.extend([
            ("attestationSignature", "attestationSignature", signature.Signature, False, None, False),
            ("identityCertificate", "identityCertificate", str, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, True),
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
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
