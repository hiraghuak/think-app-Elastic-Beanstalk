from django.db import models


class entrepreneurmodel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class businessmodel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class generalmodel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class faqresultmodel(models.Model):
    entrepreneurmy = models.ManyToManyField(entrepreneurmodel, related_name='entrepreneur')
    businessmy = models.ManyToManyField(businessmodel, related_name='business')
    generalmy = models.ManyToManyField(generalmodel, related_name='general')


