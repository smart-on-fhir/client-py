#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class QuestionnaireResponse(domainresource.DomainResource):
    """ 
    A
    s
    t
    r
    u
    c
    t
    u
    r
    e
    d
    s
    e
    t
    o
    f
    q
    u
    e
    s
    t
    i
    o
    n
    s
    a
    n
    d
    t
    h
    e
    i
    r
    a
    n
    s
    w
    e
    r
    s
    .
    
    
    A
    s
    t
    r
    u
    c
    t
    u
    r
    e
    d
    s
    e
    t
    o
    f
    q
    u
    e
    s
    t
    i
    o
    n
    s
    a
    n
    d
    t
    h
    e
    i
    r
    a
    n
    s
    w
    e
    r
    s
    .
    T
    h
    e
    q
    u
    e
    s
    t
    i
    o
    n
    s
    a
    r
    e
    o
    r
    d
    e
    r
    e
    d
    a
    n
    d
    g
    r
    o
    u
    p
    e
    d
    i
    n
    t
    o
    c
    o
    h
    e
    r
    e
    n
    t
    s
    u
    b
    s
    e
    t
    s
    ,
    c
    o
    r
    r
    e
    s
    p
    o
    n
    d
    i
    n
    g
    t
    o
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
    e
    o
    f
    t
    h
    e
    g
    r
    o
    u
    p
    i
    n
    g
    o
    f
    t
    h
    e
    q
    u
    e
    s
    t
    i
    o
    n
    n
    a
    i
    r
    e
    b
    e
    i
    n
    g
    r
    e
    s
    p
    o
    n
    d
    e
    d
    t
    o
    .
    
    """
    
    resource_type = "QuestionnaireResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ 
        P
        e
        r
        s
        o
        n
        w
        h
        o
        r
        e
        c
        e
        i
        v
        e
        d
        a
        n
        d
        r
        e
        c
        o
        r
        d
        e
        d
        t
        h
        e
        a
        n
        s
        w
        e
        r
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authored = None
        """ 
        D
        a
        t
        e
        t
        h
        e
        a
        n
        s
        w
        e
        r
        s
        w
        e
        r
        e
        g
        a
        t
        h
        e
        r
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        f
        u
        l
        f
        i
        l
        l
        e
        d
        b
        y
        t
        h
        i
        s
        Q
        u
        e
        s
        t
        i
        o
        n
        n
        a
        i
        r
        e
        R
        e
        s
        p
        o
        n
        s
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        E
        n
        c
        o
        u
        n
        t
        e
        r
        c
        r
        e
        a
        t
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
        i
        d
        f
        o
        r
        t
        h
        i
        s
        s
        e
        t
        o
        f
        a
        n
        s
        w
        e
        r
        s
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.item = None
        """ 
        G
        r
        o
        u
        p
        s
        a
        n
        d
        q
        u
        e
        s
        t
        i
        o
        n
        s
        .
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ 
        P
        a
        r
        t
        o
        f
        t
        h
        i
        s
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.questionnaire = None
        """ 
        F
        o
        r
        m
        b
        e
        i
        n
        g
        a
        n
        s
        w
        e
        r
        e
        d
        .
        Type `str`. """
        
        self.source = None
        """ 
        T
        h
        e
        p
        e
        r
        s
        o
        n
        w
        h
        o
        a
        n
        s
        w
        e
        r
        e
        d
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        i
        n
        -
        p
        r
        o
        g
        r
        e
        s
        s
        |
        c
        o
        m
        p
        l
        e
        t
        e
        d
        |
        a
        m
        e
        n
        d
        e
        d
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
        |
        s
        t
        o
        p
        p
        e
        d
        .
        Type `str`. """
        
        self.subject = None
        """ 
        T
        h
        e
        s
        u
        b
        j
        e
        c
        t
        o
        f
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(QuestionnaireResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponse, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authored", "authored", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("questionnaire", "questionnaire", str, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireResponseItem(backboneelement.BackboneElement):
    """ 
    G
    r
    o
    u
    p
    s
    a
    n
    d
    q
    u
    e
    s
    t
    i
    o
    n
    s
    .
    
    
    A
    g
    r
    o
    u
    p
    o
    r
    q
    u
    e
    s
    t
    i
    o
    n
    i
    t
    e
    m
    f
    r
    o
    m
    t
    h
    e
    o
    r
    i
    g
    i
    n
    a
    l
    q
    u
    e
    s
    t
    i
    o
    n
    n
    a
    i
    r
    e
    f
    o
    r
    w
    h
    i
    c
    h
    a
    n
    s
    w
    e
    r
    s
    a
    r
    e
    p
    r
    o
    v
    i
    d
    e
    d
    .
    
    """
    
    resource_type = "QuestionnaireResponseItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer = None
        """ 
        T
        h
        e
        r
        e
        s
        p
        o
        n
        s
        e
        (
        s
        )
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        List of `QuestionnaireResponseItemAnswer` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ 
        E
        l
        e
        m
        e
        n
        t
        D
        e
        f
        i
        n
        i
        t
        i
        o
        n
        -
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
        i
        t
        e
        m
        .
        Type `str`. """
        
        self.item = None
        """ 
        N
        e
        s
        t
        e
        d
        q
        u
        e
        s
        t
        i
        o
        n
        n
        a
        i
        r
        e
        r
        e
        s
        p
        o
        n
        s
        e
        i
        t
        e
        m
        s
        .
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        self.linkId = None
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
        e
        m
        f
        r
        o
        m
        Q
        u
        e
        s
        t
        i
        o
        n
        n
        a
        i
        r
        e
        .
        Type `str`. """
        
        self.text = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        g
        r
        o
        u
        p
        o
        r
        q
        u
        e
        s
        t
        i
        o
        n
        t
        e
        x
        t
        .
        Type `str`. """
        
        super(QuestionnaireResponseItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponseItem, self).elementProperties()
        js.extend([
            ("answer", "answer", QuestionnaireResponseItemAnswer, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("text", "text", str, False, None, False),
        ])
        return js


class QuestionnaireResponseItemAnswer(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    r
    e
    s
    p
    o
    n
    s
    e
    (
    s
    )
    t
    o
    t
    h
    e
    q
    u
    e
    s
    t
    i
    o
    n
    .
    
    
    T
    h
    e
    r
    e
    s
    p
    o
    n
    d
    e
    n
    t
    '
    s
    a
    n
    s
    w
    e
    r
    (
    s
    )
    t
    o
    t
    h
    e
    q
    u
    e
    s
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "QuestionnaireResponseItemAnswer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item = None
        """ 
        N
        e
        s
        t
        e
        d
        g
        r
        o
        u
        p
        s
        a
        n
        d
        q
        u
        e
        s
        t
        i
        o
        n
        s
        .
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `bool`. """
        
        self.valueCoding = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `float`. """
        
        self.valueInteger = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `int`. """
        
        self.valueQuantity = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.valueTime = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueUri = None
        """ 
        S
        i
        n
        g
        l
        e
        -
        v
        a
        l
        u
        e
        d
        a
        n
        s
        w
        e
        r
        t
        o
        t
        h
        e
        q
        u
        e
        s
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(QuestionnaireResponseItemAnswer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponseItemAnswer, self).elementProperties()
        js.extend([
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
