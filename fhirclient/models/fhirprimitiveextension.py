from . import backboneelement, extension


class FHIRPrimitiveExtension(backboneelement.BackboneElement):
    """A special kind of FHIR extension which can be used to extend primitives.
    """

    def __init__(self, jsondict=None, strict=True):
        self.extension = None
        """ The extension value(s).
        List of `Extension` items (represented as `list[dict]` in JSON). """

        super(FHIRPrimitiveExtension, self).__init__(jsondict=jsondict,
                                                     strict=strict)

    def elementProperties(self):
        js = super(FHIRPrimitiveExtension, self).elementProperties()
        js.extend([
            ("extension", "extension", extension.Extension, True, None, False),
        ])
        return js
