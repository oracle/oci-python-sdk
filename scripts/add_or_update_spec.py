#!/usr/bin/env python

#
# This script manipulates pom.xml to either add new specs or update the versions of existing specs.
#

import xml.etree.ElementTree as ET
import re
import click
from click.exceptions import UsageError

POM_LOCATION = "pom.xml"

SPEC_FILE_PROPERTY_TEMPLATE = """
<{spec_name}-spec-file>{spec_path_relative_to_jar}</{spec_name}-spec-file>
"""

INITIAL_DEPENDENCY_TEMPLATE = """
<dependency>
    <groupId>{group_id}</groupId>
    <artifactId>{artifact_id}</artifactId>
</dependency>
"""

UNPACK_EXECUTION_TEMPLATE = """
<execution>
    <id>unpack-{spec_name}</id>
    <phase>initialize</phase>
    <goals>
        <goal>unpack</goal>
    </goals>
    <configuration>
        <artifactItems>
            <artifactItem>
                <groupId>{group_id}</groupId>
                <artifactId>{artifact_id}</artifactId>
                <type>jar</type>
                <includes>**/*</includes>
                <outputDirectory>${{spec-temp-dir}}/{spec_name}</outputDirectory>
            </artifactItem>
        </artifactItems>
    </configuration>
</execution>
"""

PREFER_EXECUTION_TEMPLATE = """
<execution>
    <id>spec-conditionals-prefer-{spec_name}</id>
    <phase>initialize</phase>
    <goals>
        <goal>prefer</goal>
    </goals>
    <configuration>
        <inputFiles>
            <!-- New layout: source/<spec.proto.yaml> -->
            <inputFile>${{spec-temp-dir}}/{spec_name}/source/${{{spec_name}-spec-file}}</inputFile>
            <!-- Old layout: ./<spec.proto.yaml> -->
            <inputFile>${{spec-temp-dir}}/{spec_name}/${{{spec_name}-spec-file}}</inputFile>
        </inputFiles>
        <outputFile>${{preferred-temp-dir}}/${{{spec_name}-spec-file}}</outputFile>
    </configuration>
</execution>
"""

PREPROCESS_EXECUTION_TEMPLATE = """
<execution>
    <id>spec-conditionals-preprocess-{spec_name}</id>
    <phase>initialize</phase>
    <goals>
        <goal>preprocess</goal>
    </goals>
    <configuration>
        <inputFile>${{preferred-temp-dir}}/${{{spec_name}-spec-file}}</inputFile>
        <outputFile>${{preprocessed-temp-dir}}/${{{spec_name}-spec-file}}</outputFile>
        <groupFile>${{project.basedir}}/release-sdk.txt</groupFile>
    </configuration>
</execution>
"""

GENERATE_EXECUTION_TEMPLATE = """
<execution>
    <id>python-public-sdk-{spec_name}</id>
    <phase>compile</phase>
    <goals>
        <goal>generate</goal>
    </goals>
    <configuration>
        <language>oracle-python-sdk</language>
        <specPath>${{preprocessed-temp-dir}}/${{{spec_name}-spec-file}}</specPath>
        <outputDir>src/oci</outputDir>
        <basePackage>OCI</basePackage>
        <specGenerationType>{spec_generation_type}</specGenerationType>
        <additionalProperties>
            <specName>{spec_name}</specName>
            <generateInitFile>true</generateInitFile>
            <endpoint>{endpoint}</endpoint>
        </additionalProperties>
        <featureIdConfigFile>${{project.basedir}}/featureId.yaml</featureIdConfigFile>
    </configuration>
</execution>
"""

CLEAN_ELEMENT_TEMPLATE = """
 <fileset>
    <directory>src/oci/{spec_name}</directory>
    <includes>
        <include>**/*</include>
    </includes>
</fileset>
"""

DEPENDENCY_MANAGEMENT_TEMPLATE = """
    <dependency>
        <groupId>{group_id}</groupId>
        <artifactId>{artifact_id}</artifactId>
        <version>{version}</version>
    </dependency>
"""

