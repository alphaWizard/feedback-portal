from django.contrib import admin
from .models import total_authenticated_users,designations,hostellist,accesslevels,siang_authorities,kapili_authorities,manas_authorities,dhansiri_authorities,subansiri_authorities,dihing_authorities,dibang_authorities,brahmputra_authorities,lohit_authorities
# Register your models here.



admin.site.register(siang_authorities)
admin.site.register(manas_authorities)
admin.site.register(lohit_authorities)
admin.site.register(dhansiri_authorities)
admin.site.register(subansiri_authorities)
admin.site.register(brahmputra_authorities)
admin.site.register(dibang_authorities)
admin.site.register(dihing_authorities)
admin.site.register(kapili_authorities)
admin.site.register(total_authenticated_users)
