# -*- coding: utf-8 -*-
"""Create an application instance."""
from flaskshop.app import create_app

app = create_app()


if __name__ == "__main__":
    # Allows: `python app.py` (useful on Windows)
    app.run(debug=True)
