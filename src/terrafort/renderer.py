import subprocess

import jinja2


class Renderer:
    """
    Jinja template rendering funcitons
    """
    counter = 0

    def __init__(self, fmt_enabled=True):
        self.fmt_enabled = fmt_enabled

    def count(self):
        """
        This method is inserted into the Jinja environment
        It can be used to keep a global count across multiple
        render() calls
        :return:
        """

        # Return the value before incrementing
        count = self.counter
        self.counter += 1
        return count

    def reset_count(self):
        self.counter = 0

    def render(self, resource, template_path):
        """
        Creates jinja environment and attaches global functions
        :param resource:
        :param template_path:
        :return:
        """
        template_loader = jinja2.PackageLoader('terrafort', 'templates')
        template_env = jinja2.Environment(loader=template_loader)
        template_env.globals['count'] = self.count
        template = template_env.get_template(template_path)
        rendered = template.render(resource=resource)

        if self.fmt_enabled:
            return self.fmt(rendered)

        return rendered

    @staticmethod
    def fmt(content):
        """
        Pipes the content into terraform fmt. Basically this:
        echo $content | terraform fmt -
        :param content:
        :return:
        """
        formatted = subprocess.run(["terraform", "fmt", "-"],
                                   stdout=subprocess.PIPE,
                                   input=content,
                                   encoding='ascii',
                                   check=False)
        return formatted.stdout
