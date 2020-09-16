# Zat'nik'tel (zat)

Much like its Stargate namesake, **zat** is a process manager with the following behavior:

* 1st shot 'stuns' (suspends) the process
* 2nd shot kills the process
* 3rd shot disintegrates the underlying command (or at least tries to)

```
$ ps a | grep sloth | grep -v grep
12416 s003  S+     0:00.05 sloth 100ms
$ zat 12416
suspending 12416 sloth
$ zat 12416
killing 12416 sloth
$ zat 12416
disintegrating /usr/local/bin/sloth
$ sloth
-bash: sloth: command not found
```

_NOTE: I have only seen two seasons of SG-1 thus far. Please do not post spoilers via Issues, Pull Requests, etc._