ns = {"ns":"http://maven.apache.org/POM/4.0.0"}

# allow default namespace for output, dont print ns0: prefixes everywhere
ET.register_namespace('',"http://maven.apache.org/POM/4.0.0")

def parse_pom():
    return ET.parse(POM_LOCATION)


def generate_and_add_property_element(pom, spec_name, spec_path_relative_to_jar):
    content = SPEC_FILE_PROPERTY_TEMPLATE.format(
        spec_name=spec_name,
        spec_path_relative_to_jar=spec_path_relative_to_jar)
    
    property_element = ET.fromstring(content)

    xpath = ".//ns:properties"
    properties = pom.findall(xpath, ns)[0]
    properties.append(property_element)


def generate_and_add_unpack_element(pom, spec_name, group_id, artifact_id, spec_path_relative_to_jar):
    content = UNPACK_EXECUTION_TEMPLATE.format(
        spec_name=spec_name,
        group_id=group_id,
        artifact_id=artifact_id,
        spec_path_relative_to_jar=spec_path_relative_to_jar)
    
    unpack_element = ET.fromstring(content)

    # find maven-dependency-plugin where unpacking happens
    unpack_plugin_executions = pom.findall(".//ns:plugin[ns:artifactId='maven-dependency-plugin']/ns:executions", ns)[0]
    unpack_plugin_executions.append(unpack_element)


def generate_and_add_prefer_element(pom, spec_name, group_id, artifact_id, spec_path_relative_to_jar):
    content = PREFER_EXECUTION_TEMPLATE.format(
        spec_name=spec_name,
        group_id=group_id,
        artifact_id=artifact_id,
        spec_path_relative_to_jar=spec_path_relative_to_jar)
    
    unpack_element = ET.fromstring(content)

    # find maven-dependency-plugin where unpacking happens
    unpack_plugin_executions = pom.findall(".//ns:plugin[ns:artifactId='spec-conditionals-preprocessor-plugin']/ns:executions", ns)[0]
    unpack_plugin_executions.append(unpack_element)


def generate_and_add_preprocess_element(pom, spec_name, group_id, artifact_id, spec_path_relative_to_jar):
    content = PREPROCESS_EXECUTION_TEMPLATE.format(
        spec_name=spec_name,
        group_id=group_id,
        artifact_id=artifact_id,
        spec_path_relative_to_jar=spec_path_relative_to_jar)
    
    unpack_element = ET.fromstring(content)

    # find maven-dependency-plugin where unpacking happens
    unpack_plugin_executions = pom.findall(".//ns:plugin[ns:artifactId='spec-conditionals-preprocessor-plugin']/ns:executions", ns)[0]
    unpack_plugin_executions.append(unpack_element)


def generate_and_add_generate_section(pom, spec_name, spec_path_relative_to_jar, endpoint, spec_generation_type):
    content = GENERATE_EXECUTION_TEMPLATE.format(
        spec_name=spec_name,
        spec_path_relative_to_jar=spec_path_relative_to_jar,
        endpoint=endpoint,
        spec_generation_type=spec_generation_type)

    generate_element = ET.fromstring(content)

    # find bmc-sdk-swagger-maven-plugin where generation happens
    generate_plugin_executions = pom.findall(".//ns:plugin[ns:artifactId='bmc-sdk-swagger-maven-plugin']/ns:executions", ns)[0]
    generate_plugin_executions.append(generate_element)


def generate_and_add_clean_section(pom, spec_name):
    content = CLEAN_ELEMENT_TEMPLATE.format(
        spec_name=spec_name)

    clean_element = ET.fromstring(content)

    # find filesetes where clean directory goes
    filesets = pom.findall(".//ns:plugin[ns:artifactId='maven-clean-plugin']//ns:filesets", ns)[0]
    filesets.append(clean_element)


