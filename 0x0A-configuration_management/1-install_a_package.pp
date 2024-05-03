# Define a resource class for managing pip packages
class { 'pip' : }

# Define a resource to install flask with a specific version
package { 'python-flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
