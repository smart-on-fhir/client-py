#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Questionnaire(domainresource.DomainResource):
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
    i
    n
    t
    e
    n
    d
    e
    d
    t
    o
    g
    u
    i
    d
    e
    t
    h
    e
    c
    o
    l
    l
    e
    c
    t
    i
    o
    n
    o
    f
    a
    n
    s
    w
    e
    r
    s
    f
    r
    o
    m
    e
    n
    d
    -
    u
    s
    e
    r
    s
    .
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
    s
    p
    r
    o
    v
    i
    d
    e
    d
    e
    t
    a
    i
    l
    e
    d
    c
    o
    n
    t
    r
    o
    l
    o
    v
    e
    r
    o
    r
    d
    e
    r
    ,
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
    ,
    p
    h
    r
    a
    s
    e
    o
    l
    o
    g
    y
    a
    n
    d
    g
    r
    o
    u
    p
    i
    n
    g
    t
    o
    a
    l
    l
    o
    w
    c
    o
    h
    e
    r
    e
    n
    t
    ,
    c
    o
    n
    s
    i
    s
    t
    e
    n
    t
    d
    a
    t
    a
    c
    o
    l
    l
    e
    c
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "Questionnaire"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ 
        W
        h
        e
        n
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
        w
        a
        s
        a
        p
        p
        r
        o
        v
        e
        d
        b
        y
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.code = None
        """ 
        C
        o
        n
        c
        e
        p
        t
        t
        h
        a
        t
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
        t
        h
        e
        o
        v
        e
        r
        a
        l
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
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ 
        C
        o
        n
        t
        a
        c
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
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ 
        U
        s
        e
        a
        n
        d
        /
        o
        r
        p
        u
        b
        l
        i
        s
        h
        i
        n
        g
        r
        e
        s
        t
        r
        i
        c
        t
        i
        o
        n
        s
        .
        Type `str`. """
        
        self.date = None
        """ 
        D
        a
        t
        e
        l
        a
        s
        t
        c
        h
        a
        n
        g
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.derivedFrom = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
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
        .
        List of `str` items. """
        
        self.description = None
        """ 
        N
        a
        t
        u
        r
        a
        l
        l
        a
        n
        g
        u
        a
        g
        e
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
        .
        Type `str`. """
        
        self.effectivePeriod = None
        """ 
        W
        h
        e
        n
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
        i
        s
        e
        x
        p
        e
        c
        t
        e
        d
        t
        o
        b
        e
        u
        s
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ 
        F
        o
        r
        t
        e
        s
        t
        i
        n
        g
        p
        u
        r
        p
        o
        s
        e
        s
        ,
        n
        o
        t
        r
        e
        a
        l
        u
        s
        a
        g
        e
        .
        Type `bool`. """
        
        self.identifier = None
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.item = None
        """ 
        Q
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
        s
        e
        c
        t
        i
        o
        n
        s
        w
        i
        t
        h
        i
        n
        t
        h
        e
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
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
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
        f
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
        n
        a
        i
        r
        e
        (
        i
        f
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
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ 
        W
        h
        e
        n
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
        w
        a
        s
        l
        a
        s
        t
        r
        e
        v
        i
        e
        w
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ 
        N
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
        (
        c
        o
        m
        p
        u
        t
        e
        r
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.publisher = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        p
        u
        b
        l
        i
        s
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
        Type `str`. """
        
        self.purpose = None
        """ 
        W
        h
        y
        t
        h
        i
        s
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
        i
        s
        d
        e
        f
        i
        n
        e
        d
        .
        Type `str`. """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        a
        c
        t
        i
        v
        e
        |
        r
        e
        t
        i
        r
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
        Type `str`. """
        
        self.subjectType = None
        """ 
        R
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
        c
        a
        n
        b
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
        List of `str` items. """
        
        self.title = None
        """ 
        N
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
        (
        h
        u
        m
        a
        n
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.url = None
        """ 
        C
        a
        n
        o
        n
        i
        c
        a
        l
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
        ,
        r
        e
        p
        r
        e
        s
        e
        n
        t
        e
        d
        a
        s
        a
        U
        R
        I
        (
        g
        l
        o
        b
        a
        l
        l
        y
        u
        n
        i
        q
        u
        e
        )
        .
        Type `str`. """
        
        self.useContext = None
        """ 
        T
        h
        e
        c
        o
        n
        t
        e
        x
        t
        t
        h
        a
        t
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
        i
        s
        i
        n
        t
        e
        n
        d
        e
        d
        t
        o
        s
        u
        p
        p
        o
        r
        t
        .
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
        v
        e
        r
        s
        i
        o
        n
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
        .
        Type `str`. """
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivedFrom", "derivedFrom", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectType", "subjectType", str, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireItem(backboneelement.BackboneElement):
    """ 
    Q
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
    s
    e
    c
    t
    i
    o
    n
    s
    w
    i
    t
    h
    i
    n
    t
    h
    e
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
    
    
    A
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
    q
    u
    e
    s
    t
    i
    o
    n
    ,
    q
    u
    e
    s
    t
    i
    o
    n
    g
    r
    o
    u
    p
    i
    n
    g
    o
    r
    d
    i
    s
    p
    l
    a
    y
    t
    e
    x
    t
    t
    h
    a
    t
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
    .
    
    """
    
    resource_type = "QuestionnaireItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answerOption = None
        """ 
        P
        e
        r
        m
        i
        t
        t
        e
        d
        a
        n
        s
        w
        e
        r
        .
        List of `QuestionnaireItemAnswerOption` items (represented as `dict` in JSON). """
        
        self.answerValueSet = None
        """ 
        V
        a
        l
        u
        e
        s
        e
        t
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
        p
        e
        r
        m
        i
        t
        t
        e
        d
        a
        n
        s
        w
        e
        r
        s
        .
        Type `str`. """
        
        self.code = None
        """ 
        C
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
        c
        o
        n
        c
        e
        p
        t
        f
        o
        r
        t
        h
        i
        s
        i
        t
        e
        m
        i
        n
        a
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
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
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
        
        self.enableBehavior = None
        """ 
        a
        l
        l
        |
        a
        n
        y
        .
        Type `str`. """
        
        self.enableWhen = None
        """ 
        O
        n
        l
        y
        a
        l
        l
        o
        w
        d
        a
        t
        a
        w
        h
        e
        n
        .
        List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON). """
        
        self.initial = None
        """ 
        I
        n
        i
        t
        i
        a
        l
        v
        a
        l
        u
        e
        (
        s
        )
        w
        h
        e
        n
        i
        t
        e
        m
        i
        s
        f
        i
        r
        s
        t
        r
        e
        n
        d
        e
        r
        e
        d
        .
        List of `QuestionnaireItemInitial` items (represented as `dict` in JSON). """
        
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
        i
        t
        e
        m
        s
        .
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        self.linkId = None
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
        i
        t
        e
        m
        i
        n
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
        .
        Type `str`. """
        
        self.maxLength = None
        """ 
        N
        o
        m
        o
        r
        e
        t
        h
        a
        n
        t
        h
        i
        s
        m
        a
        n
        y
        c
        h
        a
        r
        a
        c
        t
        e
        r
        s
        .
        Type `int`. """
        
        self.prefix = None
        """ 
        E
        .
        g
        .
        "
        1
        (
        a
        )
        "
        ,
        "
        2
        .
        5
        .
        3
        "
        .
        Type `str`. """
        
        self.readOnly = None
        """ 
        D
        o
        n
        '
        t
        a
        l
        l
        o
        w
        h
        u
        m
        a
        n
        e
        d
        i
        t
        i
        n
        g
        .
        Type `bool`. """
        
        self.repeats = None
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
        i
        t
        e
        m
        m
        a
        y
        r
        e
        p
        e
        a
        t
        .
        Type `bool`. """
        
        self.required = None
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
        i
        t
        e
        m
        m
        u
        s
        t
        b
        e
        i
        n
        c
        l
        u
        d
        e
        d
        i
        n
        d
        a
        t
        a
        r
        e
        s
        u
        l
        t
        s
        .
        Type `bool`. """
        
        self.text = None
        """ 
        P
        r
        i
        m
        a
        r
        y
        t
        e
        x
        t
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
        
        self.type = None
        """ 
        g
        r
        o
        u
        p
        |
        d
        i
        s
        p
        l
        a
        y
        |
        b
        o
        o
        l
        e
        a
        n
        |
        d
        e
        c
        i
        m
        a
        l
        |
        i
        n
        t
        e
        g
        e
        r
        |
        d
        a
        t
        e
        |
        d
        a
        t
        e
        T
        i
        m
        e
        +
        .
        Type `str`. """
        
        super(QuestionnaireItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, True, None, False),
            ("answerValueSet", "answerValueSet", str, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("enableBehavior", "enableBehavior", str, False, None, False),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False),
            ("initial", "initial", QuestionnaireItemInitial, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("maxLength", "maxLength", int, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("readOnly", "readOnly", bool, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("required", "required", bool, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """ 
    P
    e
    r
    m
    i
    t
    t
    e
    d
    a
    n
    s
    w
    e
    r
    .
    
    
    O
    n
    e
    o
    f
    t
    h
    e
    p
    e
    r
    m
    i
    t
    t
    e
    d
    a
    n
    s
    w
    e
    r
    s
    f
    o
    r
    a
    "
    c
    h
    o
    i
    c
    e
    "
    o
    r
    "
    o
    p
    e
    n
    -
    c
    h
    o
    i
    c
    e
    "
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
    
    resource_type = "QuestionnaireItemAnswerOption"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.initialSelected = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        o
        p
        t
        i
        o
        n
        i
        s
        s
        e
        l
        e
        c
        t
        e
        d
        b
        y
        d
        e
        f
        a
        u
        l
        t
        .
        Type `bool`. """
        
        self.valueCoding = None
        """ 
        A
        n
        s
        w
        e
        r
        v
        a
        l
        u
        e
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ 
        A
        n
        s
        w
        e
        r
        v
        a
        l
        u
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ 
        A
        n
        s
        w
        e
        r
        v
        a
        l
        u
        e
        .
        Type `int`. """
        
        self.valueReference = None
        """ 
        A
        n
        s
        w
        e
        r
        v
        a
        l
        u
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ 
        A
        n
        s
        w
        e
        r
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        self.valueTime = None
        """ 
        A
        n
        s
        w
        e
        r
        v
        a
        l
        u
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(QuestionnaireItemAnswerOption, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("initialSelected", "initialSelected", bool, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
        ])
        return js


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ 
    O
    n
    l
    y
    a
    l
    l
    o
    w
    d
    a
    t
    a
    w
    h
    e
    n
    .
    
    
    A
    c
    o
    n
    s
    t
    r
    a
    i
    n
    t
    i
    n
    d
    i
    c
    a
    t
    i
    n
    g
    t
    h
    a
    t
    t
    h
    i
    s
    i
    t
    e
    m
    s
    h
    o
    u
    l
    d
    o
    n
    l
    y
    b
    e
    e
    n
    a
    b
    l
    e
    d
    (
    d
    i
    s
    p
    l
    a
    y
    e
    d
    /
    a
    l
    l
    o
    w
    a
    n
    s
    w
    e
    r
    s
    t
    o
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
    )
    w
    h
    e
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
    e
    d
    c
    o
    n
    d
    i
    t
    i
    o
    n
    i
    s
    t
    r
    u
    e
    .
    
    """
    
    resource_type = "QuestionnaireItemEnableWhen"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answerBoolean = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `bool`. """
        
        self.answerCoding = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.answerDate = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDateTime = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDecimal = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `float`. """
        
        self.answerInteger = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `int`. """
        
        self.answerQuantity = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.answerReference = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.answerString = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `str`. """
        
        self.answerTime = None
        """ 
        V
        a
        l
        u
        e
        f
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
        b
        a
        s
        e
        d
        o
        n
        o
        p
        e
        r
        a
        t
        o
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.operator = None
        """ 
        e
        x
        i
        s
        t
        s
        |
        =
        |
        !
        =
        |
        >
        |
        <
        |
        >
        =
        |
        <
        =
        .
        Type `str`. """
        
        self.question = None
        """ 
        Q
        u
        e
        s
        t
        i
        o
        n
        t
        h
        a
        t
        d
        e
        t
        e
        r
        m
        i
        n
        e
        s
        w
        h
        e
        t
        h
        e
        r
        i
        t
        e
        m
        i
        s
        e
        n
        a
        b
        l
        e
        d
        .
        Type `str`. """
        
        super(QuestionnaireItemEnableWhen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("answerBoolean", "answerBoolean", bool, False, "answer", True),
            ("answerCoding", "answerCoding", coding.Coding, False, "answer", True),
            ("answerDate", "answerDate", fhirdate.FHIRDate, False, "answer", True),
            ("answerDateTime", "answerDateTime", fhirdate.FHIRDate, False, "answer", True),
            ("answerDecimal", "answerDecimal", float, False, "answer", True),
            ("answerInteger", "answerInteger", int, False, "answer", True),
            ("answerQuantity", "answerQuantity", quantity.Quantity, False, "answer", True),
            ("answerReference", "answerReference", fhirreference.FHIRReference, False, "answer", True),
            ("answerString", "answerString", str, False, "answer", True),
            ("answerTime", "answerTime", fhirdate.FHIRDate, False, "answer", True),
            ("operator", "operator", str, False, None, True),
            ("question", "question", str, False, None, True),
        ])
        return js


class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """ 
    I
    n
    i
    t
    i
    a
    l
    v
    a
    l
    u
    e
    (
    s
    )
    w
    h
    e
    n
    i
    t
    e
    m
    i
    s
    f
    i
    r
    s
    t
    r
    e
    n
    d
    e
    r
    e
    d
    .
    
    
    O
    n
    e
    o
    r
    m
    o
    r
    e
    v
    a
    l
    u
    e
    s
    t
    h
    a
    t
    s
    h
    o
    u
    l
    d
    b
    e
    p
    r
    e
    -
    p
    o
    p
    u
    l
    a
    t
    e
    d
    i
    n
    t
    h
    e
    a
    n
    s
    w
    e
    r
    w
    h
    e
    n
    i
    n
    i
    t
    i
    a
    l
    l
    y
    r
    e
    n
    d
    e
    r
    i
    n
    g
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
    f
    o
    r
    u
    s
    e
    r
    i
    n
    p
    u
    t
    .
    
    """
    
    resource_type = "QuestionnaireItemInitial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueAttachment = None
        """ 
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        A
        c
        t
        u
        a
        l
        v
        a
        l
        u
        e
        f
        o
        r
        i
        n
        i
        t
        i
        a
        l
        i
        z
        i
        n
        g
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
        
        super(QuestionnaireItemInitial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemInitial, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
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
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
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
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
