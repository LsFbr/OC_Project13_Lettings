from django.db import migrations


def copy_addresses(apps, schema_editor):
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    NewAddress = apps.get_model("lettings", "Address")

    for old in OldAddress.objects.all():
        NewAddress.objects.create(
            id=old.id,
            number=old.number,
            street=old.street,
            city=old.city,
            state=old.state,
            zip_code=old.zip_code,
            country_iso_code=old.country_iso_code,
        )


def copy_lettings(apps, schema_editor):
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    NewLetting = apps.get_model("lettings", "Letting")

    for old in OldLetting.objects.all():
        NewLetting.objects.create(
            id=old.id,
            title=old.title,
            address_id=old.address_id,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    # Copy addresses first to avoid foreign key breaks
    operations = [
        migrations.RunPython(copy_addresses, migrations.RunPython.noop),
        migrations.RunPython(copy_lettings, migrations.RunPython.noop),
    ]