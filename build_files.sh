# build_files.sh 
#Este archivo fue generado como parte serverless en vercel, aca puedo configurar para instalar dependencias faltantes
yum install mysql-devel
pip install -r requirements.txt
pip3 install Django
pip3 install djangorestframework
pip3 install django-cors-headers==4.2.0
python3.9 manage.py collectstatic
# Confirm all alert messages during deployment
yes | vercel 