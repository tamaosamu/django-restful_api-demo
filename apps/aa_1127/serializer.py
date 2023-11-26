from rest_framework import serializers
from .models import TmPointSetting, TmProduct
from .utils import Utils

class SearchSerializer(serializers.Serializer):
    
    CODE_KIND_CHOICE = (
        ("product_cd", "product_cd"),
        ("jan_code","jan_code"),
        ("crop_product_cd","crop_product_cd")
    )
    EXPECT = "exact"
    CONTAINS = "contains"
    STARTSWITH = "startswith"
    
    CODE_MATH_CHOICE = (
        (EXPECT,"完全一致"),
        (CONTAINS, "部分一致"),
        (STARTSWITH, "前部一致")
    )
    
    WAIT_STATUS = "1"
    SUCC_STATUS = "2"
    FAIL_STATUS = "3"
    STATUS_CHOICE = (
        (WAIT_STATUS, "wait"),
        (SUCC_STATUS, "success"),
        (FAIL_STATUS, "failed")
    )
    
    code_kind = serializers.ChoiceField(choices=CODE_KIND_CHOICE, required=True)
    code_match = serializers.ChoiceField(choices=CODE_MATH_CHOICE, required=True)
    code = serializers.CharField(max_length=50, default=None)
    date_start = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    date_end = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status = serializers.MultipleChoiceField(choices=STATUS_CHOICE)
    page = serializers.IntegerField(default=1)
    sort_field = serializers.CharField(default="id")
    sort_eq = serializers.BooleanField(default=False)

        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmProduct  # 指定你要创建序列化器的模型
        fields = ("product_name",)  # 如果需要，可以指定特定的字段
        
class PointSettingSerializer(serializers.ModelSerializer):
    
    product_name = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = TmPointSetting  # 指定你要创建序列化器的模型
        fields = ('pub_date_time', 'ratio', 'status', 'product_name')  # 如果需要，可以指定特定的字段
       
    def get_product_name(self, instance: TmPointSetting):
        return instance.product.product_name
    
    def get_status(self, instance: TmPointSetting):
        statusDict = Utils.tuple_to_map(instance.STATUS_CHO)
        return statusDict.get(instance.status)