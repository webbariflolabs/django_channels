from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    
	def websocket_connect(self , event):
		print("Connected......",event)
		self.send({
			'type':'websocket.accept',
        })
		self.send({
			'type':'websocket.send',
			'text':'Connected SuccessFully'
        })
	
	def websocket_receive(self , event):
		print("Received.....",event)
		print("Message is ....",event['text'])
		self.send({
			'type':'websocket.send',
			'text':'Message From Server Hello World'
        })
	
	def websocket_disconnect(self,event):
		print("Disconnected.....",event)
		raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    
	async def websocket_connect(self , event):
		print("Connected......",event)
		await self.send({
			'type':'websocket.accept'
        })
	
	async def websocket_receive(self , event):
		print("Received.....",event)
		print("Message is ....",event['text'])
		await self.send({
            "type": "websocket.send",
            "text": "Send from Server Hello Async User",
        })
	
	async def websocket_disconnect(self,event):
		print("Disconnected.....",event)
		raise StopConsumer()
