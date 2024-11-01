# this will give admin privileges 


from admin_solo_class import *


admin = Admin("Derian", "Arroyo", "19", "Latino", "Male", 'Can add post', 'Can delete post', 'Can ban user')

admin.describe_user()
admin.greet_user()
admin.privilege()