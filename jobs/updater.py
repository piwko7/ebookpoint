from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import scrap_ebookpoint

def start():
	scheduler = BackgroundScheduler()

	if settings.SEND_PUSH is True:
		scheduler.add_job(scrap_ebookpoint, 'cron', hour=settings.CRONE_HOUR, minute=settings.CRONE_MINUTE)
	scheduler.start()

