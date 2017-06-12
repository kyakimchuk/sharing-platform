from django.conf.urls import url
from django.conf.urls.static import static

import sp.views
from django.conf import settings


urlpatterns = [
    url(r'^$', sp.views.AllCallsList.as_view(), name='home'),
    url(r'^success$', sp.views.success, name='success'),
    url(r'^registration$', sp.views.registration, name='registration'),
    url(r'^logout$', sp.views.logout_view, name='logout_view'),
    url(r'^authorization$', sp.views.authorization, name='authorization'),
    url(r'^call/add$', sp.views.CallAdd.as_view(), name='add_call'),
    url(r'^call/update/(?P<pk>\d+)$', sp.views.CallUpdate.as_view(), name='update_call'),
    url(r'^call/delete/(?P<pk>\d+)$', sp.views.CallDelete.as_view(), name='delete_call'),
    url(r'^my-profile$', sp.views.ProfileUpdate.as_view(), name='my_profile'),
    url(r'^my-calls$', sp.views.MyCallsList.as_view(), name='my_calls'),
    url(r'^user-calls/(?P<user_id>\d+)$', sp.views.UserCallsList.as_view(), name='user_calls'),
    url(r'^profile/(?P<pk>\d+)$', sp.views.ProfileDetail.as_view(), name='profile_detail'),
    url(r'^call/(?P<pk>\d+)$', sp.views.CallDetail.as_view(), name='call_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
