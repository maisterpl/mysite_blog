from django.contrib.syndication.views import Feed
from django.db.models.base import Model
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    title = 'Mój blog'
    link = '/blog/'
    descriptions = 'Nowe posty na moim blogu.'
    
    def items(self):
        return Post.published.all()[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item: Model) -> str:
        return truncatewords(item.body, 30)