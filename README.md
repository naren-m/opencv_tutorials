# OpenCV Tutorials

## Starting opencv3 Docker to run the tutorials

* Install [docker](https://docs.docker.com/engine/getstarted/step_one/#step-1-get-docker) on your system
* Git clone the [opencv_tutorials](https://github.com/naren-m/opencv_tutorials)

    ```bash
    mkdir opencv
    cd opencv
    git clone https://github.com/naren-m/opencv_tutorials.git
    ```

* Docker pull the narenm/opencv:py3 image

    ```bash
    docker pull narenm/opencv:py3
    ```

* Start the docker image

    ```bash
    docker run -it -v $PWD:/code -p 8888:8888 narenm/opencv:py3
    ```

In the docker prompt

* Start Jupyter in the docker and open the home page with token specified

    ```bash
    root@94cfd4075afc:/code# /run_jupyter.sh
    ```

After starting the jupyter notebook you will see the below

```bash
[I 13:33:26.360 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[W 13:33:26.377 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[I 13:33:26.389 NotebookApp] Serving notebooks from local directory: /code
[I 13:33:26.389 NotebookApp] 0 active kernels
[I 13:33:26.389 NotebookApp] The Jupyter Notebook is running at: http://[all ip addresses on your system]:8888/?token=72403e7797bcbab1ac32b7901f601f3f9ae75f82190ce036
[I 13:33:26.389 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 13:33:26.390 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
       http://localhost:8888/?token=72403e7797bcbab1ac32b7901f601f3f9ae75f82190ce036
```
