from django.db import models

# Create your models here.
class Product(models.Model):
    # 썸네일 이미지
    thumbnail = models.ImageField(upload_to="product/", blank=True, null=True),
    # 디테일 이미지
    detail_image = models.ImageField(upload_to="product/", blank=True, null=True),
    # 상품명
    product_name = models.CharField(max_length=20),
    # 상세 설명
    explanation = models.CharField(max_length=200),
    # 가격
    price = models.IntegerField(default=0),
    # 옵션
    OPTION = [
                ('option1', '1호'), 
                ('option2', '2호'),
                ('option3', '3호'),
            ]
    
    # 제목 설정
    def __str__(self):
        return self.product_name


class Review(models.Model):
    # 작성자
    author = models.CharField(max_length=100),
    # 내용
    content = models.CharField(max_length=200, null=True),
    # 작성 날짜
    created_at = models.DateField(auto_now_add=True),
    # 수정 날짜
    updated_at = models.DateField(auto_now=True),
    # 별점
    RATE = [
                ('star1', '1'),
                ('star2', '2'),
                ('star3', '3'),
                ('star4', '4'),
                ('star5', '5'),
            ]
    # 리뷰 이미지
    review_image = models.ImageField(upload_to ="review/", blank=True, null=True),

    # 제목 설정
    def __str__(self):
        return self.content
