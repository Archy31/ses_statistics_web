init:
	venv/bin/activate
	pip install -r requirements.txt

run:
	cd back_gin/ && bash ./ses_back
	streamlit run ./frontmain.py

start:
	init
	run