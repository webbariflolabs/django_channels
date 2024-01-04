import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter , URLRouter
import liveCalculator.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sampleProject.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": URLRouter( 
			liveCalculator.routing.websocket_urlpatterns 
		) 
})
