# build_files.sh 
#Este archivo fue generado como parte serverless en vercel, aca puedo configurar para instalar dependencias faltantes
yum install mysql-devel
pip install -r requirements.txt
pip3 install Django==4.2.3
pip3 install djangorestframework==3.14.0
pip3 install django-cors-headers==4.2.0
# mkdir -p /vercel/path0/static
# chmod +rwx /vercel/path0/static
# yes | python3.9 manage.py collectstatic
