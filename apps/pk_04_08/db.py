from django.db import models

class Database:
    
    __object_set: models.QuerySet = None
    
    SIZE_PAGE = 15
    
    def __init__(self, model: models.Model):
        self.__object_set = model.objects
    
    def set_object(self, object: models.QuerySet):
        self.__object_set = object
        return self
    
    def where(self, dict: dict):
        self.__object_set = self.__object_set.filter(**dict)
        return self
    
    def where_like(self, tuple: tuple[str, str, str], prefix = ""):
        field_name, eq, value = tuple
        key = "{}{}__{}".format(prefix, field_name, eq)
        self.__object_set = self.__object_set.filter(**{
            key: value
        })
        return self
    
    def where_in(self, tuple: tuple[str, list[str|int]]):
        field_name, value_list = tuple
        key = "{}__in".format(field_name)
        self.__object_set = self.__object_set.filter(**{
            key: value_list
        })
        return self
    
    def where_range(self, field_name: str, tuple:tuple):
        before, after = tuple
        key = "{}__range".format(field_name)
        if(before is not None and after is not None):
            self.__object_set = self.__object_set.filter(**{
                key: tuple
            })
        else:
            if before is not None:
                key = "{}__gte".format(key)
                self.__object_set = self.__object_set.filter(**{
                    key: before
                })
           
            if after is not None:
                key = "{}__lte".format(key)
                self.__object_set = self.__object_set.filter(**{
                    key: after
                })
        return self
    
    def order_by(self, tuple_list: list[tuple[str, bool]]):
        for item in tuple_list:
            field_name, is_desc = item
            sort_field_name = field_name if not is_desc else "-{}".format(field_name)
            self.__object_set = self.__object_set.order_by(sort_field_name)
        return self
       
    def get_object(self):
        return self.__object_set
       
    def get_search_pagation(self, page: int):
        index = (page -1) * self.SIZE_PAGE
        return self.__object_set.all()[index:self.SIZE_PAGE]
    
    def get_search_count(self) -> int:
        return self.__object_set.count()
    
    def get_search(self):
        return self.__object_set.all()
    
    
    # code search
    # code_kind = bodyDict.pop("code_kind")
    # code_match = bodyDict.pop("code_match")
    # code = bodyDict.pop("code")
    # if code is not None:
    #     field = {"products__product_standard__{}__{}".format(code_kind, code_match): code}
    #     # products__product_standard__jan_code="pk-0804-jan"
    #     object_set = object_set.filter(**field)
    
    # object_set = TmPointSetting.objects\
    #     .filter(del_flag=False)\
    #     .filter(products__del_flag=False)\
    #     .filter(products__product_standard__del_flag=False)\

    # date range
    # start_date = bodyDict.pop("date_start")
    # if start_date is not None:
    #     object_set = object_set.filter(pub_date_time__gte = start_date)
    # end_date = bodyDict.pop("date_end")
    # if end_date is not None:
    #     object_set = object_set.filter(pub_date_time__lte = end_date)

    # mall muitl select
    
    # status muilt select
    # status = bodyDict.pop("status")
    # if status is not None:
    #     object_set = object_set.filter(status__in=status)
    
  
    
    # order
    # sort_field_name = bodyDict.pop("sort_field")
    # sort_field_asc = bodyDict.pop("sort_eq")
    # sort_field = sort_field_name if sort_field_asc else "-{}".format(sort_field_name)
    # object_set = object_set.order_by(sort_field)
    
    # page
    # page = int(bodyDict.pop("page", 1))
    # index = (page -1) * SIZE_PAGE
    # object_set = object_set.all()[index:SIZE_PAGE]
    
 