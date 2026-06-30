from __future__ import annotations

from pydantic import Field, PositiveInt

from .acquisition import AcquisitionAuthoriser, AcquisitionFundingSource, OriginalObjectPurchasePrice
from .common import ControlledTerm, MDSModel, OneOrMany
from .date import Date, DateStringISO
from .dimension import Dimension
from .inscription_content import InscriptionContent
from .license import License
from .location import Location
from .material import Material
from .organisation import Organisation
from .people import People
from .person import Person
from .place import Place
from .reference import Reference
from .technique import Technique


class Object(MDSModel):
    accession_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which an object formally enters the collections and is recorded in the accessions "
        "register.",
    )
    acquisition_authoriser: OneOrMany[AcquisitionAuthoriser | str] = Field(
        None,
        description="The Person giving final approval for the acquisition to proceed.",
    )
    acquisition_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which title to an object or group of objects is transferred to the organisation.",
    )
    acquisition_funding_source: OneOrMany[AcquisitionFundingSource | str] = Field(
        None,
        description="The Person or Organisation from whom the Acquisition funding was obtained.",
    )
    acquisition_method: OneOrMany[ControlledTerm] = Field(
        None,
        description="The means by which title to an object is formally transferred to the organisation.",
    )
    acquisition_note: OneOrMany[str] = Field(
        None,
        description="General information about the acquisition.",
    )
    acquisition_provisos: OneOrMany[str] = Field(
        None,
        description="Restrictions applying to the objects in a single acquisition, including conditions for "
        "deposition of archaeological archives.",
    )
    acquisition_reason: OneOrMany[str] = Field(
        None,
        description="The reason or justification for an acquisition.",
    )
    acquisition_reference_number: OneOrMany[str] = Field(
        None,
        description="A unique identifying number for information on the acquisition of an object or group of objects. "
        "It should serve as the reference to written documentation of a valuation. This will normally be the "
        "object number.",
    )
    acquisition_source: OneOrMany[Organisation | People | Person | str] = Field(
        None,
        description="The People, Person or Organisation from whom an object was obtained, if different from the "
        "Owner. The Acquisition source may be an agent or other intermediary between the acquiring organisation "
        "and the Owner. For archaeological archives, use Acquisition source to record the excavating body "
        "responsible for preparing and depositing the archive with the organisation.",
    )
    age: OneOrMany[PositiveInt] = Field(
        None,
        description="The numeric age of a natural science specimen when it died. Use Age unit to describe the unit "
        "of measurement used and Age qualifier to qualify the information. Use Phase for a textual description "
        "of Age.",
    )
    age_qualifier: OneOrMany[ControlledTerm] = Field(
        None,
        description="A qualification of the statement of the Age of a natural science specimen.",
    )
    age_unit: OneOrMany[str] = Field(
        None,
        description="The unit of measurement used to describe the Age of a natural science specimen.",
    )
    associated_activity: OneOrMany[ControlledTerm] = Field(
        None,
        description="An activity associated with an object or group of objects.",
    )
    associated_concept: OneOrMany[str] = Field(
        None,
        description="A concept associated with an object or group of objects.",
    )
    associated_cultural_affinity: OneOrMany[ControlledTerm] = Field(
        None,
        description="A wider cultural context to which an object or group of objects relates.",
    )
    associated_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="A date associated with an object or group of objects.",
    )
    associated_event_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date of an event in an object's history.",
    )
    associated_event_name: OneOrMany[AssociatedEventName | str] = Field(
        None,
        description="An historical event associated with an object or group of objects, not including production and "
        "collections management events. Use the Object history note to describe details about the nature of the "
        "association.",
    )
    associated_event_organisation: OneOrMany[Organisation | str] = Field(
        None,
        description="An Organisation associated with an event in an object's or group of objects' history (other "
        "than field collection or ownership).",
    )
    associated_event_people: OneOrMany[People | str] = Field(
        None,
        description="A people associated with an event in an object's or group of objects' history (other than field "
        "collection or ownership).",
    )
    associated_event_person: OneOrMany[Person | str] = Field(
        None,
        description="A person associated with an event in an object's or group of objects' history (other than field "
        "collection or ownership).",
    )
    associated_event_place: OneOrMany[Place | str] = Field(
        None,
        description="A place associated with an event in an object's history.",
    )
    associated_object: OneOrMany[ControlledTerm] = Field(
        None,
        description="An object associated with an object or group of objects.",
    )
    associated_object_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="A term describing the nature of the Associated object.",
    )
    associated_organisation: OneOrMany[Organisation | str] = Field(
        None,
        description="An Organisation associated with an object's or group of objects' history.",
    )
    associated_people: OneOrMany[People | str] = Field(
        None,
        description="A people associated with an object's or group of objects' history.",
    )
    associated_person: OneOrMany[Person | str] = Field(
        None,
        description="A person associated with an object's or group of objects' history.",
    )
    associated_place: OneOrMany[Place | str] = Field(
        None,
        description="A place associated with an object or group of objects.",
    )
    association_note: OneOrMany[str] = Field(
        None,
        description="A narrative description of the nature of the association of an organisation, people, person or "
        "place, with the object being recorded (eg design influences and design impact).",
    )
    association_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The way in which the person/group, date, object, concept, event, activity or place is associated "
        "with the history of an object or specimen.",
    )
    brief_description: OneOrMany[str] = Field(
        None,
        description="A text description of an object in approximately one sentence; normally used for administrative "
        "and identification purposes. It records the most important information from a number of separate "
        "descriptive units of information.",
    )
    collections_review_result: OneOrMany[ControlledTerm] = Field(
        None,
        description="The result of a collections review for an object or group of objects for a Collections review "
        "criterion.",
    )
    colour: OneOrMany[ControlledTerm] = Field(
        None,
        description="The colour of an object.",
    )
    comments: OneOrMany[str] = Field(
        None,
        description="Additional comments made about an object by visitors, curators or researchers.",
    )
    completeness: OneOrMany[Completeness | str] = Field(
        None,
        description="A single term describing the completeness of an object.",
    )
    condition: OneOrMany[Condition | str] = Field(
        None,
        description="A single term describing the condition of an object.",
    )
    condition_check_assessment_method: OneOrMany[ControlledTerm] = Field(
        None,
        description="The method used when carrying out a condition check or technical assessment process.",
    )
    condition_check_assessment_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date(s) on which a condition check or technical assessment process took place.",
    )
    condition_check_assessment_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the condition checking or technical assessment process which has "
        "not been recorded elsewhere using controlled terminology.",
    )
    condition_check_assessment_reason: OneOrMany[ControlledTerm] = Field(
        None,
        description="The reason for a condition check or technical assessment process taking place.",
    )
    condition_check_assessment_reference_number: OneOrMany[str] = Field(
        None,
        description="A unique identifying number for the condition checking or technical assessment process. It "
        "should serve as the reference to written documentation of a condition check or technical assessment.",
    )
    condition_checker_assessor: OneOrMany[Organisation | Person | str] = Field(
        None,
        description="The Person or Organisation which carried out a condition check or technical assessment process.",
    )
    conservation_authoriser: OneOrMany[ConservationAuthoriser | str] = Field(
        None,
        description="The Person giving final approval for a conservation job to take place.",
    )
    conservation_material: OneOrMany[Material | str] = Field(
        None,
        description="The materials used in the conservation of an object.",
    )
    conservation_method: OneOrMany[ControlledTerm] = Field(
        None,
        description="The method used in the conservation of an object.",
    )
    conservation_note: OneOrMany[str] = Field(
        None,
        description="Additional information about conservation of an object, or group of objects, which has not been "
        "recorded elsewhere using controlled terminology.",
    )
    conservation_reference_number: OneOrMany[str] = Field(
        None,
        description="A unique identifying number for the conservation of an object or group of objects. It should "
        "serve as the reference to written documentation of conservation.",
    )
    conservator: OneOrMany[Organisation | Person | str] = Field(
        None,
        description="The Person or Organisation treating an object.",
    )
    content_activity: OneOrMany[ControlledTerm] = Field(
        None,
        description="An activity depicted in or described by an object.",
    )
    content_concept: OneOrMany[ControlledTerm] = Field(
        None,
        description="A concept depicted in or described by an object.",
    )
    content_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="A date depicted in or described by an object.",
    )
    content_description: OneOrMany[str] = Field(
        None,
        description="A general description of a depiction in an object, or description of an object without making "
        "interpretation. This may include descriptions of the content of all audio and visual works. Use Brief "
        "description and Physical description to describe an object's other features.",
    )
    content_event_name: OneOrMany[ContentEventName | str] = Field(
        None,
        description="An event depicted on or described by an object.",
    )
    content_language: OneOrMany[ControlledTerm] = Field(
        None,
        description="The language of the textual content of an object.",
    )
    content_note: OneOrMany[str] = Field(
        None,
        description="Additional information about an object's content which has not been recorded elsewhere using "
        "controlled terminology.",
    )
    content_object: OneOrMany[ContentObject | str] = Field(
        None,
        description="An object depicted in or described by another object.",
    )
    content_object_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="A term describing the nature of the Content - object.",
    )
    content_organisation: OneOrMany[Organisation | str] = Field(
        None,
        description="The Organisation depicted in or described in an object.",
    )
    content_other: OneOrMany[str] = Field(
        None,
        description="An aspect of the content depicted in or described in an object, not covered by the other "
        "content units.",
    )
    content_other_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The type of aspect being recorded by Content - other.",  # FIXME: Already nested in Spectrum docs
    )
    content_people: OneOrMany[People | str] = Field(
        None,
        description="A People depicted in or described by an object.",
    )
    content_person: OneOrMany[Person | str] = Field(
        None,
        description="A Person depicted in or described by an object.",
    )
    content_place: OneOrMany[Place | str] = Field(
        None,
        description="A Place depicted in or described by an object.",
    )
    content_position: OneOrMany[ControlledTerm] = Field(
        None,
        description="The position on an object of a depiction or description.",
    )
    content_script: OneOrMany[ControlledTerm] = Field(
        None,
        description="The script the textual content of an object.",
    )
    copy_number: OneOrMany[str] = Field(
        None,
        description="A number assigned to an object by the maker within a limited edition or special run.",
    )
    credit_line: OneOrMany[str] = Field(
        None,
        description="Text acknowledging a donation or loan, normally used on a display label.",
    )
    current_location: OneOrMany[CurrentLocation | str] = Field(
        None,
        description="The place within the organisation where an object is currently located.",
    )
    current_reproduction_location: OneOrMany[Location | str] = Field(
        None,
        description="The current location of a reproduction.",
    )
    deaccession_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date when an item was struck off the accession register.",
    )
    dimension: OneOrMany[Dimension | str] = Field(
        None,
        description="The aspect of a part or component of an object being measured.",
    )
    disposal_authoriser: OneOrMany[DisposalAuthoriser | str] = Field(
        None,
        description="The Person giving final approval for a disposal to take place.",
    )
    disposal_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date an object is disposed of.",
    )
    disposal_method: OneOrMany[ControlledTerm] = Field(
        None,
        description="The way in which an object is disposed of.",
    )
    disposal_new_object_number: OneOrMany[str] = Field(
        None,
        description="The object number assigned to a deaccessioned object by the recipient.",
    )
    disposal_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the disposal of an object which has not been recorded elsewhere "
        "using controlled terminology.",
    )
    disposal_price: OneOrMany[str] = Field(
        None,
        description="The total price paid for an object when disposed of through sale. Associated with the Object "
        "number. If no individual prices are known for specific objects in the group, use Group disposal price.",
    )
    disposal_provisos: OneOrMany[str] = Field(
        None,
        description="Restrictions applying to all the objects to be disposed of.",
    )
    disposal_reason: OneOrMany[str] = Field(
        None,
        description="The reason or justification for an object or objects being disposed of.",
    )
    disposal_recipient: OneOrMany[Organisation | People | Person | str] = Field(
        None,
        description="The People, Person or Organisation receiving an object to be disposed of by way of transfer, "
        "gift or sale.",
    )
    disposal_reference_number: OneOrMany[str] = Field(
        None,
        description="The unique number assigned to the disposal of an object or group of objects. The number should "
        "also refer to a file containing all written documentation about the disposal.",
    )
    distinguishing_features: OneOrMany[str] = Field(
        None,
        description="A description of features which could uniquely identify an object, bringing together details "
        "from other groups of units of information such as identification, inscription, and condition which could "
        "in a sentence uniquely identify an object.",
    )
    edition_number: OneOrMany[str] = Field(
        None,
        description="A number assigned to a group of objects produced at the same time by the maker.",
    )
    entry_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date on which an object or group of objects enters the organisation.",
    )
    entry_method: OneOrMany[ControlledTerm] = Field(
        None,
        description="The method by which an object or group of objects is deposited.",
    )
    entry_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the deposit of an object which has not been recorded elsewhere "
        "using controlled terminology.",
    )
    entry_number: OneOrMany[str] = Field(
        None,
        description="A unique number assigned to the entry of an object or group of objects and used to track objects "
        "prior to their return or acquisition. It should serve as the reference to written documentation of "
        "objects entering the organisation for the first time. The number should be the one assigned to an entry "
        "form or receipt.",
    )
    entry_reason: OneOrMany[ControlledTerm] = Field(
        None,
        description="The reason for an object or group of objects physically entering the organisation.",
    )
    field_collection_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date an object is collected in the field.",
    )
    field_collection_event_name: OneOrMany[str] = Field(
        None,
        description="The name of an event at which an object was collected.",
    )
    field_collection_method: OneOrMany[str] = Field(
        None,
        description="The method used to excavate or collect an object in the field.",
    )
    field_collection_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the place or method of field collection or excavation.",
    )
    field_collection_number: OneOrMany[str] = Field(
        None,
        description="A number or code assigned to an object collected in the field before an Entry number or Object "
        "number is assigned.",
    )
    field_collection_place: OneOrMany[Place | str] = Field(
        None,
        description="The place where an object was excavated or collected in the field.",
    )
    field_collection_source: OneOrMany[Organisation | People | Person | str] = Field(
        None,
        description="The social, socio-professional, or ethnic groups from which an object was collected or bought. "
        "May be different from the group of production and/or the group use.",
    )
    field_collector: OneOrMany[Organisation | Person | str] = Field(
        None,
        description="The Person or Organisation responsible for collecting a specimen or object in the field.",
    )
    form: OneOrMany[ControlledTerm] = Field(
        None,
        description="The method used to mount or preserve a specimen.",
    )
    geological_complex_name: OneOrMany[str] = Field(
        None,
        description="The name of a geological complex from which a geological specimen was collected.",
    )
    group_disposal_price: OneOrMany[str] = Field(
        None,
        description="The total price paid for a group of objects at disposal including taxes for which the purchase "
        "is liable. If individual prices are known for specific objects in the group, use Disposal price.",
    )
    group_purchase_price: OneOrMany[str] = Field(
        None,
        description="The total price paid for a group of objects at acquisition, including taxes for which the "
        "purchase is liable. If individual prices are known for specific objects in the group, use Object "
        "acquisition price.",
    )
    habitat: OneOrMany[str] = Field(
        None,
        description="A term describing the surroundings and environment of the area where a specimen was collected in "
        "the field.",
    )
    habitat_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the habitat of an object which has not been recorded elsewhere "
        "using controlled terminology.",
    )
    hazard: OneOrMany[Hazard | str] = Field(
        None,
        description="Details of potential hazards to people or other objects that the handling and storing of an "
        "object can present.",
    )
    inscription_content: OneOrMany[InscriptionContent | str] = Field(
        None,
        description="The text inscribed as part of the decoration or construction of an object recorded in the "
        "original language.",
    )
    license: License = Field(..., alias="ciim/license")
    loan_in_status: OneOrMany[ControlledTerm] = Field(
        None,
        description="The status of the process of carrying out a loan in (borrowing) event.",
    )
    material: OneOrMany[Material | str] = Field(
        None,
        description="The basic materials and media from which an object is constructed.",
    )
    normal_location: OneOrMany[Location | str] = Field(
        None,
        description="The place within the organisation where an object is normally located.",
    )
    number_of_objects: OneOrMany[PositiveInt] = Field(
        None,
        description="A record of the number of objects at the next level down in an object record.",
    )
    object_component_name: OneOrMany[ObjectComponentName | str] = Field(
        None,
        description="The non-separable part or component of an object which is being described.",
    )
    object_history_note: OneOrMany[str] = Field(
        None,
        description="The history of an object, including its creation, owners, vendors and the circumstances "
        "surrounding such events. Record information here which has not been recorded elsewhere using controlled "
        "terminology.",
    )
    object_name: list[ObjectName | str] | ObjectName | str = Field(
        ...,
        description="A description of the form, function or type of object.",
    )
    object_number: list[str] | str = Field(
        ...,
        description="A unique number identifying an object or specimens, including any separated parts.",
    )
    object_offer_price: OneOrMany[str] = Field(
        None,
        description="The price at which an object is offered for sale to the organisation.",
    )
    object_production_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date when a stage in the design, creation or manufacture of an object took place.",
    )
    object_production_note: OneOrMany[str] = Field(
        None,
        description="Additional information about an object's production.",
    )
    object_production_organisation: OneOrMany[Organisation | str] = Field(
        None,
        description="An Organisation involved in the design, creation or manufacture of the object.",
    )
    object_production_people: OneOrMany[People | str] = Field(
        None,
        description="A People involved in the design, creation or manufacture of an object.",
    )
    object_production_person: OneOrMany[Person | str] = Field(
        None,
        description="A Person involved in the design, creation or manufacture of an object. This may include the "
        "commissioner of an object.",
    )
    object_production_place: OneOrMany[Place | str] = Field(
        None,
        description="A Place where the design, creation or manufacture of an object took place.",
    )
    object_production_reason: OneOrMany[str] = Field(
        None,
        description="The reason why an object was produced.",
    )
    object_purchaser_offer_price: OneOrMany[str] = Field(
        None,
        description="The price which the organisation offers for the purchase of an object.",
    )
    object_purchase_price: OneOrMany[str] = Field(
        None,
        description="The total price paid for an object at acquisition, including taxes for which the purchase is "
        "liable. Associated with the Object number. If no individual prices are known for specific objects in "
        "the group (eg a lot bought at auction), use Group purchase price.",
    )
    object_status: OneOrMany[ControlledTerm] = Field(
        None,
        description="A statement of the standing of a natural science specimen or other object in relation to others "
        "in existence.",
    )
    original_object_purchase_price: OneOrMany[OriginalObjectPurchasePrice | str] = Field(
        None,
        description="The price paid for an object in the original currency at the time of purchase.",
    )
    other_number: OneOrMany[OtherNumber | str] = Field(
        None,
        description="An alternative number for an object other than the Object number.",
    )
    owner: OneOrMany[Organisation | People | Person | str] = Field(
        None,
        description="Details of a People, Person or Organisation who owned an object before title was transferred to "
        "the organisation.",
    )
    owners_reference: OneOrMany[Reference | str] = Field(
        None,
        description="Documentation of any additional reference to the object provided by a previous owner, eg an "
        "event, object, document, person or organisation.",
    )
    ownership_dates: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The dates when a People, Person or Organisation owned the title to an object.",
    )
    ownership_place: Place | str | None = Field(
        None,
        description="The Place where an object was owned before title was transferred to the organisation.",
    )
    phase: OneOrMany[ControlledTerm] = Field(
        None,
        description="A textual expression of the age or developmental phase of a natural science specimen.",
    )
    physical_description: OneOrMany[str] = Field(
        None,
        description="Use normal grammar and punctuation. Include a description of an object's completeness if "
        "appropriate (eg lacks left arm). Comment on condition only as it affects completeness. Describe items "
        "which would be made using an object, eg clothing from paper patterns. The frame and mount should also be "
        "described if appropriate. The following issues might be addressed: What shape or form does it take? "
        "Describe an object in reference to the direction the work faces (ie a sculpture's right side (proper "
        "right) not as the viewer). Do not use 'sinister' or 'dexter'. Where and how is it decorated? How is it "
        "mounted? How is it constructed? What colours have been used? What scale is used?",
    )
    recall_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date on which the next stage of a conservation process is due.",
    )
    related_object_number: OneOrMany[RelatedObjectNumber | str] = Field(
        None,
        description="The Object number of an object which is related to the object being documented.",
    )
    reproduction_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date on which a reproduction was created.",
    )
    reproduction_description: OneOrMany[str] = Field(
        None,
        description="A description of features which could uniquely identify a reproduction.",
    )
    reproduction_format: OneOrMany[ControlledTerm] = Field(
        None,
        description="The analogue format or digital file format of the reproduction.",
    )
    reproduction_number: OneOrMany[str] = Field(
        None,
        description="A unique identifier for the reproduction.",
    )
    reproduction_status: OneOrMany[ControlledTerm] = Field(
        None,
        description="The status of a reproduction, especially among multiple copies.",
    )
    reproduction_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The medium of the reproduction.",
    )
    responsible_department_section: OneOrMany[ControlledTerm] = Field(
        None,
        description="The department or section of the organisation responsible for the management of the object or "
        "group of objects.",
    )
    right_begin_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The first date on which a right is current.",
    )
    right_end_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The last date on which a right is current.",
    )
    right_holder: OneOrMany[Organisation | Person | str] = Field(
        None,
        description="The holder of the right associated with an object, reproduction, or text.",
    )
    right_note: OneOrMany[str] = Field(
        None,
        description="Any details of the right not covered elsewhere.",
    )
    right_type: OneOrMany[str] = Field(
        None,
        description="The specific type of right being recorded in relation to an object, reproduction, or text.",
    )
    sex: OneOrMany[ControlledTerm] = Field(
        None,
        description="The gender of an animal specimen.",
    )
    special_requirements: OneOrMany[str] = Field(
        None,
        description="Requirements that may be unique or special to a particular object.",
    )
    stratigraphic_unit_name: OneOrMany[StratigraphicUnitName | str] = Field(
        None,
        description="The stratigraphic unit from which a field collection was made.",
    )
    style: OneOrMany[ControlledTerm] = Field(
        None,
        description="Styles or schools relating to an object.",
    )
    technical_attribute: OneOrMany[ControlledTerm] = Field(
        None,
        description="A technical attribute possessed by an object which can be described and/or quantified.",
    )
    technical_attribute_measurement: OneOrMany[TechnicalAttributeMeasurement | str] = Field(
        None,
        description="The measurement of a named Technical attribute.",
    )
    technique: OneOrMany[Technique | str] = Field(
        None,
        description="Processes, methods, techniques or tools used to fabricate or decorate an object.",
    )
    text: OneOrMany[Text | str] = Field(
        None,
        description="A piece of interpretive text, or label, which was created for a use of an object or group of "
        "objects.",
    )
    text_reference_number: OneOrMany[str] = Field(
        None,  # FIXME: I think this should be moved into Text
        description="The unique identifier for a text.",
    )
    title: OneOrMany[Title | str] = Field(
        None,
        description="The name assigned to an object or group of objects by the artist/creator or collector at the "
        "time of origin or subsequent titles either specifically assigned or generally understood to refer to it.",
    )
    treatment_begin_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date at which the treatment of an object, or group of objects began.",
    )
    treatment_end_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date at which the treatment of an object, or group of objects ended.",
    )
    usage: OneOrMany[ControlledTerm] = Field(
        None,
        description="A single term describing the use of a particular kind of object.",
    )
    usage_note: OneOrMany[str] = Field(
        None,
        description="The use of a kind of object by the original or subsequent owners.",
    )
    use_begin_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date on which a use began.",
    )
    use_end_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date on which a use ended.",
    )
    use_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the use which has not been recorded elsewhere using controlled "
        "terminology. This could include an object's operations log.",
    )
    use_organiser: OneOrMany[Organisation | Person | str] = Field(
        None,
        description="The Person or Organisation organising a use event (eg exhibition, display, and demonstration).",
    )
    use_reference_number: OneOrMany[str] = Field(
        None,
        description="The unique number assigned to the use of an object or group of objects. The number should also "
        "refer to a file containing all written documentation about the use.",
    )
    use_request_note: OneOrMany[str] = Field(
        None,
        description="Additional information about request for use.",
    )
    use_restriction: OneOrMany[UseRestriction | str] = Field(
        None,
        description="A record of the restrictions on the use to an object or group of objects.",
    )
    use_result: OneOrMany[ControlledTerm] = Field(
        None,
        description="Information about the outcome of the use.",
    )
    use_title: OneOrMany[str] = Field(
        None,
        description="The name of a use event (eg exhibition title).",
    )
    use_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="A term describing the nature of the use event.",
    )
    use_venue: OneOrMany[Place | str] = Field(
        None,
        description="The Place where a use takes place.",
    )
    user: OneOrMany[User | str] = Field(
        None,
        description="The Person or Organisation researching, using, selecting or viewing an object or group of "
        "objects.",
    )
    users_reference: OneOrMany[Reference | str] = Field(
        None,
        description="Documentation of any additional reference to the object provided by a user eg an event, object, "
        "document, person or organisation.",
    )


