# Laravel for Platform.sh

This template provides a basic Laravel skeleton.  It comes pre-configured to use a MariaDB database and Redis for caching and sessions.

Laravel is an opinionated, integrated rapid-application-development framework for PHP.

## Services

* PHP 7.3
* MariaDB 10.2
* Redis 5.0

## Customizations

The following changes have been made relative to a plain Laravel project.  If using this project as a reference for your own existing project, replicate the changes below to your project.

* The `.platform.app.yaml`, `.platform/services.yaml`, and `.platform/routes.yaml` files have been added.  These provide Platform.sh-specific configuration and are present in all projects on Platform.sh.  You may customize them as you see fit.
* The `.platform.template.yaml` file contains information needed by Platform.sh's project setup process for templates.  It may be safely ignored or removed.
* An additional Composer library, [`platformsh/laravel-bridge`](https://github.com/platformsh/laravel-bridge), has been added.  It automatically maps Platform.sh's environment variables to Laravel's environment variables where possible.  It leverages the [`platformsh/config-reader`](https://github.com/platformsh/config-reader-php) library.
* The Laravel Bridge library also automatically configures Laravel to use Redis for both caching and session storage.  That may be disabled by removing or changing the name of the `rediscache` and `redissession` relationships in `.platform.app.yaml`.

## References

* [Laravel](https://laravel.com/)
* [PHP on Platform.sh](https://docs.platform.sh/languages/php.html)
