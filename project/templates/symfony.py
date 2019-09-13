from project.remoteproject import RemoteProject


class Symfony3(RemoteProject):
    major_version = 'v3.4'
    remote = 'https://github.com/symfony/symfony-standard.git'

    @property
    def platformify(self):
        return super(Symfony3, self).platformify + [
            # Symfony 3 ships with a composer.json file that specifies a platform target
            # Of PHP 5.6, for no good reason, even though it depends on Doctrine, which
            # requires PHP 7.1.  Since we're guaranteeing a PHP 7.3 environment, just
            # change that requirement to 7.3 and be done with it.
            'cd {0} && composer config platform.php 7.3'.format(
                self.builddir),
            'cd {0} && composer require platformsh/config-reader --ignore-platform-reqs'.format(
                self.builddir),
        ]


class Symfony4(RemoteProject):
    major_version = 'v4'
    remote = 'https://github.com/symfony/skeleton.git'

    @property
    def platformify(self):
        return super(Symfony4, self).platformify + [
            'cd {0} && composer require platformsh/symfonyflex-bridge ^2.1 --ignore-platform-reqs'.format(
                self.builddir)
        ]
