# Create your views here.

import json
from rest_framework.request import Request
from .utils import Utils
from .serializer import SearchSerializer, PointSettingSerializer
from .models import TmPointSetting
from .db import Database
from src.response import ApiResponse

def index(request: Request):
    
    #paramsDict = Utils.to_dict(request.GET.items())
    bodyDict = json.loads(request.body.decode("utf-8"))
    
    ser = SearchSerializer(data=bodyDict)
    ser.is_valid(raise_exception=True)
    
    # set sql condition
    db = Database(TmPointSetting).where({
        "del_flag": False,
        "product__del_flag": False,
        "product__product_standard__del_flag": False
    })\
    .where_range("pub_date_time", (bodyDict.pop("date_start"), bodyDict.pop("date_end")))\
    .where_in(("status", bodyDict.pop("status")))\
    .where_like((
        bodyDict.pop("code_kind"),
        bodyDict.pop("code_match"), 
        bodyDict.pop("code")
    ), "product__product_standard__")
    
    # get sql count
    count = db.get_search_count()
    
    # sort & page
    sort = (bodyDict.pop("sort_field"), bodyDict.pop("sort_eq"))
    models = db.order_by([sort]).get_search_pagation(bodyDict.pop("page"))
    ser = PointSettingSerializer(models, many=True)
   
    return ApiResponse(**{
        'count': count,
        'page_size': db.SIZE_PAGE,
        'results_list': ser.data
    })
