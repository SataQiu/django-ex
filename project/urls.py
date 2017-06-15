from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health
from weixin.views import ccdc_query_product_by_code

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ccdc/licai/queryByCode', ccdc_query_product_by_code),
]
