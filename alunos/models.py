from django.db import models

class Aluno(models.Model):
    CURSOS = [
        ('ADS', 'Análise e Desenvolvimento de Sistemas'),
        ('DIR', 'Direito'),
        ('ADM', 'Administração'),
        ('PED', 'Pedagogia'),
        ('ENF', 'Enfermagem'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()
    curso = models.CharField(max_length=3, choices=CURSOS)

    def __str__(self):
        return f"{self.nome} ({self.get_curso_display()})"
