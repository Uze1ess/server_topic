Thêm một file .env

Thêm các tham số sau
SECRET_KEY=;(+9=(\x0c%*\x0b*a"6CHyjC0v\\o[\n@fQH\'!tIl:P\t\r60l\x0c)d\nvBRF8c`<^\nF3-Y
DEBUG=True
DATABASE_URL=postgresql://137.66.10.99:5432/serverleaderbroadpostgre

File .gitignore
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/
tmp
.env
*.sqlite3
Dockerfile
fly.toml
tmp
.dockerignore
migrations
.venv

File .dockerignore

fly.toml
.git/
*.sqlite3
tmp
.venv
.env

Để test trên local. Hãy bỏ comment đoạn sau ở setting

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",  # Tên tệp cơ sở dữ liệu
#     }
# }