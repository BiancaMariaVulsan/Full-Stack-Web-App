from channels.layers import get_channel_layer
from channels.testing import WebsocketCommunicator
from django.test import TestCase
from routing import application

class WebSocketTests(TestCase):
    async def test_websocket_connection(self):
        # Initialize a WebSocket communicator
        communicator = WebsocketCommunicator(application, '/ws/somepath/')
        
        # Connect the WebSocket
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        # Send a message
        await communicator.send_json_to({'type': 'some_message_type', 'data': 'test'})
        
        # Receive a response
        response = await communicator.receive_json_from()
        self.assertEqual(response['data'], 'test_response')

        # Close the connection
        await communicator.disconnect()
