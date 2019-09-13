
from project.config import TEMPLATEDIR, IGNORED

from project.baseproject import *
from project.remoteproject import *

from project.templates.akeneo import Akeneo
from project.templates.pimcore import Pimcore
from project.templates.drupal import Drupal7Vanilla, Drupal8, Drupal8multi, Opigno, Govcms8
from project.templates.laravel import Laravel
from project.templates.magento import Magento2ce
from project.templates.rails import Rails
from project.templates.sculpin import Sculpin
from project.templates.symfony import Symfony3, Symfony4
from project.templates.wordpress import Wordpress


def project_factory(name):
    '''Instantiate a project object.  Class selection is based on the following naming convention:
    Project class matches template directory name with the first letter capitalized.
      laravel -> Laravel,
      drupal7_vanilla -> Drupal7_vanilla.

    The BaseProject class is used by default (class with the matching name is not imported)
    '''

    targetclass = name.capitalize()
    try:
        return globals()[targetclass](name)
    except KeyError:
        return BaseProject(name)


def project_list():
    """
    Return a list of project factories defining the available projects
    :return: list
    """
    return [project_factory(f.name) for f in os.scandir(TEMPLATEDIR) if f.is_dir() and f.name not in IGNORED]
