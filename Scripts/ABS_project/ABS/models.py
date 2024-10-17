from django.db import models
# from django import forms,Textarea
from django.forms import ModelForm, TextInput,EmailInput,PasswordInput
from django.utils import timezone

# Create your models here.
class App_User(models.Model):
    f_name = models.CharField(max_length=30)
    m_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()
    contact = models.IntegerField()
    password = models.CharField(max_length=30)
    Confirm_password = models.CharField(max_length=30)
    created = models.DateField(default=timezone.now)
    is_user = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

    class Meta:
        db_table = "user"

# class User_role(models.Model):
#     user = models.ForeignKey(User1, on_delete=models.CASCADE)
#     is_user = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)

    # class Meta:
    #     db_table = "user_role"


class UserForm(ModelForm):
    class Meta:
        model=App_User
        exclude = ['created','is_user','is_staff','is_admin']
        widgets={
            'username':TextInput(attrs={'class':'form-control','placeholder':"Enter Username",'autoComplete':"off",'onKeyup':"validateUName(this.value)"}),
            'f_name':TextInput(attrs={'class':'form-control','placeholder':"First"}),
            'm_name':TextInput(attrs={'class':'form-control','placeholder':"Middle"}),
            'l_name':TextInput(attrs={'class':'form-control','placeholder':"Last"}),
            'email':EmailInput(attrs={'class':'form-control','placeholder':"Enter email",'autoComplete':"off",'onKeyup':"validateEmail(this.value)"}),
            'contact':TextInput(attrs={'class':'form-control','placeholder':"Contact Number",'autoComplete':"off",'onKeyup':"validateContact(this.value)"}),
            'password':PasswordInput(attrs={'class':'form-control','placeholder':"Password",'autoComplete':"off",'onKeyup':"validatePassword(this.value)"}),
            'Confirm_password':PasswordInput(attrs={'class':'form-control','placeholder':"Confirm Password",'autoComplete':"off",'onKeyup':"validateC_Password(this.value)"})
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        contact = cleaned_data.get('contact')
        password = cleaned_data.get('password')
        Confirm_password = cleaned_data.get('Confirm_password')

        if username and (len(username)<8 or len(username)>15):
            self.add_error('username','username should not be less than 8 characters and more than 15 characters')
        

        def validate_digits_letters(word):
            for char in word:
                if not char.isdigit() and not char.isalpha():
                    return False
            return True
        
        def validate_password_letters(word):
            c=0
            u=0
            s=0
            for char in word:
                if char.isdigit():
                    c=c+1
                if char.isalpha():
                    s=s+1
                if char.isupper():
                    u=u+1
            if c>0 or u>0 or u>0:

                return True
            return False

        

        if not validate_digits_letters(username):
            self.add_error('username','Usernames contains characters that are not numbers nor letters')
            
        




        if contact and (len(str(contact))<10 or len(str(contact))>10):
            self.add_error('contact','Contact number should be 10 digits')


        if password and (len(password)<8 or len(password)>15):
            self.add_error('password','password should contain atlease one number one special character and one uppercase letter')

        if not validate_password_letters(password):
            self.add_error('password','password contains characters that are not numbers nor letters')


        if Confirm_password != password:
            self.add_error('Confirm_password','passwords do not match')

        return None


class ExtraUserDet(models.Model):
    user = models.OneToOneField(App_User, on_delete=models.CASCADE, primary_key=True)
    Addhar = models.CharField(max_length=50)
    Pan = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images',default='')

     
    
    class Meta:
        db_table = 'ExtraUserDetails'

class ExtraUserDetForm(ModelForm):
    class Meta:
        model = ExtraUserDet
        exclude = ['user']

class Image(models.Model):
    user = models.OneToOneField(App_User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='images',default='')

    class Meta:
        db_table = 'Image'

class ImageForm(ModelForm):
    class Meta:
        model = Image
        exclude = ['user']

desig=(
    ('Admin','Admin'),
    ('Manager','Manager'),
    ('Driver','Driver'),
    ('Cleaner','Cleaner'),
    ('Doctor','Doctor'),
    ('Nurse','Nurse'),


)



class Designation(models.Model):
    staf_id = models.IntegerField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50,choices=desig,default="")

    class Meta:
        db_table = 'Designation'

class Ambulance(models.Model):
    ambulance_id = models.IntegerField(primary_key=True)
    ambulance_name = models.CharField(max_length=50)
    ambulance_plate = models.CharField(max_length=15)
    doctor = models.CharField(max_length=50)
    cleaner = models.CharField(max_length=50)
    driver = models.CharField(max_length=50)
    isActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'Ambulance'

class AmbulanceForm(ModelForm):
    class Meta:
        model = Ambulance
        fields="__all__"

class Book(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.IntegerField()
    Addhar = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    curr_long = models.FloatField()
    curr_lat = models.FloatField()

    class Meta:
        db_table = 'Book'

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields="__all__"

class Accepted_rides(models.Model):
    accepted_by = models.CharField(max_length=50)
    accepted_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.IntegerField()
    Addhar = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pikup_long = models.FloatField()
    pikup_lat = models.FloatField()

    class Meta:
        db_table = 'Accepted_rides'