Jenkins Pipe role test
======================

Jenkins pipe ready to run an Ansible role's unitary tests with Openstack.
An example role structure, made with Ansible Galaxy, with dummy tasks and tests is included.

Requirements
------------

- Ansible role structure must be created using ansible galaxy.
- Unitary tests must be written using testinfra and placed in tests folder.
- If the role has other role dependencies, they must be configured in a '.requirements.yml' file following this:
  https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#galaxy-dependencies
- '.requirements.yml' file has to be placed in the role root folder.
- Both 'inventory' and 'test.yml' files in tests folder needs to stay unmodified.

Dependencies
------------

- A Jenkins server properly configured to check a git repo.
- Ansible Openstack playbooks from this project.

Variables
---------

OS_IMAGE_NAME: Openstack image to use when creating the instance.

License
-------

GPL3

Author Information
------------------

