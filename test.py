from django_seed import Seed
seeder = Seed.seeder()
from api.category.models import Category
from api.product.models import Product
seeder.add_entity(Category,10)
seeder.add_entity(Product,10)
inserted_pks = seeder.execute()
seeder.add_entity(Category,10)
seeder.add_entity(Product,10)
inserted_pks = seeder.execute()
from api.user.models import CustomUser
from api.order.models import Order
seeder.add_entity(User,10)
from api.user.models import CustomUser
from api.order.models import Order
seeder.add_entity(CustomUser,10)
seeder.add_entity(Order,10)
inserted_pks = seeder.execute()





