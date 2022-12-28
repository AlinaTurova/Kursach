from django.db import models

# Create your models here.
class Statement(models.Model):
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

    def __str__(self):

        return ("%s %s %s %s %s %s %s %s %s %s %s %s %s %s") % (self.directorinst, self.directorfiliala, self.group, self.fio, self.vsvazy, self.doc1, self.doc2,
         self.doc3, self.d, self.month, self.year, self.nasnachits, self.nasnachits, self.nasnachitpo, self.nasnachenas, self.nasnachenapo,
        self.dp, self.monthp, self.yearp, self.fioup, self.d2, self.month2, self.year2,)