#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Subclassing FHIR's reference to add resolving capabilities

import logging
from . import reference


class FHIRReference(reference.Reference):
    """ Subclassing FHIR's `Reference` resource to add resolving capabilities.
    """
    
    def resolved(self, klass):
        """ Resolves the reference and caches the result, returning instance(s)
        of the referenced classes.
        
        :param klass: The expected class of the resource
        :returns: An instance (or list thereof) of the resolved reference if
            dereferencing was successful, `None` otherwise
        """
        owning_resource = self.owningResource()
        if owning_resource is None:
            raise Exception("Cannot resolve reference without having an owner (which must be a `DomainResource`)")
        if klass is None:
            raise Exception("Cannot resolve reference without knowing the class")
        
        refid = self.processedReferenceIdentifier()
        if not refid:
            logging.warning("No `reference` set, cannot resolve")
            return None
        
        resolved = owning_resource.resolvedReference(refid)
        if resolved is not None:
            if isinstance(resolved, klass):
                return resolved
            logging.warning("Referenced resource {} is not a {} but a {}".format(refid, klass, resolved.__class__))
            return None
        
        # not yet resolved, see if it's a contained resource
        if owning_resource.contained is not None:
            for contained in owning_resource.contained:
                if contained.id == refid:
                    owning_resource.didResolveReference(refid, contained)
                    if isinstance(contained, klass):
                        return contained
                    logging.warning("Contained resource {} is not a {} but a {}".format(refid, klass, contained.__class__))
                    return None
        
        # fetch remote resources
        if '://' not in self.reference:
            server = owning_resource.server() if owning_resource else None
            if server is not None:
                return self._referenced_class.read_from(self.reference, server)
            
            logging.warning("Reference owner {} does not have a server, cannot resolve relative reference {}"
                .format(self._owner, self.reference))
            return None
        
        # absolute resource
        logging.warning("Not implemented: resolving absolute reference to resource {}"
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
    
