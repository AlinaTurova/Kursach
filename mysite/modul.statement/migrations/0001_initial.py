# Generated by Django 4.1.4 on 2022-12-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                directorinst = models.CharField(max_length=255, verbose_name="директору дирекции института")
                directorfiliala = models.CharField(max_length=255, verbose_name="Директору филиала")
                group = models.CharField(max_length=30, verbose_name="студента/rи группы")
                fio = models.CharField(max_length=30, verbose_name="ФИО")
                vsvazy = models.CharField(max_length=30, verbose_name="Прошу Вас рассмотреть вопрос о назначении мне государственной социальной стипендии в связи с")
                doc1 = models.CharField(max_length=30, verbose_name="Перечень документов для назначения государственной социальной стипендии, прилагаемых к заявлению документ 1")
                doc2 = models.CharField(max_length=30, verbose_name="документ 2")
                doc3 = models.CharField(max_length=30, verbose_name="документ 3")
                d = models.CharField(max_length=30, verbose_name="день")
                month = models.CharField(max_length=30, verbose_name="месяц")
                year = models.CharField(max_length=30, verbose_name="год")
                nasnachits = models.CharField(max_length=30, verbose_name="Назначить государственную социальную стипендию с")
                nasnachitpo = models.CharField(max_length=30, verbose_name="по")
                nasnachenas = models.CharField(max_length=30, verbose_name="Ранее государственная стипендия была назначена с")
                nasnachenapo = models.CharField(max_length=30, verbose_name="по")
                dp = models.CharField(max_length=30, verbose_name=" приказ от (день)")
                monthp = models.CharField(max_length=30, verbose_name="(месяц)")
                yearp = models.CharField(max_length=30, verbose_name="(год)")
                directorinst = models.CharField(max_length=30, verbose_name="дирекция института номер:")
                fioup = models.CharField(max_length=30, verbose_name="ФИО другого уполномоченного лица")
                d2 = models.CharField(max_length=30, verbose_name="день")
                month2 = models.CharField(max_length=30, verbose_name="месяц")
                year2 = models.CharField(max_length=30, verbose_name="год")
            ],
        ),
    ]