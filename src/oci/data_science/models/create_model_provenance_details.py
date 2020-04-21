# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateModelProvenanceDetails(object):
    """
    Model provenance gives data scientists information about the origin of their model. This information allows data scientists to reproduce the development environment in which the model was trained.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateModelProvenanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param repository_url:
            The value to assign to the repository_url property of this CreateModelProvenanceDetails.
        :type repository_url: str

        :param git_branch:
            The value to assign to the git_branch property of this CreateModelProvenanceDetails.
        :type git_branch: str

        :param git_commit:
            The value to assign to the git_commit property of this CreateModelProvenanceDetails.
        :type git_commit: str

        :param script_dir:
            The value to assign to the script_dir property of this CreateModelProvenanceDetails.
        :type script_dir: str

        :param training_script:
            The value to assign to the training_script property of this CreateModelProvenanceDetails.
        :type training_script: str

        """
        self.swagger_types = {
            'repository_url': 'str',
            'git_branch': 'str',
            'git_commit': 'str',
            'script_dir': 'str',
            'training_script': 'str'
        }

        self.attribute_map = {
            'repository_url': 'repositoryUrl',
            'git_branch': 'gitBranch',
            'git_commit': 'gitCommit',
            'script_dir': 'scriptDir',
            'training_script': 'trainingScript'
        }

        self._repository_url = None
        self._git_branch = None
        self._git_commit = None
        self._script_dir = None
        self._training_script = None

    @property
    def repository_url(self):
        """
        Gets the repository_url of this CreateModelProvenanceDetails.
        For model reproducibility purposes. URL of the git repository associated with model training.


        :return: The repository_url of this CreateModelProvenanceDetails.
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """
        Sets the repository_url of this CreateModelProvenanceDetails.
        For model reproducibility purposes. URL of the git repository associated with model training.


        :param repository_url: The repository_url of this CreateModelProvenanceDetails.
        :type: str
        """
        self._repository_url = repository_url

    @property
    def git_branch(self):
        """
        Gets the git_branch of this CreateModelProvenanceDetails.
        For model reproducibility purposes. Branch of the git repository associated with model training.


        :return: The git_branch of this CreateModelProvenanceDetails.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        """
        Sets the git_branch of this CreateModelProvenanceDetails.
        For model reproducibility purposes. Branch of the git repository associated with model training.


        :param git_branch: The git_branch of this CreateModelProvenanceDetails.
        :type: str
        """
        self._git_branch = git_branch

    @property
    def git_commit(self):
        """
        Gets the git_commit of this CreateModelProvenanceDetails.
        For model reproducibility purposes. Commit ID of the git repository associated with model training.


        :return: The git_commit of this CreateModelProvenanceDetails.
        :rtype: str
        """
        return self._git_commit

    @git_commit.setter
    def git_commit(self, git_commit):
        """
        Sets the git_commit of this CreateModelProvenanceDetails.
        For model reproducibility purposes. Commit ID of the git repository associated with model training.


        :param git_commit: The git_commit of this CreateModelProvenanceDetails.
        :type: str
        """
        self._git_commit = git_commit

    @property
    def script_dir(self):
        """
        Gets the script_dir of this CreateModelProvenanceDetails.
        For model reproducibility purposes. Path to model artifacts.


        :return: The script_dir of this CreateModelProvenanceDetails.
        :rtype: str
        """
        return self._script_dir

    @script_dir.setter
    def script_dir(self, script_dir):
        """
        Sets the script_dir of this CreateModelProvenanceDetails.
        For model reproducibility purposes. Path to model artifacts.


        :param script_dir: The script_dir of this CreateModelProvenanceDetails.
        :type: str
        """
        self._script_dir = script_dir

    @property
    def training_script(self):
        """
        Gets the training_script of this CreateModelProvenanceDetails.
        For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\"


        :return: The training_script of this CreateModelProvenanceDetails.
        :rtype: str
        """
        return self._training_script

    @training_script.setter
    def training_script(self, training_script):
        """
        Sets the training_script of this CreateModelProvenanceDetails.
        For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\"


        :param training_script: The training_script of this CreateModelProvenanceDetails.
        :type: str
        """
        self._training_script = training_script

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
