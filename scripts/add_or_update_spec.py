#!/usr/bin/env python

import xml.etree.ElementTree as ET
import re

POM_LOCATION = "pom.xml"

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
                    <includes>{spec_path_relative_to_jar}</includes>
                    <outputDirectory>${{spec-temp-dir}}/{spec_name}</outputDirectory>
                </artifactItem>
            </artifactItems>
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
            <specPath>${{spec-temp-dir}}/{spec_name}/{spec_path_relative_to_jar}</specPath>
            <outputDir>src/oci</outputDir>
            <basePackage>OCI</basePackage>
            <additionalProperties>
                <specName>{spec_name}</specName>
                <generateInitFile>true</generateInitFile>
            </additionalProperties>
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


def generate_and_add_unpack_element(spec_name, group_id, artifact_id, spec_path_relative_to_jar):
    content = UNPACK_EXECUTION_TEMPLATE.format(
        spec_name=spec_name,
        group_id=group_id,
        artifact_id=artifact_id,
        spec_path_relative_to_jar=spec_path_relative_to_jar)
    
    unpack_element = ET.fromstring(content)

    # find maven-dependency-plugin where unpacking happens
    unpack_plugin_executions = pom.findall(".//ns:plugin[ns:artifactId='maven-dependency-plugin']/ns:executions", ns)[0]
    unpack_plugin_executions.append(unpack_element)


def generate_and_add_generate_section(spec_name, spec_path_relative_to_jar):
    content = GENERATE_EXECUTION_TEMPLATE.format(
        spec_name=spec_name,
        spec_path_relative_to_jar=spec_path_relative_to_jar)

    generate_element = ET.fromstring(content)

    # find bmc-sdk-swagger-maven-plugin where generation happens
    generate_plugin_executions = pom.findall(".//ns:plugin[ns:artifactId='bmc-sdk-swagger-maven-plugin']/ns:executions", ns)[0]
    generate_plugin_executions.append(generate_element)


def generate_and_add_clean_section(spec_name):
    content = CLEAN_ELEMENT_TEMPLATE.format(
        spec_name=spec_name)

    clean_element = ET.fromstring(content)

    # find filesetes where clean directory goes
    filesets = pom.findall(".//ns:plugin[ns:artifactId='maven-clean-plugin']//ns:filesets", ns)[0]
    filesets.append(clean_element)


def generate_and_add_dependency_management_section(group_id, artifact_id, version):
    content = DEPENDENCY_MANAGEMENT_TEMPLATE.format(
        group_id=group_id,
        artifact_id=artifact_id,
        version=version)

    dep_mgt_element = ET.fromstring(content)

    # find dependencies where version is specified
    dependencies = pom.findall(".//ns:dependencyManagement/ns:dependencies", ns)[0]
    dependencies.append(dep_mgt_element)


def generate_and_add_initial_dependency_section(group_id, artifact_id):
    content = INITIAL_DEPENDENCY_TEMPLATE.format(
        group_id=group_id,
        artifact_id=artifact_id)

    dependency_element = ET.fromstring(content)

    # find dependencies where version is specified
    dependencies = pom.findall("./ns:dependencies", ns)[0]
    dependencies.append(dependency_element)


# params that we will ask user for
group_id = "com.oracle.pic.orchestration"
artifact_id = "maestro-spec"
version = "0.0.1-SNAPSHOT"
spec_name = "maestro"
spec_path_relative_to_jar = "api.yaml"

pom = parse_pom()

# determine if this artifact is already in the spec
xpath_for_spec_dependency_declaration = ".//ns:dependency[ns:artifactId='{artifact_id}']".format(artifact_id=artifact_id)
if (pom.findall(xpath_for_spec_dependency_declaration, ns)):
    print('Artifact {} already exists in pom.xml. Updating version...'.format(spec_name))
    pass
else:
    print('Artifact {} does not exist in pom.xml. Adding it...'.format(spec_name))
    generate_and_add_unpack_element(spec_name, group_id, artifact_id, spec_path_relative_to_jar)
    generate_and_add_generate_section(spec_name, spec_path_relative_to_jar)
    generate_and_add_clean_section(spec_name)
    generate_and_add_dependency_management_section(group_id, artifact_id, version)
    generate_and_add_initial_dependency_section(group_id, artifact_id)

# write out pom
pom.write(POM_LOCATION, xml_declaration = True, encoding='UTF-8')

print('Success!')
