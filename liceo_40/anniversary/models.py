from django.db import models


class Promotion(models.Model):
    NUMBERS = [
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
        (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16),
        (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23),
        (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30),
        (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37),
        (38, 38), (39, 39), (40, 40), (41, 41), (42, 42),
    ]
    number = models.SmallIntegerField(
        choices=NUMBERS,
        unique=True,
        verbose_name='número'
    )

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "promoción"
        verbose_name_plural = "promociones"


class Cadet(models.Model):
    last_name = models.CharField(max_length=128, verbose_name="apellido")
    first_name = models.CharField(max_length=128, verbose_name="nombre")
    dni = models.IntegerField(unique=True, verbose_name="DNI")
    promotion = models.ForeignKey(
        "anniversary.Promotion",
        on_delete=models.CASCADE,
        verbose_name="promoción")

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "cadete"
        verbose_name_plural = "cadetes"
