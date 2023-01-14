from django.db import models
import uuid
# Create your models here.

class filed(models.Model):
    id=models.AutoField(primary_key=True)
    duuid=models.UUIDField(default=uuid.uuid4,null=False,verbose_name='文件唯一值')
    name=models.CharField(max_length=100,verbose_name='文件名')
    filedf=models.FileField(upload_to='file/',verbose_name='文件')
    ctime=models.DateTimeField(auto_now=True,verbose_name='创建时间')
    class Meta:
        verbose_name='文件表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name