# blog/search_indexes.py
from haystack import indexes
from blog.models import Post

# document=True，代表 django haystack和搜索引擎将使用此字段的内容作为索引进行检索(primary field)
# use_template=True，允许我们使用数据模板去建立搜索引擎索引的文件
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        # 注意objects已经改成了my_objects
        return self.get_model().my_objects.all()