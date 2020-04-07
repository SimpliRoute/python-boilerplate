# SimpliRoute's py3 boilerplate


#### Requirements

* Python 3.x installed
* virtualenv installed (associated with you py3 installation)
* pip installed (associated with you py3 installation)

#### Scripts included

##### Rename project
[EN] After cloning the project, to rename the project it is necessary to change all the places tha contains the actual project name. For that, usually the IDEs provide ways to perform the refactor.

For PyCharm users follow the steps indicated on the [documentation](https://www.jetbrains.com/help/pycharm/renaming-projects.html). HINT: For experience, apparently, it is better to rename the project name and then the directory name.

Finally, to rename the auto-documentation, it is necessary to modify the file docs>source>index.rst. In the line 6 change *python-boilerplate* for the *new-project-name*.

##### Init
```bash
$ make init
```
Initialize application creating respective virtualenv and installing all dependencies form requirement txt. 

##### Update dependencies
```bash
$ make update-deps
```

Update dependencies in requirements.txt file to future installs.

##### Running Test
```bash
$ make test
```

Run all application tests
 
##### Generate documentation

```bash
$ make documentation
```

Generate updated documentation and open it on MAC

##### Run test generating coverage report

```bash
$ make coverage
```

Run tests and generate coverage report

### env variables
This boilerplate comes with [python-dotenv](https://pypi.org/project/python-dotenv/) as a dependency, env variables are declared and loaded from `settings.py` file, if you want to add new env vars just create a .env file on on the project root directory.



 


