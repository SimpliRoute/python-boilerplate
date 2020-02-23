# SimpliRoute's py3 boilerplate


#### Requirements

* Python 3.x installed
* virtualenv installed (associated with you py3 installation)
* pip installed (associated with you py3 installation)

#### Scripts included

##### **Init**
```bash
$ make init
```
Initialize application creating respective virtualenv and installing all 
dependencies form requirement txt. 

##### Update dependencies
```bash
$ make update-deps
```

Update dependencies in requirements.txt file
to future installs.

##### Running Test
```bash
$ make test
```

Run all application tests
 
##### Generate documentation

```bash
$ make documentation
```

Generate updated  documentation and open it on MAC

##### Run test generating coverage report

```bash
$ make coverage
```

Run tests and generate coverage report

### env variables
This boilerplate comes with [python-dotenv](https://pypi.org/project/python-dotenv/) 
as a dependency, env variables are declared and loaded from `settings.py` file,
if you want to add new env vars just create a .env file on on the
project root directory. 



 


