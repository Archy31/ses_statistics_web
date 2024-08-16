init:
	./venv/bin/activate
	pip install -r requirements.txt

run:
	cd back && uvicorn main:app --reload
	cd ../front streamlit run main.py

start:
	init
	run