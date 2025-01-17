# Akeneo PIM Community Edition for Platform.sh

This template builds the Akeneo PIM system for Platform.sh.  It requires at least a Medium plan as it uses a Worker instance for queue processing.

Akeneo is a Product Information Management (PIM) tool, which acts as a central store for product information, catalog information, and inventory management.

## Services

* PHP 7.2
* MySQL 5.7
* Elasticsearch 6.5

## Post-install

1. The first time the site is deployed, Akeneo's command line installer will run and initialize the database.  It will not run again unless the `installer/.platform.installed` is removed.  (Do not remove that file unless you want the installer to run on the next deploy!)

2. The installer will create an administrator account with username/password `admin`/`admin`.  **You need to change this password immediately. Not doing so is a security risk**.

## Customizations

The following changes have been made relative to Akeneo as it is downloaded from Akeneo.com.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional Composer library, [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php), has been added.  It provides convenience wrappers for accessing the Platform.sh environment variables.
* [`config.yml`](/app/config/config.yml) - At the top of this file in the `imports` section, a new resource is added named `parameters_platform.php`.  That will load a PHP file rather than YAML file to specify Symfony configuration parameters.
* [`parameters_platform.php`](/app/config/parameters_platform.php) - This file contains Platform.sh-specific code to map environment variables into Symfony parameters. This file will be parsed on every page load. By default it only maps a default database and Elasticsearch connection parameters. You can add to it as needed.
* [`parameters.yml.dist`](/app/config/parameters.yml.dist) - This file is modified so the install process can retrieve the database connection parameters, SwiftMailer can connect to the correct host and the initial data set is set to `minimal`.

## References

* [Akeneo](https://www.akeneo.com/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
