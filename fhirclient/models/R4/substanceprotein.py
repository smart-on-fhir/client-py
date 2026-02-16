# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceProtein).
# 2024, SMART Health IT.


from . import domainresource

class SubstanceProtein(domainresource.DomainResource):
    """ A SubstanceProtein is defined as a single unit of a linear amino acid
    sequence, or a combination of subunits that are either covalently linked or
    have a defined invariant stoichiometric relationship. This includes all
    synthetic, recombinant and purified SubstanceProteins of defined sequence,
    whether the use is therapeutic or prophylactic. This set of elements will
    be used to describe albumins, coagulation factors, cytokines, growth
    factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids,
    recombinant vaccines, and immunomodulators.
    """
    
    resource_type = "SubstanceProtein"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.disulfideLinkage = None
        """ The disulphide bond between two cysteine residues either on the
        same subunit or on two different subunits shall be described. The
        position of the disulfide bonds in the SubstanceProtein shall be
        listed in increasing order of subunit number and position within
        subunit followed by the abbreviation of the amino acids involved.
        The disulfide linkage positions shall actually contain the amino
        acid Cysteine at the respective positions.
        List of `str` items. """
        
        self.numberOfSubunits = None
        """ Number of linear sequences of amino acids linked through peptide
        bonds. The number of subunits constituting the SubstanceProtein
        shall be described. It is possible that the number of subunits can
        be variable.
        Type `int`. """
        
        self.sequenceType = None
        """ The SubstanceProtein descriptive elements will only be used when a
        complete or partial amino acid sequence is available or derivable
        from a nucleic acid sequence.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subunit = None
        """ This subclause refers to the description of each subunit
        constituting the SubstanceProtein. A subunit is a linear sequence
        of amino acids linked through peptide bonds. The Subunit
        information shall be provided when the finished SubstanceProtein is
        a complex of multiple sequences; subunits are not used to delineate
        domains within a single sequence. Subunits are listed in order of
        decreasing length; sequences of the same length will be ordered by
        decreasing molecular weight; subunits that have identical sequences
        will be repeated multiple times.
        List of `SubstanceProteinSubunit` items (represented as `dict` in JSON). """
        
        super(SubstanceProtein, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceProtein, self).elementProperties()
        js.extend([
            ("disulfideLinkage", "disulfideLinkage", str, True, None, False),
            ("numberOfSubunits", "numberOfSubunits", int, False, None, False),
            ("sequenceType", "sequenceType", codeableconcept.CodeableConcept, False, None, False),
            ("subunit", "subunit", SubstanceProteinSubunit, True, None, False),
        ])
        return js


from . import backboneelement

class SubstanceProteinSubunit(backboneelement.BackboneElement):
    """ This subclause refers to the description of each subunit constituting the
    SubstanceProtein. A subunit is a linear sequence of amino acids linked
    through peptide bonds. The Subunit information shall be provided when the
    finished SubstanceProtein is a complex of multiple sequences; subunits are
    not used to delineate domains within a single sequence. Subunits are listed
    in order of decreasing length; sequences of the same length will be ordered
    by decreasing molecular weight; subunits that have identical sequences will
    be repeated multiple times.
    """
    
    resource_type = "SubstanceProteinSubunit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cTerminalModification = None
        """ The modification at the C-terminal shall be specified.
        Type `str`. """
        
        self.cTerminalModificationId = None
        """ Unique identifier for molecular fragment modification based on the
        ISO 11238 Substance ID.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.length = None
        """ Length of linear sequences of amino acids contained in the subunit.
        Type `int`. """
        
        self.nTerminalModification = None
        """ The name of the fragment modified at the N-terminal of the
        SubstanceProtein shall be specified.
        Type `str`. """
        
        self.nTerminalModificationId = None
        """ Unique identifier for molecular fragment modification based on the
        ISO 11238 Substance ID.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ The sequence information shall be provided enumerating the amino
        acids from N- to C-terminal end using standard single-letter amino
        acid codes. Uppercase shall be used for L-amino acids and lowercase
        for D-amino acids. Transcribed SubstanceProteins will always be
        described using the translated sequence; for synthetic peptide
        containing amino acids that are not represented with a single
        letter code an X should be used within the sequence. The modified
        amino acids will be distinguished by their position in the sequence.
        Type `str`. """
        
        self.sequenceAttachment = None
        """ The sequence information shall be provided enumerating the amino
        acids from N- to C-terminal end using standard single-letter amino
        acid codes. Uppercase shall be used for L-amino acids and lowercase
        for D-amino acids. Transcribed SubstanceProteins will always be
        described using the translated sequence; for synthetic peptide
        containing amino acids that are not represented with a single
        letter code an X should be used within the sequence. The modified
        amino acids will be distinguished by their position in the sequence.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.subunit = None
        """ Index of primary sequences of amino acids linked through peptide
        bonds in order of decreasing length. Sequences of the same length
        will be ordered by molecular weight. Subunits that have identical
        sequences will be repeated and have sequential subscripts.
        Type `int`. """
        
        super(SubstanceProteinSubunit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceProteinSubunit, self).elementProperties()
        js.extend([
            ("cTerminalModification", "cTerminalModification", str, False, None, False),
            ("cTerminalModificationId", "cTerminalModificationId", identifier.Identifier, False, None, False),
            ("length", "length", int, False, None, False),
            ("nTerminalModification", "nTerminalModification", str, False, None, False),
            ("nTerminalModificationId", "nTerminalModificationId", identifier.Identifier, False, None, False),
            ("sequence", "sequence", str, False, None, False),
            ("sequenceAttachment", "sequenceAttachment", attachment.Attachment, False, None, False),
            ("subunit", "subunit", int, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import identifier
