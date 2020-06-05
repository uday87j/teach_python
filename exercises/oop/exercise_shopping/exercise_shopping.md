# Simulate shopping experience

## Problem Statement

Take a learner through the process of creating a simulation of a few *Users* purchasing their *Shopping items*.

## Part 0

### Code Structure

`Person`, `Shop` and `World` are the three main classes. Rest of the classes exist to support the behaviour of these two concepts.

`Person`'s attributes:

* Gets money from somewhere
* Can `go` to a `Shop` to view the `items` it stores
* Purchases some `items` from one or more `Shop`

`Shop`'s attributes:

* Stores one or more items
* Accepts `visit` from one or more `Person`
* Allows purchasing of `items` by one or more `Person`

`World`'s attributes:

* Contains `n Person` and `m Shop` objects
* Allows interaction between any combination of `Person` and `Shop` objects

#### Goals

* Do not break APIs between versions, enhance them instead
* Use *duck-typing* appropriately to manage dependencies between classes
* Name `code_entities` very clearly
* Use `assert` generously
* Create **classes, objects and their relationships** meaningfully and not just to solve some small part of the problem. Always keep whether they make sense in the real world.
* Create *class hierarchy* and *object hierarchy* before solving a problem

## Part 1

### Things to do

* Add an API in `Person` to go and do some shopping
  * This will be invoked by `World`
* Add an API in `Shop` to enable purchasing of 1 or more items
* In `World::run()`, invoke `Person` to do shopping for five times with a gap of some small time
* Print `Person` available money before and after all the shopping is done
* Print `Shop` contents before and after all the shopping is done
* Print *shopping-profile* for each `Person`
  * Initial-balance, things-bought-and-their-price, Final-balance
