import os
from toy_tribe import app




if __name__ ==  "__main__":
    app.run(
        host= os.environ.get("IP"),
        port= int(os.environ.get("PORT")),
        debug = os.environ.get("DEBUG")
    )
