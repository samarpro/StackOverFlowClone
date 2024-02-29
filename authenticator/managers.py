'''
File is Custom managers are defined
like objects
'''
from django.contrib.auth.base_user import BaseUserManager

class CustomModelManager(BaseUserManager):
    '''
    Custom model manager which creates user on the basis of email rather than username.
    '''

    def create_user(self,email=None,password=None,**kwargs):
        """
        self: model to which this manager is associated to.
        email,
        password
        """

        if email is None or password is None:
            raise AttributeError("Email and Password has to be provided. ")
        email = self.normalize_email(email)
        # creating a user with email
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**kwargs):
        '''
        self: object of model that manager is associated with
        '''
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        kwargs.setdefault('is_active',True)

        if email is None or password is None:
            raise AttributeError("Email and Password has to be provided. ")
        
        user = self.model(email=email)
        user.set_pasword(password)
        user.save()
        return user