class AssociatedActivity(MDSModel):
    value: str | None = None

    associated_activity_note: OneOrMany[str] = Field(
        None,
        description="A description of, or comments relating to, an activity associated with an object.",
    )


class AssociatedEventName(MDSModel):
    value: str | None = None

    associated_event_name_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The type of historical event associated with an object or group of objects.",
    )


class Completeness(MDSModel):
    value: ControlledTerm | None = None

    completeness_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which the completeness of an object was recorded.",
    )
    completeness_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the completeness of an object which has not been recorded elsewhere "
        "using controlled terminology.",
    )


class Condition(MDSModel):
    value: ControlledTerm | None = None

    condition_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which the condition of an object was recorded.",
    )
    condition_note: OneOrMany[str] = Field(
        None,
        description="A brief description of the condition of an object.",
    )


class ConservationAuthoriser(Person):
    value: str | None = None

    conservation_authorisation_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date on which the Conservation authoriser gives final approval for an acquisition to "
        "proceed.",
    )


class ContentEventName(MDSModel):
    value: ControlledTerm | None = None

    content_event_name_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="A term describing the nature of the Content - event name.",
    )


class ContentObject(MDSModel):
    value: ControlledTerm | None = None

    content_object_type: OneOrMany[str] = Field(
        None,
        description="A term describing the nature of the Content - object.",
    )


