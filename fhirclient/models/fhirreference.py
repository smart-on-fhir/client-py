#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Subclassing FHIR's reference to add resolving capabilities

import logging
from . import reference


class FHIRReference(reference.Reference):
    """ Subclassing FHIR's resource reference to add resolving capabilities.
    """
    
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
            contained.owner.didResolveReference(refid, instance)
            return instance
        
        # fetch remote resources
        server = self._owner.server()
        if server is None:
            logging.warning("Reference owner {} does not have a server, cannot resolve reference {}"
                .format(self._owner, self.reference))
            return None
        
        if '://' not in self.reference:
            return self._referenced_class.read_from(self.reference, server)
        
        logging.warning("Not implemented: resolving reference to foreign resource {}"
            .format(self.reference))
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
    
