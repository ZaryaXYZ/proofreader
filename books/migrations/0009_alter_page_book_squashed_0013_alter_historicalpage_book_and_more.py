# Generated by Django 4.2.5 on 2023-10-22 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("books", "0009_alter_page_book"),
        ("books", "0010_remove_historicalpage_text_size_and_more"),
        ("books", "0011_historicalpage_number_in_book_page_number_in_book"),
        ("books", "0012_alter_historicalpage_number_in_book_and_more"),
        ("books", "0013_alter_historicalpage_book_and_more"),
    ]

    dependencies = [
        ("books", "0008_remove_historicalpage_processed_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to="books.book",
            ),
        ),
        migrations.RemoveField(
            model_name="historicalpage",
            name="text_size",
        ),
        migrations.RemoveField(
            model_name="page",
            name="text_size",
        ),
        migrations.AddField(
            model_name="historicalpage",
            name="number_in_book",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="Номер страницы в книге",
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="number_in_book",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="Номер страницы в книге",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpage",
            name="book",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="books.book",
                verbose_name="Книга",
            ),
        ),
        migrations.AlterField(
            model_name="historicalpage",
            name="number",
            field=models.IntegerField(verbose_name="Порядковй номер страницы"),
        ),
        migrations.AlterField(
            model_name="historicalpage",
            name="status",
            field=models.CharField(
                choices=[
                    ("processing", "Идет распознавание"),
                    ("redy", "Готово к вычитке"),
                    ("in_progress", "В процессе вычитки"),
                    ("done", "Вычитано"),
                ],
                default="processing",
                max_length=100,
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to="books.book",
                verbose_name="Книга",
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="number",
            field=models.IntegerField(verbose_name="Порядковй номер страницы"),
        ),
        migrations.AlterField(
            model_name="page",
            name="status",
            field=models.CharField(
                choices=[
                    ("processing", "Идет распознавание"),
                    ("redy", "Готово к вычитке"),
                    ("in_progress", "В процессе вычитки"),
                    ("done", "Вычитано"),
                ],
                default="processing",
                max_length=100,
                verbose_name="Статус",
            ),
        ),
    ]