class ContentOther(MDSModel):
    value: str | None = None

    content_other_type: OneOrMany[str] = Field(
        None,
        description="The type of aspect being recorded by Content - other.",
    )


class CurrentLocation(Location):
    value: ControlledTerm | None = None

    location_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date an object was place at the Current location.",
    )
    current_location_fitness: OneOrMany[ControlledTerm] = Field(
        None,
        description="A term describing the extent to which an object's current location is fitted to an object's "
        "requirements.",
    )
    current_location_note: OneOrMany[str] = Field(
        None,
        description="Information about the reason for an object's being at its Current location.",
    )


class DisposalAuthoriser(Person):
    value: str | None = None

    disposal_authorisation_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date on which the Disposal authoriser gives final approval for a disposal to proceed.",
    )


class Hazard(MDSModel):
    value: str | None = None

    hazard_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which a Hazard was identified.",
    )
    hazards_note: OneOrMany[str] = Field(
        None,
        description="Details of potential hazards to people or other objects that the handling and storing of an "
        "object can present which are not recorded using controlled terminology in Hazard.",
    )


class ObjectComponentName(MDSModel):
    value: ControlledTerm | None = None

    object_component_information: OneOrMany[ControlledTerm] = Field(
        None,
        description="The unit of information describing an Object component name.",
    )


