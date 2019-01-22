#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ClaimResponse(domainresource.DomainResource):
    """ 
    R
    e
    s
    p
    o
    n
    s
    e
    t
    o
    a
    c
    l
    a
    i
    m
    p
    r
    e
    d
    e
    t
    e
    r
    m
    i
    n
    a
    t
    i
    o
    n
    o
    r
    p
    r
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
    
    
    T
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
    p
    r
    o
    v
    i
    d
    e
    s
    t
    h
    e
    a
    d
    j
    u
    d
    i
    c
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
    s
    f
    r
    o
    m
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
    i
    n
    g
    o
    f
    a
    C
    l
    a
    i
    m
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    """
    
    resource_type = "ClaimResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.addItem = None
        """ 
        I
        n
        s
        u
        r
        e
        r
        a
        d
        d
        e
        d
        l
        i
        n
        e
        i
        t
        e
        m
        s
        .
        List of `ClaimResponseAddItem` items (represented as `dict` in JSON). """
        
        self.adjudication = None
        """ 
        H
        e
        a
        d
        e
        r
        -
        l
        e
        v
        e
        l
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.communicationRequest = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        f
        o
        r
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.created = None
        """ 
        R
        e
        s
        p
        o
        n
        s
        e
        c
        r
        e
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
        
        self.disposition = None
        """ 
        D
        i
        s
        p
        o
        s
        i
        t
        i
        o
        n
        M
        e
        s
        s
        a
        g
        e
        .
        Type `str`. """
        
        self.error = None
        """ 
        P
        r
        o
        c
        e
        s
        s
        i
        n
        g
        e
        r
        r
        o
        r
        s
        .
        List of `ClaimResponseError` items (represented as `dict` in JSON). """
        
        self.form = None
        """ 
        P
        r
        i
        n
        t
        e
        d
        r
        e
        f
        e
        r
        e
        n
        c
        e
        o
        r
        a
        c
        t
        u
        a
        l
        f
        o
        r
        m
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.formCode = None
        """ 
        P
        r
        i
        n
        t
        e
        d
        f
        o
        r
        m
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
        
        self.fundsReserve = None
        """ 
        F
        u
        n
        d
        s
        r
        e
        s
        e
        r
        v
        e
        d
        s
        t
        a
        t
        u
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        a
        c
        l
        a
        i
        m
        r
        e
        s
        p
        o
        n
        s
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        i
        n
        s
        u
        r
        a
        n
        c
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
        .
        List of `ClaimResponseInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        """ 
        P
        a
        r
        t
        y
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
        r
        e
        i
        m
        b
        u
        r
        s
        e
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        """ 
        A
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        f
        o
        r
        c
        l
        a
        i
        m
        l
        i
        n
        e
        i
        t
        e
        m
        s
        .
        List of `ClaimResponseItem` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ 
        q
        u
        e
        u
        e
        d
        |
        c
        o
        m
        p
        l
        e
        t
        e
        |
        e
        r
        r
        o
        r
        |
        p
        a
        r
        t
        i
        a
        l
        .
        Type `str`. """
        
        self.patient = None
        """ 
        T
        h
        e
        r
        e
        c
        i
        p
        i
        e
        n
        t
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
        s
        a
        n
        d
        s
        e
        r
        v
        i
        c
        e
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payeeType = None
        """ 
        P
        a
        r
        t
        y
        t
        o
        b
        e
        p
        a
        i
        d
        a
        n
        y
        b
        e
        n
        e
        f
        i
        t
        s
        p
        a
        y
        a
        b
        l
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.payment = None
        """ 
        P
        a
        y
        m
        e
        n
        t
        D
        e
        t
        a
        i
        l
        s
        .
        Type `ClaimResponsePayment` (represented as `dict` in JSON). """
        
        self.preAuthPeriod = None
        """ 
        P
        r
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
        r
        e
        f
        e
        r
        e
        n
        c
        e
        e
        f
        f
        e
        c
        t
        i
        v
        e
        p
        e
        r
        i
        o
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        """ 
        P
        r
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
        Type `str`. """
        
        self.processNote = None
        """ 
        N
        o
        t
        e
        c
        o
        n
        c
        e
        r
        n
        i
        n
        g
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `ClaimResponseProcessNote` items (represented as `dict` in JSON). """
        
        self.request = None
        """ 
        I
        d
        o
        f
        r
        e
        s
        o
        u
        r
        c
        e
        t
        r
        i
        g
        g
        e
        r
        i
        n
        g
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestor = None
        """ 
        P
        a
        r
        t
        y
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
        h
        e
        c
        l
        a
        i
        m
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
        e
        |
        c
        a
        n
        c
        e
        l
        l
        e
        d
        |
        d
        r
        a
        f
        t
        |
        e
        n
        t
        e
        r
        e
        d
        -
        i
        n
        -
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        self.subType = None
        """ 
        M
        o
        r
        e
        g
        r
        a
        n
        u
        l
        a
        r
        c
        l
        a
        i
        m
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.total = None
        """ 
        A
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        t
        o
        t
        a
        l
        s
        .
        List of `ClaimResponseTotal` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        M
        o
        r
        e
        g
        r
        a
        n
        u
        l
        a
        r
        c
        l
        a
        i
        m
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        """ 
        c
        l
        a
        i
        m
        |
        p
        r
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
        |
        p
        r
        e
        d
        e
        t
        e
        r
        m
        i
        n
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(ClaimResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponse, self).elementProperties()
        js.extend([
            ("addItem", "addItem", ClaimResponseAddItem, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("communicationRequest", "communicationRequest", fhirreference.FHIRReference, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", ClaimResponseError, True, None, False),
            ("form", "form", attachment.Attachment, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", ClaimResponseInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("item", "item", ClaimResponseItem, True, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("payeeType", "payeeType", codeableconcept.CodeableConcept, False, None, False),
            ("payment", "payment", ClaimResponsePayment, False, None, False),
            ("preAuthPeriod", "preAuthPeriod", period.Period, False, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("processNote", "processNote", ClaimResponseProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("total", "total", ClaimResponseTotal, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


from . import backboneelement

class ClaimResponseAddItem(backboneelement.BackboneElement):
    """ 
    I
    n
    s
    u
    r
    e
    r
    a
    d
    d
    e
    d
    l
    i
    n
    e
    i
    t
    e
    m
    s
    .
    
    
    T
    h
    e
    f
    i
    r
    s
    t
    -
    t
    i
    e
    r
    s
    e
    r
    v
    i
    c
    e
    a
    d
    j
    u
    d
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
    p
    a
    y
    o
    r
    a
    d
    d
    e
    d
    p
    r
    o
    d
    u
    c
    t
    o
    r
    s
    e
    r
    v
    i
    c
    e
    l
    i
    n
    e
    s
    .
    
    """
    
    resource_type = "ClaimResponseAddItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ 
        A
        d
        d
        e
        d
        i
        t
        e
        m
        s
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ 
        A
        n
        a
        t
        o
        m
        i
        c
        a
        l
        l
        o
        c
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        """ 
        I
        n
        s
        u
        r
        e
        r
        a
        d
        d
        e
        d
        l
        i
        n
        e
        d
        e
        t
        a
        i
        l
        s
        .
        List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON). """
        
        self.detailSequence = None
        """ 
        D
        e
        t
        a
        i
        l
        s
        e
        q
        u
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
        List of `int` items. """
        
        self.factor = None
        """ 
        P
        r
        i
        c
        e
        s
        c
        a
        l
        i
        n
        g
        f
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.itemSequence = None
        """ 
        I
        t
        e
        m
        s
        e
        q
        u
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
        List of `int` items. """
        
        self.locationAddress = None
        """ 
        P
        l
        a
        c
        e
        o
        f
        s
        e
        r
        v
        i
        c
        e
        o
        r
        w
        h
        e
        r
        e
        p
        r
        o
        d
        u
        c
        t
        w
        a
        s
        s
        u
        p
        p
        l
        i
        e
        d
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept = None
        """ 
        P
        l
        a
        c
        e
        o
        f
        s
        e
        r
        v
        i
        c
        e
        o
        r
        w
        h
        e
        r
        e
        p
        r
        o
        d
        u
        c
        t
        w
        a
        s
        s
        u
        p
        p
        l
        i
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ 
        P
        l
        a
        c
        e
        o
        f
        s
        e
        r
        v
        i
        c
        e
        o
        r
        w
        h
        e
        r
        e
        p
        r
        o
        d
        u
        c
        t
        w
        a
        s
        s
        u
        p
        p
        l
        i
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        /
        P
        r
        o
        d
        u
        c
        t
        b
        i
        l
        l
        i
        n
        g
        m
        o
        d
        i
        f
        i
        e
        r
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        """ 
        T
        o
        t
        a
        l
        i
        t
        e
        m
        c
        o
        s
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
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
        n
        o
        t
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
        
        self.productOrService = None
        """ 
        B
        i
        l
        l
        i
        n
        g
        ,
        s
        e
        r
        v
        i
        c
        e
        ,
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
        d
        r
        u
        g
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.programCode = None
        """ 
        P
        r
        o
        g
        r
        a
        m
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
        o
        r
        s
        e
        r
        v
        i
        c
        e
        i
        s
        p
        r
        o
        v
        i
        d
        e
        d
        u
        n
        d
        e
        r
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.provider = None
        """ 
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
        p
        r
        o
        v
        i
        d
        e
        r
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        C
        o
        u
        n
        t
        o
        f
        p
        r
        o
        d
        u
        c
        t
        s
        o
        r
        s
        e
        r
        v
        i
        c
        e
        s
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ 
        D
        a
        t
        e
        o
        r
        d
        a
        t
        e
        s
        o
        f
        s
        e
        r
        v
        i
        c
        e
        o
        r
        p
        r
        o
        d
        u
        c
        t
        d
        e
        l
        i
        v
        e
        r
        y
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ 
        D
        a
        t
        e
        o
        r
        d
        a
        t
        e
        s
        o
        f
        s
        e
        r
        v
        i
        c
        e
        o
        r
        p
        r
        o
        d
        u
        c
        t
        d
        e
        l
        i
        v
        e
        r
        y
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
        """ 
        A
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
        u
        b
        -
        l
        o
        c
        a
        t
        i
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subdetailSequence = None
        """ 
        S
        u
        b
        d
        e
        t
        a
        i
        l
        s
        e
        q
        u
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
        List of `int` items. """
        
        self.unitPrice = None
        """ 
        F
        e
        e
        ,
        c
        h
        a
        r
        g
        e
        o
        r
        c
        o
        s
        t
        p
        e
        r
        i
        t
        e
        m
        .
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ClaimResponseAddItemDetail, True, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("itemSequence", "itemSequence", int, True, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("subdetailSequence", "subdetailSequence", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """ 
    I
    n
    s
    u
    r
    e
    r
    a
    d
    d
    e
    d
    l
    i
    n
    e
    d
    e
    t
    a
    i
    l
    s
    .
    
    
    T
    h
    e
    s
    e
    c
    o
    n
    d
    -
    t
    i
    e
    r
    s
    e
    r
    v
    i
    c
    e
    a
    d
    j
    u
    d
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
    p
    a
    y
    o
    r
    a
    d
    d
    e
    d
    s
    e
    r
    v
    i
    c
    e
    s
    .
    
    """
    
    resource_type = "ClaimResponseAddItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ 
        A
        d
        d
        e
        d
        i
        t
        e
        m
        s
        d
        e
        t
        a
        i
        l
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.factor = None
        """ 
        P
        r
        i
        c
        e
        s
        c
        a
        l
        i
        n
        g
        f
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.modifier = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        /
        P
        r
        o
        d
        u
        c
        t
        b
        i
        l
        l
        i
        n
        g
        m
        o
        d
        i
        f
        i
        e
        r
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        """ 
        T
        o
        t
        a
        l
        i
        t
        e
        m
        c
        o
        s
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
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
        n
        o
        t
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
        
        self.productOrService = None
        """ 
        B
        i
        l
        l
        i
        n
        g
        ,
        s
        e
        r
        v
        i
        c
        e
        ,
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
        d
        r
        u
        g
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        C
        o
        u
        n
        t
        o
        f
        p
        r
        o
        d
        u
        c
        t
        s
        o
        r
        s
        e
        r
        v
        i
        c
        e
        s
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.subDetail = None
        """ 
        I
        n
        s
        u
        r
        e
        r
        a
        d
        d
        e
        d
        l
        i
        n
        e
        i
        t
        e
        m
        s
        .
        List of `ClaimResponseAddItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ 
        F
        e
        e
        ,
        c
        h
        a
        r
        g
        e
        o
        r
        c
        o
        s
        t
        p
        e
        r
        i
        t
        e
        m
        .
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("subDetail", "subDetail", ClaimResponseAddItemDetailSubDetail, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimResponseAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ 
    I
    n
    s
    u
    r
    e
    r
    a
    d
    d
    e
    d
    l
    i
    n
    e
    i
    t
    e
    m
    s
    .
    
    
    T
    h
    e
    t
    h
    i
    r
    d
    -
    t
    i
    e
    r
    s
    e
    r
    v
    i
    c
    e
    a
    d
    j
    u
    d
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
    p
    a
    y
    o
    r
    a
    d
    d
    e
    d
    s
    e
    r
    v
    i
    c
    e
    s
    .
    
    """
    
    resource_type = "ClaimResponseAddItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ 
        A
        d
        d
        e
        d
        i
        t
        e
        m
        s
        d
        e
        t
        a
        i
        l
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.factor = None
        """ 
        P
        r
        i
        c
        e
        s
        c
        a
        l
        i
        n
        g
        f
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.modifier = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        /
        P
        r
        o
        d
        u
        c
        t
        b
        i
        l
        l
        i
        n
        g
        m
        o
        d
        i
        f
        i
        e
        r
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        """ 
        T
        o
        t
        a
        l
        i
        t
        e
        m
        c
        o
        s
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
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
        n
        o
        t
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
        
        self.productOrService = None
        """ 
        B
        i
        l
        l
        i
        n
        g
        ,
        s
        e
        r
        v
        i
        c
        e
        ,
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
        d
        r
        u
        g
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        C
        o
        u
        n
        t
        o
        f
        p
        r
        o
        d
        u
        c
        t
        s
        o
        r
        s
        e
        r
        v
        i
        c
        e
        s
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ 
        F
        e
        e
        ,
        c
        h
        a
        r
        g
        e
        o
        r
        c
        o
        s
        t
        p
        e
        r
        i
        t
        e
        m
        .
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimResponseError(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    c
    e
    s
    s
    i
    n
    g
    e
    r
    r
    o
    r
    s
    .
    
    
    E
    r
    r
    o
    r
    s
    e
    n
    c
    o
    u
    n
    t
    e
    r
    e
    d
    d
    u
    r
    i
    n
    g
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
    i
    n
    g
    o
    f
    t
    h
    e
    a
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "ClaimResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        E
        r
        r
        o
        r
        c
        o
        d
        e
        d
        e
        t
        a
        i
        l
        i
        n
        g
        p
        r
        o
        c
        e
        s
        s
        i
        n
        g
        i
        s
        s
        u
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detailSequence = None
        """ 
        D
        e
        t
        a
        i
        l
        s
        e
        q
        u
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
        Type `int`. """
        
        self.itemSequence = None
        """ 
        I
        t
        e
        m
        s
        e
        q
        u
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
        Type `int`. """
        
        self.subDetailSequence = None
        """ 
        S
        u
        b
        d
        e
        t
        a
        i
        l
        s
        e
        q
        u
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
        Type `int`. """
        
        super(ClaimResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("detailSequence", "detailSequence", int, False, None, False),
            ("itemSequence", "itemSequence", int, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, False),
        ])
        return js


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """ 
    P
    a
    t
    i
    e
    n
    t
    i
    n
    s
    u
    r
    a
    n
    c
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
    .
    
    
    F
    i
    n
    a
    n
    c
    i
    a
    l
    i
    n
    s
    t
    r
    u
    m
    e
    n
    t
    s
    f
    o
    r
    r
    e
    i
    m
    b
    u
    r
    s
    e
    m
    e
    n
    t
    f
    o
    r
    t
    h
    e
    h
    e
    a
    l
    t
    h
    c
    a
    r
    e
    p
    r
    o
    d
    u
    c
    t
    s
    a
    n
    d
    s
    e
    r
    v
    i
    c
    e
    s
    s
    p
    e
    c
    i
    f
    i
    e
    d
    o
    n
    t
    h
    e
    c
    l
    a
    i
    m
    .
    
    """
    
    resource_type = "ClaimResponseInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None
        """ 
        A
        d
        d
        i
        t
        i
        o
        n
        a
        l
        p
        r
        o
        v
        i
        d
        e
        r
        c
        o
        n
        t
        r
        a
        c
        t
        n
        u
        m
        b
        e
        r
        .
        Type `str`. """
        
        self.claimResponse = None
        """ 
        A
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        r
        e
        s
        u
        l
        t
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ 
        I
        n
        s
        u
        r
        a
        n
        c
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focal = None
        """ 
        C
        o
        v
        e
        r
        a
        g
        e
        t
        o
        b
        e
        u
        s
        e
        d
        f
        o
        r
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        .
        Type `bool`. """
        
        self.sequence = None
        """ 
        I
        n
        s
        u
        r
        a
        n
        c
        e
        i
        n
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
        .
        Type `int`. """
        
        super(ClaimResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimResponseItem(backboneelement.BackboneElement):
    """ 
    A
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    f
    o
    r
    c
    l
    a
    i
    m
    l
    i
    n
    e
    i
    t
    e
    m
    s
    .
    
    
    A
    c
    l
    a
    i
    m
    l
    i
    n
    e
    .
    E
    i
    t
    h
    e
    r
    a
    s
    i
    m
    p
    l
    e
    (
    a
    p
    r
    o
    d
    u
    c
    t
    o
    r
    s
    e
    r
    v
    i
    c
    e
    )
    o
    r
    a
    '
    g
    r
    o
    u
    p
    '
    o
    f
    d
    e
    t
    a
    i
    l
    s
    w
    h
    i
    c
    h
    c
    a
    n
    a
    l
    s
    o
    b
    e
    a
    s
    i
    m
    p
    l
    e
    i
    t
    e
    m
    s
    o
    r
    g
    r
    o
    u
    p
    s
    o
    f
    s
    u
    b
    -
    d
    e
    t
    a
    i
    l
    s
    .
    
    """
    
    resource_type = "ClaimResponseItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ 
        A
        d
        j
        u
        d
        i
        c
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
        s
        .
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ 
        A
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        f
        o
        r
        c
        l
        a
        i
        m
        d
        e
        t
        a
        i
        l
        s
        .
        List of `ClaimResponseItemDetail` items (represented as `dict` in JSON). """
        
        self.itemSequence = None
        """ 
        C
        l
        a
        i
        m
        i
        t
        e
        m
        i
        n
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
        .
        Type `int`. """
        
        self.noteNumber = None
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
        n
        o
        t
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
        
        super(ClaimResponseItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("detail", "detail", ClaimResponseItemDetail, True, None, False),
            ("itemSequence", "itemSequence", int, False, None, True),
            ("noteNumber", "noteNumber", int, True, None, False),
        ])
        return js


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """ 
    A
    d
    j
    u
    d
    i
    c
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
    s
    .
    
    
    I
    f
    t
    h
    i
    s
    i
    t
    e
    m
    i
    s
    a
    g
    r
    o
    u
    p
    t
    h
    e
    n
    t
    h
    e
    v
    a
    l
    u
    e
    s
    h
    e
    r
    e
    a
    r
    e
    a
    s
    u
    m
    m
    a
    r
    y
    o
    f
    t
    h
    e
    a
    d
    j
    u
    d
    i
    c
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
    d
    e
    t
    a
    i
    l
    i
    t
    e
    m
    s
    .
    I
    f
    t
    h
    i
    s
    i
    t
    e
    m
    i
    s
    a
    s
    i
    m
    p
    l
    e
    p
    r
    o
    d
    u
    c
    t
    o
    r
    s
    e
    r
    v
    i
    c
    e
    t
    h
    e
    n
    t
    h
    i
    s
    i
    s
    t
    h
    e
    r
    e
    s
    u
    l
    t
    o
    f
    t
    h
    e
    a
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    o
    f
    t
    h
    i
    s
    i
    t
    e
    m
    .
    
    """
    
    resource_type = "ClaimResponseItemAdjudication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        M
        o
        n
        e
        t
        a
        r
        y
        a
        m
        o
        u
        n
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        T
        y
        p
        e
        o
        f
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ 
        E
        x
        p
        l
        a
        n
        a
        t
        i
        o
        n
        o
        f
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        o
        u
        t
        c
        o
        m
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        N
        o
        n
        -
        m
        o
        n
        e
        t
        a
        r
        y
        v
        a
        l
        u
        e
        .
        Type `float`. """
        
        super(ClaimResponseItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """ 
    A
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    f
    o
    r
    c
    l
    a
    i
    m
    d
    e
    t
    a
    i
    l
    s
    .
    
    
    A
    c
    l
    a
    i
    m
    d
    e
    t
    a
    i
    l
    .
    E
    i
    t
    h
    e
    r
    a
    s
    i
    m
    p
    l
    e
    (
    a
    p
    r
    o
    d
    u
    c
    t
    o
    r
    s
    e
    r
    v
    i
    c
    e
    )
    o
    r
    a
    '
    g
    r
    o
    u
    p
    '
    o
    f
    s
    u
    b
    -
    d
    e
    t
    a
    i
    l
    s
    w
    h
    i
    c
    h
    a
    r
    e
    s
    i
    m
    p
    l
    e
    i
    t
    e
    m
    s
    .
    
    """
    
    resource_type = "ClaimResponseItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ 
        D
        e
        t
        a
        i
        l
        l
        e
        v
        e
        l
        a
        d
        j
        u
        d
        i
        c
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
        s
        .
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.detailSequence = None
        """ 
        C
        l
        a
        i
        m
        d
        e
        t
        a
        i
        l
        i
        n
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
        .
        Type `int`. """
        
        self.noteNumber = None
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
        n
        o
        t
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
        
        self.subDetail = None
        """ 
        A
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        f
        o
        r
        c
        l
        a
        i
        m
        s
        u
        b
        -
        d
        e
        t
        a
        i
        l
        s
        .
        List of `ClaimResponseItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        super(ClaimResponseItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("detailSequence", "detailSequence", int, False, None, True),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("subDetail", "subDetail", ClaimResponseItemDetailSubDetail, True, None, False),
        ])
        return js


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """ 
    A
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    f
    o
    r
    c
    l
    a
    i
    m
    s
    u
    b
    -
    d
    e
    t
    a
    i
    l
    s
    .
    
    
    A
    s
    u
    b
    -
    d
    e
    t
    a
    i
    l
    a
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    o
    f
    a
    s
    i
    m
    p
    l
    e
    p
    r
    o
    d
    u
    c
    t
    o
    r
    s
    e
    r
    v
    i
    c
    e
    .
    
    """
    
    resource_type = "ClaimResponseItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ 
        S
        u
        b
        d
        e
        t
        a
        i
        l
        l
        e
        v
        e
        l
        a
        d
        j
        u
        d
        i
        c
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
        s
        .
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.noteNumber = None
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
        n
        o
        t
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
        
        self.subDetailSequence = None
        """ 
        C
        l
        a
        i
        m
        s
        u
        b
        -
        d
        e
        t
        a
        i
        l
        i
        n
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
        .
        Type `int`. """
        
        super(ClaimResponseItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, True),
        ])
        return js


class ClaimResponsePayment(backboneelement.BackboneElement):
    """ 
    P
    a
    y
    m
    e
    n
    t
    D
    e
    t
    a
    i
    l
    s
    .
    
    
    P
    a
    y
    m
    e
    n
    t
    d
    e
    t
    a
    i
    l
    s
    f
    o
    r
    t
    h
    e
    a
    d
    j
    u
    d
    i
    c
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
    c
    l
    a
    i
    m
    .
    
    """
    
    resource_type = "ClaimResponsePayment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjustment = None
        """ 
        P
        a
        y
        m
        e
        n
        t
        a
        d
        j
        u
        s
        t
        m
        e
        n
        t
        f
        o
        r
        n
        o
        n
        -
        c
        l
        a
        i
        m
        i
        s
        s
        u
        e
        s
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.adjustmentReason = None
        """ 
        E
        x
        p
        l
        a
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
        a
        d
        j
        u
        s
        t
        m
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.amount = None
        """ 
        P
        a
        y
        a
        b
        l
        e
        a
        m
        o
        u
        n
        t
        a
        f
        t
        e
        r
        a
        d
        j
        u
        s
        t
        m
        e
        n
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        E
        x
        p
        e
        c
        t
        e
        d
        d
        a
        t
        e
        o
        f
        p
        a
        y
        m
        e
        n
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        p
        a
        y
        m
        e
        n
        t
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        P
        a
        r
        t
        i
        a
        l
        o
        r
        c
        o
        m
        p
        l
        e
        t
        e
        p
        a
        y
        m
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimResponsePayment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponsePayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", money.Money, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """ 
    N
    o
    t
    e
    c
    o
    n
    c
    e
    r
    n
    i
    n
    g
    a
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    .
    
    
    A
    n
    o
    t
    e
    t
    h
    a
    t
    d
    e
    s
    c
    r
    i
    b
    e
    s
    o
    r
    e
    x
    p
    l
    a
    i
    n
    s
    a
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    r
    e
    s
    u
    l
    t
    s
    i
    n
    a
    h
    u
    m
    a
    n
    r
    e
    a
    d
    a
    b
    l
    e
    f
    o
    r
    m
    .
    
    """
    
    resource_type = "ClaimResponseProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        t
        e
        x
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.number = None
        """ 
        N
        o
        t
        e
        i
        n
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
        .
        Type `int`. """
        
        self.text = None
        """ 
        N
        o
        t
        e
        e
        x
        p
        l
        a
        n
        a
        t
        o
        r
        y
        t
        e
        x
        t
        .
        Type `str`. """
        
        self.type = None
        """ 
        d
        i
        s
        p
        l
        a
        y
        |
        p
        r
        i
        n
        t
        |
        p
        r
        i
        n
        t
        o
        p
        e
        r
        .
        Type `str`. """
        
        super(ClaimResponseProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, True),
            ("type", "type", str, False, None, False),
        ])
        return js


class ClaimResponseTotal(backboneelement.BackboneElement):
    """ 
    A
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    t
    o
    t
    a
    l
    s
    .
    
    
    C
    a
    t
    e
    g
    o
    r
    i
    z
    e
    d
    m
    o
    n
    e
    t
    a
    r
    y
    t
    o
    t
    a
    l
    s
    f
    o
    r
    t
    h
    e
    a
    d
    j
    u
    d
    i
    c
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "ClaimResponseTotal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        F
        i
        n
        a
        n
        c
        i
        a
        l
        t
        o
        t
        a
        l
        f
        o
        r
        t
        h
        e
        c
        a
        t
        e
        g
        o
        r
        y
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        T
        y
        p
        e
        o
        f
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimResponseTotal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
