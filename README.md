# webapp_initializer
### aka wapi 
#### (not to be confused with with the [World Association of Professional Investigators](https://www.wapi.com)

## What does it do
This tool exists to reduce the friction of starting little sideprojects
Just give it an application name (no spaces) with a path to put it (relative to home, dirs don't need to exist but they can)
and it generate the startercode for a Flask, React, Sqlite3 webapp. 
It's probably best for SPAs but you can extend the code it generates however you want

## How is it used
first clone the repo wherever you like and cd into it 
I recomend installing in a virtual enviroment to keep things tidy. 

```
➜  python3 -m venv env  # create a virtual enviroment called 'env'
➜  source env/bin/activate  # activate it
(env) ➜ pip install -e .  # install wapi
```

now so long as the enviroment is active, you can use wapi like so 
```
wapi "<dir_relative_to_home_for_project>" "<side_project_name>"
```
for example:
```
(env) ➜  wapi "Documents/projects/landing_page" "site"
```
now we can deactivate the virtual enviroment for wapi and navigate to the dir for our new project
```
(env) ➜  deactivate
➜  cd ~/Documents/projects/landing_page
```
now to get the application up and running
```
➜  chmod +x ./bin/*
➜  ./bin/install # TODO this might be flaky
➜  source env/bin/activate
(env) ➜  ./bin/run
```
now we can navigate to localhost in the browser to see a page rendered by our starter application that explains how it works a little further
![starter page](https://imgur.com/a/urR3EAW)

## How it works
todo
