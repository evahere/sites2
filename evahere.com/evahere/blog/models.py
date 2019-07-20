from django.db import models
# from ckeditor.fields import RichTextField

from DjangoUeditor.models import UEditorField

# Create your models here.



class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章主要内容
    content = UEditorField('内容',width=800,height=500,toolbars="full",imagePath="upimg/",filePath="upfile/",upload_settings={"imageMaxSize":1204000},settings={},command=None,blank=True)
    publish_date = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title
