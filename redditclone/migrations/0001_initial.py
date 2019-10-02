# Generated by Django 2.2.5 on 2019-10-02 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(max_length=200)),
                ('rules', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RedditUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayname', models.CharField(max_length=30)),
                ('bio', models.TextField(max_length=200)),
                ('birthdate', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.URLField(max_length=250)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditclone.RedditUser')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditclone.Community')),
                ('post_dislikes', models.ManyToManyField(related_name='post_dislikes', to='redditclone.RedditUser')),
                ('post_likes', models.ManyToManyField(related_name='post_likes', to='redditclone.RedditUser')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditclone.Comment')),
                ('reddit_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditclone.RedditUser')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='banlist',
            field=models.ManyToManyField(related_name='banned', to='redditclone.RedditUser'),
        ),
        migrations.AddField(
            model_name='community',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditclone.RedditUser'),
        ),
        migrations.AddField(
            model_name='community',
            name='moderators',
            field=models.ManyToManyField(related_name='moderator', to='redditclone.RedditUser'),
        ),
        migrations.AddField(
            model_name='community',
            name='subscriber',
            field=models.ManyToManyField(related_name='subsribers', to='redditclone.RedditUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_dislikes',
            field=models.ManyToManyField(related_name='comment_dislikes', to='redditclone.RedditUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_likes',
            field=models.ManyToManyField(related_name='comment_likes', to='redditclone.RedditUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditclone.RedditUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redditclone.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='redditclone.Comment'),
        ),
    ]
