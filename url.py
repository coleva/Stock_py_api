from tastypie.api import Api
from projectname.api import *

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
