# build_files.sh 
#Este archivo fue generado como parte serverless en vercel, aca puedo configurar para instalar dependencias faltantes
yum install mysql-devel
pip install -r requirements.txt
pip3 install Django==3.0.5
pip3 install djangorestframework==3.14.0
pip3 install django-cors-headers==3.2.0
#yes | python3.9 manage.py collectstatic
