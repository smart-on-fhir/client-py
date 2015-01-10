#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Subclassing FHIR's reference to add resolving capabilities

import logging
import reference


class FHIRReference(reference.Reference):
    """ Subclassing FHIR's resource reference to add resolving capabilities.
    """
    
    @property
    def resolved(self, klass):
        """ Resolves the reference and caches the result, returning instance(s)
        of the referenced classes.
        
        :returns: An instance (or list thereof) of the resolved reference if
            dereferencing was successful, `None` otherwise
        """
        if self._owner is None:
            raise Exception("Cannot resolve reference without having an owner")
        if klass is None:
            raise Exception("Cannot resolve reference without knowing the class")
        
        refid = self.processedReferenceIdentifier()
        if not refid:
            logging.warning("No `reference` set, cannot resolve")
            return None
        
        resolved = self._owner.resolvedReference(refid)
        if resolved is not None:
            if isinstance(resolved, klass):
                return resolved
            logging.warning("Reference {} is not a {} but a {}".format(refid, klass, resolved.__class__))
            return None
        
        # not yet resolved, see if it's a contained resource
        contained = self._owner.containedReference(refid)
        if contained is not None:
            instance = klass(jsondict=contained.json)
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
    
