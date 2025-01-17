# Express for Platform.sh

This template builds the Express framework for Platform.sh.  It includes a minimalist application skeleton for demonstration, but you are free to alter it as needed.

Express is a minimalist web framework written in Node.js.

## Services

* Node.js 10
* MariaDB 10.2

## Customizations

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional module, [`config-reader-nodejs`](https://github.com/platformsh/config-reader-nodejs), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.

## References

* [Express](https://expressjs.com/)
* [Node.js on Platform.sh](https://docs.platform.sh/languages/nodejs.html)
