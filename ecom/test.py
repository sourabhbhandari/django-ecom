from django_seed import Seed

seeder = Seed.seeder()

from api.user.models import CustomUser
from api.order.models import Order
seeder.add_entity(CustomUser, 5)
seeder.add_entity(Order, 10)

inserted_pks = seeder.execute()
