MPIFR Presto docker
===================

Pulling a built image
---------------------

If you are instead looking to simply pull the corresponding docker image, please use:

<pre><code> 
docker pull mpifrpsr/presto
</code></pre>

Building from Dockerfile
------------------------

If you wish to build directly from this repo, pull it and run the following:

<pre><code>
docker build -t "desired name for image" .
</code></pre>

The container can then be accessed in the normal ways.

Starting as a service
---------------------

If you have already build the image, you can start a container as a ssh service. This is necessary for those who want to use X11 forwarding to see the output from GUI applications.

To start the server, run the **start.py** script as so:

<pre><code>
./start.py docker-compose.yml
</code></pre>

This will call <pre><code>docker-compose -f docker-compose.yml up -d</code></pre> and then copy your public ssh keys into the container to allow for passwordless access as usr "psr".

Using the container with SSH
----------------------------

As noted above, the image comes with an OpenSSH server and X11 forwarding enabled. To use this from your machine effectively, it is recommended that you append the contents of the **ssh.cfg** file into your **~/.ssh/config** file. This will allways enable X11 forwarding and will ensure that your authorized hosts list does not become invalidated on restart of a container.



