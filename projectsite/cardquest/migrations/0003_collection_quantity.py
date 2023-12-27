from django.db import migrations, models


def set_default_quantity(apps, schema_editor):
    Collection = apps.get_model('cardquest', 'Collection')
    for collection in Collection.objects.all():
        collection.quantity = 1  # Set an appropriate default value
        collection.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0002_pokemoncard_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RunPython(set_default_quantity),
    ]
