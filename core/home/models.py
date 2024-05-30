from django.db import models

# Create your models here.
class PersonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    
 
APP_REF=('SOCIAL_MEDIA','GOOGLE','REFERAL','OTHER') 
GENDER=('MALE','FEMALE','MAN','WOMAN','SHE','HER','HIM','HE','NON-BINARY','TRANSGENDER','GENDER NEUTRAL','NON-CONFIRMING','PREFER NOT TO RESPOND','OTHER') 

CONDITIONS=('ATTENTION DEFICIT/ HYPERACTIVITY DISORDER (ADHD)','ABULIA','ADJUSTMENT DISORDER','AGORAPHOBIA','AMNESIA','ANTEROGRADE AMNESIA',
             'ANTISOCIAL PERSONALITY DISORDER','ALZHEIMER DISEASE','ANXIETY DISORDER','ASPERGERS SYNDROME','ATAXIA','ATTENTION DEFICIT DISORDER',
             'ATTENTIVENESS/ CONCENTRATION','AVOIDANT PERSONALITY DISORDER','AUDITORY PROCESSING DISORDER','AUDITORY SEQUENCING','BEHAVIORAL','BIPOLAR DISORDER',
             'BRAIN INJURY CAUSING BEHAVIORAL/ PERSONALITY CONGITIVE CHANGES','BORDERLINE INTELLECTUAL FUNCTIONING','BRUXISM','CATATONIC DISORDER') 

ETHNICITY = ('AFRICAN AMERICAN','AFRICAN','PACIFIC ISLANDER','ASIAN AMERICAN','NATIVE AMERICAN','EAST INDIAN','NATIVE HAWAIIANS',
             'HISPANIC AMERICAN','LATIN AMERICAN','ARAB AMERICAN','WHITE AMERICAN','OTHERS')

    
class UserDetailModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    otp = models.CharField(max_length=6, blank=True, default='')
    app_ref = models.CharField(choices=APP_REF, default='OTHER')
    app_ref_detail = models.TextField(blank=True,)
    address = models.TextField(blank=True,)
    precinct = models.TextField(blank=True,)
    gender = models.CharField(choices=GENDER, default='OTHER')
    gender_detail = models.CharField(max_length=100, blank=True)
    condition = models.CharField(choices=CONDITIONS)
    ethinicity = models.CharField(choices=ETHNICITY, default='OTHER')
    ethinicity_detail = models.CharField(max_length=100, blank=True)
    date_of_birth = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)
    driving_license_info = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    is_completed = models.BooleanField(default=False)