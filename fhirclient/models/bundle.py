# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Bundle).
# 2024, SMART Health IT.


from . import resource

class Bundle(resource.Resource):
    """ Contains a collection of resources.
    
    A container for a collection of resources.
    """
    
    resource_type = "Bundle"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entry = None
        """ Entry in the bundle - will have a resource or information.
        List of `BundleEntry` items (represented as `dict` in JSON). """
        self._entry = None
        """ Primitive extension for entry. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Persistent identifier for the bundle.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Links related to this Bundle.
        List of `BundleLink` items (represented as `dict` in JSON). """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        self.signature = None
        """ Digital Signature.
        Type `Signature` (represented as `dict` in JSON). """
        self._signature = None
        """ Primitive extension for signature. Type `FHIRPrimitiveExtension` """
        
        self.timestamp = None
        """ When the bundle was assembled.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._timestamp = None
        """ Primitive extension for timestamp. Type `FHIRPrimitiveExtension` """
        
        self.total = None
        """ If search, the total number of matches.
        Type `int`. """
        self._total = None
        """ Primitive extension for total. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ document | message | transaction | transaction-response | batch |
        batch-response | history | searchset | collection.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Bundle, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Bundle, self).elementProperties()
        js.extend([
            ("entry", "entry", BundleEntry, True, None, False),
            ("_entry", "_entry", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("signature", "signature", signature.Signature, False, None, False),
            ("_signature", "_signature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timestamp", "timestamp", fhirinstant.FHIRInstant, False, None, False),
            ("_timestamp", "_timestamp", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("total", "total", int, False, None, False),
            ("_total", "_total", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class BundleEntry(backboneelement.BackboneElement):
    """ Entry in the bundle - will have a resource or information.
    
    An entry in a bundle resource - will either contain a resource or
    information about a resource (transactions and history only).
    """
    
    resource_type = "BundleEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fullUrl = None
        """ URI for resource (Absolute URL server address or URI for UUID/OID).
        Type `str`. """
        self._fullUrl = None
        """ Primitive extension for fullUrl. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Links related to this entry.
        List of `BundleLink` items (represented as `dict` in JSON). """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Additional execution information (transaction/batch/history).
        Type `BundleEntryRequest` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ A resource in the bundle.
        Type `Resource` (represented as `dict` in JSON). """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.response = None
        """ Results of execution (transaction/batch/history).
        Type `BundleEntryResponse` (represented as `dict` in JSON). """
        self._response = None
        """ Primitive extension for response. Type `FHIRPrimitiveExtension` """
        
        self.search = None
        """ Search related information.
        Type `BundleEntrySearch` (represented as `dict` in JSON). """
        self._search = None
        """ Primitive extension for search. Type `FHIRPrimitiveExtension` """
        
        super(BundleEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntry, self).elementProperties()
        js.extend([
            ("fullUrl", "fullUrl", str, False, None, False),
            ("_fullUrl", "_fullUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", BundleEntryRequest, False, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("response", "response", BundleEntryResponse, False, None, False),
            ("_response", "_response", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("search", "search", BundleEntrySearch, False, None, False),
            ("_search", "_search", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class BundleEntryRequest(backboneelement.BackboneElement):
    """ Additional execution information (transaction/batch/history).
    
    Additional information about how this entry should be processed as part of
    a transaction or batch.  For history, it shows how the entry was processed
    to create the version contained in the entry.
    """
    
    resource_type = "BundleEntryRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ifMatch = None
        """ For managing update contention.
        Type `str`. """
        self._ifMatch = None
        """ Primitive extension for ifMatch. Type `FHIRPrimitiveExtension` """
        
        self.ifModifiedSince = None
        """ For managing cache currency.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._ifModifiedSince = None
        """ Primitive extension for ifModifiedSince. Type `FHIRPrimitiveExtension` """
        
        self.ifNoneExist = None
        """ For conditional creates.
        Type `str`. """
        self._ifNoneExist = None
        """ Primitive extension for ifNoneExist. Type `FHIRPrimitiveExtension` """
        
        self.ifNoneMatch = None
        """ For managing cache currency.
        Type `str`. """
        self._ifNoneMatch = None
        """ Primitive extension for ifNoneMatch. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ GET | HEAD | POST | PUT | DELETE | PATCH.
        Type `str`. """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ URL for HTTP equivalent of this entry.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(BundleEntryRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntryRequest, self).elementProperties()
        js.extend([
            ("ifMatch", "ifMatch", str, False, None, False),
            ("_ifMatch", "_ifMatch", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ifModifiedSince", "ifModifiedSince", fhirinstant.FHIRInstant, False, None, False),
            ("_ifModifiedSince", "_ifModifiedSince", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ifNoneExist", "ifNoneExist", str, False, None, False),
            ("_ifNoneExist", "_ifNoneExist", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ifNoneMatch", "ifNoneMatch", str, False, None, False),
            ("_ifNoneMatch", "_ifNoneMatch", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", str, False, None, True),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class BundleEntryResponse(backboneelement.BackboneElement):
    """ Results of execution (transaction/batch/history).
    
    Indicates the results of processing the corresponding 'request' entry in
    the batch or transaction being responded to or what the results of an
    operation where when returning history.
    """
    
    resource_type = "BundleEntryResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.etag = None
        """ The Etag for the resource (if relevant).
        Type `str`. """
        self._etag = None
        """ Primitive extension for etag. Type `FHIRPrimitiveExtension` """
        
        self.lastModified = None
        """ Server's date time modified.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._lastModified = None
        """ Primitive extension for lastModified. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ The location (if the operation returns a location).
        Type `str`. """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ OperationOutcome with hints and warnings (for batch/transaction).
        Type `Resource` (represented as `dict` in JSON). """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ Status response code (text optional).
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(BundleEntryResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntryResponse, self).elementProperties()
        js.extend([
            ("etag", "etag", str, False, None, False),
            ("_etag", "_etag", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastModified", "lastModified", fhirinstant.FHIRInstant, False, None, False),
            ("_lastModified", "_lastModified", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", str, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", resource.Resource, False, None, False),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class BundleEntrySearch(backboneelement.BackboneElement):
    """ Search related information.
    
    Information about the search process that lead to the creation of this
    entry.
    """
    
    resource_type = "BundleEntrySearch"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        """ match | include | outcome - why this is in the result set.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.score = None
        """ Search ranking (between 0 and 1).
        Type `float`. """
        self._score = None
        """ Primitive extension for score. Type `FHIRPrimitiveExtension` """
        
        super(BundleEntrySearch, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntrySearch, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, False),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("score", "score", float, False, None, False),
            ("_score", "_score", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class BundleLink(backboneelement.BackboneElement):
    """ Links related to this Bundle.
    
    A series of links that provide context to this bundle.
    """
    
    resource_type = "BundleLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.relation = None
        """ See http://www.iana.org/assignments/link-relations/link-
        relations.xhtml#link-relations-1.
        Type `str`. """
        self._relation = None
        """ Primitive extension for relation. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Reference details for the link.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(BundleLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleLink, self).elementProperties()
        js.extend([
            ("relation", "relation", str, False, None, True),
            ("_relation", "_relation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import fhirinstant
from . import identifier
from . import signature