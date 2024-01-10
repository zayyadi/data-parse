import uuid
from pydantic import BaseModel, validator
from typing import Any
from datetime import datetime


class DataParse(BaseModel):
    id: str = uuid.uuid4()
    service_type: str
    source_addr_ton: str
    source_addr_npi: str
    source_addr: str
    dest_addr_ton: str
    dest_addr_npi: str
    destination_addr: str
    esm_class: str
    protocol_id: str
    priority_flag: str
    schedule_delivery_time: str
    validity_period: datetime | None
    registered_delivery: str
    replace_if_present_flag: str
    data_coding: str
    sm_default_msg_id: str
    short_message: str

    @validator("service_type", pre=True, always=True)
    def coerce_name_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("source_addr_ton", pre=True, always=True)
    def coerce_srcton_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("source_addr_npi", pre=True, always=True)
    def coerce_srcnpi_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("source_addr", pre=True, always=True)
    def coerce_srcaddr_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("dest_addr_ton", pre=True, always=True)
    def coerce_destton_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("dest_addr_npi", pre=True, always=True)
    def coerce_destnpi_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("destination_addr", pre=True, always=True)
    def coerce_destaddr_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("esm_class", pre=True, always=True)
    def coerce_esm_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("protocol_id", pre=True, always=True)
    def coerce_protocol_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("priority_flag", pre=True, always=True)
    def coerce_priority_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("schedule_delivery_time", pre=True, always=True)
    def coerce_schedule_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("validity_period", pre=True, always=True)
    def coerce_validity_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("registered_delivery", pre=True, always=True)
    def coerce_register_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("replace_if_present_flag", pre=True, always=True)
    def coerce_replaceif_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("data_coding", pre=True, always=True)
    def coerce_datacoding_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("sm_default_msg_id", pre=True, always=True)
    def coerce_smdef_to_str(cls, value: Any) -> str:
        return str(value)

    @validator("short_message", pre=True, always=True)
    def coerce_shmsg_to_str(cls, value: Any) -> str:
        return str(value)


# def data(
#     service_type,
#     source_addr_ton,
#     source_addr_npi,
#     source_addr,
#     dest_addr_ton,
#     dest_addr_npi,
#     destination_addr,
#     esm_class,
#     protocol_id,
#     priority_flag,
#     schedule_delivery_time,
#     validity_period,
#     registered_delivery,
#     replace_if_present_flag,
#     data_coding,
#     sm_default_msg_id,
#     short_message,
# ) -> dict:
#     dict_list = {
#         "service_type": service_type,
#         "source_addr_ton": source_addr_ton,
#         "source_addr_npi": source_addr_npi,
#         "source_addr": source_addr,
#         "dest_addr_ton": dest_addr_ton,
#         "dest_addr_npi": dest_addr_npi,
#         "dest_addr": destination_addr,
#         "esm_class": esm_class,
#         "protocol_id": protocol_id,
#         "protocol_flag": priority_flag,
#         "schedule_delivery_time": schedule_delivery_time,
#         "validity_period": validity_period,
#         "registered_delivery": registered_delivery,
#         "replace_if_present_flag": replace_if_present_flag,
#         "data_coding": data_coding,
#         "sm_default_msg_id": sm_default_msg_id,
#         "short_message": short_message,
#     }

#     return dict_list


# | None = datetime

# @validator("*", pre=True, each_item=True)
# def coerce_to_string(cls, v):
#     return str(v)
