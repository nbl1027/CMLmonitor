# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Ablresutqc(models.Model):
    ablresutqcid = models.AutoField(primary_key=True)
    sampleid = models.ForeignKey('Samples', models.DO_NOTHING, db_column='sampleid', blank=True, null=True)
    ablanalysis = models.FloatField(blank=True, null=True)
    totalcheck = models.IntegerField(blank=True, null=True)
    individualcheck = models.IntegerField(blank=True, null=True)
    qcresult = models.ForeignKey('Passfail', models.DO_NOTHING, db_column='qcresult', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ablresutqc'


class Analysistype(models.Model):
    analysistypeid = models.AutoField(primary_key=True)
    analysistype = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysistype'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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


class Controlresults(models.Model):
    controlresultid = models.AutoField(primary_key=True)
    controltypeid = models.ForeignKey('Controltype', models.DO_NOTHING, db_column='controltypeid', blank=True, null=True)
    resulttypeid = models.ForeignKey('Resulttype', models.DO_NOTHING, db_column='resulttypeid', blank=True, null=True)
    wellnumber = models.CharField(max_length=45, blank=True, null=True)
    controlct = models.FloatField(blank=True, null=True)
    controlctmean = models.FloatField(blank=True, null=True)
    controlquant = models.FloatField(blank=True, null=True)
    controlquantmean = models.FloatField(blank=True, null=True)
    controlctthresh = models.FloatField(blank=True, null=True)
    controlbasestart = models.FloatField(blank=True, null=True)
    controlbaseend = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controlresults'


class Controltype(models.Model):
    controltypeid = models.AutoField(primary_key=True)
    controltype = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controltype'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Passfail(models.Model):
    passfailid = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passfail'


class Patientinfo(models.Model):
    patientinfoid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nhsnumber = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    postcode = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patientinfo'


class Plate(models.Model):
    plateid = models.AutoField(primary_key=True)
    dateofrun = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plate'


class Plate2Control(models.Model):
    plate2controlid = models.AutoField(primary_key=True)
    plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', blank=True, null=True)
    controlresultid = models.ForeignKey(Controlresults, models.DO_NOTHING, db_column='controlresultid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plate2control'


class Plate2Standard(models.Model):
    plate2standardid = models.AutoField(primary_key=True)
    plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', blank=True, null=True)
    standardresultid = models.ForeignKey('Standardresults', models.DO_NOTHING, db_column='standardresultid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plate2standard'


class Plateqc(models.Model):
    plateqcid = models.AutoField(primary_key=True)
    plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', blank=True, null=True)
    resulttypeid = models.ForeignKey('Resulttype', models.DO_NOTHING, db_column='resulttypeid', blank=True, null=True)
    watercheck = models.IntegerField(blank=True, null=True)
    negcheck = models.IntegerField(blank=True, null=True)
    thresholdcheck = models.IntegerField(blank=True, null=True)
    baselinecheck = models.IntegerField(blank=True, null=True)
    poscheck = models.IntegerField(blank=True, null=True)
    stdcurve2050 = models.IntegerField(blank=True, null=True)
    stdcurvepoints = models.IntegerField(blank=True, null=True)
    slopecheck = models.IntegerField(blank=True, null=True)
    correlationcheck = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plateqc'


class Plateqcresult(models.Model):
    idplateqcresult = models.AutoField(primary_key=True)
    plateid = models.IntegerField(blank=True, null=True)
    passfailid = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plateqcresult'


class Qcreport(models.Model):
    qcreportid = models.AutoField(primary_key=True)
    plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', blank=True, null=True)
    qcreport = models.TextField(blank=True, null=True)
    reportstatusid = models.ForeignKey('Reportstatus', models.DO_NOTHING, db_column='reportstatusid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qcreport'


class Replicatect(models.Model):
    replicatectid = models.AutoField(primary_key=True)
    plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', blank=True, null=True)
    standardtypeid = models.ForeignKey('Standardtype', models.DO_NOTHING, db_column='standardtypeid', blank=True, null=True)
    resulttypeid = models.ForeignKey('Resulttype', models.DO_NOTHING, db_column='resulttypeid', blank=True, null=True)
    replicatect = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'replicatect'


class Reportstatus(models.Model):
    reportstatusid = models.AutoField(primary_key=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportstatus'


class Resultanalysis(models.Model):
    resultanalysisid = models.AutoField(primary_key=True)
    sampleid = models.ForeignKey('Samples', models.DO_NOTHING, db_column='sampleid', blank=True, null=True)
    bcrcopies = models.FloatField(db_column='BCRcopies', blank=True, null=True)  # Field name made lowercase.
    bcrablratio = models.FloatField(db_column='BCRABLratio', blank=True, null=True)  # Field name made lowercase.
    percentageratio = models.FloatField(blank=True, null=True)
    mr = models.CharField(max_length=5, blank=True, null=True)
    sensitivity = models.CharField(max_length=45, blank=True, null=True)
    statementsid = models.ForeignKey('Statements', models.DO_NOTHING, db_column='statementsid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resultanalysis'


class Resultreports(models.Model):
    resultreportsid = models.AutoField(primary_key=True)
    resultreport = models.TextField(blank=True, null=True)
    sampleid = models.ForeignKey('Samples', models.DO_NOTHING, db_column='sampleid', blank=True, null=True)
    reportstatusid = models.ForeignKey(Reportstatus, models.DO_NOTHING, db_column='reportstatusid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resultreports'


class Resulttype(models.Model):
    resulttypeid = models.AutoField(primary_key=True)
    resulttype = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resulttype'


class Sampleinfo(models.Model):
    sampleinfoid = models.AutoField(primary_key=True)
    taken = models.DateTimeField(blank=True, null=True)
    recieved = models.DateTimeField(blank=True, null=True)
    analysistypeid = models.ForeignKey(Analysistype, models.DO_NOTHING, db_column='analysistypeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sampleinfo'


class Sampleresult(models.Model):
    sampleresultid = models.AutoField(primary_key=True)
    resulttypeid = models.ForeignKey(Resulttype, models.DO_NOTHING, db_column='resulttypeid', blank=True, null=True)
    wellnumber = models.CharField(max_length=45, blank=True, null=True)
    samplect = models.FloatField(blank=True, null=True)
    samplectmean = models.FloatField(blank=True, null=True)
    samplequant = models.FloatField(blank=True, null=True)
    samplequantmean = models.FloatField(blank=True, null=True)
    samplectthresh = models.FloatField(blank=True, null=True)
    samplebasestart = models.FloatField(blank=True, null=True)
    samplebaseend = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sampleresult'


class Samples(models.Model):
    sampleid = models.AutoField(primary_key=True)
    samplenumber = models.CharField(max_length=45, blank=True, null=True)
    patientid = models.ForeignKey(Patientinfo, models.DO_NOTHING, db_column='patientid', blank=True, null=True)
    sampleinfoid = models.ForeignKey(Sampleinfo, models.DO_NOTHING, db_column='sampleinfoid', blank=True, null=True)
    resultreportsid = models.ForeignKey(Resultreports, models.DO_NOTHING, db_column='resultreportsid', blank=True, null=True)
    samplestatusid = models.ForeignKey('Samplestatus', models.DO_NOTHING, db_column='samplestatusid', blank=True, null=True)
    taken = models.DateField(blank=True, null=True)
    recieved = models.DateField(blank=True, null=True)
    activated = models.DateField(blank=True, null=True)
    authorised = models.DateField(blank=True, null=True)
    samtype = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'samples'


class Sampleseg(models.Model):
    samplesegid = models.AutoField(primary_key=True)
    sampleid = models.ForeignKey(Samples, models.DO_NOTHING, db_column='sampleid', blank=True, null=True)
    sampleresultid = models.ForeignKey(Sampleresult, models.DO_NOTHING, db_column='sampleresultid', blank=True, null=True)
    plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sampleseg'


class Samplestatus(models.Model):
    samplestatusid = models.AutoField(primary_key=True)
    samplestatus = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'samplestatus'


class Standardcurve(models.Model):
    standardcurveid = models.AutoField(primary_key=True)
    standardcurvedescription = models.CharField(max_length=45, blank=True, null=True)
    point1 = models.FloatField(blank=True, null=True)
    point2 = models.FloatField(blank=True, null=True)
    point3 = models.FloatField(blank=True, null=True)
    point4 = models.FloatField(blank=True, null=True)
    point5 = models.FloatField(blank=True, null=True)
    point6 = models.FloatField(blank=True, null=True)
    point7 = models.FloatField(blank=True, null=True)
    point8 = models.FloatField(blank=True, null=True)
    point9 = models.FloatField(blank=True, null=True)
    point10 = models.FloatField(blank=True, null=True)
    point11 = models.FloatField(blank=True, null=True)
    point12 = models.FloatField(blank=True, null=True)
    point13 = models.FloatField(blank=True, null=True)
    point14 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standardcurve'


class Standardcurvecriteria(models.Model):
    standardcurvecriteriaid = models.AutoField(primary_key=True)
    plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', blank=True, null=True)
    resulttypeid = models.ForeignKey(Resulttype, models.DO_NOTHING, db_column='resulttypeid', blank=True, null=True)
    slope = models.FloatField(blank=True, null=True)
    correlation = models.FloatField(blank=True, null=True)
    intercept = models.FloatField(blank=True, null=True)
    baseline3 = models.FloatField(blank=True, null=True)
    posdeltact = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standardcurvecriteria'


class Standardresults(models.Model):
    standardresultid = models.AutoField(primary_key=True)
    standardtypeid = models.ForeignKey('Standardtype', models.DO_NOTHING, db_column='standardtypeid', blank=True, null=True)
    resulttypeid = models.ForeignKey(Resulttype, models.DO_NOTHING, db_column='resulttypeid', blank=True, null=True)
    wellnumber = models.CharField(max_length=45, blank=True, null=True)
    standardct = models.FloatField(blank=True, null=True)
    standardctmean = models.FloatField(blank=True, null=True)
    standardquant = models.FloatField(blank=True, null=True)
    standardquantmean = models.FloatField(blank=True, null=True)
    standardctthresh = models.FloatField(blank=True, null=True)
    standardbasestart = models.FloatField(blank=True, null=True)
    standardbaseend = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standardresults'


class Standardtype(models.Model):
    standardtypeid = models.AutoField(primary_key=True)
    standardtype = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standardtype'


class Statements(models.Model):
    statementsid = models.AutoField(primary_key=True)
    statement = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statements'
