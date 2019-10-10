# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Department(models.Model):
    iddepartment = models.CharField(db_column='idDepartment', primary_key=True, max_length=3)  # Field name made lowercase.
    departmentname = models.CharField(db_column='DepartmentName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    departmentcomment = models.CharField(db_column='DepartmentComment', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Person(models.Model):
    idperson = models.CharField(db_column='idPerson', primary_key=True, max_length=8)  # Field name made lowercase.
    personpho = models.TextField(db_column='PersonPho', blank=True, null=True)  # Field name made lowercase.
    personname = models.CharField(db_column='PersonName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    personbirthdate = models.DateField(db_column='PersonBirthDate', blank=True, null=True)  # Field name made lowercase.
    personnation = models.CharField(db_column='PersonNation', max_length=5, blank=True, null=True)  # Field name made lowercase.
    personpoliticaloutlook = models.CharField(db_column='PersonPoliticalOutlook', max_length=6, blank=True, null=True)  # Field name made lowercase.
    personismarry = models.IntegerField(db_column='PersonIsMarry', blank=True, null=True)  # Field name made lowercase.
    persontitle = models.CharField(db_column='PersonTitle', max_length=10, blank=True, null=True)  # Field name made lowercase.
    personcolmajor = models.CharField(db_column='PersoncolMajor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    personeducation = models.CharField(db_column='PersonEducation', max_length=2, blank=True, null=True)  # Field name made lowercase.
    persongraduationschool = models.CharField(db_column='PersonGraduationSchool', max_length=10, blank=True, null=True)  # Field name made lowercase.
    persongraduationdate = models.DateField(db_column='PersonGraduationDate', blank=True, null=True)  # Field name made lowercase.
    personbasesalary = models.DecimalField(db_column='PersonBaseSalary', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    personidnumber = models.CharField(db_column='PersonIDNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    persondepartementnum = models.ForeignKey(Department, models.DO_NOTHING, db_column='PersonDepartementNum', blank=True, null=True)  # Field name made lowercase.
    personworkposition = models.CharField(db_column='PersonWorkPosition', max_length=10, blank=True, null=True)  # Field name made lowercase.
    personteam = models.CharField(db_column='PersonTeam', max_length=10, blank=True, null=True)  # Field name made lowercase.
    personadmissiondate = models.DateField(db_column='PersonAdmissionDate', blank=True, null=True)  # Field name made lowercase.
    personparticipatedate = models.DateField(db_column='PersonParticipateDate', blank=True, null=True)  # Field name made lowercase.
    personcategory = models.CharField(db_column='PersonCategory', max_length=3, blank=True, null=True)  # Field name made lowercase.
    personcolcontractperiod = models.IntegerField(db_column='PersoncolContractPeriod', blank=True, null=True)  # Field name made lowercase.
    personfamilyaddress = models.CharField(db_column='PersonFamilyAddress', max_length=45, blank=True, null=True)  # Field name made lowercase.
    personcontactinformation = models.CharField(db_column='PersonContactInformation', max_length=11, blank=True, null=True)  # Field name made lowercase.
    personcomment = models.CharField(db_column='PersonComment', max_length=45, blank=True, null=True)  # Field name made lowercase.
    persongender = models.CharField(db_column='PersonGender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    personstate = models.CharField(db_column='PersonState', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person'


class Salary(models.Model):
    idsalary = models.AutoField(db_column='idSalary', primary_key=True)  # Field name made lowercase.
    salarycardnumber = models.CharField(db_column='SalaryCardNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salaryidperson = models.ForeignKey(Person, models.DO_NOTHING, db_column='SalaryidPerson', blank=True, null=True)  # Field name made lowercase.
    salarybase = models.DecimalField(db_column='SalaryBase', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryworkyears = models.IntegerField(db_column='SalaryWorkYears', blank=True, null=True)  # Field name made lowercase.
    salaryworkyearsallowance = models.DecimalField(db_column='SalaryWorkYearsAllowance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryfoodsubsidy = models.DecimalField(db_column='SalaryFoodSubsidy', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryman_hourcompletionrate = models.CharField(db_column='SalaryMan-hourCompletionRate', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salaryqualityvetocoefficient = models.CharField(db_column='SalaryQualityVetoCoefficient', max_length=5, blank=True, null=True)  # Field name made lowercase.
    salaryattendancedays = models.IntegerField(db_column='SalaryAttendanceDays', blank=True, null=True)  # Field name made lowercase.
    salarybasicpay = models.DecimalField(db_column='SalaryBasicPay', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarycolworksubsidy = models.DecimalField(db_column='SalarycolWorkSubsidy', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryhousesubsidy = models.DecimalField(db_column='SalaryHouseSubsidy', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryhealthfee = models.DecimalField(db_column='SalaryHealthFee', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarynightsnackfee = models.DecimalField(db_column='SalaryNightSnackFee', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryovertimefee = models.DecimalField(db_column='SalaryOvertimeFee', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarymaternityleave = models.IntegerField(db_column='SalaryMaternityLeave', blank=True, null=True)  # Field name made lowercase.
    salaryflexiblesubsidy = models.DecimalField(db_column='SalaryFlexibleSubsidy', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryflexiblededuction = models.DecimalField(db_column='SalaryFlexibleDeduction', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryteamsubsidy = models.DecimalField(db_column='SalaryTeamSubsidy', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarypayable = models.DecimalField(db_column='SalaryPayable', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryinsurancemoney = models.DecimalField(db_column='SalaryInsuranceMoney', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarypayfund = models.DecimalField(db_column='SalaryPayFund', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryincometax = models.DecimalField(db_column='SalaryIncomeTax', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarydeduction = models.DecimalField(db_column='SalaryDeduction', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryhousefee = models.DecimalField(db_column='SalaryHouseFee', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarwaterfee = models.DecimalField(db_column='SalarWaterFee', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryelectricityfee = models.DecimalField(db_column='SalaryElectricityFee', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salaryreal = models.DecimalField(db_column='SalaryReal', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarycomment = models.CharField(db_column='SalaryComment', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salary'
