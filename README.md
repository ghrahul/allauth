# allauth
A django restframework and  allauth with enabled Social auth
--
signin functionality== http://127.0.0.1:8000/accounts/login/  (while locally hosted)

![screenshot 125](https://user-images.githubusercontent.com/22416933/38640765-cfcc8f1e-3df2-11e8-9c63-1584c4a76a85.png)
--
signup funtionality == http://127.0.0.1:8000/accounts/signup/ (while locally hosted)


![screenshot 126](https://user-images.githubusercontent.com/22416933/38640833-04496bfe-3df3-11e8-862e-49c3848d6ce5.png)

--
Also there are other functionalities like password reset email confirmation.

--
userlist api--
--api for users data communication


get functionality--

![screenshot 141](https://user-images.githubusercontent.com/22416933/38683941-3017eb18-3e8c-11e8-98cf-c1e6c897210c.png)


post functionality--

![screenshot 147](https://user-images.githubusercontent.com/22416933/38684268-ee4078da-3e8c-11e8-898b-f6009b5ba466.png)

delete functionality--

![screenshot 146](https://user-images.githubusercontent.com/22416933/38684130-a4db174a-3e8c-11e8-9d49-63d5d3836a8b.png)

put functionality--

![screenshot 145](https://user-images.githubusercontent.com/22416933/38684097-8f2c8c94-3e8c-11e8-8fcd-34bd0d785189.png)



framework design
  Model==# This is an example model where i have implemented all the functions(get,put,post,delete) explicitly
      
    
      from django.db import models
      from django.db import models
      class Country(models.Model):
          name = models.CharField(max_length=20)
          capital = models.CharField(max_length=20)
          president = models.CharField(max_length = 20)
          def __str__(self):
              return self.name
        
--
framework==

   get and post == http://127.0.0.1:8000/country/  (while locally hosted)
     get==
     ![screenshot 127](https://user-images.githubusercontent.com/22416933/38641212-202f6458-3df4-11e8-9eb7-04e87b359bbf.png)
     
     
   post==
     
     
   ![screenshot 128](https://user-images.githubusercontent.com/22416933/38641347-5dfd4002-3df4-11e8-84aa-3bfc64959323.png)

   delete and put== http://127.0.0.1:8000/country/(give primary key number)/  (while locally hosted)
     delete==
     
     
   ![screenshot 129](https://user-images.githubusercontent.com/22416933/38641405-8912f8fe-3df4-11e8-8f29-7450454de91a.png)
     
     Put==
     
     
   ![screenshot 129](https://user-images.githubusercontent.com/22416933/38641405-8912f8fe-3df4-11e8-8f29-7450454de91a.png)

django administration

![screenshot 131](https://user-images.githubusercontent.com/22416933/38641892-ec098486-3df5-11e8-9140-0fec792e528e.png)

    
