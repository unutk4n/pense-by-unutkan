Sqlite is not directly developed for client/server database engines such as MySQL or other ones. 
It's used for local data storages for individual projects.

# Situations Where SQLite Works Well

It works great with devices/ projects where no human control is needed. It's designed for projects that doesn't hava a datacenter.

It can also handle website request but it's not recommended. Sqlite can handle 10k clicks per day much or less.
It's experienced 10 times more traffic than this but it's better to keep it lower.

Data analysis

Cache for enterprise  data

server side database
    System designers report success using Sqlite as a data store on server applications running in the data center or in other words, using Sqlite as the underlying storage engine for an application-specific database server.


File archive and/ or data container.

Internal or temporary databases.

For programs that hava a lot of data that must be sifted and sorted in diverse ways, it is often easier and quicker to load the data into an in memory sqlite database and use querieswith joins and ORDER BY clauses to extract the data in the form and order needed rather than to try to code the same operations manually.


# TO SUM UP

## if you have many concurrent writers >> choose client/server.

## If you have big data > > choose client / server.

## if otherwise >> GO WITH SQLITE