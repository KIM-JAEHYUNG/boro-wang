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
        (0, "종로구"),
        (1, "중구"),
        (2, "용산구"),
        (3, "성동구"),
        (4, "광진구"),
        (5, "동대문구"),
        (6, "중랑구"),
        (7, "성북구"),
        (8, "강북구"),
        (9, "도봉구"),
        (10, "노원구"),
        (11, "은평구"),
        (12, "서대문구"),
        (13, "마포구"),
        (14, "양천구"),
        (15, "강서구"),
        (16, "구로구"),
        (17, "금천구"),
        (18, "영등포구"),
        (19, "동작구"),
        (20, "관악구"),
        (21, "서초구"),
        (22, "강남구"),
        (23, "송파구"),
        (24, "강동구")]

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
