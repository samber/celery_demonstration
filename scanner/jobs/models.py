
from    django.db                       import models
import  uuid

class                           Credential(models.Model):

    _id                         = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4, editable=False)
    hostname                    = models.CharField(max_length=255, null=False)
    username                    = models.EmailField(max_length=255, null=False)
    password                    = models.CharField(max_length=255, null=False)

    class Meta:
        db_table                = '"credentials"'
        app_label               = 'scanner'


