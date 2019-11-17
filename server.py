import os
from manage import app

port = os.getenv("PORT")
if __name__ == "__main__":
	app.run(port=port)
