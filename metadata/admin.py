from metadata.models import MetaData
from django.contrib.contenttypes import admin

class MetaDataTabularInline(admin.GenericTabularInline):
    model = MetaData
    
class MetaDataStackedInline(admin.GenericStackedInline):
    model = MetaData