def generate_and_add_dependency_management_section(pom, group_id, artifact_id, version):
    content = DEPENDENCY_MANAGEMENT_TEMPLATE.format(
        group_id=group_id,
        artifact_id=artifact_id,
        version=version)

    dep_mgt_element = ET.fromstring(content)

    # find dependencies where version is specified
    dependencies = pom.findall(".//ns:dependencyManagement/ns:dependencies", ns)[0]
    dependencies.append(dep_mgt_element)


def generate_and_add_initial_dependency_section(pom, group_id, artifact_id):
    content = INITIAL_DEPENDENCY_TEMPLATE.format(
        group_id=group_id,
        artifact_id=artifact_id)

    dependency_element = ET.fromstring(content)

    # find dependencies where version is specified
    dependencies = pom.findall("./ns:dependencies", ns)[0]
    dependencies.append(dependency_element)


def update_version_of_existing_spec(pom, artifact_id, version):
    xpath = ".//ns:dependencyManagement//ns:dependency[ns:artifactId='{artifact_id}']".format(artifact_id=artifact_id)
    dependency = pom.findall(xpath, ns)[0]
    dependency.find('./ns:version', ns).text = version


def indent(elem, level=0):
    indent_str = "    "
    i = "\n" + level*indent_str
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + indent_str
        for e in elem:
            indent(e, level+1)
            if not e.tail or not e.tail.strip():
                e.tail = i + indent_str
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


@click.command()
@click.option('--artifact-id', required=True, help='The artifact id for the spec artifact (e.g. coreservices-api-spec')
@click.option('--group-id', help='The group id for the spec artifact (e.g. com.oracle.pic.commons)')
@click.option('--spec-name', help='The name of the spec. This will be used (e.g. core, identity, object_storage). This is also used as the module name.')
@click.option('--relative-spec-path', help='The relative path of the spec within the artifact (e.g. coreservices-api-spec-20160918-external.yaml)')
@click.option('--endpoint', help='The base endpoint for the service (e.g. https://iaas.{domain}/20160918)')
@click.option('--version', required=True, help='The version of the spec artifact (e.g. 0.0.1-SNAPSHOT')
@click.option('--spec-generation-type', help='The generation type: PUBLIC or PREVIEW')
def add_or_update_spec(artifact_id, group_id, spec_name, relative_spec_path, endpoint, version, spec_generation_type):
    pom = parse_pom()

    # determine if this artifact is already in the spec
    xpath_for_spec_dependency_declaration = ".//ns:dependency[ns:artifactId='{artifact_id}']".format(artifact_id=artifact_id)
    if (pom.findall(xpath_for_spec_dependency_declaration, ns)):
        print('Artifact {} already exists in pom.xml. Updating version...'.format(artifact_id))
        update_version_of_existing_spec(pom, artifact_id, version)
    else:
        if not group_id:
            raise UsageError('Must specify --group-id for new spec')

        if not spec_name:
            raise UsageError('Must specify --spec-name for new spec')

        if not relative_spec_path:
            raise UsageError('Must specify --relative-spec-path for new spec')

        if not endpoint:
            raise UsageError('Must specify --endpoint for new spec')
        
        if not spec_generation_type:
            spec_generation_type = 'PUBLIC'

        print('Artifact {} does not exist in pom.xml. Adding it...'.format(spec_name))
        generate_and_add_property_element(pom, spec_name, relative_spec_path)
        generate_and_add_unpack_element(pom, spec_name, group_id, artifact_id, relative_spec_path)
        generate_and_add_prefer_element(pom, spec_name, group_id, artifact_id, relative_spec_path)
        generate_and_add_preprocess_element(pom, spec_name, group_id, artifact_id, relative_spec_path)
        generate_and_add_generate_section(pom, spec_name, relative_spec_path, endpoint, spec_generation_type)
        generate_and_add_clean_section(pom, spec_name)
        generate_and_add_dependency_management_section(pom, group_id, artifact_id, version)
        generate_and_add_initial_dependency_section(pom, group_id, artifact_id)

    # pretty print pom
    indent(pom.getroot())
    pom.write(POM_LOCATION, encoding="UTF-8", xml_declaration=True) 

    print('Success!')


if __name__ == '__main__':
    add_or_update_spec()