class ObjectName(MDSModel):
    value: str | None = None

    object_name_currency: OneOrMany[ControlledTerm] = Field(
        None,
        description="A statement of the status of an Object name.",
    )
    object_name_level: OneOrMany[ControlledTerm] = Field(
        None,
        description="A statement of the position of the Object name in a classification scheme.",
    )
    object_name_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the Object name.",
    )
    object_name_system: OneOrMany[str] = Field(
        None,
        description="The classification system from which the Object name is taken.",
    )
    object_name_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The type of Object name recorded.",
    )
    # FIXME: Property named the same as for object_name?
    object_name_title_language: OneOrMany[ControlledTerm] = Field(
        None,
        description="The language for an Object name, Other name or Title given to an object.",
    )


class OtherNumber(MDSModel):
    value: str | None = None

    other_number_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="A description of an Other number assigned to an object.",
    )


class RelatedObjectNumber(MDSModel):
    value: str | None = None

    related_object_association: OneOrMany[ControlledTerm] = Field(
        None,
        description="The nature of the relationship of an object to the object being documented.",
    )
    related_object_note: OneOrMany[str] = Field(
        None,
        description="A narrative description of the nature of the relationship of an object to the object being "
        "documented.",
    )


# TODO: Check spectrum documentation to see if this is defined twice
class StratigraphicUnitName(MDSModel):
    value: str | None = None

    stratigraphic_unit_type: OneOrMany[str] = Field(
        None,
        description="The nature of the Stratigraphic unit name from which a field collection was made.",
    )
    stratigraphic_unit_note: OneOrMany[str] = Field(
        None,
        description="Additional information about a Stratigraphic unit name.",
    )


