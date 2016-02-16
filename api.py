from tastypie import authorization
from tastypie_mongoengine import resources
from project.models import *
from tastypie.resources import *

class UserResource(resources.MongoEngineResource):
class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    allowed_methods = ('get', 'post', 'put', 'delete','patch')
    authorization = authorization.Authorization()
