from cStringIO import StringIO
import struct
import uuid

from . import conf
from . import messages


class EventstoreClient(object):

    #: 1 byte command + 1 byte auth + UUID correlation length
    HEADER_LENGTH = 1 + 1 + 16

    def __init__(self, socket):
        self._socket = socket

    def write_events(
        self, event_stream_id, events,
        expected_version=-2, require_master=False
    ):
        """
        Send events to eventstore blindly which means there is no data
        validation.

        :param str event_stream_id: Name of the stream
        :param list events: tuples (event_id, event_type, event_data)
        """
        collection = messages.WriteEvents()
        collection.event_stream_id = event_stream_id
        collection.expected_version = expected_version
        collection.require_master = require_master
        for event_id, event_type, event_data in events:
            event = collection.events.add()
            event.event_id = event_id.replace('-','').decode('hex')
            event.event_type = event_type
            event.data = event_data
            event.data_content_type = 1
            event.metadata_content_type = 0
        serialized = collection.SerializeToString()
        correlation_id = uuid.uuid4().bytes

        output = StringIO()
        output.write(struct.pack('<I', len(serialized)+self.HEADER_LENGTH))
        output.write(conf.WriteEventsCmd)  # Command
        output.write('\x00')  # Flags
        output.write(correlation_id)  # Correlation id
        output.write(serialized)

        self._socket.sendall(output.getvalue())
        return self.receive_response()

    def receive_response(self):
        length = self._socket.recv(4)
        response = self._socket.recv(struct.unpack('<I', length)[0])
        command, flags, correlation_id = \
            struct.unpack('cc16s', response[:self.HEADER_LENGTH])
        response_cls = conf.classes[command]
        instance = response_cls()
        instance.ParseFromString(response)
        return instance
