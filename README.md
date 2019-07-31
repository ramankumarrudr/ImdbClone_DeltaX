# ImdbClone_DeltaX
This Project is developed as a selection process for Deltax. It Contains the basic requirements that are mentioned by the company. The entire project is developed using Django(MVCT) Faramework.Users can add movies and actors and Tv-shows and can edit them and delete if they have the root privilages. More Documentation will be available in Documentation.txt file.This project has two versions 1)This version allows the user deploy the app using Docker Server. 2)Run on local host with installing required dependencies as pip install and run the python manage.py command from the imdb_clone directory.(Better to run it as a docker file 
as it reduces your burden)
# Note1) for entering multiple actors in movie form use - (ctr+left mouse click)
# Note2) In forms use DOB and Year-of-Release feilds informat (yyyy-mm-dd) - 1986-7-16 i.e 16th july 
# Note 3) if you are using docker please do use sudo every time you run the docker-compose command
# Note 4) For deleting records you need to login to the /admin/ page . For creating user name and password you can use createsuper command as mentioned below.
# Clone the git Repo
# Method 1(Using docker-compose)

Install Docker
```
$ sudo apt install docker.io
```
Test Docker using this command:
```
$ docker run hello-world
```
Install Docker-composer
```
$ sudo apt install docker-compose
```
Navigate to src_docker_version(in the cloned Repo)
```
$ cd src_docker_version
```
Run docker-compose and build in thid directory containing the yaml file
# This is where you will be working
# run as root
```
src_docker_version/$sudo chown -R $USER:$USER imdb_clone/manage.py (give permissions)
src_docker_version/$sudo chown -R $USER:$USER imdb_clone/imdb_clone/
src_docker_version/$ sudo docker-compose build  (Takes Some time)
src_docker_version/$ sudo docker-compose up  (This will run the django imdb_clone @ http://0.0.0.0:8000) 
```
You can edit and add movies , tvshows and actors using this app.To delete you need to be superuser you can do that by navigating to   
(http://0.0.0.0:8000/admin/) username - root , password = rootuser 
You can also create your own super user by using
```
src_docker_version/$ sudo docker-compose run web python3 manage.py createsuperuser
```
You can do migrations to database using (perform only if you want to make an edit to the db models created by me)
```
src_docker_version/$ sudo docker-compose run web python3 manage.py makemigrations
src_docker_version/$ sudo docker-compose run web python3 manage.py migrate
```

# Method 2(run using python manage.py runserver)
Install pip:
```
$ sudo apt install python3-pip
```
Install python packages:
```
$ pip3 install -r requirement.txt
```
Navigate To src/imdb_clone/ (It will be the working directory)

```
$ cd src/imdb_clone/
```

Run python server which will be running at (http://127.0.0.1:8000)
```
src/imdb_clone/$ python3 manage.py runserver (Runs server @ http://127.0.0.1:8000)
```
Now you can acess the imdb_clone mvc app at http://127.0.0.1:8000
for admin page you can navigate to http://127.0.0.1:8000/admin/

# Aditional Usefull commands
 - python3 manage.py createsuperuser (creates a root account for acessing database internals and deleting records) 
 - python3 manage.py makemigrations (For migrating models and making changes)
 - python3 manage.py migrate (for migrating changes made using makemigrations)

