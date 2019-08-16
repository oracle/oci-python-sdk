import inspect
import jinja2
import oci  # noqa: F401
import os
import os.path
import shutil
import sys

API_DOC_DIRECTORY = 'docs/api'


class Services:
    """
    Find all the swagger spec files for the services.

    services_for_doc_gen is a list of dictionaries with the following keys.
    module_name         --> module_name in oci package
    service_root_header --> human readable modulename
    target_file_name    --> same as module_name
    service_names       --> List of clients in module

    service_name_to_path --> lookup from service name to path for rst file.
    """
    def __init__(self):

        # SOURCE_DIRECTORY = "src/oci"
        service_name_to_path = {}
        services = {}

        for item in dir(oci):
            for subitem in dir(eval("oci.{}".format(item))):
                if subitem.endswith('Client'):
                    if subitem == "BaseClient":
                        continue
                    import_name = "oci.{}.{}".format(item, subitem)
                    full_path = inspect.getfile(eval(import_name))
                    client_file = os.path.basename(full_path)
                    service_name = client_file
                    if client_file.endswith("_client.pyc"):
                        service_name = client_file[:-1 * len("_client.pyc")]
                    elif client_file.endswith("_client.py"):
                        service_name = client_file[:-1 * len("_client.py")]
                    service_name_to_path[service_name] = "{}/client/{}".format(item, import_name)
                    if item not in services:
                        services[item] = {'module_name': item,
                                          'service_root_header': humanize(item),
                                          'target_file_name': item,
                                          'service_names': [service_name]}
                    else:
                        services[item]['service_names'].append(service_name)

        services_for_doc_gen = []
        keys = list(services.keys())
        keys.sort()
        for service in keys:
            services_for_doc_gen.append(services[service])

        self.services_name_to_path = service_name_to_path
        self.services_for_doc_gen = services_for_doc_gen


# A data bag so that we can pass it to single_page_reference.rst.j2 to render
class SinglePageReferenceServiceGroup(object):
    def __init__(self, group_header, module_name, services):
        self.group_header = group_header
        self.module_name = module_name
        self.services = services

        self.multiple_services = len(self.services) > 1
        self.first_service = self.services[0]


def get_rst_header(header_content, header_char):
    return header_char * len(header_content)


def camelize(source_string):
    split_by_underscore = source_string.split('_')
    full_string = ''
    for s in split_by_underscore:
        if len(s) == 1:
            full_string += s
            continue
        full_string += s[0].upper()
        full_string += s[1:]

    return full_string


def humanize(source_string):
    if source_string == 'blockstorage':
        return 'Block Storage'
    elif source_string == 'dns':
        return 'DNS'
    elif source_string == 'core':
        return 'Core Services'

    split_by_underscore = source_string.split('_')
    full_string = ''
    for s in split_by_underscore:
        if len(s) == 1:
            full_string += s
            continue
        full_string += s[0].upper()
        full_string += '{} '.format(s[1:])

    return full_string.strip()


# Produces the right link for the api/landing.rst page - for most services it's just the name but for services
# which are bundled together into a single spec (e.g. Core has Block Storage, Compute and Virtual Networking)
# the links are nested a bit deeper
def landing_page_linkify(service_name):
    if service_name in services.services_name_to_path:
        return services.services_name_to_path[service_name]

    return service_name


def generate_rst(module_name, service_root_header, target_file_name, service_names, jinja_environment):
    target_file = os.path.join(API_DOC_DIRECTORY, '{}.rst'.format(target_file_name))
    service_client_classes = ['oci.{}.{}Client'.format(module_name, camelize(s)) for s in service_names]
    service_client_classes.extend(['oci.{}.{}ClientCompositeOperations'.format(module_name, camelize(s)) for s in service_names])

    models = []
    for model_info in inspect.getmembers(sys.modules['oci.{}.models'.format(module_name)], inspect.isclass):
        # model_info is a tuple like: ('AuditEvent', <class 'oci.audit.models.audit_event.AuditEvent'>)
        models.append('oci.{}.models.{}'.format(module_name, model_info[0]))

    template = jinja_environment.get_template('service_root.rst.j2')
    content = template.render(service_root_header=service_root_header,
                              module_name=module_name,
                              service_client_classes=service_client_classes,
                              models=models)
    try:
        with open(target_file, 'r') as f:
            existing_content = f.read()
    except Exception:
        # Don't care about the exception, just set the existing content such that the file will be generated or overwritten.
        existing_content = None
    if content != existing_content:
        # Clean out existing models so no orphans exist after docs are generated
        path_to_models = os.path.join(API_DOC_DIRECTORY, target_file_name, "models")
        if os.path.exists(path_to_models):
            shutil.rmtree(path_to_models)
        print("  writing {}".format(target_file))
        with open(target_file, 'w') as f:
            f.write(content)
    else:
        print("  No changes detected")


environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader('scripts/doc_gen/templates'),
    trim_blocks=True,
    lstrip_blocks=True
)
environment.filters['get_rst_header'] = get_rst_header
environment.filters['camelize'] = camelize
environment.filters['humanize'] = humanize

service_groups = []
flattened_services = []
services = Services()

for service_for_doc_gen in services.services_for_doc_gen:
    print('Generating RST files for: {}'.format(service_for_doc_gen['module_name']))
    generate_rst(
        service_for_doc_gen['module_name'],
        service_for_doc_gen['service_root_header'],
        service_for_doc_gen['target_file_name'],
        service_for_doc_gen['service_names'],
        environment
    )

    # We can also create our SinglePageReferenceServiceGroup here for use when generating the single page reference
    service_group = SinglePageReferenceServiceGroup(
        service_for_doc_gen['service_root_header'],
        service_for_doc_gen['module_name'],
        service_for_doc_gen['service_names']
    )
    service_groups.append(service_group)

    # We need these services flattened out for rendering links on the api/landing.rst page
    flattened_services.extend([(landing_page_linkify(s), humanize(s)) for s in service_for_doc_gen['service_names']])

# print('Generating single page reference')
# template = environment.get_template('single_page_reference.rst.j2')
# with open(os.path.join(API_DOC_DIRECTORY, 'index.rst'), 'w') as f:
#     f.write(template.render(service_groups=service_groups))

print('Generating API landing page')
template = environment.get_template('api_landing.rst.j2')
with open(os.path.join(API_DOC_DIRECTORY, 'landing.rst'), 'w') as f:
    f.write(template.render(flattened_services=flattened_services, services_for_doc_gen=services.services_for_doc_gen))

print('Finished generating RST files')
