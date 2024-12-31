from .models import UserInfo, Course
from django.core.exceptions import ValidationError
from cloudinary.uploader import upload

def get_users_data():
    users = UserInfo.objects.all()

    return users

def add_user_data(username, email, password, image):
    if not username or not email or not password:
        raise ValidationError("Thiếu thông tin bắt buộc!")

    if UserInfo.objects.filter(username=username).exists():
        raise ValidationError("Username đã tồn tại!")

    if UserInfo.objects.filter(email=email).exists():
        raise ValidationError("Email đã tồn tại!")

    # Xử lý upload ảnh (nếu có)
    image_url = None
    if image:
        try:
            upload_result = upload(image)
            image_url = upload_result['url']
        except Exception as e:
            raise ValueError(f"Lỗi khi tải ảnh lên Cloudinary: {str(e)}")

    # Tạo bản ghi người dùng
    return UserInfo.objects.create(
        username=username,
        email=email,
        password=password,
        image=image_url,
        courses=None,
        target=None,
        study=None
    )