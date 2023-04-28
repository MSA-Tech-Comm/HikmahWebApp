'''Create an admin user'''
from django.core.management.base import BaseCommand, CommandError
from user.models import User
from user.utils import ROLE_CHOICES

class Command(BaseCommand):
	help = 'Create an admin user'

	def add_arguments(self, parser):
		parser.add_argument('username', type=str)
		parser.add_argument('email', type=str)
		parser.add_argument('password', type=str)

	def handle(self, *args, **options):
		user = User.objects.get_or_create(username=options['username'],
                                    	  email=options['email'])[0]
		user.set_password(options['password'])
		user.save()

