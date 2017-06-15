import urllib, urllib2
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ccdc_query_product_by_code(request):
    code = request.GET.get('code')
    data = {'cpdjbm':code}
    data_urlencode = urllib.urlencode(data)
    requrl = "http://wap.chinawealth.com.cn/lccpMbByDjbmServlet.go"
    req = urllib2.Request(url=requrl, data=data_urlencode)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return HttpResponse(res)
