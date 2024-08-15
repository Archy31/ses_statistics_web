init:
	./venv/bin/activate
	pip install -r requirements.txt

run:
	uvicorn back:main:app --reload
	streamlit run front/main.py
