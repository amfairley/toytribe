import os
from toy_tribe import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
    )
