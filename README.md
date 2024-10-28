# skript

A collection of personal automation scripts for my known-repeatable tasks.

## Setup

- Create a new symbolic link of a script, or update an existing one.

```console
// create
ln -s source-path destination-path

// update
ln -sf source-path destination-path
```

NOTE: Enter the full path for the `source` and `destination` paths.

- Make the script file executable.

```console
chmod +x file
```

Or,

```console
chmod 755 file
```
