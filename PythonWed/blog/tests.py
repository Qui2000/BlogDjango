from django.http import response
from django.test import TestCase
from . models import Post

# Create your tests here.
class BlogTests(TestCase):
    def setUp(seft):
        Post.objects.create(
            title = 'myTitle',
            body = 'just a test',
        )
    
    def test_string_representation(self):
        post = Post(title = 'My entry title')
        self.assertEquals(str(post), post.title)

    def test_post_list_view(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response, 'blog/blog.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/blog/1')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'myTitle')
        self.assertTemplateUsed(response, 'blog/post.html')
