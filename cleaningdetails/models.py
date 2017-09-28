from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class accesslevels(models.Model):
    level=models.CharField(max_length=200)

    def __str__(self):
        return self.level

class hostellist (models.Model):
    hostelname=models.CharField(max_length=200)

    def __str__(self):
        return self.hostelname


class designations(models.Model):
    authoritystatus=models.CharField(max_length=200)

    def __str__(self):
        return self.authoritystatus


class total_authenticated_users(models.Model):
    hostel_name = models.ForeignKey(hostellist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )
    webmail_id =models.EmailField()
    access_level =models.ForeignKey(accesslevels, on_delete=models.CASCADE)

    class Meta:
            unique_together = ["hostel_name", "name", "designation"]

    def __str__(self):
        return '%s - %s - %s' % (self.name, self.hostel_name, self.designation)

class siang_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)

class manas_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)

class lohit_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)



class kapili_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)





class dhansiri_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)





class subansiri_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)





class dibang_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)




class dihing_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)



class brahmputra_authorities(models.Model):
    name = models.CharField(max_length=200)
    webmail_id =models.EmailField()
    designation= models.ForeignKey(designations, on_delete=models.CASCADE )

    class Meta:
           unique_together = ["name",  "designation"]

    def __str__(self):
        return '%s - %s' % (self.name,self.designation)
