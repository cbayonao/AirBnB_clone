# AirBnB_clone
![Image of HBnB Clone](https://github.com/cbayonao/AirBnB_clone/blob/master/hbnb_clone.png?raw=true)
In this project we build a console to be able to manage the objects of our project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object


# Description of the project
BACKEND
HBNB CONSOLE
# Description of the command interpreter

## How to start it
```
# We will clone the repo locally
git clone https://github.com/cbayonao/AirBnB_clone.git && cd AirBnB_clone
# Now we will execute it
./console.py
```
```
 (hbnb)
```
## How to use it
### Getting help about commands
```
(hbnb) ?

Documented commands (type help <topic>):
========================================
EOF all create destroy help quit show update
(hbnb) ? EOF
Exit program at End Of File (EOF)
(hbnb) help EOF
Exit program at End Of File (EOF)
```
### All
Prints all string representation of all instances based or not on the class name.
```
# Return all classes according to your name or simply all classes
(hbnb) all <classname>
(hbnb) all
```
##### Examples
```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```
### Create

Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
```
(hbnb) create
** class name missing **
(hbnb) create class_that_does_not_exist
** class doesn't exist **
```
##### Examples
```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```
### Destroy
Deletes an instance based on the class name and `id` (save the change into the JSON file).
Usage:
`destroy <classname> <uuid>`
##### Examples
```
If the class name is missing
(hbnb) destroy
** class name missing **

If the class name doesn’t exist
(hbnb) destroy MyModel
** class doesn't exist **

If the `id` is missing
(hbnb) destroy BaseModel
** instance id missing **

If the instance of the class name doesn’t exist for the `id`
(hbnb) destroy BaseModel 121212
** no instance found **

Else: success don't return nothing
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
```
### Quit
To exit the program
##### Examples
```
(hbnb) quit
```
### Show
Prints the string representation of an instance based on the class name and `id`.
Usage:
`show <classname> <uuid>`
##### Examples
```
If the class name is missing
(hbnb) show
** class name missing **

If the class name doesn’t exist
(hbnb) show MyModel
** class doesn't exist **

If the `id` is missing
(hbnb) show BaseModel
** instance id missing **

If the instance of the class name doesn’t exist for the `id`
(hbnb) show BaseModel 121212
** no instance found **

Else: success return the representation of an instance
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
### Update
Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file).
-   Only one attribute can be updated at the time
-   You can assume the attribute name is valid (exists for this model)
-   The attribute value must be casted to the attribute type

`id`,  `created_at`  and  `updated_at`  cant’ be updated.

Usage:
`update <classname> <uuid> <attribute> <value>`
##### Examples
```
If the class name is missing
(hbnb) update
** class name missing **

If the class name doesn’t exist
(hbnb) update MyModel
** class doesn't exist **

If the  `id`  is missing
(hbnb) update BaseModel
** instance id missing **

If the instance of the class name doesn’t exist for the  `id`
(hbnb) update BaseModel 121212
** no instance found **

If the attribute name is missing
(hbnb) update BaseModel existing-id
** attribute name missing **

If the value for the attribute name doesn’t exist
(hbnb) update BaseModel existing-id first_name
** value missing **
```
### Objects
These are the objects that you can manipulate with the console

| Objects       | Description                    |
|----------------|-------------------------------|
|User              |User that reserve            |
|Place             |Place that is reserved       |
|City              |City where the place is located|
|State             |Country where the place is located|
|Amenity           |Characteristics of the place |
|Review            |Comments from other users    |


### Authors
---
## Collaborators
[John Alexander Urrego Sandoval](https://github.com/mateo-a)
[Camilo Bayona Orduz](https://www.bayona.me/)
