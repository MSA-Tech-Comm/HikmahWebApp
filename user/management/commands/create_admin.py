'''Create an admin user'''
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from user.utils import ROLE_CHOICES

class Command(BaseCommand):
	help = 'Create an admin user'

	def add_arguments(self, parser):
		parser.add_argument('username', type=str)
		parser.add_argument('password', type=str)

	def handle(self, *args, **options):
		user = User.objects.get_or_create(role=4, 