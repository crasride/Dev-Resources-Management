<p align="center"> <img width="" height="" src="./docs/images/panel.png" </p>





# Introduction

This web application creates an online catalog for a small local library, where users can create, search, and manage resources stored on their computer or local network.

- The main features that have currently been implemented are:

  - There is a model for books with the following fields:
  - Techno, language, authors, year, image, pdf, description.

  - There is a template for CheatSheets with the following fields:
	  Techno, image, pdf and description.
  - There is an online search option.

<br></br>
<p align="left"> <img width="" height="" src="./docs/images/Data%20Modelling-1.jpg" </p>
<br></br>

These are the `Links` available about my project:
* [The deployed site](https://dev-resources-management.onrender.com/)
* [The blog post](https://medium.com/@4990/my-project-provides-programmers-a-document-management-solution-to-store-resources-about-programming-eed9d7a4b058)
* [The Author](https://www.linkedin.com/in/jd-fernandez)

<br></br>

# Installation

## To get this project up and running locally on your computer:

1) Set up the [Python development environment](https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04). We recommend using a Python virtual environment.

	Note: This has been tested against Django 4.1.6 (and may not work or be "optimal" for other versions).
<br></br>
2) Then clone the repository with the code:

```
crasride@ubuntu:~/$ git clone https://github.com/crasride/Dev-Resources-Management.git
```

3) Assuming you have your Python setup, run the following commands (if you're on Windows, you can use py or py-3 instead of python to start Python):

```
crasride@ubuntu:~/$ pip3 install -r requirements.txt
# Create a superuser Administrator
crasride@ubuntu:~/$ python3 manage.py createsuperuser
# Create a runtime server
crasride@ubuntu:~/$ python3 manage.py runtime server
```
<br></br>

# Usage

### User mode:
- Create a few test books of each type.
Open the tab at http://127.0.0.1:8000 to see the main site, with its new books.

You can then proceed to:

- Create a new user by accepting email, password, and username.

	- Once logged in, you will access the main menu.


      - `List` to list all the books in the database

      - `Search` to retrieve a list of all books by user or technology.

      - Create a `Books`

      - Create a `Cheat Sheet`

      - `Gallery` CheatSheet

      - `Online` to search for a book online connecting the result to Open Library
<br></br>
### Administrator mode:
- Open a browser at http://127.0.0.1:8000/admin/ to open the administration site.

	- Use the `user` created from the `createsuperuser` command




<br></br>

# Contributing

Me, `José Fernàndez` , I'm the only contributor


<br></br>

# Related projects
The projects made before that permits to create this MVP :

* [AirBnB clone](https://github.com/crasride/holbertonschool-AirBnB_clone_v4/tree/main/web_dynamic)



<br></br>

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

As far as possible according to the law, `Josè Fernàndez` has renounced all copyright and related rights over this work.




<br></br>

### About me:

<sub>_You can contact me_ 📩

[Fernandez Armas José Daniel](https://github.com/crasride)

<p align="left">
<a href="https://twitter.com/JosFern35900656" target="blank"><img align="center" src="./docs/images/twitter.svg" alt="crasride" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/jd-fernandez/" target="blank"><img align="center" src="./docs/images/linked-in-alt.svg" alt="crasride" height="30" width="40" /></a>
<a href="https://medium.com/@4990" target="blank"><img align="center" src="./docs/images/medium.svg" alt="@crasride" height="30" width="40" /></a>
<a href="https://discord.gg/José Fernandez Armas#7992" target="blank"><img align="center" src="./docs/images/discord.svg" alt="crasride" height="30" width="40" /></a>
</p>
