from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db.models import signals

def create_groups_and_permissions(sender, **kwargs):
    if sender.name == 'mydukaapp':
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from mydukaapp.models import CustomUser

        admin_group, _ = Group.objects.get_or_create(name='Admins')
        user_group, _ = Group.objects.get_or_create(name='Users')

        content_type = ContentType.objects.get_for_model(CustomUser)

        permission, _ = Permission.objects.get_or_create(
            codename='can_manage_products',
            name='Can manage products',
            content_type=content_type,
        )

        admin_group.permissions.add(permission)

signals.post_migrate.connect(create_groups_and_permissions)

