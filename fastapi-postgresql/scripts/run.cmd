cd ..

python -m venv venv
call venv/scripts/activate

pip install -r requirements.txt

uvicorn main:app --reload

cmd