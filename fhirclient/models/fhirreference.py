#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Subclassing FHIR's reference to add resolving capabilities

import logging
from . import reference

logger = logging.getLogger(__name__)


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
            logger.warning("No `reference` set, cannot resolve")
            return None
        
        # already resolved and cached?
        resolved = owning_resource.resolvedReference(refid)
        if resolved is not None:
            if isinstance(resolved, klass):
                return resolved
            logger.warning("Referenced resource {} is not a {} but a {}".format(refid, klass, resolved.__class__))
            return None
        
        # not yet resolved, see if it's a contained resource
        if owning_resource.contained is not None:
            for contained in owning_resource.contained:
                if contained.id == refid:
                    owning_resource.didResolveReference(refid, contained)
                    if isinstance(contained, klass):
                        return contained
                    logger.warning("Contained resource {} is not a {} but a {}".format(refid, klass, contained.__class__))
                    return None
        
        # are we in a bundle?
        ref_is_relative = '://' not in self.reference and 'urn:' != self.reference[:4]
        bundle = self.owningBundle()
        while bundle is not None:
            if bundle.entry is not None:
                fullUrl = self.reference
                if ref_is_relative:
                    base = bundle.server.base_uri if bundle.server else ''
                    fullUrl = base + self.reference
                
                for entry in bundle.entry:
                    if entry.fullUrl == fullUrl:
                        found = entry.resource
                        if isinstance(found, klass):
                            return found
                        logger.warning("Bundled resource {} is not a {} but a {}".format(refid, klass, found.__class__))
                        return None
            bundle = bundle.owningBundle()
        
        # relative references, use the same server
        server = None
        if ref_is_relative:
            server = owning_resource.server if owning_resource else None
        
        # TODO: instantiate server for absolute resource
        if server is None:
            logger.warning("Not implemented: resolving absolute reference to resource {}"
                .format(self.reference))
            return None
        
        # fetch remote resource; unable to verify klass since we use klass.read_from()
        relative = klass.read_from(self.reference, server)
        owning_resource.didResolveReference(refid, relative)
        return relative
    
    def processedReferenceIdentifier(self):
        """ Normalizes the reference-id.
        """
        if self.reference and '#' == self.reference[0]:
            return self.reference[1:]
        return self.reference

