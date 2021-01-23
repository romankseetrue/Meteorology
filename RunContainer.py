# A Python library for the Docker Engine API
# pip install docker
import docker

def remove_container(container_name):
    client = docker.from_env()

    containers = [container.name for container in client.containers.list(all=True)]

    if container_name in containers:
        client.containers.get(container_name).remove(force=True)

def build_image(dockerfile_path, image_name):
    client = docker.from_env()
    client.images.build(path=dockerfile_path, tag=image_name)

def run_container(image_name, container_name):
    client = docker.from_env()
    client.containers.run(image_name, name=container_name, detach=True, tty=True, stdin_open=True)

if __name__ == "__main__":
    dockerfile_path = '.'
    image_name = 'roman.kushnirenk/meteorology'
    container_name = 'meteorology'

    remove_container(container_name)
    build_image(dockerfile_path, image_name)
    run_container(image_name, container_name)