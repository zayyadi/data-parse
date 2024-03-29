# Generated by CodiumAI
from app.main import DataParse
from app.main import post_data
from app.models import PDUData
from http import client


# Dependencies:
# pip install pytest-mock
import pytest


class TestPostData:
    # The function successfully receives data in the expected format.
    def test_receives_data_in_expected_format(self, mocker):
        # Arrange
        mock_session = mocker.Mock()
        mock_data = DataParse(
            service_type="test",
            source_addr_ton="test",
            source_addr_npi="test",
            source_addr="test",
            dest_addr_ton="test",
            dest_addr_npi="test",
            destination_addr="test",
            esm_class="test",
            protocol_id="test",
            priority_flag="test",
            schedule_delivery_time="test",
            validity_period="test",
            registered_delivery="test",
            replace_if_present_flag="test",
            data_coding="test",
            sm_default_msg_id="test",
            short_message="test",
        )

        # Act
        result = post_data(mock_data, session=mock_session)

        # Assert
        assert result is not None
        assert isinstance(result, PDUData)
        assert mock_session.add.called
        assert mock_session.commit.called
        assert mock_session.refresh.called
        assert client.set.called

    # The function successfully creates a new PDUData object with the received data.
    def test_creates_new_pdu_data_object(self, mocker):
        # Arrange
        mock_session = mocker.Mock()
        mock_data = DataParse(
            service_type="test",
            source_addr_ton="test",
            source_addr_npi="test",
            source_addr="test",
            dest_addr_ton="test",
            dest_addr_npi="test",
            destination_addr="test",
            esm_class="test",
            protocol_id="test",
            priority_flag="test",
            schedule_delivery_time="test",
            validity_period="test",
            registered_delivery="test",
            replace_if_present_flag="test",
            data_coding="test",
            sm_default_msg_id="test",
            short_message="test",
        )

        # Act
        result = post_data(mock_data, session=mock_session)

        # Assert
        assert result is not None
        assert isinstance(result, PDUData)
        assert result.service_type == mock_data.service_type
        assert result.source_addr_ton == mock_data.source_addr_ton
        assert result.source_addr_npi == mock_data.source_addr_npi
        assert result.source_addr == mock_data.source_addr
        assert result.dest_addr_ton == mock_data.dest_addr_ton
        assert result.dest_addr_npi == mock_data.dest_addr_npi
        assert result.destination_addr == mock_data.destination_addr
        assert result.esm_class == mock_data.esm_class
        assert result.protocol_id == mock_data.protocol_id
        assert result.priority_flag == mock_data.priority_flag
        assert result.schedule_delivery_time == mock_data.schedule_delivery_time
        assert result.validity_period == mock_data.validity_period
        assert result.registered_delivery == mock_data.registered_delivery
        assert result.replace_if_present_flag == mock_data.replace_if_present_flag
        assert result.data_coding == mock_data.data_coding
        assert result.sm_default_msg_id == mock_data.sm_default_msg_id
        assert result.short_message == mock_data.short_message
