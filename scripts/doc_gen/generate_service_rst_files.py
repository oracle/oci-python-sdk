import inspect
import jinja2
import oci
import os
import os.path
import sys

API_DOC_DIRECTORY = 'docs/api'

SERVICES_FOR_DOC_GEN = [
    {
        'module_name': 'audit',
        'service_root_header': 'Audit',
        'target_file_name': 'audit',
        'service_names': ['audit']
    },
    {
        'module_name': 'container_engine',
        'service_root_header': 'Container Engine',
        'target_file_name': 'container_engine',
        'service_names': ['container_engine']
    },
    {
        'module_name': 'core',
        'service_root_header': 'Core Services',
        'target_file_name': 'core',
        'service_names': ['blockstorage', 'compute', 'virtual_network']
    },
    {
        'module_name': 'database',
        'service_root_header': 'Database',
        'target_file_name': 'database',
        'service_names': ['database']
    },
    {
        'module_name': 'dns',
        'service_root_header': 'DNS',
        'target_file_name': 'dns',
        'service_names': ['dns']
    },
    {
        'module_name': 'email',
        'service_root_header': 'Email',
        'target_file_name': 'email',
        'service_names': ['email']
    },
    {
        'module_name': 'file_storage',
        'service_root_header': 'File Storage',
        'target_file_name': 'file_storage',
        'service_names': ['file_storage']
    },
    {
        'module_name': 'identity',
        'service_root_header': 'Identity',
        'target_file_name': 'identity',
        'service_names': ['identity']
    },
    {
        'module_name': 'load_balancer',
        'service_root_header': 'Load Balancer',
        'target_file_name': 'load_balancer',
        'service_names': ['load_balancer']
    },
    {
        'module_name': 'object_storage',
        'service_root_header': 'Object Storage',
        'target_file_name': 'object_storage',
        'service_names': ['object_storage']
    },
    {
        'module_name': 'resource_search',
        'service_root_header': 'Resource Search',
        'target_file_name': 'resource_search',
        'service_names': ['resource_search']
    }
]


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

    split_by_underscore = source_string.split('_')
    full_string = ''
    for s in split_by_underscore:
        if len(s) == 1:
            full_string += s
            continue
        full_string += s[0].upper()
        full_string += '{} '.format(s[1:])

    return full_string


# Produces the right link for the api/landing.rst page - for most services it's just the name but for services
# which are bundled together into a single spec (e.g. Core has Block Storage, Compute and Virtual Networking)
# the links are nested a bit deeper
def landing_page_linkify(service_name):
    if service_name == 'blockstorage':
        return 'core/client/oci.core.BlockstorageClient'
    elif service_name == 'compute':
        return 'core/client/oci.core.ComputeClient'
    elif service_name == 'virtual_network':
        return 'core/client/oci.core.VirtualNetworkClient'
    else:
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
    with open(target_file, 'w') as f:
        f.write(
            template.render(
                service_root_header=service_root_header,
                module_name=module_name,
                service_client_classes=service_client_classes,
                models=models
            )
        )


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

for service_for_doc_gen in SERVICES_FOR_DOC_GEN:
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

print('Generating single page reference')
template = environment.get_template('single_page_reference.rst.j2')
with open(os.path.join(API_DOC_DIRECTORY, 'index.rst'), 'w') as f:
    f.write(template.render(service_groups=service_groups))

print('Generating API landing page')
template = environment.get_template('api_landing.rst.j2')
with open(os.path.join(API_DOC_DIRECTORY, 'landing.rst'), 'w') as f:
    f.write(template.render(flattened_services=flattened_services, services_for_doc_gen=SERVICES_FOR_DOC_GEN))

print('Finished generating RST files')
