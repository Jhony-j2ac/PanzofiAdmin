# build_files.sh 
#Este archivo fue generado como parte serverless en vercel, aca puedo configurar para instalar dependencias faltantes
pip install -r requirements.txt
pip3 install Django
python3.9 manage.py collectstatic