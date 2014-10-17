#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Construct server search parameters.
#  2014, SMART Platforms.

import fhirsearch


class FHIRSearchElement(object):
    """ This class enables pythonic creation of search URL strings.
    
    Search elements are designed to be chained together. The first parameter
    instance in the chain must define `resource_type`, all subsequent params
    must have their `subject` set to be useful. Upon calling `construct()` on
    the last item in a chain, all instances are constructed into a URL query:
    
    qry = Patient.where().address("Boston").gender('male').given_exact("Willis")
    
    Then qry.construct() will create the string:
    
    "Patient?address=Boston&gender=male&given:exact=Willis"
    """
    
    def __init__(self, subject):
        self._previous = None
        self._next = None
        
        self.subject = subject
        """ The name of the search parameter. """
        
        self.resource_type = None
        """ The first search parameter in a list must define a resource type to
        which the search is applied. """
        
        self.supported_profiles = None
        """ On which profiles the receiver's subject is supported; can be used
        for validation. """
        
        self.string = None
        """ The param's value is a string.
        http://www.hl7.org/implement/standards/fhir/search.html#string """
        
        self.token = None
        """ The param's value is a token. Can be modified with `token_as_text`.
        http://www.hl7.org/implement/standards/fhir/search.html#token """
        
        self.number = None
        """ The param describes a numerical value.
        http://www.hl7.org/implement/standards/fhir/search.html#number """
        
        self.date = None
        """ The param's value is a date string.
        http://www.hl7.org/implement/standards/fhir/search.html#date """
        
        self.quantity = None
        """ The param describes a numerical quantity.
        http://www.hl7.org/implement/standards/fhir/search.html#quantity """
        
        self.reference = None
        """ The param's value is a reference.
        http://www.hl7.org/implement/standards/fhir/search.html#reference """
        
        self.composite = None
        """ A composite search parameter.
        http://www.hl7.org/implement/standards/fhir/search.html#combining """
        
        # Modifiers: http://www.hl7.org/implement/standards/fhir/search.html#modifiers
        
        self.missing = None
        """ If `true` we're looking for a missing parameter. """
        
        self.string_exact = False
        """ Only needed for strings; if `true` the match must be exact. """
        
        self.token_as_text = False
        """ Only needed for tokens; if `true` the token should be queried like text. """
        
        self.reference_type = None
        """ Only needed for references: the type of the reference. """
    
    
    # MARK: Construction
    
    def as_param(self):
        """ Returns a FHIRSearchParam instance representing the receiver.
        """
        if self.subject:
            if self.missing is not None:
                return fhirsearch.FHIRSearchParam('{}:missing'.format(self.subject), 'true' if self.missing else 'false')
            
            if self.string and self.string_exact:
                return fhirsearch.FHIRSearchParam('{}:exact'.format(self.subject), self.param_value())
            
            if self.token and self.token_as_text:
                return fhirsearch.FHIRSearchParam('{}:text'.format(self.subject), self.param_value())
            
        return fhirsearch.FHIRSearchParam(self.subject, self.param_value())
    
    def param_value(self):
        """ The value of the parameter. """
        if self.string:
            return self.string
        if self.token:
            return self.token
        if self.number:
            return self.number
        if self.date:
            return self.date
        if self.quantity:
            return self.quantity
        if self.reference:
            return self.reference
        return ''
    
    
    # MARK: Execution
    
    def as_search(self):
        """ Create a `FHIRSearch` representation of the chain up to the
        receiver. This is internally used for the `construct` and `perform`
        calls, which are executed on the FHIRSearch instance created here.
        """
        params = []
        prev = self
        while prev.previous is not None:
            params.insert(0, prev.as_param())
            prev = prev.previous
        
        if not prev.resource_type:
            raise Exception("The first search parameter needs to have \"resource_type\" set")
        
        srch = fhirsearch.FHIRSearch(prev.resource_type)
        srch.params = params
        return srch
    
    def construct(self):
        """ Construct and return the search query string.
        
        Use the `last` method to get the last param of a chain if needed, then
        call this method to create the parameter string of the whole chain.
        """
        return self.as_search().construct()
    
    def perform(self, server):
        """ Construct the search URL, execute it against the given server and
        return a list of instances created from returned data.
        """
        return self.as_search().perform(server)
    
    
    # MARK: Chaning
    
    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, prev):
        if self._previous == prev:
            return
        if self._previous is not None and self == self._previous.next:
            self._previous.next = None
        self._previous = prev
        prev.next = self
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, nxt):
        if self._next == nxt:
            return
        if self._next is not None and self == self._next.previous:
            self._next.previous = None
        self._next = nxt
        nxt.previous = self
    
    def first(self):
        if self._previous is not None:
            return self._previous.first()
        return self
    
    def last(self):
        if self._next is not None:
            return self._next.last()
        return self
    
    
    # MARK: Generated Methods
    
    def _id(self, token):
        """ Perform a search for "_id" token. """
        p = FHIRSearchElement(subject="_id")
        p.token = token
        p.previous = self
        return p
    
    def _id_as_text(self, token):
        """ Perform a fulltext search for token "_id". """
        p = FHIRSearchElement(subject="_id")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def _language(self, token):
        """ Perform a search for "_language" token. """
        p = FHIRSearchElement(subject="_language")
        p.token = token
        p.previous = self
        return p
    
    def _language_as_text(self, token):
        """ Perform a fulltext search for token "_language". """
        p = FHIRSearchElement(subject="_language")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def accession(self, token):
        """ Perform a search for "accession" token. """
        p = FHIRSearchElement(subject="accession")
        p.token = token
        p.supported_profiles = [
            "ImagingStudy"
        ]
        p.previous = self
        return p
    
    def accession_as_text(self, token):
        """ Perform a fulltext search for token "accession". """
        p = FHIRSearchElement(subject="accession")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def accession_missing(self, flag):
        """ Specify if "accession" should be missing or not. """
        p = FHIRSearchElement(subject="accession")
        p.missing = flag
        p.previous = self
        return p
    
    def action(self, token):
        """ Perform a search for "action" token. """
        p = FHIRSearchElement(subject="action")
        p.token = token
        p.supported_profiles = [
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def action_as_text(self, token):
        """ Perform a fulltext search for token "action". """
        p = FHIRSearchElement(subject="action")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def action_missing(self, flag):
        """ Specify if "action" should be missing or not. """
        p = FHIRSearchElement(subject="action")
        p.missing = flag
        p.previous = self
        return p
    
    def active(self, token):
        """ Perform a search for "active" token. """
        p = FHIRSearchElement(subject="active")
        p.token = token
        p.supported_profiles = [
            "Organization",
            "Patient"
        ]
        p.previous = self
        return p
    
    def active_as_text(self, token):
        """ Perform a fulltext search for token "active". """
        p = FHIRSearchElement(subject="active")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def active_missing(self, flag):
        """ Specify if "active" should be missing or not. """
        p = FHIRSearchElement(subject="active")
        p.missing = flag
        p.previous = self
        return p
    
    def activitycode(self, token):
        """ Perform a search for "activitycode" token. """
        p = FHIRSearchElement(subject="activitycode")
        p.token = token
        p.supported_profiles = [
            "CarePlan"
        ]
        p.previous = self
        return p
    
    def activitycode_as_text(self, token):
        """ Perform a fulltext search for token "activitycode". """
        p = FHIRSearchElement(subject="activitycode")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def activitycode_missing(self, flag):
        """ Specify if "activitycode" should be missing or not. """
        p = FHIRSearchElement(subject="activitycode")
        p.missing = flag
        p.previous = self
        return p
    
    def activitydate(self, date):
        """ Perform a search for "activitydate" date. """
        p = FHIRSearchElement(subject="activitydate")
        p.date = date
        p.supported_profiles = [
            "CarePlan"
        ]
        p.previous = self
        return p
    
    def activitydate_missing(self, flag):
        """ Specify if "activitydate" should be missing or not. """
        p = FHIRSearchElement(subject="activitydate")
        p.missing = flag
        p.previous = self
        return p
    
    def activitydetail(self, reference):
        """ Perform a search for "activitydetail" reference. """
        p = FHIRSearchElement(subject="activitydetail")
        p.reference = reference
        p.supported_profiles = [
            "CarePlan"
        ]
        p.previous = self
        return p
    
    def activitydetail_missing(self, flag):
        """ Specify if "activitydetail" should be missing or not. """
        p = FHIRSearchElement(subject="activitydetail")
        p.missing = flag
        p.previous = self
        return p
    
    def actor(self, reference):
        """ Perform a search for "actor" reference. """
        p = FHIRSearchElement(subject="actor")
        p.reference = reference
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def actor_missing(self, flag):
        """ Specify if "actor" should be missing or not. """
        p = FHIRSearchElement(subject="actor")
        p.missing = flag
        p.previous = self
        return p
    
    def actual(self, token):
        """ Perform a search for "actual" token. """
        p = FHIRSearchElement(subject="actual")
        p.token = token
        p.supported_profiles = [
            "Group"
        ]
        p.previous = self
        return p
    
    def actual_as_text(self, token):
        """ Perform a fulltext search for token "actual". """
        p = FHIRSearchElement(subject="actual")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def actual_missing(self, flag):
        """ Specify if "actual" should be missing or not. """
        p = FHIRSearchElement(subject="actual")
        p.missing = flag
        p.previous = self
        return p
    
    def address(self, string):
        """ Perform a search for "address" string. """
        p = FHIRSearchElement(subject="address")
        p.string = string
        p.supported_profiles = [
            "Location",
            "Patient",
            "Practitioner",
            "RelatedPerson",
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def address_exact(self, string):
        """ Search for an exact match for "address". """
        p = FHIRSearchElement(subject="address")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def address_missing(self, flag):
        """ Specify if "address" should be missing or not. """
        p = FHIRSearchElement(subject="address")
        p.missing = flag
        p.previous = self
        return p
    
    def address(self, token):
        """ Perform a search for "address" token. """
        p = FHIRSearchElement(subject="address")
        p.token = token
        p.supported_profiles = [
            "Location",
            "Patient",
            "Practitioner",
            "RelatedPerson",
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def address_as_text(self, token):
        """ Perform a fulltext search for token "address". """
        p = FHIRSearchElement(subject="address")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def altid(self, token):
        """ Perform a search for "altid" token. """
        p = FHIRSearchElement(subject="altid")
        p.token = token
        p.supported_profiles = [
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def altid_as_text(self, token):
        """ Perform a fulltext search for token "altid". """
        p = FHIRSearchElement(subject="altid")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def altid_missing(self, flag):
        """ Specify if "altid" should be missing or not. """
        p = FHIRSearchElement(subject="altid")
        p.missing = flag
        p.previous = self
        return p
    
    def animal_breed(self, token):
        """ Perform a search for "animal-breed" token. """
        p = FHIRSearchElement(subject="animal-breed")
        p.token = token
        p.supported_profiles = [
            "Patient"
        ]
        p.previous = self
        return p
    
    def animal_breed_as_text(self, token):
        """ Perform a fulltext search for token "animal-breed". """
        p = FHIRSearchElement(subject="animal-breed")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def animal_breed_missing(self, flag):
        """ Specify if "animal-breed" should be missing or not. """
        p = FHIRSearchElement(subject="animal-breed")
        p.missing = flag
        p.previous = self
        return p
    
    def animal_species(self, token):
        """ Perform a search for "animal-species" token. """
        p = FHIRSearchElement(subject="animal-species")
        p.token = token
        p.supported_profiles = [
            "Patient"
        ]
        p.previous = self
        return p
    
    def animal_species_as_text(self, token):
        """ Perform a fulltext search for token "animal-species". """
        p = FHIRSearchElement(subject="animal-species")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def animal_species_missing(self, flag):
        """ Specify if "animal-species" should be missing or not. """
        p = FHIRSearchElement(subject="animal-species")
        p.missing = flag
        p.previous = self
        return p
    
    def asserter(self, reference):
        """ Perform a search for "asserter" reference. """
        p = FHIRSearchElement(subject="asserter")
        p.reference = reference
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def asserter_missing(self, flag):
        """ Specify if "asserter" should be missing or not. """
        p = FHIRSearchElement(subject="asserter")
        p.missing = flag
        p.previous = self
        return p
    
    def attester(self, reference):
        """ Perform a search for "attester" reference. """
        p = FHIRSearchElement(subject="attester")
        p.reference = reference
        p.supported_profiles = [
            "Composition"
        ]
        p.previous = self
        return p
    
    def attester_missing(self, flag):
        """ Specify if "attester" should be missing or not. """
        p = FHIRSearchElement(subject="attester")
        p.missing = flag
        p.previous = self
        return p
    
    def authenticator(self, reference):
        """ Perform a search for "authenticator" reference. """
        p = FHIRSearchElement(subject="authenticator")
        p.reference = reference
        p.supported_profiles = [
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def authenticator_missing(self, flag):
        """ Specify if "authenticator" should be missing or not. """
        p = FHIRSearchElement(subject="authenticator")
        p.missing = flag
        p.previous = self
        return p
    
    def authored(self, date):
        """ Perform a search for "authored" date. """
        p = FHIRSearchElement(subject="authored")
        p.date = date
        p.supported_profiles = [
            "Questionnaire"
        ]
        p.previous = self
        return p
    
    def authored_missing(self, flag):
        """ Specify if "authored" should be missing or not. """
        p = FHIRSearchElement(subject="authored")
        p.missing = flag
        p.previous = self
        return p
    
    def authority(self, reference):
        """ Perform a search for "authority" reference. """
        p = FHIRSearchElement(subject="authority")
        p.reference = reference
        p.supported_profiles = [
            "Order"
        ]
        p.previous = self
        return p
    
    def authority_missing(self, flag):
        """ Specify if "authority" should be missing or not. """
        p = FHIRSearchElement(subject="authority")
        p.missing = flag
        p.previous = self
        return p
    
    def author(self, reference):
        """ Perform a search for "author" reference. """
        p = FHIRSearchElement(subject="author")
        p.reference = reference
        p.supported_profiles = [
            "Composition",
            "DocumentManifest",
            "DocumentReference",
            "Questionnaire"
        ]
        p.previous = self
        return p
    
    def author_missing(self, flag):
        """ Specify if "author" should be missing or not. """
        p = FHIRSearchElement(subject="author")
        p.missing = flag
        p.previous = self
        return p
    
    def birthdate(self, date):
        """ Perform a search for "birthdate" date. """
        p = FHIRSearchElement(subject="birthdate")
        p.date = date
        p.supported_profiles = [
            "Patient"
        ]
        p.previous = self
        return p
    
    def birthdate_missing(self, flag):
        """ Specify if "birthdate" should be missing or not. """
        p = FHIRSearchElement(subject="birthdate")
        p.missing = flag
        p.previous = self
        return p
    
    def bodysite(self, token):
        """ Perform a search for "bodysite" token. """
        p = FHIRSearchElement(subject="bodysite")
        p.token = token
        p.supported_profiles = [
            "DiagnosticOrder",
            "ImagingStudy"
        ]
        p.previous = self
        return p
    
    def bodysite_as_text(self, token):
        """ Perform a fulltext search for token "bodysite". """
        p = FHIRSearchElement(subject="bodysite")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def bodysite_missing(self, flag):
        """ Specify if "bodysite" should be missing or not. """
        p = FHIRSearchElement(subject="bodysite")
        p.missing = flag
        p.previous = self
        return p
    
    def category(self, token):
        """ Perform a search for "category" token. """
        p = FHIRSearchElement(subject="category")
        p.token = token
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def category_as_text(self, token):
        """ Perform a fulltext search for token "category". """
        p = FHIRSearchElement(subject="category")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def category_missing(self, flag):
        """ Specify if "category" should be missing or not. """
        p = FHIRSearchElement(subject="category")
        p.missing = flag
        p.previous = self
        return p
    
    def channel(self, token):
        """ Perform a search for "channel" token. """
        p = FHIRSearchElement(subject="channel")
        p.token = token
        p.supported_profiles = [
            "DeviceObservationReport"
        ]
        p.previous = self
        return p
    
    def channel_as_text(self, token):
        """ Perform a fulltext search for token "channel". """
        p = FHIRSearchElement(subject="channel")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def channel_missing(self, flag):
        """ Specify if "channel" should be missing or not. """
        p = FHIRSearchElement(subject="channel")
        p.missing = flag
        p.previous = self
        return p
    
    def characteristic_value(self, composite):
        """ Perform a search for "characteristic-value" composite. """
        p = FHIRSearchElement(subject="characteristic-value")
        p.composite = composite
        p.supported_profiles = [
            "Group"
        ]
        p.previous = self
        return p
    
    def characteristic_value_missing(self, flag):
        """ Specify if "characteristic-value" should be missing or not. """
        p = FHIRSearchElement(subject="characteristic-value")
        p.missing = flag
        p.previous = self
        return p
    
    def characteristic(self, token):
        """ Perform a search for "characteristic" token. """
        p = FHIRSearchElement(subject="characteristic")
        p.token = token
        p.supported_profiles = [
            "Group"
        ]
        p.previous = self
        return p
    
    def characteristic_as_text(self, token):
        """ Perform a fulltext search for token "characteristic". """
        p = FHIRSearchElement(subject="characteristic")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def characteristic_missing(self, flag):
        """ Specify if "characteristic" should be missing or not. """
        p = FHIRSearchElement(subject="characteristic")
        p.missing = flag
        p.previous = self
        return p
    
    def klass(self, token):
        """ Perform a search for "class" token. """
        p = FHIRSearchElement(subject="class")
        p.token = token
        p.previous = self
        return p
    
    def klass_as_text(self, token):
        """ Perform a fulltext search for token "class". """
        p = FHIRSearchElement(subject="class")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def klass_missing(self, flag):
        """ Specify if "class" should be missing or not. """
        p = FHIRSearchElement(subject="class")
        p.missing = flag
        p.previous = self
        return p
    
    def code(self, token):
        """ Perform a search for "code" token. """
        p = FHIRSearchElement(subject="code")
        p.token = token
        p.supported_profiles = [
            "Condition",
            "DeviceObservationReport",
            "DiagnosticOrder",
            "Group",
            "List",
            "Medication",
            "OrderResponse",
            "Other",
            "Profile",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def code_as_text(self, token):
        """ Perform a fulltext search for token "code". """
        p = FHIRSearchElement(subject="code")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def code_missing(self, flag):
        """ Specify if "code" should be missing or not. """
        p = FHIRSearchElement(subject="code")
        p.missing = flag
        p.previous = self
        return p
    
    def condition(self, reference):
        """ Perform a search for "condition" reference. """
        p = FHIRSearchElement(subject="condition")
        p.reference = reference
        p.supported_profiles = [
            "CarePlan"
        ]
        p.previous = self
        return p
    
    def condition_missing(self, flag):
        """ Specify if "condition" should be missing or not. """
        p = FHIRSearchElement(subject="condition")
        p.missing = flag
        p.previous = self
        return p
    
    def confidentiality(self, token):
        """ Perform a search for "confidentiality" token. """
        p = FHIRSearchElement(subject="confidentiality")
        p.token = token
        p.supported_profiles = [
            "DocumentManifest",
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def confidentiality_as_text(self, token):
        """ Perform a fulltext search for token "confidentiality". """
        p = FHIRSearchElement(subject="confidentiality")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def confidentiality_missing(self, flag):
        """ Specify if "confidentiality" should be missing or not. """
        p = FHIRSearchElement(subject="confidentiality")
        p.missing = flag
        p.previous = self
        return p
    
    def container(self, token):
        """ Perform a search for "container" token. """
        p = FHIRSearchElement(subject="container")
        p.token = token
        p.supported_profiles = [
            "Medication"
        ]
        p.previous = self
        return p
    
    def container_as_text(self, token):
        """ Perform a fulltext search for token "container". """
        p = FHIRSearchElement(subject="container")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def container_missing(self, flag):
        """ Specify if "container" should be missing or not. """
        p = FHIRSearchElement(subject="container")
        p.missing = flag
        p.previous = self
        return p
    
    def content(self, reference):
        """ Perform a search for "content" reference. """
        p = FHIRSearchElement(subject="content")
        p.reference = reference
        p.supported_profiles = [
            "DocumentManifest",
            "Medication"
        ]
        p.previous = self
        return p
    
    def content_missing(self, flag):
        """ Specify if "content" should be missing or not. """
        p = FHIRSearchElement(subject="content")
        p.missing = flag
        p.previous = self
        return p
    
    def context(self, token):
        """ Perform a search for "context" token. """
        p = FHIRSearchElement(subject="context")
        p.token = token
        p.supported_profiles = [
            "Composition"
        ]
        p.previous = self
        return p
    
    def context_as_text(self, token):
        """ Perform a fulltext search for token "context". """
        p = FHIRSearchElement(subject="context")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def context_missing(self, flag):
        """ Specify if "context" should be missing or not. """
        p = FHIRSearchElement(subject="context")
        p.missing = flag
        p.previous = self
        return p
    
    def created(self, date):
        """ Perform a search for "created" date. """
        p = FHIRSearchElement(subject="created")
        p.date = date
        p.supported_profiles = [
            "DocumentManifest",
            "DocumentReference",
            "Other"
        ]
        p.previous = self
        return p
    
    def created_missing(self, flag):
        """ Specify if "created" should be missing or not. """
        p = FHIRSearchElement(subject="created")
        p.missing = flag
        p.previous = self
        return p
    
    def custodian(self, reference):
        """ Perform a search for "custodian" reference. """
        p = FHIRSearchElement(subject="custodian")
        p.reference = reference
        p.supported_profiles = [
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def custodian_missing(self, flag):
        """ Specify if "custodian" should be missing or not. """
        p = FHIRSearchElement(subject="custodian")
        p.missing = flag
        p.previous = self
        return p
    
    def date_asserted(self, date):
        """ Perform a search for "date-asserted" date. """
        p = FHIRSearchElement(subject="date-asserted")
        p.date = date
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def date_asserted_missing(self, flag):
        """ Specify if "date-asserted" should be missing or not. """
        p = FHIRSearchElement(subject="date-asserted")
        p.missing = flag
        p.previous = self
        return p
    
    def datewritten(self, date):
        """ Perform a search for "datewritten" date. """
        p = FHIRSearchElement(subject="datewritten")
        p.date = date
        p.supported_profiles = [
            "MedicationPrescription"
        ]
        p.previous = self
        return p
    
    def datewritten_missing(self, flag):
        """ Specify if "datewritten" should be missing or not. """
        p = FHIRSearchElement(subject="datewritten")
        p.missing = flag
        p.previous = self
        return p
    
    def date(self, date):
        """ Perform a search for "date" date. """
        p = FHIRSearchElement(subject="date")
        p.date = date
        p.supported_profiles = [
            "AdverseReaction",
            "AllergyIntolerance",
            "CarePlan",
            "Composition",
            "ConceptMap",
            "Conformance",
            "DiagnosticReport",
            "Encounter",
            "ImagingStudy",
            "Immunization",
            "ImmunizationRecommendation",
            "List",
            "Media",
            "Observation",
            "Order",
            "OrderResponse",
            "Procedure",
            "Profile",
            "SecurityEvent",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def date_missing(self, flag):
        """ Specify if "date" should be missing or not. """
        p = FHIRSearchElement(subject="date")
        p.missing = flag
        p.previous = self
        return p
    
    def dependson(self, token):
        """ Perform a search for "dependson" token. """
        p = FHIRSearchElement(subject="dependson")
        p.token = token
        p.supported_profiles = [
            "ConceptMap"
        ]
        p.previous = self
        return p
    
    def dependson_as_text(self, token):
        """ Perform a fulltext search for token "dependson". """
        p = FHIRSearchElement(subject="dependson")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def dependson_missing(self, flag):
        """ Specify if "dependson" should be missing or not. """
        p = FHIRSearchElement(subject="dependson")
        p.missing = flag
        p.previous = self
        return p
    
    def description(self, string):
        """ Perform a search for "description" string. """
        p = FHIRSearchElement(subject="description")
        p.string = string
        p.supported_profiles = [
            "ConceptMap",
            "Conformance",
            "DocumentManifest",
            "DocumentReference",
            "Profile",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def description_exact(self, string):
        """ Search for an exact match for "description". """
        p = FHIRSearchElement(subject="description")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def description_missing(self, flag):
        """ Specify if "description" should be missing or not. """
        p = FHIRSearchElement(subject="description")
        p.missing = flag
        p.previous = self
        return p
    
    def desc(self, string):
        """ Perform a search for "desc" string. """
        p = FHIRSearchElement(subject="desc")
        p.string = string
        p.supported_profiles = [
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def desc_exact(self, string):
        """ Search for an exact match for "desc". """
        p = FHIRSearchElement(subject="desc")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def desc_missing(self, flag):
        """ Specify if "desc" should be missing or not. """
        p = FHIRSearchElement(subject="desc")
        p.missing = flag
        p.previous = self
        return p
    
    def destination(self, reference):
        """ Perform a search for "destination" reference. """
        p = FHIRSearchElement(subject="destination")
        p.reference = reference
        p.supported_profiles = [
            "MedicationDispense"
        ]
        p.previous = self
        return p
    
    def destination_missing(self, flag):
        """ Specify if "destination" should be missing or not. """
        p = FHIRSearchElement(subject="destination")
        p.missing = flag
        p.previous = self
        return p
    
    def detail(self, reference):
        """ Perform a search for "detail" reference. """
        p = FHIRSearchElement(subject="detail")
        p.reference = reference
        p.supported_profiles = [
            "Order"
        ]
        p.previous = self
        return p
    
    def detail_missing(self, flag):
        """ Specify if "detail" should be missing or not. """
        p = FHIRSearchElement(subject="detail")
        p.missing = flag
        p.previous = self
        return p
    
    def device(self, reference):
        """ Perform a search for "device" reference. """
        p = FHIRSearchElement(subject="device")
        p.reference = reference
        p.supported_profiles = [
            "MedicationAdministration",
            "MedicationStatement"
        ]
        p.previous = self
        return p
    
    def device_missing(self, flag):
        """ Specify if "device" should be missing or not. """
        p = FHIRSearchElement(subject="device")
        p.missing = flag
        p.previous = self
        return p
    
    def diagnosis(self, token):
        """ Perform a search for "diagnosis" token. """
        p = FHIRSearchElement(subject="diagnosis")
        p.token = token
        p.supported_profiles = [
            "DiagnosticReport"
        ]
        p.previous = self
        return p
    
    def diagnosis_as_text(self, token):
        """ Perform a fulltext search for token "diagnosis". """
        p = FHIRSearchElement(subject="diagnosis")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def diagnosis_missing(self, flag):
        """ Specify if "diagnosis" should be missing or not. """
        p = FHIRSearchElement(subject="diagnosis")
        p.missing = flag
        p.previous = self
        return p
    
    def dicom_class(self, token):
        """ Perform a search for "dicom-class" token. """
        p = FHIRSearchElement(subject="dicom-class")
        p.token = token
        p.supported_profiles = [
            "ImagingStudy"
        ]
        p.previous = self
        return p
    
    def dicom_class_as_text(self, token):
        """ Perform a fulltext search for token "dicom-class". """
        p = FHIRSearchElement(subject="dicom-class")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def dicom_class_missing(self, flag):
        """ Specify if "dicom-class" should be missing or not. """
        p = FHIRSearchElement(subject="dicom-class")
        p.missing = flag
        p.previous = self
        return p
    
    def dispenseid(self, token):
        """ Perform a search for "dispenseid" token. """
        p = FHIRSearchElement(subject="dispenseid")
        p.token = token
        p.supported_profiles = [
            "Supply"
        ]
        p.previous = self
        return p
    
    def dispenseid_as_text(self, token):
        """ Perform a fulltext search for token "dispenseid". """
        p = FHIRSearchElement(subject="dispenseid")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def dispenseid_missing(self, flag):
        """ Specify if "dispenseid" should be missing or not. """
        p = FHIRSearchElement(subject="dispenseid")
        p.missing = flag
        p.previous = self
        return p
    
    def dispenser(self, reference):
        """ Perform a search for "dispenser" reference. """
        p = FHIRSearchElement(subject="dispenser")
        p.reference = reference
        p.supported_profiles = [
            "MedicationDispense"
        ]
        p.previous = self
        return p
    
    def dispenser_missing(self, flag):
        """ Specify if "dispenser" should be missing or not. """
        p = FHIRSearchElement(subject="dispenser")
        p.missing = flag
        p.previous = self
        return p
    
    def dispensestatus(self, token):
        """ Perform a search for "dispensestatus" token. """
        p = FHIRSearchElement(subject="dispensestatus")
        p.token = token
        p.supported_profiles = [
            "Supply"
        ]
        p.previous = self
        return p
    
    def dispensestatus_as_text(self, token):
        """ Perform a fulltext search for token "dispensestatus". """
        p = FHIRSearchElement(subject="dispensestatus")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def dispensestatus_missing(self, flag):
        """ Specify if "dispensestatus" should be missing or not. """
        p = FHIRSearchElement(subject="dispensestatus")
        p.missing = flag
        p.previous = self
        return p
    
    def dose_number(self, number):
        """ Perform a search for "dose-number" number. """
        p = FHIRSearchElement(subject="dose-number")
        p.number = number
        p.supported_profiles = [
            "ImmunizationRecommendation"
        ]
        p.previous = self
        return p
    
    def dose_number_missing(self, flag):
        """ Specify if "dose-number" should be missing or not. """
        p = FHIRSearchElement(subject="dose-number")
        p.missing = flag
        p.previous = self
        return p
    
    def dose_sequence(self, number):
        """ Perform a search for "dose-sequence" number. """
        p = FHIRSearchElement(subject="dose-sequence")
        p.number = number
        p.supported_profiles = [
            "Immunization",
            "ImmunizationRecommendation"
        ]
        p.previous = self
        return p
    
    def dose_sequence(self, token):
        """ Perform a search for "dose-sequence" token. """
        p = FHIRSearchElement(subject="dose-sequence")
        p.token = token
        p.supported_profiles = [
            "Immunization",
            "ImmunizationRecommendation"
        ]
        p.previous = self
        return p
    
    def dose_sequence_as_text(self, token):
        """ Perform a fulltext search for token "dose-sequence". """
        p = FHIRSearchElement(subject="dose-sequence")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def empty_reason(self, token):
        """ Perform a search for "empty-reason" token. """
        p = FHIRSearchElement(subject="empty-reason")
        p.token = token
        p.supported_profiles = [
            "List"
        ]
        p.previous = self
        return p
    
    def empty_reason_as_text(self, token):
        """ Perform a fulltext search for token "empty-reason". """
        p = FHIRSearchElement(subject="empty-reason")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def empty_reason_missing(self, flag):
        """ Specify if "empty-reason" should be missing or not. """
        p = FHIRSearchElement(subject="empty-reason")
        p.missing = flag
        p.previous = self
        return p
    
    def encounter(self, reference):
        """ Perform a search for "encounter" reference. """
        p = FHIRSearchElement(subject="encounter")
        p.reference = reference
        p.supported_profiles = [
            "Condition",
            "DiagnosticOrder",
            "MedicationAdministration",
            "MedicationPrescription",
            "Questionnaire"
        ]
        p.previous = self
        return p
    
    def encounter_missing(self, flag):
        """ Specify if "encounter" should be missing or not. """
        p = FHIRSearchElement(subject="encounter")
        p.missing = flag
        p.previous = self
        return p
    
    def end(self, date):
        """ Perform a search for "end" date. """
        p = FHIRSearchElement(subject="end")
        p.date = date
        p.supported_profiles = [
            "Provenance"
        ]
        p.previous = self
        return p
    
    def end_missing(self, flag):
        """ Specify if "end" should be missing or not. """
        p = FHIRSearchElement(subject="end")
        p.missing = flag
        p.previous = self
        return p
    
    def event_date(self, date):
        """ Perform a search for "event-date" date. """
        p = FHIRSearchElement(subject="event-date")
        p.date = date
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def event_date_missing(self, flag):
        """ Specify if "event-date" should be missing or not. """
        p = FHIRSearchElement(subject="event-date")
        p.missing = flag
        p.previous = self
        return p
    
    def event_status_date(self, composite):
        """ Perform a search for "event-status-date" composite. """
        p = FHIRSearchElement(subject="event-status-date")
        p.composite = composite
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def event_status_date_missing(self, flag):
        """ Specify if "event-status-date" should be missing or not. """
        p = FHIRSearchElement(subject="event-status-date")
        p.missing = flag
        p.previous = self
        return p
    
    def event_status(self, token):
        """ Perform a search for "event-status" token. """
        p = FHIRSearchElement(subject="event-status")
        p.token = token
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def event_status_as_text(self, token):
        """ Perform a fulltext search for token "event-status". """
        p = FHIRSearchElement(subject="event-status")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def event_status_missing(self, flag):
        """ Specify if "event-status" should be missing or not. """
        p = FHIRSearchElement(subject="event-status")
        p.missing = flag
        p.previous = self
        return p
    
    def event(self, token):
        """ Perform a search for "event" token. """
        p = FHIRSearchElement(subject="event")
        p.token = token
        p.supported_profiles = [
            "Conformance",
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def event_as_text(self, token):
        """ Perform a fulltext search for token "event". """
        p = FHIRSearchElement(subject="event")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def event_missing(self, flag):
        """ Specify if "event" should be missing or not. """
        p = FHIRSearchElement(subject="event")
        p.missing = flag
        p.previous = self
        return p
    
    def evidence(self, token):
        """ Perform a search for "evidence" token. """
        p = FHIRSearchElement(subject="evidence")
        p.token = token
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def evidence_as_text(self, token):
        """ Perform a fulltext search for token "evidence". """
        p = FHIRSearchElement(subject="evidence")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def evidence_missing(self, flag):
        """ Specify if "evidence" should be missing or not. """
        p = FHIRSearchElement(subject="evidence")
        p.missing = flag
        p.previous = self
        return p
    
    def exclude(self, token):
        """ Perform a search for "exclude" token. """
        p = FHIRSearchElement(subject="exclude")
        p.token = token
        p.supported_profiles = [
            "Group"
        ]
        p.previous = self
        return p
    
    def exclude_as_text(self, token):
        """ Perform a fulltext search for token "exclude". """
        p = FHIRSearchElement(subject="exclude")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def exclude_missing(self, flag):
        """ Specify if "exclude" should be missing or not. """
        p = FHIRSearchElement(subject="exclude")
        p.missing = flag
        p.previous = self
        return p
    
    def expiry(self, date):
        """ Perform a search for "expiry" date. """
        p = FHIRSearchElement(subject="expiry")
        p.date = date
        p.supported_profiles = [
            "Substance"
        ]
        p.previous = self
        return p
    
    def expiry_missing(self, flag):
        """ Specify if "expiry" should be missing or not. """
        p = FHIRSearchElement(subject="expiry")
        p.missing = flag
        p.previous = self
        return p
    
    def extension(self, token):
        """ Perform a search for "extension" token. """
        p = FHIRSearchElement(subject="extension")
        p.token = token
        p.supported_profiles = [
            "Profile"
        ]
        p.previous = self
        return p
    
    def extension_as_text(self, token):
        """ Perform a fulltext search for token "extension". """
        p = FHIRSearchElement(subject="extension")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def extension_missing(self, flag):
        """ Specify if "extension" should be missing or not. """
        p = FHIRSearchElement(subject="extension")
        p.missing = flag
        p.previous = self
        return p
    
    def facility(self, token):
        """ Perform a search for "facility" token. """
        p = FHIRSearchElement(subject="facility")
        p.token = token
        p.supported_profiles = [
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def facility_as_text(self, token):
        """ Perform a fulltext search for token "facility". """
        p = FHIRSearchElement(subject="facility")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def facility_missing(self, flag):
        """ Specify if "facility" should be missing or not. """
        p = FHIRSearchElement(subject="facility")
        p.missing = flag
        p.previous = self
        return p
    
    def family(self, string):
        """ Perform a search for "family" string. """
        p = FHIRSearchElement(subject="family")
        p.string = string
        p.supported_profiles = [
            "Patient",
            "Practitioner"
        ]
        p.previous = self
        return p
    
    def family_exact(self, string):
        """ Search for an exact match for "family". """
        p = FHIRSearchElement(subject="family")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def family_missing(self, flag):
        """ Specify if "family" should be missing or not. """
        p = FHIRSearchElement(subject="family")
        p.missing = flag
        p.previous = self
        return p
    
    def fhirversion(self, token):
        """ Perform a search for "fhirversion" token. """
        p = FHIRSearchElement(subject="fhirversion")
        p.token = token
        p.supported_profiles = [
            "Conformance"
        ]
        p.previous = self
        return p
    
    def fhirversion_as_text(self, token):
        """ Perform a fulltext search for token "fhirversion". """
        p = FHIRSearchElement(subject="fhirversion")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def fhirversion_missing(self, flag):
        """ Specify if "fhirversion" should be missing or not. """
        p = FHIRSearchElement(subject="fhirversion")
        p.missing = flag
        p.previous = self
        return p
    
    def format(self, token):
        """ Perform a search for "format" token. """
        p = FHIRSearchElement(subject="format")
        p.token = token
        p.supported_profiles = [
            "Conformance",
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def format_as_text(self, token):
        """ Perform a fulltext search for token "format". """
        p = FHIRSearchElement(subject="format")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def format_missing(self, flag):
        """ Specify if "format" should be missing or not. """
        p = FHIRSearchElement(subject="format")
        p.missing = flag
        p.previous = self
        return p
    
    def form(self, token):
        """ Perform a search for "form" token. """
        p = FHIRSearchElement(subject="form")
        p.token = token
        p.supported_profiles = [
            "Medication"
        ]
        p.previous = self
        return p
    
    def form_as_text(self, token):
        """ Perform a fulltext search for token "form". """
        p = FHIRSearchElement(subject="form")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def form_missing(self, flag):
        """ Specify if "form" should be missing or not. """
        p = FHIRSearchElement(subject="form")
        p.missing = flag
        p.previous = self
        return p
    
    def fulfillment(self, reference):
        """ Perform a search for "fulfillment" reference. """
        p = FHIRSearchElement(subject="fulfillment")
        p.reference = reference
        p.supported_profiles = [
            "OrderResponse"
        ]
        p.previous = self
        return p
    
    def fulfillment_missing(self, flag):
        """ Specify if "fulfillment" should be missing or not. """
        p = FHIRSearchElement(subject="fulfillment")
        p.missing = flag
        p.previous = self
        return p
    
    def gender(self, token):
        """ Perform a search for "gender" token. """
        p = FHIRSearchElement(subject="gender")
        p.token = token
        p.supported_profiles = [
            "Patient",
            "Practitioner",
            "RelatedPerson"
        ]
        p.previous = self
        return p
    
    def gender_as_text(self, token):
        """ Perform a fulltext search for token "gender". """
        p = FHIRSearchElement(subject="gender")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def gender_missing(self, flag):
        """ Specify if "gender" should be missing or not. """
        p = FHIRSearchElement(subject="gender")
        p.missing = flag
        p.previous = self
        return p
    
    def given(self, string):
        """ Perform a search for "given" string. """
        p = FHIRSearchElement(subject="given")
        p.string = string
        p.supported_profiles = [
            "Patient",
            "Practitioner"
        ]
        p.previous = self
        return p
    
    def given_exact(self, string):
        """ Search for an exact match for "given". """
        p = FHIRSearchElement(subject="given")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def given_missing(self, flag):
        """ Specify if "given" should be missing or not. """
        p = FHIRSearchElement(subject="given")
        p.missing = flag
        p.previous = self
        return p
    
    def identifier(self, token):
        """ Perform a search for "identifier" token. """
        p = FHIRSearchElement(subject="identifier")
        p.token = token
        p.supported_profiles = [
            "Composition",
            "ConceptMap",
            "Conformance",
            "Device",
            "DiagnosticOrder",
            "DiagnosticReport",
            "DocumentManifest",
            "DocumentReference",
            "Encounter",
            "Group",
            "Immunization",
            "ImmunizationRecommendation",
            "Location",
            "Media",
            "MedicationAdministration",
            "MedicationDispense",
            "MedicationPrescription",
            "MedicationStatement",
            "Organization",
            "Patient",
            "Practitioner",
            "Profile",
            "Query",
            "Questionnaire",
            "RelatedPerson",
            "Substance",
            "Supply",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def identifier_as_text(self, token):
        """ Perform a fulltext search for token "identifier". """
        p = FHIRSearchElement(subject="identifier")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def identifier_missing(self, flag):
        """ Specify if "identifier" should be missing or not. """
        p = FHIRSearchElement(subject="identifier")
        p.missing = flag
        p.previous = self
        return p
    
    def identity(self, token):
        """ Perform a search for "identity" token. """
        p = FHIRSearchElement(subject="identity")
        p.token = token
        p.supported_profiles = [
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def identity_as_text(self, token):
        """ Perform a fulltext search for token "identity". """
        p = FHIRSearchElement(subject="identity")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def identity_missing(self, flag):
        """ Specify if "identity" should be missing or not. """
        p = FHIRSearchElement(subject="identity")
        p.missing = flag
        p.previous = self
        return p
    
    def image(self, reference):
        """ Perform a search for "image" reference. """
        p = FHIRSearchElement(subject="image")
        p.reference = reference
        p.supported_profiles = [
            "DiagnosticReport"
        ]
        p.previous = self
        return p
    
    def image_missing(self, flag):
        """ Specify if "image" should be missing or not. """
        p = FHIRSearchElement(subject="image")
        p.missing = flag
        p.previous = self
        return p
    
    def indexed(self, date):
        """ Perform a search for "indexed" date. """
        p = FHIRSearchElement(subject="indexed")
        p.date = date
        p.supported_profiles = [
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def indexed_missing(self, flag):
        """ Specify if "indexed" should be missing or not. """
        p = FHIRSearchElement(subject="indexed")
        p.missing = flag
        p.previous = self
        return p
    
    def indication(self, reference):
        """ Perform a search for "indication" reference. """
        p = FHIRSearchElement(subject="indication")
        p.reference = reference
        p.supported_profiles = [
            "Encounter"
        ]
        p.previous = self
        return p
    
    def indication_missing(self, flag):
        """ Specify if "indication" should be missing or not. """
        p = FHIRSearchElement(subject="indication")
        p.missing = flag
        p.previous = self
        return p
    
    def information(self, reference):
        """ Perform a search for "information" reference. """
        p = FHIRSearchElement(subject="information")
        p.reference = reference
        p.supported_profiles = [
            "ImmunizationRecommendation"
        ]
        p.previous = self
        return p
    
    def information_missing(self, flag):
        """ Specify if "information" should be missing or not. """
        p = FHIRSearchElement(subject="information")
        p.missing = flag
        p.previous = self
        return p
    
    def ingredient(self, reference):
        """ Perform a search for "ingredient" reference. """
        p = FHIRSearchElement(subject="ingredient")
        p.reference = reference
        p.supported_profiles = [
            "Medication"
        ]
        p.previous = self
        return p
    
    def ingredient_missing(self, flag):
        """ Specify if "ingredient" should be missing or not. """
        p = FHIRSearchElement(subject="ingredient")
        p.missing = flag
        p.previous = self
        return p
    
    def issued(self, date):
        """ Perform a search for "issued" date. """
        p = FHIRSearchElement(subject="issued")
        p.date = date
        p.supported_profiles = [
            "DiagnosticReport"
        ]
        p.previous = self
        return p
    
    def issued_missing(self, flag):
        """ Specify if "issued" should be missing or not. """
        p = FHIRSearchElement(subject="issued")
        p.missing = flag
        p.previous = self
        return p
    
    def item_date(self, date):
        """ Perform a search for "item-date" date. """
        p = FHIRSearchElement(subject="item-date")
        p.date = date
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def item_date_missing(self, flag):
        """ Specify if "item-date" should be missing or not. """
        p = FHIRSearchElement(subject="item-date")
        p.missing = flag
        p.previous = self
        return p
    
    def item_past_status(self, token):
        """ Perform a search for "item-past-status" token. """
        p = FHIRSearchElement(subject="item-past-status")
        p.token = token
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def item_past_status_as_text(self, token):
        """ Perform a fulltext search for token "item-past-status". """
        p = FHIRSearchElement(subject="item-past-status")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def item_past_status_missing(self, flag):
        """ Specify if "item-past-status" should be missing or not. """
        p = FHIRSearchElement(subject="item-past-status")
        p.missing = flag
        p.previous = self
        return p
    
    def item_status_date(self, composite):
        """ Perform a search for "item-status-date" composite. """
        p = FHIRSearchElement(subject="item-status-date")
        p.composite = composite
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def item_status_date_missing(self, flag):
        """ Specify if "item-status-date" should be missing or not. """
        p = FHIRSearchElement(subject="item-status-date")
        p.missing = flag
        p.previous = self
        return p
    
    def item_status(self, token):
        """ Perform a search for "item-status" token. """
        p = FHIRSearchElement(subject="item-status")
        p.token = token
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def item_status_as_text(self, token):
        """ Perform a fulltext search for token "item-status". """
        p = FHIRSearchElement(subject="item-status")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def item_status_missing(self, flag):
        """ Specify if "item-status" should be missing or not. """
        p = FHIRSearchElement(subject="item-status")
        p.missing = flag
        p.previous = self
        return p
    
    def item(self, reference):
        """ Perform a search for "item" reference. """
        p = FHIRSearchElement(subject="item")
        p.reference = reference
        p.supported_profiles = [
            "List"
        ]
        p.previous = self
        return p
    
    def item_missing(self, flag):
        """ Specify if "item" should be missing or not. """
        p = FHIRSearchElement(subject="item")
        p.missing = flag
        p.previous = self
        return p
    
    def kind(self, token):
        """ Perform a search for "kind" token. """
        p = FHIRSearchElement(subject="kind")
        p.token = token
        p.supported_profiles = [
            "Supply"
        ]
        p.previous = self
        return p
    
    def kind_as_text(self, token):
        """ Perform a fulltext search for token "kind". """
        p = FHIRSearchElement(subject="kind")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def kind_missing(self, flag):
        """ Specify if "kind" should be missing or not. """
        p = FHIRSearchElement(subject="kind")
        p.missing = flag
        p.previous = self
        return p
    
    def language(self, token):
        """ Perform a search for "language" token. """
        p = FHIRSearchElement(subject="language")
        p.token = token
        p.supported_profiles = [
            "DocumentReference",
            "Patient"
        ]
        p.previous = self
        return p
    
    def language_as_text(self, token):
        """ Perform a fulltext search for token "language". """
        p = FHIRSearchElement(subject="language")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def language_missing(self, flag):
        """ Specify if "language" should be missing or not. """
        p = FHIRSearchElement(subject="language")
        p.missing = flag
        p.previous = self
        return p
    
    def length(self, number):
        """ Perform a search for "length" number. """
        p = FHIRSearchElement(subject="length")
        p.number = number
        p.supported_profiles = [
            "Encounter"
        ]
        p.previous = self
        return p
    
    def length_missing(self, flag):
        """ Specify if "length" should be missing or not. """
        p = FHIRSearchElement(subject="length")
        p.missing = flag
        p.previous = self
        return p
    
    def link(self, reference):
        """ Perform a search for "link" reference. """
        p = FHIRSearchElement(subject="link")
        p.reference = reference
        p.supported_profiles = [
            "Patient"
        ]
        p.previous = self
        return p
    
    def link_missing(self, flag):
        """ Specify if "link" should be missing or not. """
        p = FHIRSearchElement(subject="link")
        p.missing = flag
        p.previous = self
        return p
    
    def location_period(self, date):
        """ Perform a search for "location-period" date. """
        p = FHIRSearchElement(subject="location-period")
        p.date = date
        p.supported_profiles = [
            "Encounter"
        ]
        p.previous = self
        return p
    
    def location_period_missing(self, flag):
        """ Specify if "location-period" should be missing or not. """
        p = FHIRSearchElement(subject="location-period")
        p.missing = flag
        p.previous = self
        return p
    
    def location(self, reference):
        """ Perform a search for "location" reference. """
        p = FHIRSearchElement(subject="location")
        p.reference = reference
        p.supported_profiles = [
            "Condition",
            "Device",
            "DocumentReference",
            "Encounter",
            "Immunization",
            "Provenance"
        ]
        p.previous = self
        return p
    
    def location(self, string):
        """ Perform a search for "location" string. """
        p = FHIRSearchElement(subject="location")
        p.string = string
        p.supported_profiles = [
            "Condition",
            "Device",
            "DocumentReference",
            "Encounter",
            "Immunization",
            "Provenance"
        ]
        p.previous = self
        return p
    
    def location_exact(self, string):
        """ Search for an exact match for "location". """
        p = FHIRSearchElement(subject="location")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def location_missing(self, flag):
        """ Specify if "location" should be missing or not. """
        p = FHIRSearchElement(subject="location")
        p.missing = flag
        p.previous = self
        return p
    
    def location(self, token):
        """ Perform a search for "location" token. """
        p = FHIRSearchElement(subject="location")
        p.token = token
        p.supported_profiles = [
            "Condition",
            "Device",
            "DocumentReference",
            "Encounter",
            "Immunization",
            "Provenance"
        ]
        p.previous = self
        return p
    
    def location_as_text(self, token):
        """ Perform a fulltext search for token "location". """
        p = FHIRSearchElement(subject="location")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def lot_number(self, string):
        """ Perform a search for "lot-number" string. """
        p = FHIRSearchElement(subject="lot-number")
        p.string = string
        p.supported_profiles = [
            "Immunization"
        ]
        p.previous = self
        return p
    
    def lot_number_exact(self, string):
        """ Search for an exact match for "lot-number". """
        p = FHIRSearchElement(subject="lot-number")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def lot_number_missing(self, flag):
        """ Specify if "lot-number" should be missing or not. """
        p = FHIRSearchElement(subject="lot-number")
        p.missing = flag
        p.previous = self
        return p
    
    def manufacturer(self, reference):
        """ Perform a search for "manufacturer" reference. """
        p = FHIRSearchElement(subject="manufacturer")
        p.reference = reference
        p.supported_profiles = [
            "Device",
            "Immunization",
            "Medication"
        ]
        p.previous = self
        return p
    
    def manufacturer(self, string):
        """ Perform a search for "manufacturer" string. """
        p = FHIRSearchElement(subject="manufacturer")
        p.string = string
        p.supported_profiles = [
            "Device",
            "Immunization",
            "Medication"
        ]
        p.previous = self
        return p
    
    def manufacturer_exact(self, string):
        """ Search for an exact match for "manufacturer". """
        p = FHIRSearchElement(subject="manufacturer")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def manufacturer_missing(self, flag):
        """ Specify if "manufacturer" should be missing or not. """
        p = FHIRSearchElement(subject="manufacturer")
        p.missing = flag
        p.previous = self
        return p
    
    def medication(self, reference):
        """ Perform a search for "medication" reference. """
        p = FHIRSearchElement(subject="medication")
        p.reference = reference
        p.supported_profiles = [
            "MedicationAdministration",
            "MedicationDispense",
            "MedicationPrescription",
            "MedicationStatement"
        ]
        p.previous = self
        return p
    
    def medication_missing(self, flag):
        """ Specify if "medication" should be missing or not. """
        p = FHIRSearchElement(subject="medication")
        p.missing = flag
        p.previous = self
        return p
    
    def member(self, reference):
        """ Perform a search for "member" reference. """
        p = FHIRSearchElement(subject="member")
        p.reference = reference
        p.supported_profiles = [
            "Group"
        ]
        p.previous = self
        return p
    
    def member_missing(self, flag):
        """ Specify if "member" should be missing or not. """
        p = FHIRSearchElement(subject="member")
        p.missing = flag
        p.previous = self
        return p
    
    def modality(self, token):
        """ Perform a search for "modality" token. """
        p = FHIRSearchElement(subject="modality")
        p.token = token
        p.supported_profiles = [
            "ImagingStudy"
        ]
        p.previous = self
        return p
    
    def modality_as_text(self, token):
        """ Perform a fulltext search for token "modality". """
        p = FHIRSearchElement(subject="modality")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def modality_missing(self, flag):
        """ Specify if "modality" should be missing or not. """
        p = FHIRSearchElement(subject="modality")
        p.missing = flag
        p.previous = self
        return p
    
    def model(self, string):
        """ Perform a search for "model" string. """
        p = FHIRSearchElement(subject="model")
        p.string = string
        p.supported_profiles = [
            "Device"
        ]
        p.previous = self
        return p
    
    def model_exact(self, string):
        """ Search for an exact match for "model". """
        p = FHIRSearchElement(subject="model")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def model_missing(self, flag):
        """ Specify if "model" should be missing or not. """
        p = FHIRSearchElement(subject="model")
        p.missing = flag
        p.previous = self
        return p
    
    def mode(self, token):
        """ Perform a search for "mode" token. """
        p = FHIRSearchElement(subject="mode")
        p.token = token
        p.supported_profiles = [
            "Conformance"
        ]
        p.previous = self
        return p
    
    def mode_as_text(self, token):
        """ Perform a fulltext search for token "mode". """
        p = FHIRSearchElement(subject="mode")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def mode_missing(self, flag):
        """ Specify if "mode" should be missing or not. """
        p = FHIRSearchElement(subject="mode")
        p.missing = flag
        p.previous = self
        return p
    
    def name_value_x(self, composite):
        """ Perform a search for "name-value-[x]" composite. """
        p = FHIRSearchElement(subject="name-value-[x]")
        p.composite = composite
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def name_value_x_missing(self, flag):
        """ Specify if "name-value-[x]" should be missing or not. """
        p = FHIRSearchElement(subject="name-value-[x]")
        p.missing = flag
        p.previous = self
        return p
    
    def name(self, string):
        """ Perform a search for "name" string. """
        p = FHIRSearchElement(subject="name")
        p.string = string
        p.supported_profiles = [
            "ConceptMap",
            "Conformance",
            "DiagnosticReport",
            "Location",
            "Medication",
            "Observation",
            "Organization",
            "Patient",
            "Practitioner",
            "Profile",
            "Questionnaire",
            "RelatedPerson",
            "SecurityEvent",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def name_exact(self, string):
        """ Search for an exact match for "name". """
        p = FHIRSearchElement(subject="name")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def name_missing(self, flag):
        """ Specify if "name" should be missing or not. """
        p = FHIRSearchElement(subject="name")
        p.missing = flag
        p.previous = self
        return p
    
    def name(self, token):
        """ Perform a search for "name" token. """
        p = FHIRSearchElement(subject="name")
        p.token = token
        p.supported_profiles = [
            "ConceptMap",
            "Conformance",
            "DiagnosticReport",
            "Location",
            "Medication",
            "Observation",
            "Organization",
            "Patient",
            "Practitioner",
            "Profile",
            "Questionnaire",
            "RelatedPerson",
            "SecurityEvent",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def name_as_text(self, token):
        """ Perform a fulltext search for token "name". """
        p = FHIRSearchElement(subject="name")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def near_distance(self, token):
        """ Perform a search for "near-distance" token. """
        p = FHIRSearchElement(subject="near-distance")
        p.token = token
        p.supported_profiles = [
            "Location"
        ]
        p.previous = self
        return p
    
    def near_distance_as_text(self, token):
        """ Perform a fulltext search for token "near-distance". """
        p = FHIRSearchElement(subject="near-distance")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def near_distance_missing(self, flag):
        """ Specify if "near-distance" should be missing or not. """
        p = FHIRSearchElement(subject="near-distance")
        p.missing = flag
        p.previous = self
        return p
    
    def near(self, token):
        """ Perform a search for "near" token. """
        p = FHIRSearchElement(subject="near")
        p.token = token
        p.supported_profiles = [
            "Location"
        ]
        p.previous = self
        return p
    
    def near_as_text(self, token):
        """ Perform a fulltext search for token "near". """
        p = FHIRSearchElement(subject="near")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def near_missing(self, flag):
        """ Specify if "near" should be missing or not. """
        p = FHIRSearchElement(subject="near")
        p.missing = flag
        p.previous = self
        return p
    
    def notgiven(self, token):
        """ Perform a search for "notgiven" token. """
        p = FHIRSearchElement(subject="notgiven")
        p.token = token
        p.supported_profiles = [
            "MedicationAdministration"
        ]
        p.previous = self
        return p
    
    def notgiven_as_text(self, token):
        """ Perform a fulltext search for token "notgiven". """
        p = FHIRSearchElement(subject="notgiven")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def notgiven_missing(self, flag):
        """ Specify if "notgiven" should be missing or not. """
        p = FHIRSearchElement(subject="notgiven")
        p.missing = flag
        p.previous = self
        return p
    
    def object_type(self, token):
        """ Perform a search for "object-type" token. """
        p = FHIRSearchElement(subject="object-type")
        p.token = token
        p.supported_profiles = [
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def object_type_as_text(self, token):
        """ Perform a fulltext search for token "object-type". """
        p = FHIRSearchElement(subject="object-type")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def object_type_missing(self, flag):
        """ Specify if "object-type" should be missing or not. """
        p = FHIRSearchElement(subject="object-type")
        p.missing = flag
        p.previous = self
        return p
    
    def observation(self, reference):
        """ Perform a search for "observation" reference. """
        p = FHIRSearchElement(subject="observation")
        p.reference = reference
        p.supported_profiles = [
            "DeviceObservationReport"
        ]
        p.previous = self
        return p
    
    def observation_missing(self, flag):
        """ Specify if "observation" should be missing or not. """
        p = FHIRSearchElement(subject="observation")
        p.missing = flag
        p.previous = self
        return p
    
    def onset(self, date):
        """ Perform a search for "onset" date. """
        p = FHIRSearchElement(subject="onset")
        p.date = date
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def onset_missing(self, flag):
        """ Specify if "onset" should be missing or not. """
        p = FHIRSearchElement(subject="onset")
        p.missing = flag
        p.previous = self
        return p
    
    def operator(self, reference):
        """ Perform a search for "operator" reference. """
        p = FHIRSearchElement(subject="operator")
        p.reference = reference
        p.supported_profiles = [
            "Media"
        ]
        p.previous = self
        return p
    
    def operator_missing(self, flag):
        """ Specify if "operator" should be missing or not. """
        p = FHIRSearchElement(subject="operator")
        p.missing = flag
        p.previous = self
        return p
    
    def orderer(self, reference):
        """ Perform a search for "orderer" reference. """
        p = FHIRSearchElement(subject="orderer")
        p.reference = reference
        p.supported_profiles = [
            "DiagnosticOrder"
        ]
        p.previous = self
        return p
    
    def orderer_missing(self, flag):
        """ Specify if "orderer" should be missing or not. """
        p = FHIRSearchElement(subject="orderer")
        p.missing = flag
        p.previous = self
        return p
    
    def organization(self, reference):
        """ Perform a search for "organization" reference. """
        p = FHIRSearchElement(subject="organization")
        p.reference = reference
        p.supported_profiles = [
            "Device",
            "Practitioner"
        ]
        p.previous = self
        return p
    
    def organization_missing(self, flag):
        """ Specify if "organization" should be missing or not. """
        p = FHIRSearchElement(subject="organization")
        p.missing = flag
        p.previous = self
        return p
    
    def participant(self, reference):
        """ Perform a search for "participant" reference. """
        p = FHIRSearchElement(subject="participant")
        p.reference = reference
        p.supported_profiles = [
            "CarePlan"
        ]
        p.previous = self
        return p
    
    def participant_missing(self, flag):
        """ Specify if "participant" should be missing or not. """
        p = FHIRSearchElement(subject="participant")
        p.missing = flag
        p.previous = self
        return p
    
    def partof(self, reference):
        """ Perform a search for "partof" reference. """
        p = FHIRSearchElement(subject="partof")
        p.reference = reference
        p.supported_profiles = [
            "Location",
            "Organization"
        ]
        p.previous = self
        return p
    
    def partof_missing(self, flag):
        """ Specify if "partof" should be missing or not. """
        p = FHIRSearchElement(subject="partof")
        p.missing = flag
        p.previous = self
        return p
    
    def partytype(self, token):
        """ Perform a search for "partytype" token. """
        p = FHIRSearchElement(subject="partytype")
        p.token = token
        p.supported_profiles = [
            "Provenance"
        ]
        p.previous = self
        return p
    
    def partytype_as_text(self, token):
        """ Perform a fulltext search for token "partytype". """
        p = FHIRSearchElement(subject="partytype")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def partytype_missing(self, flag):
        """ Specify if "partytype" should be missing or not. """
        p = FHIRSearchElement(subject="partytype")
        p.missing = flag
        p.previous = self
        return p
    
    def party(self, token):
        """ Perform a search for "party" token. """
        p = FHIRSearchElement(subject="party")
        p.token = token
        p.supported_profiles = [
            "Provenance"
        ]
        p.previous = self
        return p
    
    def party_as_text(self, token):
        """ Perform a fulltext search for token "party". """
        p = FHIRSearchElement(subject="party")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def party_missing(self, flag):
        """ Specify if "party" should be missing or not. """
        p = FHIRSearchElement(subject="party")
        p.missing = flag
        p.previous = self
        return p
    
    def patientid(self, token):
        """ Perform a search for "patientid" token. """
        p = FHIRSearchElement(subject="patientid")
        p.token = token
        p.supported_profiles = [
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def patientid_as_text(self, token):
        """ Perform a fulltext search for token "patientid". """
        p = FHIRSearchElement(subject="patientid")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def patientid_missing(self, flag):
        """ Specify if "patientid" should be missing or not. """
        p = FHIRSearchElement(subject="patientid")
        p.missing = flag
        p.previous = self
        return p
    
    def patient(self, reference):
        """ Perform a search for "patient" reference. """
        p = FHIRSearchElement(subject="patient")
        p.reference = reference
        p.supported_profiles = [
            "CarePlan",
            "Device",
            "MedicationAdministration",
            "MedicationDispense",
            "MedicationPrescription",
            "MedicationStatement",
            "RelatedPerson",
            "Supply"
        ]
        p.previous = self
        return p
    
    def patient_missing(self, flag):
        """ Specify if "patient" should be missing or not. """
        p = FHIRSearchElement(subject="patient")
        p.missing = flag
        p.previous = self
        return p
    
    def performer(self, reference):
        """ Perform a search for "performer" reference. """
        p = FHIRSearchElement(subject="performer")
        p.reference = reference
        p.supported_profiles = [
            "DiagnosticReport",
            "Immunization",
            "Observation"
        ]
        p.previous = self
        return p
    
    def performer_missing(self, flag):
        """ Specify if "performer" should be missing or not. """
        p = FHIRSearchElement(subject="performer")
        p.missing = flag
        p.previous = self
        return p
    
    def period(self, date):
        """ Perform a search for "period" date. """
        p = FHIRSearchElement(subject="period")
        p.date = date
        p.supported_profiles = [
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def period_missing(self, flag):
        """ Specify if "period" should be missing or not. """
        p = FHIRSearchElement(subject="period")
        p.missing = flag
        p.previous = self
        return p
    
    def phonetic(self, string):
        """ Perform a search for "phonetic" string. """
        p = FHIRSearchElement(subject="phonetic")
        p.string = string
        p.supported_profiles = [
            "Organization",
            "Patient",
            "Practitioner",
            "RelatedPerson"
        ]
        p.previous = self
        return p
    
    def phonetic_exact(self, string):
        """ Search for an exact match for "phonetic". """
        p = FHIRSearchElement(subject="phonetic")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def phonetic_missing(self, flag):
        """ Specify if "phonetic" should be missing or not. """
        p = FHIRSearchElement(subject="phonetic")
        p.missing = flag
        p.previous = self
        return p
    
    def prescription(self, reference):
        """ Perform a search for "prescription" reference. """
        p = FHIRSearchElement(subject="prescription")
        p.reference = reference
        p.supported_profiles = [
            "MedicationAdministration",
            "MedicationDispense"
        ]
        p.previous = self
        return p
    
    def prescription_missing(self, flag):
        """ Specify if "prescription" should be missing or not. """
        p = FHIRSearchElement(subject="prescription")
        p.missing = flag
        p.previous = self
        return p
    
    def product(self, token):
        """ Perform a search for "product" token. """
        p = FHIRSearchElement(subject="product")
        p.token = token
        p.supported_profiles = [
            "ConceptMap"
        ]
        p.previous = self
        return p
    
    def product_as_text(self, token):
        """ Perform a fulltext search for token "product". """
        p = FHIRSearchElement(subject="product")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def product_missing(self, flag):
        """ Specify if "product" should be missing or not. """
        p = FHIRSearchElement(subject="product")
        p.missing = flag
        p.previous = self
        return p
    
    def profile(self, reference):
        """ Perform a search for "profile" reference. """
        p = FHIRSearchElement(subject="profile")
        p.reference = reference
        p.supported_profiles = [
            "Conformance"
        ]
        p.previous = self
        return p
    
    def profile_missing(self, flag):
        """ Specify if "profile" should be missing or not. """
        p = FHIRSearchElement(subject="profile")
        p.missing = flag
        p.previous = self
        return p
    
    def provider(self, reference):
        """ Perform a search for "provider" reference. """
        p = FHIRSearchElement(subject="provider")
        p.reference = reference
        p.supported_profiles = [
            "Patient"
        ]
        p.previous = self
        return p
    
    def provider_missing(self, flag):
        """ Specify if "provider" should be missing or not. """
        p = FHIRSearchElement(subject="provider")
        p.missing = flag
        p.previous = self
        return p
    
    def publisher(self, string):
        """ Perform a search for "publisher" string. """
        p = FHIRSearchElement(subject="publisher")
        p.string = string
        p.supported_profiles = [
            "ConceptMap",
            "Conformance",
            "Profile",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def publisher_exact(self, string):
        """ Search for an exact match for "publisher". """
        p = FHIRSearchElement(subject="publisher")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def publisher_missing(self, flag):
        """ Specify if "publisher" should be missing or not. """
        p = FHIRSearchElement(subject="publisher")
        p.missing = flag
        p.previous = self
        return p
    
    def quantity(self, number):
        """ Perform a search for "quantity" number. """
        p = FHIRSearchElement(subject="quantity")
        p.number = number
        p.supported_profiles = [
            "Substance"
        ]
        p.previous = self
        return p
    
    def quantity_missing(self, flag):
        """ Specify if "quantity" should be missing or not. """
        p = FHIRSearchElement(subject="quantity")
        p.missing = flag
        p.previous = self
        return p
    
    def reaction_date(self, date):
        """ Perform a search for "reaction-date" date. """
        p = FHIRSearchElement(subject="reaction-date")
        p.date = date
        p.supported_profiles = [
            "Immunization"
        ]
        p.previous = self
        return p
    
    def reaction_date_missing(self, flag):
        """ Specify if "reaction-date" should be missing or not. """
        p = FHIRSearchElement(subject="reaction-date")
        p.missing = flag
        p.previous = self
        return p
    
    def reaction(self, reference):
        """ Perform a search for "reaction" reference. """
        p = FHIRSearchElement(subject="reaction")
        p.reference = reference
        p.supported_profiles = [
            "Immunization"
        ]
        p.previous = self
        return p
    
    def reaction_missing(self, flag):
        """ Specify if "reaction" should be missing or not. """
        p = FHIRSearchElement(subject="reaction")
        p.missing = flag
        p.previous = self
        return p
    
    def reason(self, token):
        """ Perform a search for "reason" token. """
        p = FHIRSearchElement(subject="reason")
        p.token = token
        p.supported_profiles = [
            "Immunization"
        ]
        p.previous = self
        return p
    
    def reason_as_text(self, token):
        """ Perform a fulltext search for token "reason". """
        p = FHIRSearchElement(subject="reason")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def reason_missing(self, flag):
        """ Specify if "reason" should be missing or not. """
        p = FHIRSearchElement(subject="reason")
        p.missing = flag
        p.previous = self
        return p
    
    def recipient(self, reference):
        """ Perform a search for "recipient" reference. """
        p = FHIRSearchElement(subject="recipient")
        p.reference = reference
        p.supported_profiles = [
            "DocumentManifest"
        ]
        p.previous = self
        return p
    
    def recipient_missing(self, flag):
        """ Specify if "recipient" should be missing or not. """
        p = FHIRSearchElement(subject="recipient")
        p.missing = flag
        p.previous = self
        return p
    
    def recorder(self, reference):
        """ Perform a search for "recorder" reference. """
        p = FHIRSearchElement(subject="recorder")
        p.reference = reference
        p.supported_profiles = [
            "AllergyIntolerance"
        ]
        p.previous = self
        return p
    
    def recorder_missing(self, flag):
        """ Specify if "recorder" should be missing or not. """
        p = FHIRSearchElement(subject="recorder")
        p.missing = flag
        p.previous = self
        return p
    
    def reference(self, reference):
        """ Perform a search for "reference" reference. """
        p = FHIRSearchElement(subject="reference")
        p.reference = reference
        p.supported_profiles = [
            "SecurityEvent",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def reference(self, token):
        """ Perform a search for "reference" token. """
        p = FHIRSearchElement(subject="reference")
        p.token = token
        p.supported_profiles = [
            "SecurityEvent",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def reference_as_text(self, token):
        """ Perform a fulltext search for token "reference". """
        p = FHIRSearchElement(subject="reference")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def refusal_reason(self, token):
        """ Perform a search for "refusal-reason" token. """
        p = FHIRSearchElement(subject="refusal-reason")
        p.token = token
        p.supported_profiles = [
            "Immunization"
        ]
        p.previous = self
        return p
    
    def refusal_reason_as_text(self, token):
        """ Perform a fulltext search for token "refusal-reason". """
        p = FHIRSearchElement(subject="refusal-reason")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def refusal_reason_missing(self, flag):
        """ Specify if "refusal-reason" should be missing or not. """
        p = FHIRSearchElement(subject="refusal-reason")
        p.missing = flag
        p.previous = self
        return p
    
    def refused(self, token):
        """ Perform a search for "refused" token. """
        p = FHIRSearchElement(subject="refused")
        p.token = token
        p.supported_profiles = [
            "Immunization"
        ]
        p.previous = self
        return p
    
    def refused_as_text(self, token):
        """ Perform a fulltext search for token "refused". """
        p = FHIRSearchElement(subject="refused")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def refused_missing(self, flag):
        """ Specify if "refused" should be missing or not. """
        p = FHIRSearchElement(subject="refused")
        p.missing = flag
        p.previous = self
        return p
    
    def related_code(self, token):
        """ Perform a search for "related-code" token. """
        p = FHIRSearchElement(subject="related-code")
        p.token = token
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def related_code_as_text(self, token):
        """ Perform a fulltext search for token "related-code". """
        p = FHIRSearchElement(subject="related-code")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def related_code_missing(self, flag):
        """ Specify if "related-code" should be missing or not. """
        p = FHIRSearchElement(subject="related-code")
        p.missing = flag
        p.previous = self
        return p
    
    def related_item(self, reference):
        """ Perform a search for "related-item" reference. """
        p = FHIRSearchElement(subject="related-item")
        p.reference = reference
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def related_item_missing(self, flag):
        """ Specify if "related-item" should be missing or not. """
        p = FHIRSearchElement(subject="related-item")
        p.missing = flag
        p.previous = self
        return p
    
    def related_target(self, reference):
        """ Perform a search for "related-target" reference. """
        p = FHIRSearchElement(subject="related-target")
        p.reference = reference
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def related_target_missing(self, flag):
        """ Specify if "related-target" should be missing or not. """
        p = FHIRSearchElement(subject="related-target")
        p.missing = flag
        p.previous = self
        return p
    
    def related_type(self, token):
        """ Perform a search for "related-type" token. """
        p = FHIRSearchElement(subject="related-type")
        p.token = token
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def related_type_as_text(self, token):
        """ Perform a fulltext search for token "related-type". """
        p = FHIRSearchElement(subject="related-type")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def related_type_missing(self, flag):
        """ Specify if "related-type" should be missing or not. """
        p = FHIRSearchElement(subject="related-type")
        p.missing = flag
        p.previous = self
        return p
    
    def related(self, composite):
        """ Perform a search for "related" composite. """
        p = FHIRSearchElement(subject="related")
        p.composite = composite
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def related_missing(self, flag):
        """ Specify if "related" should be missing or not. """
        p = FHIRSearchElement(subject="related")
        p.missing = flag
        p.previous = self
        return p
    
    def relatesto(self, reference):
        """ Perform a search for "relatesto" reference. """
        p = FHIRSearchElement(subject="relatesto")
        p.reference = reference
        p.supported_profiles = [
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def relatesto_missing(self, flag):
        """ Specify if "relatesto" should be missing or not. """
        p = FHIRSearchElement(subject="relatesto")
        p.missing = flag
        p.previous = self
        return p
    
    def relationship(self, composite):
        """ Perform a search for "relationship" composite. """
        p = FHIRSearchElement(subject="relationship")
        p.composite = composite
        p.supported_profiles = [
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def relationship_missing(self, flag):
        """ Specify if "relationship" should be missing or not. """
        p = FHIRSearchElement(subject="relationship")
        p.missing = flag
        p.previous = self
        return p
    
    def relation(self, token):
        """ Perform a search for "relation" token. """
        p = FHIRSearchElement(subject="relation")
        p.token = token
        p.supported_profiles = [
            "DocumentReference"
        ]
        p.previous = self
        return p
    
    def relation_as_text(self, token):
        """ Perform a fulltext search for token "relation". """
        p = FHIRSearchElement(subject="relation")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def relation_missing(self, flag):
        """ Specify if "relation" should be missing or not. """
        p = FHIRSearchElement(subject="relation")
        p.missing = flag
        p.previous = self
        return p
    
    def reliability(self, token):
        """ Perform a search for "reliability" token. """
        p = FHIRSearchElement(subject="reliability")
        p.token = token
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def reliability_as_text(self, token):
        """ Perform a fulltext search for token "reliability". """
        p = FHIRSearchElement(subject="reliability")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def reliability_missing(self, flag):
        """ Specify if "reliability" should be missing or not. """
        p = FHIRSearchElement(subject="reliability")
        p.missing = flag
        p.previous = self
        return p
    
    def requester(self, reference):
        """ Perform a search for "requester" reference. """
        p = FHIRSearchElement(subject="requester")
        p.reference = reference
        p.supported_profiles = [
            "Immunization"
        ]
        p.previous = self
        return p
    
    def requester_missing(self, flag):
        """ Specify if "requester" should be missing or not. """
        p = FHIRSearchElement(subject="requester")
        p.missing = flag
        p.previous = self
        return p
    
    def request(self, reference):
        """ Perform a search for "request" reference. """
        p = FHIRSearchElement(subject="request")
        p.reference = reference
        p.supported_profiles = [
            "DiagnosticReport",
            "OrderResponse"
        ]
        p.previous = self
        return p
    
    def request_missing(self, flag):
        """ Specify if "request" should be missing or not. """
        p = FHIRSearchElement(subject="request")
        p.missing = flag
        p.previous = self
        return p
    
    def resource(self, token):
        """ Perform a search for "resource" token. """
        p = FHIRSearchElement(subject="resource")
        p.token = token
        p.supported_profiles = [
            "Conformance"
        ]
        p.previous = self
        return p
    
    def resource_as_text(self, token):
        """ Perform a fulltext search for token "resource". """
        p = FHIRSearchElement(subject="resource")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def resource_missing(self, flag):
        """ Specify if "resource" should be missing or not. """
        p = FHIRSearchElement(subject="resource")
        p.missing = flag
        p.previous = self
        return p
    
    def response(self, token):
        """ Perform a search for "response" token. """
        p = FHIRSearchElement(subject="response")
        p.token = token
        p.supported_profiles = [
            "Query"
        ]
        p.previous = self
        return p
    
    def response_as_text(self, token):
        """ Perform a fulltext search for token "response". """
        p = FHIRSearchElement(subject="response")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def response_missing(self, flag):
        """ Specify if "response" should be missing or not. """
        p = FHIRSearchElement(subject="response")
        p.missing = flag
        p.previous = self
        return p
    
    def responsibleparty(self, reference):
        """ Perform a search for "responsibleparty" reference. """
        p = FHIRSearchElement(subject="responsibleparty")
        p.reference = reference
        p.supported_profiles = [
            "MedicationDispense"
        ]
        p.previous = self
        return p
    
    def responsibleparty_missing(self, flag):
        """ Specify if "responsibleparty" should be missing or not. """
        p = FHIRSearchElement(subject="responsibleparty")
        p.missing = flag
        p.previous = self
        return p
    
    def result(self, reference):
        """ Perform a search for "result" reference. """
        p = FHIRSearchElement(subject="result")
        p.reference = reference
        p.supported_profiles = [
            "DiagnosticReport"
        ]
        p.previous = self
        return p
    
    def result_missing(self, flag):
        """ Specify if "result" should be missing or not. """
        p = FHIRSearchElement(subject="result")
        p.missing = flag
        p.previous = self
        return p
    
    def section_content(self, reference):
        """ Perform a search for "section-content" reference. """
        p = FHIRSearchElement(subject="section-content")
        p.reference = reference
        p.supported_profiles = [
            "Composition"
        ]
        p.previous = self
        return p
    
    def section_content_missing(self, flag):
        """ Specify if "section-content" should be missing or not. """
        p = FHIRSearchElement(subject="section-content")
        p.missing = flag
        p.previous = self
        return p
    
    def section_type(self, token):
        """ Perform a search for "section-type" token. """
        p = FHIRSearchElement(subject="section-type")
        p.token = token
        p.supported_profiles = [
            "Composition"
        ]
        p.previous = self
        return p
    
    def section_type_as_text(self, token):
        """ Perform a fulltext search for token "section-type". """
        p = FHIRSearchElement(subject="section-type")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def section_type_missing(self, flag):
        """ Specify if "section-type" should be missing or not. """
        p = FHIRSearchElement(subject="section-type")
        p.missing = flag
        p.previous = self
        return p
    
    def security(self, token):
        """ Perform a search for "security" token. """
        p = FHIRSearchElement(subject="security")
        p.token = token
        p.supported_profiles = [
            "Conformance"
        ]
        p.previous = self
        return p
    
    def security_as_text(self, token):
        """ Perform a fulltext search for token "security". """
        p = FHIRSearchElement(subject="security")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def security_missing(self, flag):
        """ Specify if "security" should be missing or not. """
        p = FHIRSearchElement(subject="security")
        p.missing = flag
        p.previous = self
        return p
    
    def series(self, token):
        """ Perform a search for "series" token. """
        p = FHIRSearchElement(subject="series")
        p.token = token
        p.supported_profiles = [
            "ImagingStudy"
        ]
        p.previous = self
        return p
    
    def series_as_text(self, token):
        """ Perform a fulltext search for token "series". """
        p = FHIRSearchElement(subject="series")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def series_missing(self, flag):
        """ Specify if "series" should be missing or not. """
        p = FHIRSearchElement(subject="series")
        p.missing = flag
        p.previous = self
        return p
    
    def service(self, token):
        """ Perform a search for "service" token. """
        p = FHIRSearchElement(subject="service")
        p.token = token
        p.supported_profiles = [
            "DiagnosticReport"
        ]
        p.previous = self
        return p
    
    def service_as_text(self, token):
        """ Perform a fulltext search for token "service". """
        p = FHIRSearchElement(subject="service")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def service_missing(self, flag):
        """ Specify if "service" should be missing or not. """
        p = FHIRSearchElement(subject="service")
        p.missing = flag
        p.previous = self
        return p
    
    def severity(self, token):
        """ Perform a search for "severity" token. """
        p = FHIRSearchElement(subject="severity")
        p.token = token
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def severity_as_text(self, token):
        """ Perform a fulltext search for token "severity". """
        p = FHIRSearchElement(subject="severity")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def severity_missing(self, flag):
        """ Specify if "severity" should be missing or not. """
        p = FHIRSearchElement(subject="severity")
        p.missing = flag
        p.previous = self
        return p
    
    def site(self, token):
        """ Perform a search for "site" token. """
        p = FHIRSearchElement(subject="site")
        p.token = token
        p.supported_profiles = [
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def site_as_text(self, token):
        """ Perform a fulltext search for token "site". """
        p = FHIRSearchElement(subject="site")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def site_missing(self, flag):
        """ Specify if "site" should be missing or not. """
        p = FHIRSearchElement(subject="site")
        p.missing = flag
        p.previous = self
        return p
    
    def size(self, number):
        """ Perform a search for "size" number. """
        p = FHIRSearchElement(subject="size")
        p.number = number
        p.supported_profiles = [
            "DocumentReference",
            "ImagingStudy"
        ]
        p.previous = self
        return p
    
    def size_missing(self, flag):
        """ Specify if "size" should be missing or not. """
        p = FHIRSearchElement(subject="size")
        p.missing = flag
        p.previous = self
        return p
    
    def software(self, string):
        """ Perform a search for "software" string. """
        p = FHIRSearchElement(subject="software")
        p.string = string
        p.supported_profiles = [
            "Conformance"
        ]
        p.previous = self
        return p
    
    def software_exact(self, string):
        """ Search for an exact match for "software". """
        p = FHIRSearchElement(subject="software")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def software_missing(self, flag):
        """ Specify if "software" should be missing or not. """
        p = FHIRSearchElement(subject="software")
        p.missing = flag
        p.previous = self
        return p
    
    def source(self, reference):
        """ Perform a search for "source" reference. """
        p = FHIRSearchElement(subject="source")
        p.reference = reference
        p.supported_profiles = [
            "ConceptMap",
            "DeviceObservationReport",
            "List",
            "Order",
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def source(self, token):
        """ Perform a search for "source" token. """
        p = FHIRSearchElement(subject="source")
        p.token = token
        p.supported_profiles = [
            "ConceptMap",
            "DeviceObservationReport",
            "List",
            "Order",
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def source_as_text(self, token):
        """ Perform a fulltext search for token "source". """
        p = FHIRSearchElement(subject="source")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def specimen(self, reference):
        """ Perform a search for "specimen" reference. """
        p = FHIRSearchElement(subject="specimen")
        p.reference = reference
        p.supported_profiles = [
            "DiagnosticOrder",
            "DiagnosticReport",
            "Observation"
        ]
        p.previous = self
        return p
    
    def specimen_missing(self, flag):
        """ Specify if "specimen" should be missing or not. """
        p = FHIRSearchElement(subject="specimen")
        p.missing = flag
        p.previous = self
        return p
    
    def stage(self, token):
        """ Perform a search for "stage" token. """
        p = FHIRSearchElement(subject="stage")
        p.token = token
        p.supported_profiles = [
            "Condition"
        ]
        p.previous = self
        return p
    
    def stage_as_text(self, token):
        """ Perform a fulltext search for token "stage". """
        p = FHIRSearchElement(subject="stage")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def stage_missing(self, flag):
        """ Specify if "stage" should be missing or not. """
        p = FHIRSearchElement(subject="stage")
        p.missing = flag
        p.previous = self
        return p
    
    def start(self, date):
        """ Perform a search for "start" date. """
        p = FHIRSearchElement(subject="start")
        p.date = date
        p.supported_profiles = [
            "Provenance"
        ]
        p.previous = self
        return p
    
    def start_missing(self, flag):
        """ Specify if "start" should be missing or not. """
        p = FHIRSearchElement(subject="start")
        p.missing = flag
        p.previous = self
        return p
    
    def status(self, token):
        """ Perform a search for "status" token. """
        p = FHIRSearchElement(subject="status")
        p.token = token
        p.supported_profiles = [
            "AllergyIntolerance",
            "ConceptMap",
            "Condition",
            "Conformance",
            "DiagnosticOrder",
            "DiagnosticReport",
            "DocumentManifest",
            "DocumentReference",
            "Encounter",
            "ImmunizationRecommendation",
            "Location",
            "MedicationAdministration",
            "MedicationDispense",
            "MedicationPrescription",
            "Observation",
            "Profile",
            "Questionnaire",
            "Supply",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def status_as_text(self, token):
        """ Perform a fulltext search for token "status". """
        p = FHIRSearchElement(subject="status")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def status_missing(self, flag):
        """ Specify if "status" should be missing or not. """
        p = FHIRSearchElement(subject="status")
        p.missing = flag
        p.previous = self
        return p
    
    def study(self, token):
        """ Perform a search for "study" token. """
        p = FHIRSearchElement(subject="study")
        p.token = token
        p.supported_profiles = [
            "ImagingStudy"
        ]
        p.previous = self
        return p
    
    def study_as_text(self, token):
        """ Perform a fulltext search for token "study". """
        p = FHIRSearchElement(subject="study")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def study_missing(self, flag):
        """ Specify if "study" should be missing or not. """
        p = FHIRSearchElement(subject="study")
        p.missing = flag
        p.previous = self
        return p
    
    def subject(self, reference):
        """ Perform a search for "subject" reference. """
        p = FHIRSearchElement(subject="subject")
        p.reference = reference
        p.supported_profiles = [
            "AdverseReaction",
            "Alert",
            "AllergyIntolerance",
            "Composition",
            "Condition",
            "DeviceObservationReport",
            "DiagnosticOrder",
            "DiagnosticReport",
            "DocumentManifest",
            "DocumentReference",
            "Encounter",
            "FamilyHistory",
            "ImagingStudy",
            "Immunization",
            "ImmunizationRecommendation",
            "List",
            "Media",
            "Observation",
            "Order",
            "Other",
            "Procedure",
            "Questionnaire",
            "Specimen"
        ]
        p.previous = self
        return p
    
    def subject_missing(self, flag):
        """ Specify if "subject" should be missing or not. """
        p = FHIRSearchElement(subject="subject")
        p.missing = flag
        p.previous = self
        return p
    
    def substance(self, reference):
        """ Perform a search for "substance" reference. """
        p = FHIRSearchElement(subject="substance")
        p.reference = reference
        p.supported_profiles = [
            "AdverseReaction",
            "AllergyIntolerance",
            "Substance"
        ]
        p.previous = self
        return p
    
    def substance_missing(self, flag):
        """ Specify if "substance" should be missing or not. """
        p = FHIRSearchElement(subject="substance")
        p.missing = flag
        p.previous = self
        return p
    
    def subtype(self, token):
        """ Perform a search for "subtype" token. """
        p = FHIRSearchElement(subject="subtype")
        p.token = token
        p.supported_profiles = [
            "Media",
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def subtype_as_text(self, token):
        """ Perform a fulltext search for token "subtype". """
        p = FHIRSearchElement(subject="subtype")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def subtype_missing(self, flag):
        """ Specify if "subtype" should be missing or not. """
        p = FHIRSearchElement(subject="subtype")
        p.missing = flag
        p.previous = self
        return p
    
    def supersedes(self, reference):
        """ Perform a search for "supersedes" reference. """
        p = FHIRSearchElement(subject="supersedes")
        p.reference = reference
        p.supported_profiles = [
            "DocumentManifest"
        ]
        p.previous = self
        return p
    
    def supersedes_missing(self, flag):
        """ Specify if "supersedes" should be missing or not. """
        p = FHIRSearchElement(subject="supersedes")
        p.missing = flag
        p.previous = self
        return p
    
    def supplier(self, reference):
        """ Perform a search for "supplier" reference. """
        p = FHIRSearchElement(subject="supplier")
        p.reference = reference
        p.supported_profiles = [
            "Supply"
        ]
        p.previous = self
        return p
    
    def supplier_missing(self, flag):
        """ Specify if "supplier" should be missing or not. """
        p = FHIRSearchElement(subject="supplier")
        p.missing = flag
        p.previous = self
        return p
    
    def supported_profile(self, reference):
        """ Perform a search for "supported-profile" reference. """
        p = FHIRSearchElement(subject="supported-profile")
        p.reference = reference
        p.supported_profiles = [
            "Conformance"
        ]
        p.previous = self
        return p
    
    def supported_profile_missing(self, flag):
        """ Specify if "supported-profile" should be missing or not. """
        p = FHIRSearchElement(subject="supported-profile")
        p.missing = flag
        p.previous = self
        return p
    
    def support(self, reference):
        """ Perform a search for "support" reference. """
        p = FHIRSearchElement(subject="support")
        p.reference = reference
        p.supported_profiles = [
            "ImmunizationRecommendation"
        ]
        p.previous = self
        return p
    
    def support_missing(self, flag):
        """ Specify if "support" should be missing or not. """
        p = FHIRSearchElement(subject="support")
        p.missing = flag
        p.previous = self
        return p
    
    def symptom(self, token):
        """ Perform a search for "symptom" token. """
        p = FHIRSearchElement(subject="symptom")
        p.token = token
        p.supported_profiles = [
            "AdverseReaction"
        ]
        p.previous = self
        return p
    
    def symptom_as_text(self, token):
        """ Perform a fulltext search for token "symptom". """
        p = FHIRSearchElement(subject="symptom")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def symptom_missing(self, flag):
        """ Specify if "symptom" should be missing or not. """
        p = FHIRSearchElement(subject="symptom")
        p.missing = flag
        p.previous = self
        return p
    
    def system(self, token):
        """ Perform a search for "system" token. """
        p = FHIRSearchElement(subject="system")
        p.token = token
        p.supported_profiles = [
            "ConceptMap",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def system_as_text(self, token):
        """ Perform a fulltext search for token "system". """
        p = FHIRSearchElement(subject="system")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def system_missing(self, flag):
        """ Specify if "system" should be missing or not. """
        p = FHIRSearchElement(subject="system")
        p.missing = flag
        p.previous = self
        return p
    
    def target(self, reference):
        """ Perform a search for "target" reference. """
        p = FHIRSearchElement(subject="target")
        p.reference = reference
        p.supported_profiles = [
            "ConceptMap",
            "Order",
            "Provenance"
        ]
        p.previous = self
        return p
    
    def target_missing(self, flag):
        """ Specify if "target" should be missing or not. """
        p = FHIRSearchElement(subject="target")
        p.missing = flag
        p.previous = self
        return p
    
    def telecom(self, string):
        """ Perform a search for "telecom" string. """
        p = FHIRSearchElement(subject="telecom")
        p.string = string
        p.supported_profiles = [
            "Patient",
            "Practitioner",
            "RelatedPerson"
        ]
        p.previous = self
        return p
    
    def telecom_exact(self, string):
        """ Search for an exact match for "telecom". """
        p = FHIRSearchElement(subject="telecom")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def telecom_missing(self, flag):
        """ Specify if "telecom" should be missing or not. """
        p = FHIRSearchElement(subject="telecom")
        p.missing = flag
        p.previous = self
        return p
    
    def type(self, token):
        """ Perform a search for "type" token. """
        p = FHIRSearchElement(subject="type")
        p.token = token
        p.supported_profiles = [
            "AllergyIntolerance",
            "Composition",
            "Device",
            "DocumentManifest",
            "DocumentReference",
            "Group",
            "Location",
            "Media",
            "MedicationDispense",
            "Organization",
            "Procedure",
            "Profile",
            "SecurityEvent",
            "Substance"
        ]
        p.previous = self
        return p
    
    def type_as_text(self, token):
        """ Perform a fulltext search for token "type". """
        p = FHIRSearchElement(subject="type")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def type_missing(self, flag):
        """ Specify if "type" should be missing or not. """
        p = FHIRSearchElement(subject="type")
        p.missing = flag
        p.previous = self
        return p
    
    def udi(self, string):
        """ Perform a search for "udi" string. """
        p = FHIRSearchElement(subject="udi")
        p.string = string
        p.supported_profiles = [
            "Device"
        ]
        p.previous = self
        return p
    
    def udi_exact(self, string):
        """ Search for an exact match for "udi". """
        p = FHIRSearchElement(subject="udi")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def udi_missing(self, flag):
        """ Specify if "udi" should be missing or not. """
        p = FHIRSearchElement(subject="udi")
        p.missing = flag
        p.previous = self
        return p
    
    def uid(self, token):
        """ Perform a search for "uid" token. """
        p = FHIRSearchElement(subject="uid")
        p.token = token
        p.supported_profiles = [
            "ImagingStudy"
        ]
        p.previous = self
        return p
    
    def uid_as_text(self, token):
        """ Perform a fulltext search for token "uid". """
        p = FHIRSearchElement(subject="uid")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def uid_missing(self, flag):
        """ Specify if "uid" should be missing or not. """
        p = FHIRSearchElement(subject="uid")
        p.missing = flag
        p.previous = self
        return p
    
    def user(self, token):
        """ Perform a search for "user" token. """
        p = FHIRSearchElement(subject="user")
        p.token = token
        p.supported_profiles = [
            "SecurityEvent"
        ]
        p.previous = self
        return p
    
    def user_as_text(self, token):
        """ Perform a fulltext search for token "user". """
        p = FHIRSearchElement(subject="user")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def user_missing(self, flag):
        """ Specify if "user" should be missing or not. """
        p = FHIRSearchElement(subject="user")
        p.missing = flag
        p.previous = self
        return p
    
    def vaccine_type(self, token):
        """ Perform a search for "vaccine-type" token. """
        p = FHIRSearchElement(subject="vaccine-type")
        p.token = token
        p.supported_profiles = [
            "Immunization",
            "ImmunizationRecommendation"
        ]
        p.previous = self
        return p
    
    def vaccine_type_as_text(self, token):
        """ Perform a fulltext search for token "vaccine-type". """
        p = FHIRSearchElement(subject="vaccine-type")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def vaccine_type_missing(self, flag):
        """ Specify if "vaccine-type" should be missing or not. """
        p = FHIRSearchElement(subject="vaccine-type")
        p.missing = flag
        p.previous = self
        return p
    
    def value_concept(self, token):
        """ Perform a search for "value-concept" token. """
        p = FHIRSearchElement(subject="value-concept")
        p.token = token
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def value_concept_as_text(self, token):
        """ Perform a fulltext search for token "value-concept". """
        p = FHIRSearchElement(subject="value-concept")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def value_concept_missing(self, flag):
        """ Specify if "value-concept" should be missing or not. """
        p = FHIRSearchElement(subject="value-concept")
        p.missing = flag
        p.previous = self
        return p
    
    def value_date(self, date):
        """ Perform a search for "value-date" date. """
        p = FHIRSearchElement(subject="value-date")
        p.date = date
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def value_date_missing(self, flag):
        """ Specify if "value-date" should be missing or not. """
        p = FHIRSearchElement(subject="value-date")
        p.missing = flag
        p.previous = self
        return p
    
    def value_quantity(self, quantity):
        """ Perform a search for "value-quantity" quantity. """
        p = FHIRSearchElement(subject="value-quantity")
        p.quantity = quantity
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def value_quantity_missing(self, flag):
        """ Specify if "value-quantity" should be missing or not. """
        p = FHIRSearchElement(subject="value-quantity")
        p.missing = flag
        p.previous = self
        return p
    
    def value_string(self, string):
        """ Perform a search for "value-string" string. """
        p = FHIRSearchElement(subject="value-string")
        p.string = string
        p.supported_profiles = [
            "Observation"
        ]
        p.previous = self
        return p
    
    def value_string_exact(self, string):
        """ Search for an exact match for "value-string". """
        p = FHIRSearchElement(subject="value-string")
        p.string = string
        p.string_exact = True
        p.previous = self
        return p
    
    def value_string_missing(self, flag):
        """ Specify if "value-string" should be missing or not. """
        p = FHIRSearchElement(subject="value-string")
        p.missing = flag
        p.previous = self
        return p
    
    def valueset(self, reference):
        """ Perform a search for "valueset" reference. """
        p = FHIRSearchElement(subject="valueset")
        p.reference = reference
        p.supported_profiles = [
            "Profile"
        ]
        p.previous = self
        return p
    
    def valueset_missing(self, flag):
        """ Specify if "valueset" should be missing or not. """
        p = FHIRSearchElement(subject="valueset")
        p.missing = flag
        p.previous = self
        return p
    
    def value(self, token):
        """ Perform a search for "value" token. """
        p = FHIRSearchElement(subject="value")
        p.token = token
        p.supported_profiles = [
            "Group"
        ]
        p.previous = self
        return p
    
    def value_as_text(self, token):
        """ Perform a fulltext search for token "value". """
        p = FHIRSearchElement(subject="value")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def value_missing(self, flag):
        """ Specify if "value" should be missing or not. """
        p = FHIRSearchElement(subject="value")
        p.missing = flag
        p.previous = self
        return p
    
    def version(self, token):
        """ Perform a search for "version" token. """
        p = FHIRSearchElement(subject="version")
        p.token = token
        p.supported_profiles = [
            "ConceptMap",
            "Conformance",
            "Profile",
            "ValueSet"
        ]
        p.previous = self
        return p
    
    def version_as_text(self, token):
        """ Perform a fulltext search for token "version". """
        p = FHIRSearchElement(subject="version")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def version_missing(self, flag):
        """ Specify if "version" should be missing or not. """
        p = FHIRSearchElement(subject="version")
        p.missing = flag
        p.previous = self
        return p
    
    def view(self, token):
        """ Perform a search for "view" token. """
        p = FHIRSearchElement(subject="view")
        p.token = token
        p.supported_profiles = [
            "Media"
        ]
        p.previous = self
        return p
    
    def view_as_text(self, token):
        """ Perform a fulltext search for token "view". """
        p = FHIRSearchElement(subject="view")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def view_missing(self, flag):
        """ Specify if "view" should be missing or not. """
        p = FHIRSearchElement(subject="view")
        p.missing = flag
        p.previous = self
        return p
    
    def when_code(self, token):
        """ Perform a search for "when_code" token. """
        p = FHIRSearchElement(subject="when_code")
        p.token = token
        p.supported_profiles = [
            "Order"
        ]
        p.previous = self
        return p
    
    def when_code_as_text(self, token):
        """ Perform a fulltext search for token "when_code". """
        p = FHIRSearchElement(subject="when_code")
        p.token = token
        p.token_as_text = True
        p.previous = self
        return p
    
    def when_code_missing(self, flag):
        """ Specify if "when_code" should be missing or not. """
        p = FHIRSearchElement(subject="when_code")
        p.missing = flag
        p.previous = self
        return p
    
    def when_given(self, date):
        """ Perform a search for "when-given" date. """
        p = FHIRSearchElement(subject="when-given")
        p.date = date
        p.supported_profiles = [
            "MedicationStatement"
        ]
        p.previous = self
        return p
    
    def when_given_missing(self, flag):
        """ Specify if "when-given" should be missing or not. """
        p = FHIRSearchElement(subject="when-given")
        p.missing = flag
        p.previous = self
        return p
    
    def whengiven(self, date):
        """ Perform a search for "whengiven" date. """
        p = FHIRSearchElement(subject="whengiven")
        p.date = date
        p.supported_profiles = [
            "MedicationAdministration"
        ]
        p.previous = self
        return p
    
    def whengiven_missing(self, flag):
        """ Specify if "whengiven" should be missing or not. """
        p = FHIRSearchElement(subject="whengiven")
        p.missing = flag
        p.previous = self
        return p
    
    def whenhandedover(self, date):
        """ Perform a search for "whenhandedover" date. """
        p = FHIRSearchElement(subject="whenhandedover")
        p.date = date
        p.supported_profiles = [
            "MedicationDispense"
        ]
        p.previous = self
        return p
    
    def whenhandedover_missing(self, flag):
        """ Specify if "whenhandedover" should be missing or not. """
        p = FHIRSearchElement(subject="whenhandedover")
        p.missing = flag
        p.previous = self
        return p
    
    def whenprepared(self, date):
        """ Perform a search for "whenprepared" date. """
        p = FHIRSearchElement(subject="whenprepared")
        p.date = date
        p.supported_profiles = [
            "MedicationDispense"
        ]
        p.previous = self
        return p
    
    def whenprepared_missing(self, flag):
        """ Specify if "whenprepared" should be missing or not. """
        p = FHIRSearchElement(subject="whenprepared")
        p.missing = flag
        p.previous = self
        return p
    
    def when(self, date):
        """ Perform a search for "when" date. """
        p = FHIRSearchElement(subject="when")
        p.date = date
        p.supported_profiles = [
            "Order"
        ]
        p.previous = self
        return p
    
    def when_missing(self, flag):
        """ Specify if "when" should be missing or not. """
        p = FHIRSearchElement(subject="when")
        p.missing = flag
        p.previous = self
        return p
    
    def who(self, reference):
        """ Perform a search for "who" reference. """
        p = FHIRSearchElement(subject="who")
        p.reference = reference
        p.supported_profiles = [
            "OrderResponse"
        ]
        p.previous = self
        return p
    
    def who_missing(self, flag):
        """ Specify if "who" should be missing or not. """
        p = FHIRSearchElement(subject="who")
        p.missing = flag
        p.previous = self
        return p
    


# some tests, to be removed after development phase
if '__main__' == __name__:
    from patient import Patient
    print('1 '+Patient.where().name("Willis").name_exact("Bruce").construct())
    print('= Patient?name=Willis&name:exact=Bruce')
    print('')
    print('2 '+Patient.where().address("Boston").gender('male').given_exact("Willis").construct())
    print('= Patient?address=Boston&gender=male&given:exact=Willis')
