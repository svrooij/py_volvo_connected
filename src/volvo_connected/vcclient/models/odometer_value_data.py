from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .resource_instance_integer import ResourceInstanceInteger

@dataclass
class OdometerValue_data(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The odometer property
    odometer: Optional[ResourceInstanceInteger] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OdometerValue_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OdometerValue_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OdometerValue_data()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .resource_instance_integer import ResourceInstanceInteger

        from .resource_instance_integer import ResourceInstanceInteger

        fields: Dict[str, Callable[[Any], None]] = {
            "odometer": lambda n : setattr(self, 'odometer', n.get_object_value(ResourceInstanceInteger)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .resource_instance_integer import ResourceInstanceInteger

        writer.write_object_value("odometer", self.odometer)
        writer.write_additional_data_value(self.additional_data)
    

