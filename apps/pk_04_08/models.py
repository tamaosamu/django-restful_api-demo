from django.db import models

# Create your models here.
    
class TmProduct(models.Model):
    product_cd = models.CharField(unique=True)
    product_name = models.CharField()
    del_flag = models.BooleanField()
    
    class Meta:
        db_table = "tm_product"
        
    # def __str__(self) -> str:
    #     return self.product_name

class TmProductStandard(models.Model):
    
    jan_code = models.CharField()
    crop_product_cd = models.CharField()
    del_flag = models.BooleanField()
    
    product = models.ForeignKey(
        TmProduct, 
        to_field="product_cd",
        db_column="product_cd",
        on_delete=models.DO_NOTHING, 
        related_name="product_standard")
    
    class Meta:
        db_table = "tm_product_standard"

class TmPointSetting(models.Model):
    WAIT_STATUS = "1"
    SUCC_STATUS = "2"
    FAIL_STATUS = "3"
    STATUS_CHO = (
        (WAIT_STATUS, "wait"),
        (SUCC_STATUS, "success"),
        (FAIL_STATUS, "failed")
    )
    pub_date_time = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHO)
    ratio = models.DecimalField(max_digits=3, decimal_places=1)
    del_flag = models.BooleanField()
    
    product = models.ForeignKey(
        TmProduct, 
        to_field="product_cd",
        db_column="product_cd",
        on_delete=models.DO_NOTHING, 
        related_name="point_setting")
    
    class Meta:
        db_table = "tm_point_setting"
        
        