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
framework design
  Model==
      from django.db import models

    # This is an example model

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

    
