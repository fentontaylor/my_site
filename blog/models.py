from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return(f"<Category: name='{self.name}'>")


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        body_text = f'{self.body[0:10]}...'
        cats = '[ Categories ]' if len(list(self.categories.all())) > 0 else '[]'
        return f"<Post: title='{self.title}', " \
                      f"body='{body_text}, " \
                      f"categories={cats}, " \
                      f"created_on={self.created_on}, " \
                      f"last_modified={self.last_modified}>"


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        body_text = f'{self.body[0:10]}...'
        return f"<Comment: author='{self.author}', " \
                         f"body='{body_text}', " \
                         f"created_on={self.created_on}>"
