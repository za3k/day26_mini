run-debug:
	flask --debug run
run-demo:
	gunicorn3 -e SCRIPT_NAME=/hackaday/mini --bind 0.0.0.0:8026 app:app
