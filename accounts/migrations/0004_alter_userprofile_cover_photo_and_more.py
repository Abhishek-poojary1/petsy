
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221105_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/users/cover_photo'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/users/profile_picture'),
        ),
    ]
