from django.db import models
from django.contrib.auth.models import User

class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile = models.CharField(max_length=200, null=True)

# class User(models.Model):
#
#     user_email = models.CharField(max_length=45, unique=True)
#     user_password = models.CharField(max_length=45)
#     user_nick_name = models.CharField(max_length=45, unique=True)
#     user_profile = models.CharField(max_length=200, null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user_nick_name
#
#     class Meta:
#         db_table = 'tbl_user'
#         ordering = ['-created_date']
#

#
# class Certificate(models.Model):
#
#     user=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     cert_no = models.CharField(max_length=45, null=False)
#     cert_name = models.CharField(max_length=45, null=False)
#
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'tbl_certificate'
#         ordering = ['-created_date']
#
