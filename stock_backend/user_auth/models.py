from django.db import models
## this library will allow me to import a basic model
from django.contrib.auth.models import AbstractUser





## Creating this taking it from the deault data that is seen in the AbstractUser template
class CustomUser(AbstractUser):
    pass
    

