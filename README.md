# Get current CPU load, memory usage and execution time.

excec-time-test is a small utility to retrieve the current system and measure it's own execution time. This is how you install and use it on an IoTmaxx gateway.

    usage: python -m exec_time_test [-h] [-i <num>] [-s <s>]

    get the current load of a linux system

    options:
      -h, --help                    show this help message and exit
      -i <num>, --iterations <num>  # of iterations (default: 1)
      -s <s>, --sleep <s>           time(s) between iterations (default: 0.1)

    Copyright (C) 2025 IoTmaxx GmbH

## Run on IoTmaxx Gateway

### Copy folder exec_time_test to /data/p1 on the gateway.

    scp -r exec_time_test/ root@192.168.1.1:/data/p1

### Interactive execution via ssh

    ssh root@192.168.1.1 "cd /data/p1;python -m exec_time_test"

### Non interactive execution via ssh

To remove the need for interactive authorization pre-shared keys can be used. To do so gateway and host have to be prepared as described in the following paragraph.

#### On the IoTmaxx gateway

Following steps have to be executed on the gateway.

##### Create ssh directory in /config partition.

```
mkdir -p /config/ssh/.ssh && chmod 700 /config/ssh/.ssh
```
```
touch /config/ssh/.ssh/authorized_keys && chmod 600 /config/ssh/.ssh/authorized_keys
```

##### Link ssh directory to /config partition

```
mount -o remount,rw /
```
```
ln -s /config/ssh/.ssh /root/.ssh
```
```
mount -o remount,ro /
```

Please be aware that currently firmware updates on the gateway will remove the symbolic link from /root/.ssh to /config/ssh/.ssh annd this step has to be repeated. Future firmware versions will contain this link and repeating this step will no longer be necessary.

#### On the host computer

This shows how the host computer is prepared.

##### Create dedicated ssh key pair for gateway access on host computer

```
mkdir -p ~/.ssh
```
```
ssh-keygen -t rsa -N "" -C "gateway access key" -f ~/.ssh/gw_rsa
```

##### Copy public key to gateway
    cat ~/.ssh/gw_rsa.pub | ssh root@192.168.1.1 "cat >> ~/.ssh/authorized_keys"

##### Execute command
    ssh -i ~/.ssh/gw_rsa root@192.168.1.1 "cd /data/p1;python -m exec_time_test"

## Hint

In case you intent to connect to different gateways (with different host keys)from the same host you can add the following to ~/.ssh/config (create if not exists) to avoid ssh complaining about changed host keys:

    Host 192.168.1.1
    	StrictHostKeyChecking no
    	UserKnownHostsFile /dev/null

Please be aware that this is considered insecure and would allow for man-in-the-middle attacks (you might be willing to accept this risk for gateways connected to your local LAN or directly to the host)
