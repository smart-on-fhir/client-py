#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationKnowledge) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicationKnowledge(domainresource.DomainResource):
    """ 
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
    o
    f
    M
    e
    d
    i
    c
    a
    t
    i
    o
    n
    K
    n
    o
    w
    l
    e
    d
    g
    e
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
    a
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
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
    t
    o
    s
    u
    p
    p
    o
    r
    t
    k
    n
    o
    w
    l
    e
    d
    g
    e
    .
    
    """
    
    resource_type = "MedicationKnowledge"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.administrationGuidelines = None
        """ 
        G
        u
        i
        d
        e
        l
        i
        n
        e
        s
        f
        o
        r
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
        t
        i
        o
        n
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
        a
        t
        i
        o
        n
        .
        List of `MedicationKnowledgeAdministrationGuidelines` items (represented as `dict` in JSON). """
        
        self.amount = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
        d
        r
        u
        g
        i
        n
        p
        a
        c
        k
        a
        g
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.associatedMedication = None
        """ 
        A
        m
        e
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
        o
        u
        r
        c
        e
        t
        h
        a
        t
        i
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
        i
        s
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        C
        o
        d
        e
        t
        h
        a
        t
        i
        d
        e
        n
        t
        i
        f
        i
        e
        s
        t
        h
        i
        s
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contraindication = None
        """ 
        P
        o
        t
        e
        n
        t
        i
        a
        l
        c
        l
        i
        n
        i
        c
        a
        l
        i
        s
        s
        u
        e
        w
        i
        t
        h
        o
        r
        b
        e
        t
        w
        e
        e
        n
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        (
        s
        )
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.cost = None
        """ 
        T
        h
        e
        p
        r
        i
        c
        i
        n
        g
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
        a
        t
        i
        o
        n
        .
        List of `MedicationKnowledgeCost` items (represented as `dict` in JSON). """
        
        self.doseForm = None
        """ 
        p
        o
        w
        d
        e
        r
        |
        t
        a
        b
        l
        e
        t
        s
        |
        c
        a
        p
        s
        u
        l
        e
        +
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.drugCharacteristic = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        s
        d
        e
        s
        c
        r
        i
        p
        t
        i
        v
        e
        p
        r
        o
        p
        e
        r
        t
        i
        e
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
        e
        .
        List of `MedicationKnowledgeDrugCharacteristic` items (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ 
        A
        c
        t
        i
        v
        e
        o
        r
        i
        n
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
        .
        List of `MedicationKnowledgeIngredient` items (represented as `dict` in JSON). """
        
        self.intendedRoute = None
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
        o
        r
        a
        p
        p
        r
        o
        v
        e
        d
        r
        o
        u
        t
        e
        o
        f
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
        t
        i
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kinetics = None
        """ 
        T
        h
        e
        t
        i
        m
        e
        c
        o
        u
        r
        s
        e
        o
        f
        d
        r
        u
        g
        a
        b
        s
        o
        r
        p
        t
        i
        o
        n
        ,
        d
        i
        s
        t
        r
        i
        b
        u
        t
        i
        o
        n
        ,
        m
        e
        t
        a
        b
        o
        l
        i
        s
        m
        a
        n
        d
        e
        x
        c
        r
        e
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
        a
        t
        i
        o
        n
        f
        r
        o
        m
        t
        h
        e
        b
        o
        d
        y
        .
        List of `MedicationKnowledgeKinetics` items (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ 
        M
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
        f
        t
        h
        e
        i
        t
        e
        m
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.medicineClassification = None
        """ 
        C
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
        a
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
        f
        o
        r
        m
        u
        l
        a
        r
        y
        o
        r
        c
        l
        a
        s
        s
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
        y
        s
        t
        e
        m
        .
        List of `MedicationKnowledgeMedicineClassification` items (represented as `dict` in JSON). """
        
        self.monitoringProgram = None
        """ 
        P
        r
        o
        g
        r
        a
        m
        u
        n
        d
        e
        r
        w
        h
        i
        c
        h
        a
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        i
        s
        r
        e
        v
        i
        e
        w
        e
        d
        .
        List of `MedicationKnowledgeMonitoringProgram` items (represented as `dict` in JSON). """
        
        self.monograph = None
        """ 
        A
        s
        s
        o
        c
        i
        a
        t
        e
        d
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
        a
        b
        o
        u
        t
        t
        h
        e
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `MedicationKnowledgeMonograph` items (represented as `dict` in JSON). """
        
        self.packaging = None
        """ 
        D
        e
        t
        a
        i
        l
        s
        a
        b
        o
        u
        t
        p
        a
        c
        k
        a
        g
        e
        d
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        s
        .
        Type `MedicationKnowledgePackaging` (represented as `dict` in JSON). """
        
        self.preparationInstruction = None
        """ 
        T
        h
        e
        i
        n
        s
        t
        r
        u
        c
        t
        i
        o
        n
        s
        f
        o
        r
        p
        r
        e
        p
        a
        r
        i
        n
        g
        t
        h
        e
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.productType = None
        """ 
        C
        a
        t
        e
        g
        o
        r
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
        a
        t
        i
        o
        n
        o
        r
        p
        r
        o
        d
        u
        c
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.regulatory = None
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
        a
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `MedicationKnowledgeRegulatory` items (represented as `dict` in JSON). """
        
        self.relatedMedicationKnowledge = None
        """ 
        A
        s
        s
        o
        c
        i
        a
        t
        e
        d
        o
        r
        r
        e
        l
        a
        t
        e
        d
        m
        e
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
        List of `MedicationKnowledgeRelatedMedicationKnowledge` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
        e
        |
        i
        n
        a
        c
        t
        i
        v
        e
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
        
        self.synonym = None
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
        n
        a
        m
        e
        s
        f
        o
        r
        a
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `str` items. """
        
        super(MedicationKnowledge, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledge, self).elementProperties()
        js.extend([
            ("administrationGuidelines", "administrationGuidelines", MedicationKnowledgeAdministrationGuidelines, True, None, False),
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("associatedMedication", "associatedMedication", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contraindication", "contraindication", fhirreference.FHIRReference, True, None, False),
            ("cost", "cost", MedicationKnowledgeCost, True, None, False),
            ("doseForm", "doseForm", codeableconcept.CodeableConcept, False, None, False),
            ("drugCharacteristic", "drugCharacteristic", MedicationKnowledgeDrugCharacteristic, True, None, False),
            ("ingredient", "ingredient", MedicationKnowledgeIngredient, True, None, False),
            ("intendedRoute", "intendedRoute", codeableconcept.CodeableConcept, True, None, False),
            ("kinetics", "kinetics", MedicationKnowledgeKinetics, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("medicineClassification", "medicineClassification", MedicationKnowledgeMedicineClassification, True, None, False),
            ("monitoringProgram", "monitoringProgram", MedicationKnowledgeMonitoringProgram, True, None, False),
            ("monograph", "monograph", MedicationKnowledgeMonograph, True, None, False),
            ("packaging", "packaging", MedicationKnowledgePackaging, False, None, False),
            ("preparationInstruction", "preparationInstruction", str, False, None, False),
            ("productType", "productType", codeableconcept.CodeableConcept, True, None, False),
            ("regulatory", "regulatory", MedicationKnowledgeRegulatory, True, None, False),
            ("relatedMedicationKnowledge", "relatedMedicationKnowledge", MedicationKnowledgeRelatedMedicationKnowledge, True, None, False),
            ("status", "status", str, False, None, False),
            ("synonym", "synonym", str, True, None, False),
        ])
        return js


from . import backboneelement

class MedicationKnowledgeAdministrationGuidelines(backboneelement.BackboneElement):
    """ 
    G
    u
    i
    d
    e
    l
    i
    n
    e
    s
    f
    o
    r
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
    t
    i
    o
    n
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
    a
    t
    i
    o
    n
    .
    
    
    G
    u
    i
    d
    e
    l
    i
    n
    e
    s
    f
    o
    r
    t
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
    t
    i
    o
    n
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
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "MedicationKnowledgeAdministrationGuidelines"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dosage = None
        """ 
        D
        o
        s
        a
        g
        e
        f
        o
        r
        t
        h
        e
        m
        e
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
        g
        u
        i
        d
        e
        l
        i
        n
        e
        s
        .
        List of `MedicationKnowledgeAdministrationGuidelinesDosage` items (represented as `dict` in JSON). """
        
        self.indicationCodeableConcept = None
        """ 
        I
        n
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
        u
        s
        e
        t
        h
        a
        t
        a
        p
        p
        l
        y
        t
        o
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
        t
        i
        o
        n
        g
        u
        i
        d
        e
        l
        i
        n
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.indicationReference = None
        """ 
        I
        n
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
        u
        s
        e
        t
        h
        a
        t
        a
        p
        p
        l
        y
        t
        o
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
        t
        i
        o
        n
        g
        u
        i
        d
        e
        l
        i
        n
        e
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patientCharacteristics = None
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
        o
        f
        t
        h
        e
        p
        a
        t
        i
        e
        n
        t
        t
        h
        a
        t
        a
        r
        e
        r
        e
        l
        e
        v
        a
        n
        t
        t
        o
        t
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
        t
        i
        o
        n
        g
        u
        i
        d
        e
        l
        i
        n
        e
        s
        .
        List of `MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics` items (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeAdministrationGuidelines, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelines, self).elementProperties()
        js.extend([
            ("dosage", "dosage", MedicationKnowledgeAdministrationGuidelinesDosage, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", codeableconcept.CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", fhirreference.FHIRReference, False, "indication", False),
            ("patientCharacteristics", "patientCharacteristics", MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, True, None, False),
        ])
        return js


class MedicationKnowledgeAdministrationGuidelinesDosage(backboneelement.BackboneElement):
    """ 
    D
    o
    s
    a
    g
    e
    f
    o
    r
    t
    h
    e
    m
    e
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
    g
    u
    i
    d
    e
    l
    i
    n
    e
    s
    .
    """
    
    resource_type = "MedicationKnowledgeAdministrationGuidelinesDosage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dosage = None
        """ 
        D
        o
        s
        a
        g
        e
        f
        o
        r
        t
        h
        e
        m
        e
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
        g
        u
        i
        d
        e
        l
        i
        n
        e
        s
        .
        List of `Dosage` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        d
        o
        s
        a
        g
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeAdministrationGuidelinesDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesDosage, self).elementProperties()
        js.extend([
            ("dosage", "dosage", dosage.Dosage, True, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(backboneelement.BackboneElement):
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
    o
    f
    t
    h
    e
    p
    a
    t
    i
    e
    n
    t
    t
    h
    a
    t
    a
    r
    e
    r
    e
    l
    e
    v
    a
    n
    t
    t
    o
    t
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
    t
    i
    o
    n
    g
    u
    i
    d
    e
    l
    i
    n
    e
    s
    .
    
    
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
    o
    f
    t
    h
    e
    p
    a
    t
    i
    e
    n
    t
    t
    h
    a
    t
    a
    r
    e
    r
    e
    l
    e
    v
    a
    n
    t
    t
    o
    t
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
    t
    i
    o
    n
    g
    u
    i
    d
    e
    l
    i
    n
    e
    s
    (
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
    ,
    h
    e
    i
    g
    h
    t
    ,
    w
    e
    i
    g
    h
    t
    ,
    g
    e
    n
    d
    e
    r
    ,
    e
    t
    c
    .
    )
    .
    
    """
    
    resource_type = "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.characteristicCodeableConcept = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
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
        t
        h
        a
        t
        i
        s
        r
        e
        l
        e
        v
        a
        n
        t
        t
        o
        t
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
        t
        i
        o
        n
        g
        u
        i
        d
        e
        l
        i
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.characteristicQuantity = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
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
        t
        h
        a
        t
        i
        s
        r
        e
        l
        e
        v
        a
        n
        t
        t
        o
        t
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
        t
        i
        o
        n
        g
        u
        i
        d
        e
        l
        i
        n
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.value = None
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
        List of `str` items. """
        
        super(MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, self).elementProperties()
        js.extend([
            ("characteristicCodeableConcept", "characteristicCodeableConcept", codeableconcept.CodeableConcept, False, "characteristic", True),
            ("characteristicQuantity", "characteristicQuantity", quantity.Quantity, False, "characteristic", True),
            ("value", "value", str, True, None, False),
        ])
        return js


class MedicationKnowledgeCost(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    p
    r
    i
    c
    i
    n
    g
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
    a
    t
    i
    o
    n
    .
    
    
    T
    h
    e
    p
    r
    i
    c
    e
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
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "MedicationKnowledgeCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cost = None
        """ 
        T
        h
        e
        p
        r
        i
        c
        e
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
        a
        t
        i
        o
        n
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        T
        h
        e
        s
        o
        u
        r
        c
        e
        o
        r
        o
        w
        n
        e
        r
        f
        o
        r
        t
        h
        e
        p
        r
        i
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
        Type `str`. """
        
        self.type = None
        """ 
        T
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
        o
        f
        t
        h
        e
        c
        o
        s
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeCost, self).elementProperties()
        js.extend([
            ("cost", "cost", money.Money, False, None, True),
            ("source", "source", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicationKnowledgeDrugCharacteristic(backboneelement.BackboneElement):
    """ 
    S
    p
    e
    c
    i
    f
    i
    e
    s
    d
    e
    s
    c
    r
    i
    p
    t
    i
    v
    e
    p
    r
    o
    p
    e
    r
    t
    i
    e
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
    e
    .
    
    
    S
    p
    e
    c
    i
    f
    i
    e
    s
    d
    e
    s
    c
    r
    i
    p
    t
    i
    v
    e
    p
    r
    o
    p
    e
    r
    t
    i
    e
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
    e
    ,
    s
    u
    c
    h
    a
    s
    c
    o
    l
    o
    r
    ,
    s
    h
    a
    p
    e
    ,
    i
    m
    p
    r
    i
    n
    t
    s
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "MedicationKnowledgeDrugCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ 
        C
        o
        d
        e
        s
        p
        e
        c
        i
        f
        y
        i
        n
        g
        t
        h
        e
        t
        y
        p
        e
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
        o
        f
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ 
        D
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
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ 
        D
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
        
        self.valueQuantity = None
        """ 
        D
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
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ 
        D
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
        Type `str`. """
        
        super(MedicationKnowledgeDrugCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeDrugCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js


class MedicationKnowledgeIngredient(backboneelement.BackboneElement):
    """ 
    A
    c
    t
    i
    v
    e
    o
    r
    i
    n
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
    .
    
    
    I
    d
    e
    n
    t
    i
    f
    i
    e
    s
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
    c
    o
    n
    s
    t
    i
    t
    u
    e
    n
    t
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
    i
    n
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
    
    """
    
    resource_type = "MedicationKnowledgeIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.isActive = None
        """ 
        A
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
        i
        n
        d
        i
        c
        a
        t
        o
        r
        .
        Type `bool`. """
        
        self.itemCodeableConcept = None
        """ 
        M
        e
        d
        i
        c
        a
        t
        i
        o
        n
        (
        s
        )
        o
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
        (
        s
        )
        c
        o
        n
        t
        a
        i
        n
        e
        d
        i
        n
        t
        h
        e
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ 
        M
        e
        d
        i
        c
        a
        t
        i
        o
        n
        (
        s
        )
        o
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
        (
        s
        )
        c
        o
        n
        t
        a
        i
        n
        e
        d
        i
        n
        t
        h
        e
        m
        e
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
        
        self.strength = None
        """ 
        Q
        u
        a
        n
        t
        i
        t
        y
        o
        f
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
        p
        r
        e
        s
        e
        n
        t
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("strength", "strength", ratio.Ratio, False, None, False),
        ])
        return js


class MedicationKnowledgeKinetics(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    t
    i
    m
    e
    c
    o
    u
    r
    s
    e
    o
    f
    d
    r
    u
    g
    a
    b
    s
    o
    r
    p
    t
    i
    o
    n
    ,
    d
    i
    s
    t
    r
    i
    b
    u
    t
    i
    o
    n
    ,
    m
    e
    t
    a
    b
    o
    l
    i
    s
    m
    a
    n
    d
    e
    x
    c
    r
    e
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
    a
    t
    i
    o
    n
    f
    r
    o
    m
    t
    h
    e
    b
    o
    d
    y
    .
    """
    
    resource_type = "MedicationKnowledgeKinetics"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.areaUnderCurve = None
        """ 
        T
        h
        e
        d
        r
        u
        g
        c
        o
        n
        c
        e
        n
        t
        r
        a
        t
        i
        o
        n
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
        c
        e
        r
        t
        a
        i
        n
        d
        i
        s
        c
        r
        e
        t
        e
        p
        o
        i
        n
        t
        s
        i
        n
        t
        i
        m
        e
        .
        List of `Quantity` items (represented as `dict` in JSON). """
        
        self.halfLifePeriod = None
        """ 
        T
        i
        m
        e
        r
        e
        q
        u
        i
        r
        e
        d
        f
        o
        r
        c
        o
        n
        c
        e
        n
        t
        r
        a
        t
        i
        o
        n
        i
        n
        t
        h
        e
        b
        o
        d
        y
        t
        o
        d
        e
        c
        r
        e
        a
        s
        e
        b
        y
        h
        a
        l
        f
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.lethalDose50 = None
        """ 
        T
        h
        e
        m
        e
        d
        i
        a
        n
        l
        e
        t
        h
        a
        l
        d
        o
        s
        e
        o
        f
        a
        d
        r
        u
        g
        .
        List of `Quantity` items (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeKinetics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeKinetics, self).elementProperties()
        js.extend([
            ("areaUnderCurve", "areaUnderCurve", quantity.Quantity, True, None, False),
            ("halfLifePeriod", "halfLifePeriod", duration.Duration, False, None, False),
            ("lethalDose50", "lethalDose50", quantity.Quantity, True, None, False),
        ])
        return js


class MedicationKnowledgeMedicineClassification(backboneelement.BackboneElement):
    """ 
    C
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
    a
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
    f
    o
    r
    m
    u
    l
    a
    r
    y
    o
    r
    c
    l
    a
    s
    s
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
    y
    s
    t
    e
    m
    .
    """
    
    resource_type = "MedicationKnowledgeMedicineClassification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        c
        a
        t
        e
        g
        o
        r
        y
        a
        s
        s
        i
        g
        n
        e
        d
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
        a
        t
        i
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        e
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        (
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
        ,
        t
        h
        e
        r
        a
        p
        e
        u
        t
        i
        c
        c
        l
        a
        s
        s
        i
        f
        i
        c
        a
        t
        i
        o
        n
        ,
        t
        h
        e
        r
        a
        p
        e
        u
        t
        i
        c
        s
        u
        b
        -
        c
        l
        a
        s
        s
        i
        f
        i
        c
        a
        t
        i
        o
        n
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeMedicineClassification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMedicineClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicationKnowledgeMonitoringProgram(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    g
    r
    a
    m
    u
    n
    d
    e
    r
    w
    h
    i
    c
    h
    a
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    i
    s
    r
    e
    v
    i
    e
    w
    e
    d
    .
    
    
    T
    h
    e
    p
    r
    o
    g
    r
    a
    m
    u
    n
    d
    e
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
    a
    t
    i
    o
    n
    i
    s
    r
    e
    v
    i
    e
    w
    e
    d
    .
    
    """
    
    resource_type = "MedicationKnowledgeMonitoringProgram"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
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
        r
        e
        v
        i
        e
        w
        i
        n
        g
        p
        r
        o
        g
        r
        a
        m
        .
        Type `str`. """
        
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
        g
        r
        a
        m
        u
        n
        d
        e
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
        a
        t
        i
        o
        n
        i
        s
        m
        o
        n
        i
        t
        o
        r
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeMonitoringProgram, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMonitoringProgram, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicationKnowledgeMonograph(backboneelement.BackboneElement):
    """ 
    A
    s
    s
    o
    c
    i
    a
    t
    e
    d
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
    a
    b
    o
    u
    t
    t
    h
    e
    m
    e
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
    
    resource_type = "MedicationKnowledgeMonograph"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.source = None
        """ 
        A
        s
        s
        o
        c
        i
        a
        t
        e
        d
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
        a
        b
        o
        u
        t
        t
        h
        e
        m
        e
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
        
        self.type = None
        """ 
        T
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
        o
        f
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        d
        o
        c
        u
        m
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeMonograph, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMonograph, self).elementProperties()
        js.extend([
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicationKnowledgePackaging(backboneelement.BackboneElement):
    """ 
    D
    e
    t
    a
    i
    l
    s
    a
    b
    o
    u
    t
    p
    a
    c
    k
    a
    g
    e
    d
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    s
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
    t
    h
    a
    t
    o
    n
    l
    y
    a
    p
    p
    l
    i
    e
    s
    t
    o
    p
    a
    c
    k
    a
    g
    e
    s
    (
    n
    o
    t
    p
    r
    o
    d
    u
    c
    t
    s
    )
    .
    
    """
    
    resource_type = "MedicationKnowledgePackaging"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        p
        r
        o
        d
        u
        c
        t
        u
        n
        i
        t
        s
        t
        h
        e
        p
        a
        c
        k
        a
        g
        e
        w
        o
        u
        l
        d
        c
        o
        n
        t
        a
        i
        n
        i
        f
        f
        u
        l
        l
        y
        l
        o
        a
        d
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        A
        c
        o
        d
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
        s
        p
        e
        c
        i
        f
        i
        c
        t
        y
        p
        e
        o
        f
        p
        a
        c
        k
        a
        g
        i
        n
        g
        t
        h
        a
        t
        t
        h
        e
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        c
        a
        n
        b
        e
        f
        o
        u
        n
        d
        i
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgePackaging, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgePackaging, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicationKnowledgeRegulatory(backboneelement.BackboneElement):
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
    a
    m
    e
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
    
    resource_type = "MedicationKnowledgeRegulatory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.maxDispense = None
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
        n
        u
        m
        b
        e
        r
        o
        f
        u
        n
        i
        t
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
        a
        t
        i
        o
        n
        t
        h
        a
        t
        c
        a
        n
        b
        e
        d
        i
        s
        p
        e
        n
        s
        e
        d
        i
        n
        a
        p
        e
        r
        i
        o
        d
        .
        Type `MedicationKnowledgeRegulatoryMaxDispense` (represented as `dict` in JSON). """
        
        self.regulatoryAuthority = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        s
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
        t
        y
        o
        f
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
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        s
        t
        h
        e
        s
        c
        h
        e
        d
        u
        l
        e
        o
        f
        a
        m
        e
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
        .
        List of `MedicationKnowledgeRegulatorySchedule` items (represented as `dict` in JSON). """
        
        self.substitution = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        s
        i
        f
        c
        h
        a
        n
        g
        e
        s
        a
        r
        e
        a
        l
        l
        o
        w
        e
        d
        w
        h
        e
        n
        d
        i
        s
        p
        e
        n
        s
        i
        n
        g
        a
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        f
        r
        o
        m
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
        y
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
        .
        List of `MedicationKnowledgeRegulatorySubstitution` items (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRegulatory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatory, self).elementProperties()
        js.extend([
            ("maxDispense", "maxDispense", MedicationKnowledgeRegulatoryMaxDispense, False, None, False),
            ("regulatoryAuthority", "regulatoryAuthority", fhirreference.FHIRReference, False, None, True),
            ("schedule", "schedule", MedicationKnowledgeRegulatorySchedule, True, None, False),
            ("substitution", "substitution", MedicationKnowledgeRegulatorySubstitution, True, None, False),
        ])
        return js


class MedicationKnowledgeRegulatoryMaxDispense(backboneelement.BackboneElement):
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
    n
    u
    m
    b
    e
    r
    o
    f
    u
    n
    i
    t
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
    a
    t
    i
    o
    n
    t
    h
    a
    t
    c
    a
    n
    b
    e
    d
    i
    s
    p
    e
    n
    s
    e
    d
    i
    n
    a
    p
    e
    r
    i
    o
    d
    .
    """
    
    resource_type = "MedicationKnowledgeRegulatoryMaxDispense"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ 
        T
        h
        e
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
        a
        p
        p
        l
        i
        e
        s
        t
        o
        t
        h
        e
        m
        a
        x
        i
        m
        u
        m
        n
        u
        m
        b
        e
        r
        o
        f
        u
        n
        i
        t
        s
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.quantity = None
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
        n
        u
        m
        b
        e
        r
        o
        f
        u
        n
        i
        t
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
        a
        t
        i
        o
        n
        t
        h
        a
        t
        c
        a
        n
        b
        e
        d
        i
        s
        p
        e
        n
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRegulatoryMaxDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatoryMaxDispense, self).elementProperties()
        js.extend([
            ("period", "period", duration.Duration, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
        ])
        return js


class MedicationKnowledgeRegulatorySchedule(backboneelement.BackboneElement):
    """ 
    S
    p
    e
    c
    i
    f
    i
    e
    s
    t
    h
    e
    s
    c
    h
    e
    d
    u
    l
    e
    o
    f
    a
    m
    e
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
    .
    """
    
    resource_type = "MedicationKnowledgeRegulatorySchedule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.schedule = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        s
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
        d
        r
        u
        g
        s
        c
        h
        e
        d
        u
        l
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRegulatorySchedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySchedule, self).elementProperties()
        js.extend([
            ("schedule", "schedule", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicationKnowledgeRegulatorySubstitution(backboneelement.BackboneElement):
    """ 
    S
    p
    e
    c
    i
    f
    i
    e
    s
    i
    f
    c
    h
    a
    n
    g
    e
    s
    a
    r
    e
    a
    l
    l
    o
    w
    e
    d
    w
    h
    e
    n
    d
    i
    s
    p
    e
    n
    s
    i
    n
    g
    a
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    f
    r
    o
    m
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
    y
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
    .
    """
    
    resource_type = "MedicationKnowledgeRegulatorySubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowed = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        s
        i
        f
        r
        e
        g
        u
        l
        a
        t
        i
        o
        n
        a
        l
        l
        o
        w
        s
        f
        o
        r
        c
        h
        a
        n
        g
        e
        s
        i
        n
        t
        h
        e
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        w
        h
        e
        n
        d
        i
        s
        p
        e
        n
        s
        i
        n
        g
        .
        Type `bool`. """
        
        self.type = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        s
        t
        h
        e
        t
        y
        p
        e
        o
        f
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
        a
        l
        l
        o
        w
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRegulatorySubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySubstitution, self).elementProperties()
        js.extend([
            ("allowed", "allowed", bool, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicationKnowledgeRelatedMedicationKnowledge(backboneelement.BackboneElement):
    """ 
    A
    s
    s
    o
    c
    i
    a
    t
    e
    d
    o
    r
    r
    e
    l
    a
    t
    e
    d
    m
    e
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
    
    
    A
    s
    s
    o
    c
    i
    a
    t
    e
    d
    o
    r
    r
    e
    l
    a
    t
    e
    d
    k
    n
    o
    w
    l
    e
    d
    g
    e
    a
    b
    o
    u
    t
    a
    m
    e
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
    
    resource_type = "MedicationKnowledgeRelatedMedicationKnowledge"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ 
        A
        s
        s
        o
        c
        i
        a
        t
        e
        d
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
        a
        b
        o
        u
        t
        t
        h
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
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        k
        n
        o
        w
        l
        e
        d
        g
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        C
        a
        t
        e
        g
        o
        r
        y
        o
        f
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        K
        n
        o
        w
        l
        e
        d
        g
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRelatedMedicationKnowledge, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRelatedMedicationKnowledge, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
