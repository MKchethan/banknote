create env

conda create -n bank python=3.9 -y

activate env
conda activate bank

create a req file


install requirements
pip install -r requirements.txt

git init

dvc init

dvc add data_given/BankNote_Authentication.csv

git add .
git commit -m "first commit"


git add . && git commit -m "update README.md"

git remote add origin https://github.com/MKchethan/banknote.git
git branch -M main
git push origin main


git add . && git commit -m "params added"


touch src/get_data.py
python src/get_data.py


touch src/load_data.py
python src/load_data.py

dvc repro 

git add . && git commit -m "stage 1 completed"
git push origin main

dvc repro

git add . && git commit -m "stage 2 completed"
git push origin main


git add . && git commit -m "tracker is added"
git push origin main

dvc metrics diff

dvc metrics show

pip install -r requirements.txt

git add . && git commit -m "pytest and tox"
git push origin main

tox

touch setup.py


pip install -e .