class TechnicalAttributeMeasurement(MDSModel):
    value: str | None = None

    technical_attribute_measurement_unit: ControlledTerm | None = Field(
        None,
        description="The unit of measurement used when measuring a Technical attribute.",
    )


class Text(MDSModel):
    value: str | None = None

    text_reference_number: OneOrMany[str] = Field(
        None,
        description="The unique identifier for a text.",
    )
    text_audience: OneOrMany[ControlledTerm] = Field(
        None,
        description="The type of person that the text was created for.",
    )
    text_author: OneOrMany[Organisation | Person | str] = Field(
        None,
        description="The Person or Organisation who created the text.",
    )
    text_date: Date | DateStringISO | None = Field(
        None,
        description="The date on which a text was created.",
    )
    text_language: OneOrMany[str] = Field(
        None,
        description="The language of the text.",
    )
    text_note: OneOrMany[str] = Field(
        None,
        description="Information about a text that is not recorded elsewhere.",
    )
    text_reason: OneOrMany[ControlledTerm] = Field(
        None,
        description="The reason why a text was created.",
    )


class Title(MDSModel):
    value: str | None = None
    # FIXME: Property named the same as for object_name?
    object_name_title_language: ControlledTerm | None = Field(
        None,
        description="The language for an Object name, Other name or Title given to an object.",
    )
    title_translation: OneOrMany[str] = Field(
        None,
        description="A translation into the organisation's first language of a Title as recorded.",
    )
    title_type: OneOrMany[ControlledTerm] = Field(
        None,
        description="The nature of the Title recorded.",
    )


class UserOrganisation(Organisation):
    value: str | None = None

    users_contact: OneOrMany[Person | str] = Field(
        None,
        description="The details of a Person designated by the User to be responsible for dealing with the use on "
        "their behalf.",
    )


class UserPerson(Person):
    value: str | None = None

    users_contact: OneOrMany[str] = Field(
        None,
        description="The details of a Person designated by the User to be responsible for dealing with the use on "
        "their behalf.",
    )


User = UserOrganisation | UserPerson


class UseRestriction(MDSModel):
    value: str | None = None

    use_restriction_date: OneOrMany[Date | DateStringISO] = Field(
        None,
        description="The date on which a Use restriction was recorded.",
    )
    use_restriction_note: OneOrMany[str] = Field(
        None,
        description="Additional information about the Use restriction of an object which has not been recorded "
        "elsewhere using controlled terminology.",
    )
