# rtools
An command set for remote host management

## Installation
```
~> git clone git@github.com:malokch/rtools.git
~> cd rtools
~> cp rconfig-example.py rconfig.py
~> cp rcmd-example.py rcmd.py
```

Example of configuration(rconfig.py):

```
blog = {
	'host':'127.0.0.1',
	'port_ssh':'22',
	'user':'root',
	'passwd':'',
}

route = {
	'host':'192.168.1.1',
	'port_ssh':'22',
	'user':'root',
	'passwd':'',
}
```

## Usage
Goto the path of rtools. If you add the path of rtools to PATH, you can use rtools in any work path.

```
~> cd rtools
```
### SSH
Connect to host via ssh.

```
~> ./rssh blog # ssh root@127.0.0.1
~> ./rssh route # ssh root@192.168.1.1

```

### SCP
You can copy files betwen two host

```
~> rscp blog "~/test.jpg" # Get test.jpg from remote host
~> rscp blog "~/test.jpg" "~/" # Put test.jpg to remote host
```

### rcmd
Example of rcmd.py:

```
cmds = {
	'restart samba':'sudo service samba restart',
	'reboot':'reboot',
}
```

You can add more command to rcmd.py.

```
~> rcmd blog
0 : restart samba > sudo service samba restart
1 : reboot > reboot
3 : <Exit>
:1
Are you sure to execute the following command on 45.78.44.161?
> reboot
y/n:
```
If you input 'y' and ENTER, the host "blog" will reboot.

# More features
You can tell me, or one day I have the new idea.
