from django.db.models import *
from users.models import User
from django.utils.translation import gettext as _



class TimeStampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    SHOW_LIST = [
        (0, "음악공연"),
        (1, "연극공연"),
        (2, "운동경기"),
        (3, "학술회/전시"),
        (4, "기타"), ]

    AREA_LIST = [
        (0, "강서구"),
        (1, "강남구"),
        (2, "강동구"),
        (3, "강북구"),
        (4, "구로구"),
        (5, "금천구"),
        (6, "관악구"),
        (7, "광진구"),
        (8, "노원구"),
        (9, "도봉구"),
        (10, "동대문구"),
        (11, "동작구"),
        (12, "마포구"),
        (13, "서대문구"),
        (14, "서초구"),
        (15, "성동구"),
        (16, "송파구"),
        (17, "성북구"),
        (18, "용산구"),
        (19, "양천구"),
        (20, "은평구"),
        (21, "영등포구"),
        (22, "종로구"),
        (23, "중구"),
        (24, "중랑구")]

    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=100)
    content = TextField()
    price = IntegerField(default=0)
    view_count = IntegerField(default=0)
    location = CharField(max_length=200, help_text="정확한 장소를 입력해주세요.")
    image = ImageField(upload_to="img/", null=True)
    likes = ManyToManyField(User, related_name="liked_users") 
    shows = PositiveSmallIntegerField(_('공연'), choices=SHOW_LIST, default=0, null=True)
    areas = PositiveSmallIntegerField(_('지역'), choices=AREA_LIST, default=0, null=True)

    def __str__(self):    
       return self.title

    def comments(self):
        return Comment.objects.filter(post=self)

    def like_count(self):
      return self.like_user_set.count()


class Comment(TimeStampedModel):
    user = ForeignKey(User, on_delete=CASCADE)
    post = ForeignKey(Post, on_delete=CASCADE)
    message = TextField()

    def __str__(self):
        return self.message
