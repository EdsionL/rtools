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

pi = {
	'host':'-cmd-get_server_ip.sh',
	'port_ssh':'22',
	'user':'pi',
	'passwd':'',
}


def getip():
	return '127.0.0.1'

test = {
	'host':'-func-getip',
	'port_ssh':'22',
	'user':'pi',
	'passwd':'',
}

```

If you ip(domain) is often be changed,you can set up the 'host' like that.
> 'host':'-cmd-get_server_ip.sh'
> 
> or
> 
> 'host':'-func-getip',

The program will execute "get_server_ip.sh" or call 'getip' to get ip

## Usage
Goto the path of rtools. If you add the path of rtools to PATH, you can use rtools in any work path.

```
~> cd rtools
```
### SSH
Connect to host via ssh.

```
~> ./rssh blog  # ssh root@127.0.0.1
~> ./rssh route # ssh root@192.168.1.1

```

### SCP
You can copy files betwen two host

```
~> rscp -g blog "~/test.jpg" ~/    # Get test.jpg from remote host
~> rscp -p blog "~/test.jpg" "~/"  # Put test.jpg to remote host
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


# Changelog

1.1.1

* More options in 'rscp'. 
* Discover dynamic ip

1.1.0

* Parse arguments with argpase

More idea in NOTE.md