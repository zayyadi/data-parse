# from infi.clickhouse_orm import , DateField, MergeTree
import uuid
from sqlalchemy import Column, String
from clickhouse_sqlalchemy import engines
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PDUData(Base):
    __tablename__ = "pdu_data"
    __table_args__ = (
        engines.MergeTree(order_by=["id"]),
        # {'schema': database},
    )
    id = Column(
        String,
        default=uuid.uuid4(),
        primary_key=True,
        # autoincrement="auto",
    )
    service_type = Column(String)
    source_addr_ton = Column(String)
    source_addr_npi = Column(String)
    source_addr = Column(String)
    dest_addr_ton = Column(String)
    dest_addr_npi = Column(String)
    destination_addr = Column(String)
    esm_class = Column(String)
    protocol_id = Column(String)
    priority_flag = Column(String)
    schedule_delivery_time = Column(String)
    validity_period = Column(String)
    registered_delivery = Column(String)
    replace_if_present_flag = Column(String)
    data_coding = Column(String)
    sm_default_msg_id = Column(String)
    short_message = Column(String)
