# Beego for Platform.sh

This template builds the Beego framework for Platform.sh.  It includes a minimalist application skeleton for demonstration, but you are free to alter it as needed.

Beego is a popular web framework written in Go.

## Services

* Go 1.13
* MariaDB 10.2

## Customizations

This project relies on Go module support in Go 1.11 and later.  You should commit your `go.mod` and `go.sum` files to Git, but not the `vendor` directory.

The following files and additions make the framework work.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional Go module, [`platformsh/config-reader-go`](https://github.com/platformsh/config-reader-go), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* The `conf` directory shows one way of exposing the Config Reader to the application.  You are free to take some other approach if you prefer.

## References

* [Beego](https://beego.me/)
* [Go on Platform.sh](https://docs.platform.sh/languages/go.html)
