from __future__ import annotations

from pydantic import Field

from .common import ControlledVocabField, MDSModel
from .date import Date, DateStringISO
from .organisation import Organisation
from .people import People
from .person import Person


class Acquisition(MDSModel):
    value: str | None = None

    acquisition_reference_number: list[str] | str | None = Field(None,
        description="A unique identifying number for information on the acquisition of an object or group of objects. "
            "It should serve as the reference to written documentation of a valuation. This will normally be the "
            "object number.",
        examples=["1993.123"],
    )
    accession_date: Date | DateStringISO | None = Field(None,
        description="The date on which an object formally enters the collections and is recorded in the accessions "
        "register.",
    )
    acquisition_authoriser: list[AcquisitionAuthoriser | str] | AcquisitionAuthoriser | str | None = Field(None,
        description="The Person giving final approval for the acquisition to proceed.",
    )
    acquisition_date: list[Date | DateStringISO] | Date | DateStringISO | None = Field(None,
        description="The date on which title to an object or group of objects is transferred to the organisation.",
    )
    acquisition_funding: list[AcquisitionFunding | str] | AcquisitionFunding | str | None = Field(None,
        description="The funding used to support the acquisition of an object.",
    )
    acquisition_method: ControlledVocabField = Field(None,
        description="The means by which title to an object is formally transferred to the organisation.",
    )
    acquisition_note: list[str] | str | None = Field(None,
        description="General information about the acquisition.",
    )
    acquisition_provisos: list[str] | str | None = Field(None,
        description="Restrictions applying to the objects in a single acquisition, including conditions for "
            "deposition of archaeological archives.",
    )
    acquisition_reason: list[str] | str | None = Field(None,
        description="The reason or justification for an acquisition.",
    )
    acquisition_source: list[Organisation | People | Person | str] | Organisation | People | Person | str | None = Field(None,
        description="The People, Person or Organisation from whom an object was obtained, if different from the "
            "Owner. The Acquisition source may be an agent or other intermediary between the acquiring organisation "
            "and the Owner. For archaeological archives, use Acquisition source to record the excavating body "
            "responsible for preparing and depositing the archive with the organisation.",
    )
    group_purchase_price: list[str] | str | None = Field(None,
        description="The total price paid for a group of objects at acquisition, including taxes for which the "
            "purchase is liable. If individual prices are known for specific objects in the group, use Object "
            "acquisition price.",
    )
    object_offer_price: list[str] | str | None = Field(None,
        description="The price at which an object is offered for sale to the organisation.",
    )
    object_purchaser_offer_price: list[str] | str | None = Field(None,
        description="The price which the organisation offers for the purchase of an object.",
    )
    object_purchase_price: list[str] | str | None = Field(None,
        description="The total price paid for an object at acquisition, including taxes for which the purchase is "
            "liable. Associated with the Object number. If no individual prices are known for specific objects in "
            "the group (eg a lot bought at auction), use Group purchase price.",
    )
    original_object_purchase_price: list[OriginalObjectPurchasePrice | str] | OriginalObjectPurchasePrice | str | None = Field(None,
        description="The price paid for an object in the original currency at the time of purchase.",
    )
    transfer_of_title_number: list[str] | str | None = Field(None,
        description="A unique identifying number for a transfer of title or acquisition event. It should serve as the "
            "reference to written documentation of a transfer of title or acquisition process. The number may be "
            "assigned to a transfer of title form.",
    )


class AcquisitionAuthoriser(Person):
    value: Person | str | None = None

    acquisition_authorisation_date: Date | DateStringISO | None = Field(None,
        description="The date on which the Acquisition authoriser gives final approval for an acquisition to proceed.",
    )


class AcquisitionFundingSourceOrganisation(Organisation):
    value: str | None = None

    acquisition_funding_source_provisos: list[str] | str | None = Field(None,
        description="Restrictions applying to all the objects acquired with the support from an Acquisition funding "
            "source.",
    )


class AcquisitionFundingSourcePerson(Person):
    value: str | None = None

    acquisition_funding_source_provisos: list[str] | str | None = Field(None,
        description="Restrictions applying to all the objects acquired with the support from an Acquisition funding "
            "source.",
    )


AcquisitionFundingSource = AcquisitionFundingSourceOrganisation | AcquisitionFundingSourcePerson


class AcquisitionFunding(MDSModel):
    value: str | None = None

    acquisition_funding_source: list[AcquisitionFundingSource | str] | AcquisitionFundingSource | str | None = Field(None,
        description="The Person or Organisation from whom the Acquisition funding was obtained.",
    )


class OriginalObjectPurchasePrice(MDSModel):
    value: str | None = None

    original_object_purchase_price_denomination: list[str] | str | None = Field(None,
        description="The denomination or currency of the Original object purchase price.",
    )