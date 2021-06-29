from app import application
from views import WaterBucketView
from config import settings

application.add_url_rule(
    "/water-bucket", view_func=WaterBucketView.as_view("user-login")
)

if __name__ == "__main__":
    application.run(debug=settings.DEBUG, port=settings.PORT)
