#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Subclassing FHIR's resource reference to add resolving capabilities

import logging
import resourcereference


class FHIRReference(resourcereference.ResourceReference):
    """ Subclassing FHIR's resource reference to add resolving capabilities.
    """
    
    def __init__(self, jsondict=None):
        self._owner = None
        self._referenced_class = None
        super(FHIRReference, self).__init__(jsondict)
    
    @classmethod
    def with_json_and_owner(cls, jsonobj, owner, klass):
        """ Takes the owning parent and the class the reference is referencing.
        Forwards to `with_json()`.
        
        :param dict jsonobj: Decoded JSON dictionary
        :param FHIRElement owner: The reference owning parent
        :param klass: The class the reference is representing; must be a
            FHIRElement subclass!
        :returns: An instance or a list of instances created from JSON data
        """
        instance = cls.with_json(jsonobj)
        if list == type(instance):
            for inst in instance:
                inst._owner = owner
                inst._referenced_class = klass
        else:
            instance._owner = owner
            instance._referenced_class = klass
        
        return instance
    
    
    # MARK: Reference Resolving
    
    @property
    def resolved(self):
        """ Resolves the reference and caches the result, returning instance(s)
        of the referenced classes.
        
        :returns: An instance (or list thereof) of the resolved reference if
            dereferencing was successful, `None` otherwise
        """
        if self._owner is None:
            raise Exception("Cannot resolve reference without having an owner")
        if self._referenced_class is None:
            raise Exception("Cannot resolve reference without having `_referenced_class` set")
        
        refid = self.processedReferenceIdentifier()
        if not refid:
            logging.warning("No `reference` set, cannot resolve")
            return None
        
        resolved = self._owner.resolvedReference(refid)
        if resolved is not None:
            return resolved
        
        # not yet resolved, see if it's a contained resource
        contained = self._owner.containedReference(refid)
        if contained is not None:
            instance = self._referenced_class(jsondict=contained.json)
            self._owner.didResolveReference(refid, instance)
            return instance
        
        # TODO: fetch remote resources
        return None
    
    def processedReferenceIdentifier(self):
        """ Normalizes the reference-id.
        """
        if not self.reference:
            return None
        
        if '#' == self.reference[0]:
            return self.reference[1:]
        
        # TODO: distinguish absolute (has "://") and relative URLs
        return None
    
