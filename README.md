## Hello-world app 

That is my first DevOps practice. That app is stateless and just returns the hello-world as JSON, that's it.

The app was deployed on bare metal using home server. The requests is forwarded via NAT on mikrotik.

**The architecture:**
- 1 Ubuntu live server VM
- containerized using Docker

**CI/CD Pipeline**
- GitHub Actions
  - python-app.yml: builds and pushes docker image to DockerHub
  - deploy.yml: does ssh to the server, pulls the image and run it

## Additional info

This app does not exist now as I practice a lot on the server and I need memory, RAM and CPU. That's why CD will fail.

Also there are some Ansible inventory and k8s configuration files in the repo. It was done for test purposes and works only if manually applied, it was not included in CI/CD pipeline

