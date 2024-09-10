# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/NamingSystem).
# 2024, SMART Health IT.


from . import domainresource

class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.
    
    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    
    resource_type = "NamingSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the naming system.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for naming system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.kind = None
        """ codesystem | identifier | root.
        Type `str`. """
        self._kind = None
        """ Primitive extension for kind. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this naming system (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.responsible = None
        """ Who maintains system namespace?.
        Type `str`. """
        self._responsible = None
        """ Primitive extension for responsible. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ e.g. driver,  provider,  patient, bank etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.uniqueId = None
        """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """
        self._uniqueId = None
        """ Primitive extension for uniqueId. Type `FHIRPrimitiveExtension` """
        
        self.usage = None
        """ How/where is it used.
        Type `str`. """
        self._usage = None
        """ Primitive extension for usage. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        super(NamingSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, True),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("responsible", "responsible", str, False, None, False),
            ("_responsible", "_responsible", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True),
            ("_uniqueId", "_uniqueId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("_usage", "_usage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.
    
    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    
    resource_type = "NamingSystemUniqueId"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Notes about identifier usage.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ When is identifier valid?.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.preferred = None
        """ Is this the id that should be used for this type.
        Type `bool`. """
        self._preferred = None
        """ Primitive extension for preferred. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ oid | uuid | uri | other.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The unique identifier.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(NamingSystemUniqueId, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("_preferred", "_preferred", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import period
from . import usagecontext