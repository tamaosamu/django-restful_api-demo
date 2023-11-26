from django.db import models


class Book(models.Model):
    STATUE_TYPE = ((0, "close"), (1, "open"))

    objects = models.Manager()
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"


class Info(models.Model):
    user = models.OneToOneField(
        Book, on_delete=models.CASCADE, db_column="uid", related_name="info"
    )
    # user1 = models.OneToOneField("User", on_delete=models.CASCADE, related_name="uid", db_column="uid")

    objects = models.Manager()
    nickname = models.CharField(max_length=32)
    brithday = models.DateField()

    def __str__(self) -> str:
        return f"{self.nickname}"


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, db_column="book_id", related_name="articles"
    )

    def __str__(self) -> str:
        return f"{self.title}"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        # return "%s" % [self.name]
        return f"{self.name}"
