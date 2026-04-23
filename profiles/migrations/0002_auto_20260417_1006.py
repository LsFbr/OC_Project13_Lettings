from django.db import migrations


def copy_profiles(apps, schema_editor):
    """Copy existing Profile data from oc_lettings_site to the new profiles app."""

    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    NewProfile = apps.get_model("profiles", "Profile")

    for old in OldProfile.objects.all():
        
        if not NewProfile.objects.filter(user_id=old.user_id).exists():
            NewProfile.objects.create(
                id=old.id,
                user_id=old.user_id,
                favorite_city=old.favorite_city,
            )


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_profiles, migrations.RunPython.noop),
    ]