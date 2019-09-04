# Generated by Django 2.2.4 on 2019-09-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0087_v360_update_credential_injector_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='approval_notifications',
            field=models.ManyToManyField(blank=True, related_name='organization_approval_notifications', to='main.NotificationTemplate'),
        ),
        migrations.AddField(
            model_name='unifiedjobtemplate',
            name='approval_notifications',
            field=models.ManyToManyField(blank=True, related_name='unifiedjobtemplate_approval_notifications', to='main.NotificationTemplate'),
        ),
        migrations.AlterField(
            model_name='workflowjobnode',
            name='do_not_run',
            field=models.BooleanField(default=False, help_text='Indicates that a job will not be created when True. Workflow runtime semantics will mark this True if the node is in a path that will decidedly not be ran. A value of False means the node may not run.'),
        ),
    ]
